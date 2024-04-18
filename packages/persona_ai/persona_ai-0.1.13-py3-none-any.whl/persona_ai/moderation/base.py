import time
from abc import ABC, abstractmethod
from typing import List

from persona_ai.constants import MAX_PARTICIPANT_IDLE_SECONDS
from persona_ai.domain.conversations import Message
from persona_ai.domain.tasks import Task
from persona_ai.personas.base import Persona
from persona_ai.transport.messagebus import Participant


class ModerationResult:
    """
    Represents the result of the moderation process.
    """

    next: Participant | None
    reason: str
    request: str = None
    final_answer_found: bool
    final_answer: str = None

    def __init__(
        self,
        next: Participant | None,
        reason: str,
        request: str = None,
        final_answer_found: bool = False,
        final_answer: str = None,
    ):
        self.next = next
        self.reason = reason
        self.request = request
        self.final_answer_found = final_answer_found
        self.final_answer = final_answer

    def to_dict(self):
        return {
            "next": self.next.id if self.next else None,
            "reason": self.reason,
            "request": self.request,
            "final_answer_found": self.final_answer_found,
            "final_answer": self.final_answer,
        }


class Rule(ABC):
    """
    Base interface for a rule that selects a participant.
    """

    @abstractmethod
    def select(
        self,
        conversation_history: List[Message],
        participants: List[Participant],
        task: Task,
    ) -> ModerationResult | None:
        pass


class Moderator:
    """Base interface for participants selector."""

    rules: List[Rule] = []

    def __init__(self, rules: List[Rule] = None):
        if rules:
            self.rules = rules

    def moderate(
        self,
        conversation_history: List[Message],
        participants: List[Participant],
        task: Task,
        message: Message,
        sender: Participant,
    ) -> ModerationResult:
        """Select a next participant that will continue the conversation."""

        allowed_participants = self._get_allowed_participants(
            message, participants, sender, task
        )

        if len(allowed_participants) == 1:
            return ModerationResult(
                allowed_participants[0], "Only one participant available"
            )

        for rule in self.rules:
            result = rule.select(conversation_history, allowed_participants, task)
            if result:
                return result

        return ModerationResult(None, "No next participant found")

    def _get_allowed_participants(self, message: Message, participants, sender, task):
        return [
            a
            for a in participants
            if a.included_in_moderation
            if a.id != task.init_message.sender_id
            if a.id != message.sender_id or sender.can_reply_multiple_times
            if (time.time() - a.last_activity) < (MAX_PARTICIPANT_IDLE_SECONDS * 1000)
        ]

    def begin_with(self, participant: Participant, request: str = None):
        """
        Add a rule that conversation should begin with a specific participant.
        """
        self.rules.append(BeginWithParticipantRule(participant, request))

    def continue_with(
        self, previous_sender: Persona, next_sender: Persona, request: str = None
    ):
        """
        Add a rule that conversation should continue with a specific participant.
        """
        self.rules.append(SequenceRule(previous_sender, next_sender, request))

    def finish_with(self, participant: Participant, request: str = None):
        """
        Add a rule that conversation should finish with a specific participant.
        """
        self.rules.append(FinishWithParticipantRule(participant, request))

    def set_iteration_limit(self, max_iterations: int):
        """
        Add a rule that conversation should finish after a specific number of iterations.
        """
        self.rules.append(IterationLimitRule(max_iterations))

    def add_lambda_rule(self, rule: callable, request: str = None):
        """
        Add a rule that is a lambda function.
        """
        self.rules.append(LambdaRule(rule, request))


class SequenceRule(Rule):
    """
    A rule that conversation should continue with a specific participant.
    """

    def __init__(
        self, previous_sender: Persona, next_sender: Persona, request: str = None
    ):
        self.previous_sender = previous_sender
        self.next_sender = next_sender
        self.request = request

    def select(
        self,
        conversation_history: List[Message],
        participants: List[Participant],
        task: Task,
    ) -> ModerationResult | None:
        last_message = conversation_history[-1]
        if last_message.sender_id == self.previous_sender.id:
            return ModerationResult(
                self.next_sender, "Next sender in sequence", self.request
            )
        return None


class IterationLimitRule(Rule):
    """
    A rule that conversation should finish after a specific number of iterations.
    """

    def __init__(self, max_iterations: int):
        self.max_iterations = max_iterations

    def select(
        self,
        conversation_history: List[Message],
        participants: List[Participant],
        task: Task,
    ) -> ModerationResult | None:
        if len(task.iterations) >= self.max_iterations:
            return ModerationResult(
                None, "Messages limit reached", final_answer_found=True
            )
        return None


class BeginWithParticipantRule(Rule):
    """
    A rule that conversation should begin with a specific participant.
    """

    def __init__(self, participant: Participant, request: str = None):
        self.participant = participant
        self.request = request

    def select(
        self,
        conversation_history: List[Message],
        participants: List[Participant],
        task: Task,
    ) -> ModerationResult | None:
        if task.is_first_iteration():
            return ModerationResult(
                self.participant, "Begin with participant", self.request
            )
        return None


class FinishWithParticipantRule(Rule):
    """
    A rule that conversation should finish with a specific participant.
    """

    def __init__(self, participant: Participant, request: str = None):
        self.participant = participant
        self.request = request

    def select(
        self,
        conversation_history: List[Message],
        participants: List[Participant],
        task: Task,
    ) -> ModerationResult | None:
        if conversation_history[-1].sender_id == self.participant.id:
            return ModerationResult(
                None,
                "Finish with participant",
                final_answer_found=True,
                request=self.request,
            )
        return None


class LambdaRule(Rule):
    """
    A rule that is a lambda function.
    """

    def __init__(self, rule: callable, request: str = None):
        self.rule = rule
        self.request = request

    def select(
        self,
        conversation_history: List[Message],
        participants: List[Participant],
        task: Task,
    ) -> ModerationResult | None:
        return self.rule(conversation_history, participants, task, self.request)
