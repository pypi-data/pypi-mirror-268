from datetime import datetime

from persona_ai.constants import HISTORY_SIZE
from persona_ai.domain.conversations import Conversation, Message
from persona_ai.domain.repositories import (
    MongoConversationsRepository,
    MongoMessagesRepository,
)
from persona_ai.domain.utils import create_id


class ConversationManager:
    """
    Manages conversations and messages.
    This object is responsible for creating, updating, and retrieving conversations and messages.
    Parties and Personas uses this class to interact with conversations and messages.

    Example:
    ```python
    conversation_manager = ConversationManager()
    conversation = conversation_manager.create_conversation()
    message = Message(conversation_id=conversation.id, sender_id="sender", content="Hello, World!")
    conversation_manager.add_message(message)
    ```
    """

    conversations_repository: MongoConversationsRepository
    """
    The repository for conversations.    
    """

    messages_repository: MongoMessagesRepository
    """
    The repository for messages.
    """

    def __init__(
        self,
        conversations_repository: MongoConversationsRepository = None,
        messages_repository: MongoMessagesRepository = None,
    ):
        self.conversations_repository = (
            conversations_repository
            if conversations_repository
            else MongoConversationsRepository()
        )

        self.messages_repository = (
            messages_repository if messages_repository else MongoMessagesRepository()
        )

    def get_conversation(self, conversation_id: str) -> Conversation | None:
        """
        Get a conversation by its identifier.
        """
        return self.conversations_repository.get_by_id(conversation_id)

    def create_conversation(self) -> Conversation:
        """
        Create a new conversation.
        """
        conversation_id = create_id(prefix="conversation")
        conversation = Conversation(id=conversation_id, title="", summary="")

        self.conversations_repository.create(conversation)

        return conversation

    def update_conversation(self, conversation: Conversation):
        """
        Update a conversation.
        """
        self.conversations_repository.update(conversation)

    def add_message(self, message: Message):
        """
        Add a message to the conversation.
        """
        message.timestamp = datetime.now().timestamp()
        if self.messages_repository.exists(message.id):
            self.messages_repository.update(message)

        else:
            self.messages_repository.create(message)

    def get_history(self, conversation_id: str, messages_to_take: int = HISTORY_SIZE):
        """
        Get the conversation history.
        """
        history = self.messages_repository.find(
            filter={"conversation_id": conversation_id},
            sort={"timestamp": -1},
            limit=messages_to_take,
        )
        return list(reversed(history))

    def mark_has_received(self, message: Message):
        """
        Mark a message as received.
        """
        message.mark_as_received()
        self.messages_repository.update(message)
