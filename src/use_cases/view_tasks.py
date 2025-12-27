"""ViewTasks use case - retrieves all tasks from the repository."""

from typing import List

from src.domain.task import Task
from src.interfaces.task_repository import TaskRepository


class ViewTasks:
    """Use case for viewing all tasks."""

    def __init__(self, repository: TaskRepository) -> None:
        """Initialize with task repository."""
        self.repository = repository

    def execute(self) -> List[Task]:
        """Execute the view tasks use case."""
        return self.repository.get_all()

