import logging

from persona_ai.conversations.manager import ConversationManager
from persona_ai.models.base import GenAIModel
from persona_ai.prompts.base import Prompt
from persona_ai.initializers.persona_configuration import PersonaAI
from persona_ai.prompts.jinja import JinjaTemplatePrompt

logger = logging.getLogger(__name__)


class RequestRefiner:
    """
    Refine user request in order to be better processed by the assistant.
    """

    model: GenAIModel
    """
    Language model used by the refiner to refine the request.
    """

    conversation_manager: ConversationManager = None
    """
    Conversation manager to get history of the conversation.
    """

    prompt: Prompt
    """
    Prompt manager used by the refiner to get the system prompt.
    """

    def __init__(
        self,
        model: GenAIModel = None,
        conversation_manager: ConversationManager = None,
        prompt: Prompt = None,
    ):
        self.model = model if model else PersonaAI.refiner_model
        self.conversation_manager = (
            conversation_manager
            if conversation_manager
            else PersonaAI.conversation_manager
        )
        self.prompt = prompt if prompt else JinjaTemplatePrompt(template="refiner")

    def _render_prompt(self, history, request):
        return self.prompt.render(conversation_history=history, request=request)

    def refine(self, request: str, conversation_id: str) -> str:
        """
        Refine the request.
        """
        history = self.conversation_manager.get_history(conversation_id)
        prompt = self._render_prompt(history, request)

        refined_request = self.model.generate(prompt)

        logger.debug(f"Refined request: {refined_request}")

        return refined_request.text
