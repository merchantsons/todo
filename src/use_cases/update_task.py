"""UpdateTask use case - updates a task's description."""

from src.domain.errors import TaskNotFoundError, ValidationError
from src.interfaces.task_repository import TaskRepository


class UpdateTask:
    """Use case for updating a task's description."""

    def __init__(self, repository: TaskRepository) -> None:
        """Initialize with task repository."""
        self.repository = repository

    def execute(self, task_id: int, description: str):
        """Execute the update task use case."""
        from src.domain.task import Task
        
        if not description or not description.strip():
            raise ValidationError("Task description cannot be empty")

        task = self.repository.get_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(task_id)

        task.description = description.strip()
        return self.repository.update(task)

