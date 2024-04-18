from typing import List

from pydantic import BaseModel

from persona_ai.constants import DEFAULT_MAX_ITERATIONS
from persona_ai.domain.conversations import Message


class TaskStatus:
    """Community task status."""

    PENDING = "pending"
    """Task is pending."""

    STARTED = "started"
    """Task is started."""

    COMPLETED = "completed"
    """Task is completed."""

    FAILED = "failed"
    """Task is failed."""


class TaskIteration(BaseModel):
    iteration_number: int
    """Iteration number."""

    originating_message: Message
    """The message that originate the iteration."""

    participant_id: str | None
    """The participant  selected for this step by the moderator."""

    response_message: Message | None
    """The response message."""

    reason: str | None
    """The reasoning for the candidate selection."""

    final_answer_found: bool = False
    """Flag to indicate if the final answer was found."""

    output: Message | None
    """The output for this iteration."""

    request: str | None
    """The request for the next iteration."""


class MaxIterationsExceedsError(Exception):
    pass


class Task(BaseModel):
    """
    Represents a task in a conversation, managed by a party.
    A conversation can have one running task at time
    """

    id: str
    """Task id."""

    status: str = TaskStatus.PENDING
    """Task status."""

    max_iterations: int = DEFAULT_MAX_ITERATIONS
    """Maximum number of iterations."""

    init_message: Message
    """The message that originate the task."""

    iterations: List[TaskIteration] = []
    """Task iterations."""

    def iterate(
        self,
        originating_message: Message,
        participant_id: str | None,
        reason: str | None,
        final_answer_found: bool = False,
        request: str = None,
    ) -> TaskIteration:
        if len(self.iterations) >= self.max_iterations:
            raise MaxIterationsExceedsError()

        iteration = TaskIteration(
            iteration_number=len(self.iterations) + 1,
            originating_message=originating_message,
            participant_id=participant_id,
            reason=reason,
            final_answer_found=final_answer_found,
            response_message=None,
            output=None,
            request=request,
        )
        self.iterations.append(iteration)
        return iteration

    def is_iterable(self) -> bool:
        return len(self.iterations) < self.max_iterations

    def set_iteration_output(self, message):
        if len(self.iterations) == 0:
            return

        previous_iteration = self.iterations[-1]
        previous_iteration.output = message

    def is_first_iteration(self) -> bool:
        return len(self.iterations) == 0
