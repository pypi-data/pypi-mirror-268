import logging

from persona_ai.constants import TERMINATION_TOKEN
from persona_ai.conversations.manager import ConversationManager
from persona_ai.domain import roles
from persona_ai.domain.conversations import Message, MessageBody, create_message
from persona_ai.domain.utils import create_id
from persona_ai.initializers.persona_configuration import PersonaAI
from persona_ai.models.base import GenAIModel
from persona_ai.personas.base import Persona
from persona_ai.prompts.base import Prompt
from persona_ai.prompts.jinja import JinjaTemplatePrompt
from persona_ai.transport.messagebus import MessageBus


class Assistant(Persona):
    """
    Assistant is a persona that can generate text based on the input it receives.
    """

    model: GenAIModel = None
    """Language model used by the assistant to generate text."""

    prompt: Prompt
    """
    System prompt used by the agent to generate text. Should be directly the prompt if system_prompt_type is string. 
    If system_prompt_type is template, this variable is the template name.
    """

    def __init__(
        self,
        name: str,
        scope: str,
        role: str = None,
        model: GenAIModel = None,
        message_bus: MessageBus = None,
        id: str = None,
        conversation_manager: ConversationManager = None,
        prompt: Prompt = None,
        can_reply_multiple_times: bool = False,
        allow_broadcasting: bool = False,
        included_in_moderation: bool = True,
    ):
        super().__init__(
            id=id if id else create_id(prefix="assistant"),
            name=name,
            role=role if role else roles.AI,
            scope=scope,
            message_bus=message_bus,
            conversation_manager=conversation_manager,
            can_reply_multiple_times=can_reply_multiple_times,
            allow_broadcasting=allow_broadcasting,
            included_in_moderation=included_in_moderation,
        )

        self.model = model if model else PersonaAI.assistant_model
        if not self.model:
            raise ValueError("Assistant model is not set.")

        self.prompt = prompt if prompt else JinjaTemplatePrompt("assistant")

        if not self.prompt:
            raise ValueError("Prompt is not set.")

    def receive(self, message: Message, **kwargs):
        super().receive(message, **kwargs)

        conversation = self.conversation_manager.get_conversation(
            message.conversation_id
        )

        history = self.conversation_manager.get_history(conversation.id)
        history_without_last_message = history[:-1]

        rendered_prompt = self._render_prompt(
            history=history_without_last_message, message=message
        )

        response: MessageBody = self._call_model(rendered_prompt)

        logging.info(
            f"{self.name} received message from {message.sender_name}. Response is {response.model_dump_json()}"
        )

        if response is None:
            raise ValueError("Response is None")

        if message.reply:
            reply = self._generate_reply(response, message)
            recipient = (
                message.reply_to if message.reply_to is not None else message.sender_id
            )
            self.send(
                reply,
                recipient,
            )

    def _render_prompt(self, history, message):
        return self.prompt.render(
            conversation_history=history,
            request=message,
            termination_token=TERMINATION_TOKEN,
        )

    def _call_model(self, prompt):
        return self.model.generate(prompt)

    def _generate_reply(self, body: MessageBody, request: Message) -> Message:
        is_termination_message = False

        new_body = MessageBody.clone(body=body)

        if new_body.text:
            is_termination_message = TERMINATION_TOKEN in body.text
            new_body.text = body.text.replace(TERMINATION_TOKEN, "").strip()

        return create_message(
            body=new_body,
            conversation_id=request.conversation_id,
            sender_id=self.id,
            sender_name=self.name,
            sender_role=self.role,
            is_termination_message=is_termination_message,
        )
