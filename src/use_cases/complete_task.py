"""CompleteTask use case - toggles task completion status."""

from src.domain.errors import TaskNotFoundError
from src.interfaces.task_repository import TaskRepository


class CompleteTask:
    """Use case for toggling task completion status."""

    def __init__(self, repository: TaskRepository) -> None:
        """Initialize with task repository."""
        self.repository = repository

    def execute(self, task_id: int):
        """Execute the complete task use case."""
        from src.domain.task import Task
        
        task = self.repository.get_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(task_id)

        task.completed = not task.completed
        return self.repository.update(task)

