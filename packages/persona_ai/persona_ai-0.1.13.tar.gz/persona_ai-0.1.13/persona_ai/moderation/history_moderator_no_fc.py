import re
from typing import List

from pydantic import BaseModel

from persona_ai.constants import TERMINATION_TOKEN
from persona_ai.domain.conversations import Message, MessageBody
from persona_ai.domain.tasks import Task
from persona_ai.models.base import GenAIModel
from persona_ai.moderation.ai_moderator import AIModerator
from persona_ai.moderation.base import ModerationResult, Rule
from persona_ai.prompts.base import Prompt
from persona_ai.prompts.jinja import JinjaTemplatePrompt
from persona_ai.transport.messagebus import Participant
from persona_ai.utils.extractors import extract_moderation_block


class HistoryModeratorOutput(BaseModel):
    thought: str
    participant: str
    participant_question: str


class HistoryModeratorOutputParser:
    """
    Parse the output the history moderator selector using regular expressions.
    It retrieves the assistant id and reasoning process.
    """

    def parse(self, text: str) -> HistoryModeratorOutput:
        print()
        print("***** OUTPUT *****")
        print(text)
        print("*****")
        print()

        text = extract_moderation_block(text)

        thought_pattern = r"Thought:\s*(.+)"
        participant_pattern = r"Participant:\s*(.+)"
        assistant_question_pattern = r"Participant Question:\s*(.+)"

        thought_match = re.search(thought_pattern, text)
        participant_match = re.search(participant_pattern, text)
        participant_question_match = re.search(
            assistant_question_pattern, text, re.DOTALL
        )

        thought = "UNKNOWN"
        participant = "UNKNOWN"
        participant_question = "UNKNOWN"

        if thought_match:
            thought = thought_match.group(1).strip()

        if participant_match:
            participant = participant_match.group(1).strip()

        if participant_question_match:
            participant_question = participant_question_match.group(1).strip()

        return HistoryModeratorOutput(
            thought=thought,
            participant=participant,
            participant_question=participant_question,
        )


class HistoryModeratorNoFc(AIModerator):
    """
    This moderator uses history to select the next participant.
    """

    refine_request = True
    """
    If True, the moderator will create a question for the next participant.
    """

    fallback_participant: Participant | None = None
    """
    Fallback participant to use if no participant is found.    
    """

    def __init__(
        self,
        model: GenAIModel = None,
        rules: List[Rule] = None,
        prompt: Prompt = None,
        refine_request=False,
        fallback_participant: Participant | None = None,
    ):
        super().__init__(model=model, rules=rules)
        self.prompt = (
            prompt if prompt else JinjaTemplatePrompt(template="history_moderator")
        )
        self.refine_request = refine_request
        self.fallback_participant = fallback_participant

    def _process_response(
        self, allowed_participants: List[Participant], response: MessageBody, task: Task
    ):
        output = HistoryModeratorOutputParser().parse(response.text)

        next_participant = output.participant
        reason = output.thought
        request_for_next_participant = output.participant_question
        participant = None
        final_answer_found = next_participant == TERMINATION_TOKEN

        if not final_answer_found:
            participant = next(
                filter(lambda p: p.id == next_participant, allowed_participants),
                None,
            )

            if self.fallback_participant:
                if not participant and task.is_first_iteration():
                    return ModerationResult(
                        next=self.fallback_participant,
                        reason="Fallback participant selected",
                        request=None,
                        final_answer_found=False,
                    )

        request = request_for_next_participant if self.refine_request else None

        return ModerationResult(
            next=participant,
            reason=reason,
            request=request,
            final_answer_found=final_answer_found,
        )

    def _render_prompt(
        self,
        allowed_participants,
        conversation_history,
        init_message: Message,
        task: Task,
    ):
        prompt = self.prompt.render(
            participants=allowed_participants,
            conversation_history=conversation_history,
            termination_token=TERMINATION_TOKEN,
            request=init_message.get_text(),
        )

        print("***** PROMPT *****")
        print(prompt)
        print("*****")

        return prompt

    def _create_tools(self, allowed_participants):
        return None
