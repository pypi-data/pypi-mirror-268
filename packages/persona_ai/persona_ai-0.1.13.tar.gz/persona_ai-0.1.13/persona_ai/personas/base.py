import logging
from threading import Thread

from persona_ai.conversations.manager import (
    ConversationManager,
)
from persona_ai.domain import events
from persona_ai.domain.conversations import (
    Message,
    create_text_message,
    MessageBody,
)
from persona_ai.domain.events import Event
from persona_ai.domain.utils import create_id
from persona_ai.initializers.persona_configuration import PersonaAI
from persona_ai.transport.messagebus import MessageBus, Participant, PingPong

logger = logging.getLogger(__name__)


class Persona(Participant):
    """
    Base agent class. An agent is a member of Persona AI group.
    Agents are able to execute Python code, run tools and perform requests to LLMs.
    Agents can send messages and receive messages from other personas through Persona party.
    Everything is asynchronous.
    """

    def __init__(
        self,
        name: str,
        role: str,
        scope: str,
        message_bus: MessageBus = None,
        conversation_manager: ConversationManager = None,
        id: str = None,
        can_reply_multiple_times: bool = False,
        allow_broadcasting: bool = False,
        included_in_moderation: bool = True,
    ):
        super().__init__(
            id if id else create_id(prefix="persona"),
            name,
            role,
            scope,
            can_reply_multiple_times,
            allow_broadcasting,
            included_in_moderation,
        )
        self.ping_pong_thread: Thread | None = None
        self.pings = []
        self.message_bus = message_bus if message_bus else PersonaAI.message_bus

        if not self.message_bus:
            raise ValueError("Message bus is not set.")

        self.conversation_manager = (
            conversation_manager
            if conversation_manager
            else PersonaAI.conversation_manager
        )

        if not self.conversation_manager:
            raise ValueError("Conversation manager is not set.")

        self.message_bus.register([self])

    message_bus: MessageBus
    """Message bus used by the agent to send and receive messages."""

    conversation_manager: ConversationManager
    """Conversation manager used by the agent to manage conversations."""

    def send(self, content: Message | MessageBody, recipient_id: str, **kwargs):
        """Send a message to another participant."""

        content = (
            content
            if isinstance(content, Message)
            else Message(
                body=content,
                conversation_id=self.conversation_manager.create_conversation().id,
                sender_id=self.id,
                sender_name=self.name,
                sender_role=self.role,
            )
        )

        self.conversation_manager.add_message(content)
        self.message_bus.publish_message(content, recipient_id, **kwargs)

    def send_text(self, text: str, conversation_id: str, recipient_id: str, **kwargs):
        """Send a text message to another participant."""

        self.send(
            create_text_message(
                text=text,
                conversation_id=conversation_id,
                sender_id=self.id,
                sender_name=self.name,
                sender_role=self.role,
            ),
            recipient_id,
            **kwargs,
        )

    def receive(self, message: Message, **kwargs):
        super().receive(message, **kwargs)

        self.conversation_manager.mark_has_received(message)

    def join_party(self, party_id: str):
        self.message_bus.publish_event(
            Event(
                sender_id=self.id,
                type=events.JOIN,
                body={
                    "id": self.id,
                    "name": self.name,
                    "role": self.role,
                    "scope": self.scope,
                },
            ),
            recipient_id=party_id,
        )

    def leave_party(self, party_id: str):
        self.message_bus.publish_event(
            Event(
                sender_id=self.id,
                type=events.LEAVE,
                body={
                    "id": self.id,
                    "name": self.name,
                    "role": self.role,
                    "scope": self.scope,
                },
            ),
            recipient_id=party_id,
        )

    def ping(self, recipient_id: str, **kwargs):
        """Send a ping to another participant."""
        ping = next(filter(lambda p: p.recipient_id == recipient_id, self.pings), None)
        if ping is None:
            ping = PingPong(sender_id=self.id, recipient_id=recipient_id)
            self.pings.append(ping)

        self.message_bus.publish_event(
            Event(
                sender_id=self.id,
                type=events.PING,
                body={},
            ),
            recipient_id=recipient_id,
            **kwargs,
        )

        logging.debug(f"Sent ping to {recipient_id}.")

    def handle_event(self, event: Event, **kwargs):
        """Handle an event."""
        super().handle_event(event, **kwargs)

        if event.type == events.PING:
            self._handle_ping(event, **kwargs)
        elif event.type == events.PONG:
            self._handle_pong(event, **kwargs)
        elif event.type == events.ACCEPT:
            self._handle_accept(event, **kwargs)

    def _handle_accept(self, event, **kwargs):
        """Handle an accept event."""
        logger.debug(f"Received accept event from {event.sender_id}.")

    def _handle_ping(self, event: Event, **kwargs):
        """Handle a ping event."""
        self.message_bus.publish_event(
            Event(
                sender_id=self.id,
                type=events.PONG,
                body={},
            ),
            recipient_id=event.sender_id,
            **kwargs,
        )

        logging.debug(f"Replied to ping from {event.sender_id}.")

    def _handle_pong(self, event: Event, **kwargs):
        """Handle a pong event."""
        ping = next(
            filter(lambda p: p.recipient_id == event.sender_id, self.pings), None
        )
        if ping is not None:
            ping.reset()
            logging.debug(f"Received pong from {event.sender_id}.")
        else:
            logging.warning(f"Received unexpected pong from {event.sender_id}.")

    def handle_dead_participant(self, participant_id: str):
        """Handle a dead participant."""
        logger.debug(f"Participant {participant_id} is dead.")
        pass
