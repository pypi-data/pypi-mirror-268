import time
from abc import ABC, abstractmethod
from typing import List

from persona_ai.domain.conversations import Message
from persona_ai.domain.events import Event
from persona_ai.domain.utils import create_id

PING_TIMEOUT = 5  # seconds


class PingPong:
    """
    This class is used to keep track of the last time a participant was pinged.
    """

    def __init__(self, sender_id: str, recipient_id: str):
        self.creation_time = time.time()
        self.replied = False
        self.sender_id: str = sender_id
        self.recipient_id: str = recipient_id

    def is_alive(self):
        return time.time() - self.creation_time < (PING_TIMEOUT * 1000)

    def reset(self):
        self.creation_time = time.time()


class Participant:
    id: str
    """The participant identifier."""

    name: str
    """The participant name."""

    role: str
    """The participant role."""

    scope: str
    """The participant scope in a party."""

    can_reply_multiple_times: bool = False
    """
    Indicates if the participant can reply multiple times to a message.
    If this variable is set to True, moderators can call this participant multiple times.
    """

    last_activity: float = 0
    """The last time the participant was active."""

    allow_broadcasting: bool = False
    """Indicates if the participant can receive broadcast messages."""

    included_in_moderation: bool = True
    """
    Indicates if the participant is included in the moderation process.
    """

    def __init__(
        self,
        id: str,
        name: str,
        role: str,
        scope: str,
        can_reply_multiple_times: bool = False,
        allow_broadcasting: bool = False,
        included_in_moderation: bool = True,
    ):
        self.id = id
        self.name = name
        self.role = role
        self.scope = scope
        self.can_reply_multiple_times = can_reply_multiple_times
        self.allow_broadcasting = allow_broadcasting
        self.included_in_moderation = included_in_moderation
        self.last_activity = time.time()

    def receive(self, message: Message, **kwargs):
        """Receive a message from another agent."""
        last_activity = time.time()

    def handle_event(self, event: Event, **kwargs):
        """Handle an event."""
        last_activity = time.time()


class ConversationListener(Participant):
    """
    A conversation listener is a participant that listens to a conversation.
    This is the best object to use when you want to show messages, events and iterations in some frontends,
    like terminal or web interfaces.

    Attributes:
    - conversation_id: str, the conversation identifier to listen.
    """

    conversation_id: str
    """The conversation identifier to listen."""

    def __init__(
        self,
        name: str,
        conversation_id: str,
        id: str = None,
    ):
        super().__init__(
            id if id else create_id(prefix="listener"),
            name,
            "listener",
            "Conversation Listener",
            False,
            False,
            False,
        )
        self.conversation_id = conversation_id


class MessageBus(ABC):
    """Message bus interface. This interface defines the methods for personas messages exchange."""

    @abstractmethod
    def start(self) -> Event:
        """Start the message bus."""
        raise NotImplementedError

    def stop(self) -> Event:
        """Stop the message bus."""
        raise NotImplementedError

    @abstractmethod
    def register(self, members: Participant | List[Participant]):
        """Register a personas."""
        raise NotImplementedError

    @abstractmethod
    def publish_message(self, message: Message, recipient_id: str, **kwargs):
        """Send a message to a recipient."""
        raise NotImplementedError

    @abstractmethod
    def publish_event(self, event: Event, recipient_id: str | None = None, **kwargs):
        """Send an event to a recipient."""
        raise NotImplementedError
