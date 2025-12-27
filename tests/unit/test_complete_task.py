"""Unit tests for CompleteTask use case."""

import pytest

from src.domain.task import Task
from src.domain.errors import TaskNotFoundError
from src.use_cases.complete_task import CompleteTask
from src.infrastructure.in_memory_repository import InMemoryTaskRepository


def test_complete_task_marks_task_as_complete() -> None:
    """Test that CompleteTask marks an incomplete task as complete."""
    repository = InMemoryTaskRepository()
    task = Task(id=1, description="Test task", completed=False)
    repository.add(task)
    use_case = CompleteTask(repository)

    result = use_case.execute(1)

    assert result.completed is True
    assert result.id == 1
    assert result.description == "Test task"


def test_complete_task_marks_task_as_incomplete() -> None:
    """Test that CompleteTask marks a complete task as incomplete."""
    repository = InMemoryTaskRepository()
    task = Task(id=1, description="Test task", completed=True)
    repository.add(task)
    use_case = CompleteTask(repository)

    result = use_case.execute(1)

    assert result.completed is False


def test_complete_task_raises_error_for_nonexistent_task() -> None:
    """Test that CompleteTask raises TaskNotFoundError for non-existent task."""
    repository = InMemoryTaskRepository()
    use_case = CompleteTask(repository)

    with pytest.raises(TaskNotFoundError):
        use_case.execute(999)

