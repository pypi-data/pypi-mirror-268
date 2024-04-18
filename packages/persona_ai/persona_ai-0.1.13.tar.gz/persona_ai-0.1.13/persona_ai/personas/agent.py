import logging
import re

from pydantic import BaseModel

from persona_ai.conversations.manager import ConversationManager
from persona_ai.domain import events
from persona_ai.domain.conversations import (
    MessageBody,
    Message,
    ToolSuggestion,
    create_message,
    ToolOutput,
)
from persona_ai.domain.events import Event
from persona_ai.domain.utils import create_id
from persona_ai.initializers.persona_configuration import PersonaAI
from persona_ai.models.base import GenAIModel
from persona_ai.personas.technician import Technician
from persona_ai.prompts.base import Prompt
from persona_ai.prompts.text import TextPrompt
from persona_ai.tools.manager import ToolManager
from persona_ai.transport.messagebus import MessageBus

logger = logging.getLogger(__name__)


class AgentOutput(BaseModel):
    thought: str
    action: str
    action_input: str
    final_answer: str | None


class AgentOutputParser:
    """
    Parse the output the ReAct moderator selector using regular expressions. It retrieves the assistant id and reasoning process.
    """

    def parse(self, text: str) -> AgentOutput:
        thought_pattern = r"(?:Thought: )?(.*?)(?=Action|Final Answer|$)"
        action_pattern = r"Action:\s*(.+)"
        action_input_pattern = r"Action Input:\s*(.+)"
        final_answer_pattern = r"Final Answer:\s*(.+)"

        thought_match = re.search(thought_pattern, text, re.DOTALL)
        action_match = re.search(action_pattern, text)
        action_input_match = re.search(action_input_pattern, text, re.DOTALL)
        final_answer_match = re.search(final_answer_pattern, text, re.DOTALL)

        thought = "UNKNOWN"
        action = "UNKNOWN"
        action_input = "UNKNOWN"
        final_answer = "UNKNOWN"

        if thought_match:
            thought = thought_match.group(1).replace("Thought:", "").strip()

        if action_match:
            action = action_match.group(1).strip()

        if action_input_match:
            action_input = action_input_match.group(1).strip()

        if final_answer_match:
            final_answer = final_answer_match.group(1).strip()

        return AgentOutput(
            thought=thought,
            action=action,
            action_input=action_input,
            final_answer=final_answer,
        )


class Agent(Technician):
    """
    Agent persona.
    An agent is a technician that loops with the model and use tools until
    the conversation is finished and a final answer was found.
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
            name,
            scope,
            tool_manager,
            id if id else create_id(prefix="agent"),
            role,
            model if model else PersonaAI.agent_model,
            message_bus,
            conversation_manager,
            prompt if prompt else TextPrompt("{request}"),
            can_reply_multiple_times,
            allow_broadcasting,
            included_in_moderation,
        )

        if not self.model.is_chat_supported:
            raise ValueError("Model does not support chat")

    def receive(self, message: Message, **kwargs):
        self.conversation_manager.add_message(message)
        self.conversation_manager.mark_has_received(message)

        history = self.conversation_manager.get_history(
            conversation_id=message.conversation_id
        )

        chat = self.model.start_chat()

        response: MessageBody = None

        while response is None or response.tool_output is not None:
            if response is None:
                response = chat.send_message(
                    history, tools=self.tool_manager.get_tool_definitions()
                )
            else:
                response = chat.send_message(
                    create_message(
                        conversation_id=message.conversation_id,
                        sender_id=self.id,
                        sender_role=self.role,
                        sender_name=self.name,
                        body=response,
                    ),
                    tools=self.tool_manager.get_tool_definitions(),
                )

            logger.debug(
                f"Agent received response from model. Response is {response.json()}"
            )

            if response is None:
                logger.warning("Agent response call returned None")

            tool_output = {}
            if response.tool_suggestion is not None:
                tool_output = self.run_tool(response.tool_suggestion)
                response.tool_output = ToolOutput(
                    suggestion=response.tool_suggestion, output=tool_output
                )
                response.tool_suggestion = None

                self.message_bus.publish_event(
                    Event(
                        sender_id=self.id,
                        conversation_id=message.conversation_id,
                        type=events.AGENT_STEP,
                        body={
                            "agent_id": self.id,
                            "conversation_id": message.conversation_id,
                            "tool_suggestion": response.tool_output.suggestion,
                            "tool_output": response.tool_output.output,
                        },
                    )
                )

        logger.debug(
            f"Agent received final message from model. Response is {message.get_text()}"
        )

        if message.reply:
            recipient = (
                message.reply_to if message.reply_to is not None else message.sender_id
            )
            self.send(
                create_message(
                    conversation_id=message.conversation_id,
                    sender_id=self.id,
                    sender_role=self.role,
                    sender_name=self.name,
                    body=response,
                ),
                recipient,
            )

    def run_tool(self, tool_suggestion: ToolSuggestion) -> dict:
        return super().run_tool(tool_suggestion)

    def _call_model(self, prompt):
        return super()._call_model(prompt)

    def _generate_reply(self, body: MessageBody, request: Message) -> Message:
        return super()._generate_reply(body, request)
