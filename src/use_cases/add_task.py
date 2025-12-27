"""AddTask use case - adds a new task to the repository."""

from src.domain.task import Task
from src.domain.errors import ValidationError
from src.interfaces.task_repository import TaskRepository


class AddTask:
    """Use case for adding a new task."""

    def __init__(self, repository: TaskRepository) -> None:
        """Initialize with task repository."""
        self.repository = repository

    def execute(self, description: str) -> Task:
        """Execute the add task use case."""
        if not description or not description.strip():
            raise ValidationError("Task description cannot be empty")

        task = Task(id=0, description=description.strip())
        return self.repository.add(task)

