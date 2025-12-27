"""In-memory implementation of TaskRepository."""

from typing import List, Optional

from src.domain.task import Task
from src.domain.errors import TaskNotFoundError
from src.interfaces.task_repository import TaskRepository


class InMemoryTaskRepository(TaskRepository):
    """In-memory storage implementation using Python dictionary."""

    def __init__(self) -> None:
        """Initialize the repository with empty storage."""
        self._tasks: dict[int, Task] = {}
        self._next_id: int = 1

    def add(self, task: Task) -> Task:
        """Add a new task. Assigns ID and stores in memory."""
        task.id = self._next_id
        self._tasks[task.id] = task
        self._next_id += 1
        return task

    def get_all(self) -> List[Task]:
        """Retrieve all tasks."""
        return list(self._tasks.values())

    def get_by_id(self, task_id: int) -> Optional[Task]:
        """Retrieve task by ID."""
        return self._tasks.get(task_id)

    def update(self, task: Task) -> Task:
        """Update an existing task."""
        if task.id not in self._tasks:
            raise TaskNotFoundError(task.id)
        self._tasks[task.id] = task
        return task

    def delete(self, task_id: int) -> bool:
        """Delete a task by ID."""
        if task_id not in self._tasks:
            return False
        del self._tasks[task_id]
        return True


