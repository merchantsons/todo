"""Unit tests for DeleteTask use case."""

import pytest

from src.domain.task import Task
from src.domain.errors import TaskNotFoundError
from src.use_cases.delete_task import DeleteTask
from src.infrastructure.in_memory_repository import InMemoryTaskRepository


def test_delete_task_removes_task() -> None:
    """Test that DeleteTask removes a task from repository."""
    repository = InMemoryTaskRepository()
    task = Task(id=1, description="Test task")
    repository.add(task)
    use_case = DeleteTask(repository)

    use_case.execute(1)

    assert repository.get_by_id(1) is None


def test_delete_task_raises_error_for_nonexistent_task() -> None:
    """Test that DeleteTask raises TaskNotFoundError for non-existent task."""
    repository = InMemoryTaskRepository()
    use_case = DeleteTask(repository)

    with pytest.raises(TaskNotFoundError):
        use_case.execute(999)

