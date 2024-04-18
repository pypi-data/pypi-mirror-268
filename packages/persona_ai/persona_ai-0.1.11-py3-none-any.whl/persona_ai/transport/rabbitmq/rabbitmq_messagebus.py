import json
import logging
import os
import threading
import time
from threading import Thread
from typing import List

import pika
from pika.adapters.blocking_connection import BlockingChannel, BlockingConnection

from persona_ai.domain.conversations import Message
from persona_ai.domain.utils import create_id
from persona_ai.transport.messagebus import (
    MessageBus,
    Participant,
    Event,
    ConversationListener,
)


class RabbitMQSubscription:
    participant: Participant
    messages_queue: str = None
    events_queue: str = None
    subscribed: bool = False
    is_listener: bool = False
    conversation_id: str = None

    def __init__(self, participant: Participant):
        self.participant = participant
        if isinstance(participant, ConversationListener):
            self.is_listener = True
            self.conversation_id = participant.conversation_id

    def handle_message(self, ch, method, properties, body):
        self.participant.last_activity = time.time()
        json_data = body.decode("utf-8")
        message = Message.model_validate_json(json_data)
        recipient_id = method.routing_key.split(".")[-1]
        if not self.is_listener and not self.participant.id == recipient_id:
            return
        self.participant.receive(message)

    def handle_event(self, ch, method, properties, body):
        self.participant.last_activity = time.time()
        json_data = body.decode("utf-8")
        event = Event.model_validate_json(json_data)
        recipient_id = method.routing_key.split(".")[-1]
        if not self.is_listener and not self.participant.id == recipient_id:
            return
        self.participant.handle_event(event)


class RabbitMQMessageBus(MessageBus):
    """
    This class represents a RabbitMQ message bus.
    """

    connection: BlockingConnection = None
    channel: BlockingChannel = None
    running: bool = False
    subscriptions: List[RabbitMQSubscription] = []
    thread: Thread = None
    on_start: threading.Event = None

    def __init__(self):
        self.subscriptions = []

    def complete_registration(self, subscription: RabbitMQSubscription):
        if not subscription.subscribed:
            subscription.subscribed = True

            def bind():
                self._bind_to_messages(subscription)
                self._bind_to_events(subscription)

            bind()

    def register(self, participants: Participant | List[Participant]):
        participants = (
            [participants] if isinstance(participants, Participant) else participants
        )

        for participant in participants:
            if not any(s.participant.id == participant.id for s in self.subscriptions):
                subscription = RabbitMQSubscription(participant)
                self.subscriptions.append(subscription)

                if self.running:
                    self.complete_registration(subscription)

                logging.info(
                    "Registered participant %s to message bus",
                    participant.id,
                )

    def unregister(self, participants: List[Participant]):
        for participant in participants:
            subscription = next(
                filter(
                    lambda s: s.participant.id == participant.id,
                    self.subscriptions,
                ),
                None,
            )

            if subscription is not None:
                if subscription.messages_queue is not None:
                    self.channel.queue_unbind(
                        subscription.messages_queue, exchange="amq.topic"
                    )
                    self.channel.queue_delete(subscription.messages_queue)
                if subscription.events_queue is not None:
                    self.channel.queue_unbind(
                        subscription.events_queue, exchange="amq.topic"
                    )
                    self.channel.queue_delete(subscription.events_queue)

                self.subscriptions.remove(subscription)

                logging.info(
                    "Unregistered participant %s from message bus",
                    participant.id,
                )

    def start(self) -> threading.Event:
        self.thread = Thread(target=self._start)
        self.thread.start()
        self.on_start = threading.Event()
        return self.on_start

    def wait(self):
        if self.thread is not None:
            if self.thread.is_alive():
                self.thread.join()

    def _start(self):
        self.running = True

        while self.running:
            logging.info(
                "Creating RabbitMQ connection to %s:%s - vhost: %s, user %s...",
                os.getenv("RABBITMQ_HOST"),
                os.getenv("RABBITMQ_PORT"),
                os.getenv("RABBITMQ_VIRTUAL_HOST"),
                os.getenv("RABBITMQ_USER"),
            )

            self._create_connection()
            self._create_channel()

            logging.info("RabbitMQ connection created successfully")

            for subscription in filter(lambda s: not s.subscribed, self.subscriptions):
                self.complete_registration(subscription)

            if self.on_start is not None:
                self.on_start.set()

            self.channel.start_consuming()
            self.stop()
            time.sleep(5)

    def stop(self):
        self.running = False
        if self.connection is not None:
            if self.connection.is_open:
                self.connection.add_callback_threadsafe(self._stop)

        # self.wait()
        logging.info("RabbitMQ connection closed")

    def _stop(self):
        for subscription in filter(lambda s: s.subscribed, self.subscriptions):
            self.unregister([subscription.participant])

        if self.connection is not None:
            self.connection.close()

        if self.channel is not None:
            self.channel.stop_consuming()

    def _create_connection(self):
        self.connection = BlockingConnection(
            pika.ConnectionParameters(
                host=os.getenv("RABBITMQ_HOST"),
                port=os.getenv("RABBITMQ_PORT"),
                virtual_host=os.getenv("RABBITMQ_VIRTUAL_HOST"),
                credentials=pika.PlainCredentials(
                    os.getenv("RABBITMQ_USER"), os.getenv("RABBITMQ_PASSWORD")
                ),
            )
        )

    def _create_channel(self):
        self.channel = self.connection.channel()

    def _bind_to_messages(self, subscription: RabbitMQSubscription):
        if self.channel is None or self.channel.is_closed:
            raise ValueError("Channel is not open")

        result = self.channel.queue_declare(
            queue=f"messages_{create_id(prefix=subscription.participant.id)}",
            exclusive=True,
            auto_delete=True,
        )
        queue_name = result.method.queue
        subscription_id = (
            "#" if subscription.is_listener else subscription.participant.id
        )
        conversation_id = (
            subscription.conversation_id if subscription.conversation_id else "#"
        )
        self.channel.queue_bind(
            exchange="amq.topic",
            queue=queue_name,
            routing_key=f"persona.messages.{conversation_id}.{subscription_id}",
        )
        self.channel.basic_consume(
            queue_name, subscription.handle_message, auto_ack=True
        )
        subscription.messages_queue = queue_name

        logging.info(
            "Bound to messages queue %s for participant %s",
            queue_name,
            subscription.participant.id,
        )

    def _bind_to_events(self, subscription: RabbitMQSubscription):
        if self.channel is None or self.channel.is_closed:
            raise ValueError("Channel is not open")

        result = self.channel.queue_declare(
            f"events_{create_id(prefix=subscription.participant.id)}",
            exclusive=True,
            auto_delete=True,
        )
        queue_name = result.method.queue
        subscription_id = (
            "#" if subscription.is_listener else subscription.participant.id
        )
        conversation_id = (
            subscription.conversation_id if subscription.conversation_id else "#"
        )
        self.channel.queue_bind(
            exchange="amq.topic",
            queue=queue_name,
            routing_key=f"persona.events.{conversation_id}.{subscription_id}",
        )
        self.channel.basic_consume(queue_name, subscription.handle_event, auto_ack=True)
        subscription.events_queue = queue_name

        logging.info(
            "Bound to events queue %s for participant %s",
            queue_name,
            subscription.participant.id,
        )

    def publish_message(self, message: Message, recipient_id: str, **kwargs):
        if self.channel is None or self.channel.is_closed:
            raise ValueError("Channel is not open")

        json_body: str = json.dumps(message.model_dump(by_alias=True))
        self.connection.add_callback_threadsafe(
            lambda: self.channel.basic_publish(
                exchange="amq.topic",
                routing_key=f"persona.messages.{message.conversation_id}.{recipient_id}",
                body=json_body,
            )
        )

    def publish_event(self, event: Event, recipient_id: str | None = None, **kwargs):
        if self.channel is None or self.channel.is_closed:
            raise ValueError("Channel is not open")

        recipient_id = recipient_id if recipient_id else "listeners"
        json_body: str = json.dumps(event.model_dump(by_alias=True))
        conversation_id = event.conversation_id if event.conversation_id else "none"
        self.connection.add_callback_threadsafe(
            lambda: self.channel.basic_publish(
                exchange="amq.topic",
                routing_key=f"persona.events.{conversation_id}.{recipient_id}",
                body=json_body,
            )
        )
