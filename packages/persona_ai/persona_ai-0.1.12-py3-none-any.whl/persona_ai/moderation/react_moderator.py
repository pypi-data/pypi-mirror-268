import logging
import re
from typing import List

from pydantic import BaseModel

from persona_ai.constants import TERMINATION_TOKEN
from persona_ai.models.base import GenAIModel
from persona_ai.moderation.ai_moderator import AIModerator
from persona_ai.moderation.base import ModerationResult, Rule
from persona_ai.prompts.base import Prompt
from persona_ai.prompts.jinja import JinjaTemplatePrompt
from persona_ai.transport.messagebus import Participant
from persona_ai.domain.conversations import Message, MessageBody
from persona_ai.domain.tasks import Task
from persona_ai.tools.base import ToolDefinition

_logger = logging.getLogger(__name__)
_DEBUG = False


class ReactModeratorOutput(BaseModel):
    thought: str
    assistant: str
    assistant_question: str
    final_answer: str


class ReactModeratorOutputParser:
    """
    Parse the output the ReAct moderator selector using regular expressions. It retrieves the assistant id and reasoning process.
    """

    def parse(self, text: str) -> ReactModeratorOutput:
        thought_pattern = r"(?:Thought: )?(.*?)(?=Assistant|Final Answer|$)"
        assistant_pattern = r"Assistant:\s*(.+)"
        assistant_question_pattern = r"Assistant Question:\s*(.+)"
        final_answer_pattern = r"Final Answer:\s*(.+)"

        thought_match = re.search(thought_pattern, text, re.DOTALL)
        assistant_match = re.search(assistant_pattern, text)
        assistant_question_match = re.search(
            assistant_question_pattern, text, re.DOTALL
        )
        final_answer_match = re.search(final_answer_pattern, text, re.DOTALL)

        thought = "UNKNOWN"
        assistant = "UNKNOWN"
        assistant_question = "UNKNOWN"
        final_answer = "UNKNOWN"

        if thought_match:
            thought = thought_match.group(1).replace("Thought:", "").strip()

        if assistant_match:
            assistant = assistant_match.group(1).strip()

        if assistant_question_match:
            assistant_question = assistant_question_match.group(1).strip()

        if final_answer_match:
            final_answer = final_answer_match.group(1).strip()

        return ReactModeratorOutput(
            thought=thought,
            assistant=assistant,
            assistant_question=assistant_question,
            final_answer=final_answer,
        )


class ReactModerator(AIModerator):
    """
    This moderator uses a ReAct prompt to select the next participant.
    Compared to HistoryModerator, this is more precise but less flexible.
    """

    def __init__(
        self,
        model: GenAIModel = None,
        rules: List[Rule] = None,
        prompt: Prompt = None,
    ):
        super().__init__(model=model, rules=rules)
        self.prompt = (
            prompt if prompt else JinjaTemplatePrompt(template="react_moderator")
        )

    def _process_response(
        self, allowed_participants: List[Participant], response: MessageBody, task: Task
    ):
        output = ReactModeratorOutputParser().parse(response.text)

        next_participant = output.assistant
        reason = output.thought
        request_for_next_participant = output.assistant_question
        final_answer = output.final_answer
        final_answer_found = (
            output.final_answer is not None
            and output.final_answer != "UNKNOWN"
            and output.final_answer != ""
        )

        logging.debug(
            f"next_participant: {next_participant}, reason: {reason}, request_for_next_participant: {request_for_next_participant}, final_answer_found: {final_answer_found}, final_answer: {final_answer}"
        )

        participant = next(
            filter(lambda p: p.id == next_participant, allowed_participants),
            None,
        )

        return ModerationResult(
            next=participant,
            reason=reason,
            request=request_for_next_participant,
            final_answer_found=final_answer_found,
            final_answer=final_answer,
        )

    def _render_iterations(self, task: Task):
        iterations = []
        for i in task.iterations:
            assistant = i.participant_id
            # if i.output.body.tool_suggestion:
            #    assistant = i.output.body.tool_suggestion.suggested_tool
            iterations.append(
                f"Thought: {i.reason}\nAssistant: {assistant}\nAssistant Question: {i.request}\nObservation: {i.output.get_text()}"
            )

        return "\n".join(iterations)

    def _render_prompt(
        self,
        allowed_participants,
        conversation_history,
        init_message: Message,
        task: Task,
    ):
        history_until_init_message = [
            m for m in conversation_history if m.timestamp < init_message.timestamp
        ]

        prompt = self.prompt.render(
            participants=allowed_participants,
            conversation_history=history_until_init_message,
            termination_token=TERMINATION_TOKEN,
            request=init_message.get_text(),
            iterations=self._render_iterations(task),
            first_iteration=task.is_first_iteration(),
        )

        if _DEBUG:
            print()
            print("************** REACT MODERATOR PROMPT **************")
            print(prompt)
            print("************** ************** ************** *******")
            print()

        return prompt

    def _create_tools(self, allowed_participants) -> List[ToolDefinition] | None:
        return None

    def _get_generation_kwargs(self):
        return {"stop_sequences": ["Observation"]}
