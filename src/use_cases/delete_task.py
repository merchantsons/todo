"""DeleteTask use case - removes a task from the repository."""

from src.domain.errors import TaskNotFoundError
from src.interfaces.task_repository import TaskRepository


class DeleteTask:
    """Use case for deleting a task."""

    def __init__(self, repository: TaskRepository) -> None:
        """Initialize with task repository."""
        self.repository = repository

    def execute(self, task_id: int) -> None:
        """Execute the delete task use case."""
        task = self.repository.get_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(task_id)

        self.repository.delete(task_id)

