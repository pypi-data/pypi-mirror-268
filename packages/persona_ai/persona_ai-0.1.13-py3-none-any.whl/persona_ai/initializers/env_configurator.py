import os

from persona_ai.conversations.manager import ConversationManager
from persona_ai.domain.repositories import (
    MongoConversationsRepository,
    MongoMessagesRepository,
    MongoTasksRepository,
    InMemoryConversationsRepository,
    InMemoryMessagesRepository,
    InMemoryTasksRepository,
)
from persona_ai.initializers.persona_configuration import PersonaAI
from persona_ai.models.code_bison import CodeBisonModel
from persona_ai.models.gemini import GeminiModel
from persona_ai.models.text_bison import TextBisonModel
from persona_ai.transport.local.local_messagebus import LocalMessageBus
from persona_ai.transport.rabbitmq.rabbitmq_messagebus import RabbitMQMessageBus


def get_model(
    prefix: str, force_function_calling=False, system_instructions: str = None
):
    project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
    default_location = os.getenv("GOOGLE_CLOUD_LOCATION", "us-central1")

    model_name = os.getenv(f"{prefix}_MODEL_NAME", "gemini-1.0-pro-001")
    temperature = float(os.getenv(f"{prefix}_MODEL_TEMPERATURE", 0.0))
    max_output_tokens = int(os.getenv(f"{prefix}_MODEL_MAX_OUTPUT_TOKENS", 2048))
    location = os.getenv(f"{prefix}_MODEL_LOCATION", default_location)
    system_instructions = (
        system_instructions
        if system_instructions
        else os.getenv(f"{prefix}_MODEL_SYSTEM_INSTRUCTIONS")
    )

    if "gemini" in model_name:
        return GeminiModel(
            model_name=model_name,
            temperature=temperature,
            max_output_tokens=max_output_tokens,
            location=location,
            project_id=project_id,
            force_function_calling=force_function_calling,
            system_instructions=system_instructions,
        )
    elif "text-bison" in model_name:
        return TextBisonModel(
            model_name=model_name,
            temperature=temperature,
            max_output_tokens=max_output_tokens,
            location=location,
            project_id=project_id,
        )
    elif "code-bison" in model_name:
        return CodeBisonModel(
            model_name=model_name,
            temperature=temperature,
            max_output_tokens=max_output_tokens,
            location=location,
            project_id=project_id,
        )
    else:
        raise ValueError("Invalid model name: {}".format(model_name))


def get_message_bus():
    message_bus_type = os.getenv("MESSAGE_BUS_TYPE", "local")
    if message_bus_type == "rabbitmq":
        return RabbitMQMessageBus()
    elif message_bus_type == "local":
        return LocalMessageBus()
    else:
        raise ValueError("Invalid message bus type: {}".format(message_bus_type))


def get_conversations_repository():
    if _get_repository_type() == "mongodb":
        return MongoConversationsRepository()
    elif _get_repository_type() == "in-memory":
        return InMemoryConversationsRepository()
    else:
        raise ValueError("Invalid repository type: {}".format(_get_repository_type()))


def get_messages_repository():
    if _get_repository_type() == "mongodb":
        return MongoMessagesRepository()
    elif _get_repository_type() == "in-memory":
        return InMemoryMessagesRepository()
    else:
        raise ValueError("Invalid repository type: {}".format(_get_repository_type()))


def get_conversation_manager():
    return ConversationManager(
        conversations_repository=PersonaAI.conversations_repository,
        messages_repository=PersonaAI.messages_repository,
    )


def get_tasks_repository():
    if _get_repository_type() == "mongodb":
        return MongoTasksRepository()
    elif _get_repository_type() == "in-memory":
        return InMemoryTasksRepository()
    else:
        raise ValueError("Invalid repository type: {}".format(_get_repository_type()))


def _get_repository_type():
    return os.getenv("REPOSITORIES_TYPE", "in-memory")


def configure_persona_from_env():
    """Configure a persona_ai system from environment variables."""

    PersonaAI.moderator_model = get_model("MODERATOR")
    PersonaAI.assistant_model = get_model("ASSISTANT")
    PersonaAI.technician_model = get_model("TECHNICIAN")
    PersonaAI.coder_model = get_model("CODER")
    PersonaAI.refiner_model = get_model("REFINER")
    PersonaAI.agent_model = get_model("AGENT")

    PersonaAI.message_bus = get_message_bus()

    PersonaAI.conversations_repository = get_conversations_repository()
    PersonaAI.messages_repository = get_messages_repository()
    PersonaAI.tasks_repository = get_tasks_repository()

    PersonaAI.conversation_manager = get_conversation_manager()
