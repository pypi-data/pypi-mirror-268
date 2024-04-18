from persona_ai.conversations.manager import ConversationManager
from persona_ai.domain import roles
from persona_ai.domain.conversations import (
    ToolSuggestion,
    MessageBody,
    Message,
    ToolOutput,
)
from persona_ai.domain.utils import create_id
from persona_ai.initializers.persona_configuration import PersonaAI
from persona_ai.models.base import GenAIModel
from persona_ai.personas.assistant import Assistant
from persona_ai.prompts.base import Prompt
from persona_ai.prompts.jinja import JinjaTemplatePrompt
from persona_ai.tools.manager import ToolManager
from persona_ai.transport.messagebus import MessageBus


class Technician(Assistant):
    """
    Technician is a persona that can run tools based on the input it receives.
    """

    tool_manager: ToolManager
    """
    Tool manager used by the technician to run tools.    
    """

    def __init__(
        self,
        name: str,
        scope: str,
        tool_manager: ToolManager,
        id: str = None,
        role: str = None,
        model: GenAIModel = None,
        message_bus: MessageBus = None,
        conversation_manager: ConversationManager = None,
        prompt: Prompt = None,
        can_reply_multiple_times=False,
        allow_broadcasting: bool = False,
        included_in_moderation: bool = True,
    ):
        super().__init__(
            id=id if id else create_id(prefix="technician"),
            name=name,
            role=role if role else roles.TECHNICIAN,
            scope=scope,
            model=model if model else PersonaAI.technician_model,
            message_bus=message_bus,
            prompt=prompt if prompt else JinjaTemplatePrompt(template="technician"),
            conversation_manager=conversation_manager,
            can_reply_multiple_times=can_reply_multiple_times,
            allow_broadcasting=allow_broadcasting,
            included_in_moderation=included_in_moderation,
        )

        self.tool_manager = tool_manager

    def run_tool(self, tool_suggestion: ToolSuggestion) -> dict:
        if tool_suggestion.suggested_tool is None:
            raise ValueError("Tool name is required.")

        output = self.tool_manager.execute(tool_suggestion)
        return output

    def _call_model(self, prompt):
        return self.model.generate(
            prompt, tools=self.tool_manager.get_tool_definitions()
        )

    def _generate_reply(self, body: MessageBody, request: Message) -> Message:
        message = super()._generate_reply(body, request)

        if body.tool_suggestion:
            output = self.run_tool(body.tool_suggestion)
            if not isinstance(output, dict):
                output = {"output": output}

            if "message" in output:
                message.body.text = output["message"]
                del output["message"]

            message.body.tool_suggestion = None
            message.body.tool_output = ToolOutput(
                suggestion=body.tool_suggestion, output=output
            )

        return message
