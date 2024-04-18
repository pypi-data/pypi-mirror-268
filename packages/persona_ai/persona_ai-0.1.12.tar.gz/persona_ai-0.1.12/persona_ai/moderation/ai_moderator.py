import logging
from abc import ABC, abstractmethod
from typing import List

from persona_ai.domain.conversations import Message, MessageBody
from persona_ai.domain.tasks import Task
from persona_ai.initializers.persona_configuration import PersonaAI
from persona_ai.models.base import GenAIModel
from persona_ai.moderation.base import Moderator, ModerationResult, Rule
from persona_ai.prompts.base import Prompt
from persona_ai.tools.base import ToolDefinition
from persona_ai.transport.messagebus import Participant
from persona_ai.utils.extractors import markdown_to_text

logger = logging.getLogger(__name__)


class AIModerator(ABC, Moderator):
    """
    AI moderator.
    Selects a participant suggested by LLM using name and scope.
    """

    model: GenAIModel
    """Language model used by the moderator."""

    prompt: Prompt
    """Prompt manager used to get the system prompt."""

    def __init__(
        self,
        model: GenAIModel = None,
        rules: List[Rule] = None,
    ):
        super().__init__(rules)

        self.model = model if model else PersonaAI.moderator_model
        if not self.model:
            raise ValueError("Language model is required.")

    def moderate(
        self,
        conversation_history: List[Message],
        participants: List[Participant],
        task: Task,
        message: Message,
        sender: Participant,
    ) -> ModerationResult:
        """Select next participant using AI."""

        allowed_participants = self._get_allowed_participants(
            message, participants, sender, task
        )

        logger.info(
            "Selecting participant from list: %s",
            ", ".join([x.name for x in allowed_participants]),
        )

        tools = self._create_tools(allowed_participants)

        prompt = self._render_prompt(
            allowed_participants=allowed_participants,
            conversation_history=conversation_history,
            init_message=task.init_message,
            task=task,
        )

        response = self.model.generate(
            prompt,
            tools=tools,
            **self._get_generation_kwargs(),
        )

        logger.debug("Model response: %s", response)

        if response.text:
            response.text = markdown_to_text(response.text.strip())

        return self._process_response(allowed_participants, response, task)

    def _get_generation_kwargs(self):
        return {}

    @abstractmethod
    def _process_response(
        self, allowed_participants: List[Participant], response: MessageBody, task: Task
    ) -> ModerationResult:
        raise NotImplementedError()

    @abstractmethod
    def _render_prompt(
        self,
        allowed_participants,
        conversation_history,
        init_message: Message,
        task: Task,
    ) -> str:
        raise NotImplementedError()

    @abstractmethod
    def _create_tools(self, allowed_participants) -> List[ToolDefinition] | None:
        raise NotImplementedError()
