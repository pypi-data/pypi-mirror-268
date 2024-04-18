from persona_ai.domain.conversations import Message
from persona_ai.domain.repositories import MongoTasksRepository
from persona_ai.domain.tasks import Task, TaskStatus
from persona_ai.domain.utils import create_id


class TaskManager:
    """
    Task manager is responsible for managing tasks.
    """

    tasks_repository: MongoTasksRepository
    """
    Repository used to store tasks.        
    """

    def __init__(self, repository: MongoTasksRepository):
        self.tasks_repository = repository

    def get_pending_task(self, conversation_id: str) -> Task:
        """
        Get the pending task for the given conversation.
        """
        task = next(
            iter(
                self.tasks_repository.find(
                    {
                        "init_message.conversation_id": conversation_id,
                        "status": TaskStatus.PENDING,
                    }
                )
            ),
            None,
        )

        return task

    def start_task(self, init_message: Message) -> Task:
        """
        Start a new task.
        """
        task = Task(id=create_id(prefix="task"), init_message=init_message)
        self.tasks_repository.create(task)
        return task

    def finish_pending_task(self, task: Task, status: str) -> Task | None:
        """
        Finish the pending task.
        """
        task.status = status
        self.tasks_repository.update(task)
        return task

    def iterate(
        self,
        task: Task,
        originating_message: Message,
        participant_id: str,
        reasoning: str,
        request: str,
    ):
        """
        Iterate the task.
        """
        task.iterate(
            originating_message=originating_message,
            participant_id=participant_id,
            reason=reasoning,
            request=request,
        )
        self.tasks_repository.update(task)

    def set_iteration_output(self, task, message):
        """
        Set the iteration output.
        """
        task.set_iteration_output(message)
        self.tasks_repository.update(task)

    def get_by_id(self, id: str) -> Task | None:
        """
        Get the task by id.
        """
        return self.tasks_repository.get_by_id(id)
