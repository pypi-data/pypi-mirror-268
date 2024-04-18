import logging
import threading
import time
from typing import List

from persona_ai.constants import (
    DEFAULT_MAX_ITERATIONS,
    PARTICIPANTS_PING_DELAY_SECONDS,
)
from persona_ai.conversations.manager import ConversationManager
from persona_ai.domain import events, roles
from persona_ai.domain.conversations import Message, create_text_message
from persona_ai.domain.events import Event
from persona_ai.domain.tasks import TaskStatus, Task
from persona_ai.domain.utils import create_id
from persona_ai.initializers.persona_configuration import PersonaAI
from persona_ai.models.base import GenAIModel
from persona_ai.moderation.base import ModerationResult, Moderator
from persona_ai.personas.base import Persona
from persona_ai.task_manager.base import TaskManager
from persona_ai.transport.messagebus import Participant, MessageBus

PARTY_MANAGER_DEFAULT_SCOPE = (
    "Your role is to find the best candidate to answer to the user."
)


logger = logging.getLogger(__name__)


class Party(Persona):
    """
    Party is a persona that manages a group of participants.
    A message to a party starts a new task and the conversation is moderated in order to find the best answer, like a chat group.
    """

    participants: List[Participant] = []
    moderator: Moderator
    max_iterations: int = DEFAULT_MAX_ITERATIONS
    task_manager: TaskManager
    model: GenAIModel
    _ping_thread: threading.Thread | None = None
    _running: bool = False

    def __init__(
        self,
        members: List[Persona],
        moderator: Moderator,
        message_bus: MessageBus = None,
        model: GenAIModel = None,
        conversation_manager: ConversationManager = None,
        max_iterations: int = DEFAULT_MAX_ITERATIONS,
        id: str = None,
        allow_broadcasting: bool = False,
        included_in_moderation: bool = True,
        **kwargs,
    ):
        super().__init__(
            id=id if id else create_id(prefix="party"),
            name="Party",
            role=roles.PARTY,
            scope=PARTY_MANAGER_DEFAULT_SCOPE,
            message_bus=message_bus,
            conversation_manager=conversation_manager,
            allow_broadcasting=allow_broadcasting,
            included_in_moderation=included_in_moderation,
        )
        self._running = False
        self._ping_thread = None
        self.participants = []
        self.model = model if model else PersonaAI.moderator_model
        if not self.model:
            raise ValueError("Language model is required.")

        self.moderator = moderator
        self.max_iterations = max_iterations

        self.conversation_manager = (
            conversation_manager
            if conversation_manager
            else PersonaAI.conversation_manager
        )

        if not self.conversation_manager:
            raise ValueError("Conversation manager is required.")

        self.task_manager = TaskManager(PersonaAI.tasks_repository)

        for member in members:
            self.add_member(member)

    def add_member(self, member: Participant):
        if not any([a.id == member.id for a in self.participants]):
            self.participants.append(member)
            logger.info(f"{member.name} joined {self.name}")

    def start(self) -> threading.Event:
        self._running = True
        event = self.message_bus.start()
        event.wait()
        for participant in self.participants:
            self.message_bus.publish_event(
                Event(sender_id=self.id, type=events.ACCEPT, body={}),
                recipient_id=participant.id,
            )

        self._ping_thread = threading.Thread(target=self._ping_loop)
        self._ping_thread.start()

        return event

    def _ping_loop(self):
        while self._running:
            logger.debug("Pinging participants...")
            for participant in self.participants:
                self.ping(participant.id)

            for i in range(0, PARTICIPANTS_PING_DELAY_SECONDS):
                if not self._running:
                    break
                time.sleep(1)

    def stop(self):
        self._running = False
        self.message_bus.stop()

    def _handle_pong(self, event: Event, **kwargs):
        participant = self.get_participant_by_id(event.sender_id)
        if participant:
            participant.last_activity = time.time()
            logger.debug(f"Received pong from {participant.name}.")

    def _moderate(
        self, pending_task: Task, conversation_history: List[Message], message: Message
    ) -> ModerationResult:
        last_sender = self.get_participant_by_id(message.sender_id)

        moderation_result = self.moderator.moderate(
            conversation_history=conversation_history,
            participants=self.participants,
            task=pending_task,
            message=message,
            sender=last_sender,
        )

        return moderation_result

    def receive(self, message: Message, **kwargs):
        super().receive(message, **kwargs)

        sender: Participant = self.get_participant_by_id(message.sender_id)
        if sender is None:
            logger.warning(
                "Received message from unknown sender %s: %s",
                message.sender_id,
                message.get_text(),
            )
            return

        try:
            pending_task = self.task_manager.get_pending_task(message.conversation_id)
            if pending_task is None:
                pending_task = self.task_manager.start_task(
                    init_message=message,
                )
            else:
                self.task_manager.set_iteration_output(pending_task, message)

            if message.is_termination_message:
                self._finish_pending_task(
                    pending_task,
                    message,
                    "Assistant finished with a termination message",
                )
                self.message_bus.publish_event(
                    Event(
                        sender_id=self.id,
                        type=events.ITERATION,
                        conversation_id=message.conversation_id,
                        body={
                            "task_id": pending_task.id,
                            "message": message,
                            "moderation_result": ModerationResult(
                                next=None,
                                final_answer_found=True,
                                final_answer=message.get_text(),
                                reason="Assistant finished with a termination message",
                            ).to_dict(),
                        },
                    )
                )
                return

            if not pending_task.is_iterable():
                self.task_manager.finish_pending_task(
                    pending_task,
                    TaskStatus.FAILED,
                )

                self.message_bus.publish_event(
                    Event(
                        sender_id=self.id,
                        type=events.ITERATION,
                        conversation_id=message.conversation_id,
                        body={
                            "task_id": pending_task.id,
                            "message": message,
                            "moderation_result": ModerationResult(
                                next=None,
                                final_answer_found=False,
                                final_answer=None,
                                reason="Task iterations limit reached",
                            ).to_dict(),
                        },
                    )
                )
                return

            conversation_history = self.conversation_manager.get_history(
                conversation_id=message.conversation_id
            )

            moderation_result: ModerationResult = self._moderate(
                pending_task=pending_task,
                conversation_history=conversation_history,
                message=message,
            )

            if moderation_result.final_answer_found:
                final_message = message
                if moderation_result.final_answer:
                    final_message = create_text_message(
                        text=moderation_result.final_answer,
                        conversation_id=message.conversation_id,
                        sender_id=self.id,
                        sender_name=self.name,
                        sender_role=self.role,
                    )

                self._finish_pending_task(
                    pending_task, final_message, moderation_result.reason
                )

                self.message_bus.publish_event(
                    Event(
                        sender_id=self.id,
                        type=events.ITERATION,
                        conversation_id=message.conversation_id,
                        body={
                            "task_id": pending_task.id,
                            "message": message,
                            "moderation_result": moderation_result.to_dict(),
                        },
                    )
                )
                return

            self.task_manager.iterate(
                pending_task,
                originating_message=message,
                participant_id=(
                    moderation_result.next.id if moderation_result.next else None
                ),
                reasoning=moderation_result.reason,
                request=moderation_result.request,
            )

            if moderation_result.next is None:
                self._fail_pending_task(pending_task, message, moderation_result.reason)

                self.message_bus.publish_event(
                    Event(
                        sender_id=self.id,
                        type=events.ITERATION,
                        conversation_id=message.conversation_id,
                        body={
                            "task_id": pending_task.id,
                            "message": message,
                            "moderation_result": moderation_result.to_dict(),
                        },
                    )
                )
                return

            self.message_bus.publish_event(
                Event(
                    sender_id=self.id,
                    type=events.ITERATION,
                    conversation_id=message.conversation_id,
                    body={
                        "task_id": pending_task.id,
                        "message": message,
                        "moderation_result": moderation_result.to_dict(),
                    },
                )
            )

            if message.reply:
                if (
                    moderation_result.request is not None
                    and moderation_result.request != ""
                    and moderation_result.request != message.get_text()
                ):
                    self.send_text(
                        moderation_result.request,
                        message.conversation_id,
                        moderation_result.next.id,
                    )
                else:
                    message.reply_to = self.id
                    self.send(message, moderation_result.next.id)

        finally:
            pass

    def _fail_pending_task(self, pending_task, message, reason):
        # self._reply_to_originator(message)

        self.task_manager.finish_pending_task(
            task=pending_task, status=TaskStatus.FAILED
        )

    def _finish_pending_task(self, pending_task, message, reason):
        # self._reply_to_originator(message)

        message.is_termination_message = True
        self.task_manager.finish_pending_task(pending_task, TaskStatus.COMPLETED)

    def get_participant_by_id(self, sender_id: str) -> Participant | None:
        return next(
            filter(lambda member: member.id == sender_id, self.participants), None
        )

    def handle_event(self, event: Event, **kwargs):
        super().handle_event(event, **kwargs)

        if event.type == events.JOIN:
            participant = Participant(
                id=event.body["id"],
                name=event.body["name"],
                role=event.body["role"],
                scope=event.body["scope"],
            )
            self.add_member(participant)
            self.message_bus.publish_event(
                Event(sender_id=self.id, type=events.ACCEPT, body={}),
                recipient_id=participant.id,
            )

    def _reply_to_originator(self, message):
        pending_task = self.task_manager.get_pending_task(message.conversation_id)
        if pending_task is not None:
            self.send(message, pending_task.init_message.sender_id)
        else:
            logger.warning(
                "No pending task found for conversation %s", message.conversation_id
            )


def get_input() -> str:
    print("Insert your text. Enter 'q' or press Ctrl-D (or Ctrl-Z on Windows) to end.")
    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line == "q":
            break
        contents.append(line)
    return "\n".join(contents)
