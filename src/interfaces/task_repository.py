"""TaskRepository interface - abstract contract for task storage."""

from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.task import Task


class TaskRepository(ABC):
    """Abstract base class for task storage operations."""

    @abstractmethod
    def add(self, task: Task) -> Task:
        """Add a new task. Returns the task with assigned ID."""
        pass

    @abstractmethod
    def get_all(self) -> List[Task]:
        """Retrieve all tasks. Returns list of all tasks."""
        pass

    @abstractmethod
    def get_by_id(self, task_id: int) -> Optional[Task]:
        """Retrieve task by ID. Returns task or None if not found."""
        pass

    @abstractmethod
    def update(self, task: Task) -> Task:
        """Update an existing task. Returns updated task or raises error if not found."""
        pass

    @abstractmethod
    def delete(self, task_id: int) -> bool:
        """Delete a task by ID. Returns True if deleted, False if not found."""
        pass


