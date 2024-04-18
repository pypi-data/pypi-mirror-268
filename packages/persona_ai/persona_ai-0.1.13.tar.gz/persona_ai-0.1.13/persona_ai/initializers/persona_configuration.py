from persona_ai.conversations.manager import ConversationManager
from persona_ai.domain.repositories import (
    MongoConversationsRepository,
    MongoMessagesRepository,
)
from persona_ai.models.base import GenAIModel
from persona_ai.prompts.base import Prompt
from persona_ai.transport.messagebus import MessageBus


class PersonaAI:
    """
    Configuration for the Persona AI system.
    All af these attributes are used as default values for Personas, parties and other components if not provided.
    """

    tasks_repository = None
    moderator_model: GenAIModel = None
    assistant_model: GenAIModel = None
    technician_model: GenAIModel = None
    coder_model: GenAIModel = None
    refiner_model: GenAIModel = None
    agent_model: GenAIModel = None
    conversations_repository: MongoConversationsRepository = None
    messages_repository: MongoMessagesRepository = None
    prompt_manager: Prompt = None
    message_bus: MessageBus = None
    conversation_manager: ConversationManager = None
