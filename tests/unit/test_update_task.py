"""Unit tests for UpdateTask use case."""

import pytest

from src.domain.task import Task
from src.domain.errors import TaskNotFoundError, ValidationError
from src.use_cases.update_task import UpdateTask
from src.infrastructure.in_memory_repository import InMemoryTaskRepository


def test_update_task_updates_description() -> None:
    """Test that UpdateTask updates task description."""
    repository = InMemoryTaskRepository()
    task = Task(id=1, description="Original description")
    repository.add(task)
    use_case = UpdateTask(repository)

    result = use_case.execute(1, "Updated description")

    assert result.description == "Updated description"
    assert result.id == 1
    assert result.completed is False


def test_update_task_raises_error_for_nonexistent_task() -> None:
    """Test that UpdateTask raises TaskNotFoundError for non-existent task."""
    repository = InMemoryTaskRepository()
    use_case = UpdateTask(repository)

    with pytest.raises(TaskNotFoundError):
        use_case.execute(999, "New description")


def test_update_task_validates_empty_description() -> None:
    """Test that UpdateTask raises ValidationError for empty description."""
    repository = InMemoryTaskRepository()
    task = Task(id=1, description="Original")
    repository.add(task)
    use_case = UpdateTask(repository)

    with pytest.raises(ValidationError) as exc_info:
        use_case.execute(1, "")

    assert "cannot be empty" in str(exc_info.value).lower()


