"""Unit tests for AddTask use case."""

import pytest

from src.domain.task import Task
from src.domain.errors import ValidationError
from src.use_cases.add_task import AddTask
from src.infrastructure.in_memory_repository import InMemoryTaskRepository


def test_add_task_successfully_creates_task() -> None:
    """Test that AddTask successfully creates a task with description."""
    repository = InMemoryTaskRepository()
    use_case = AddTask(repository)

    result = use_case.execute("Buy groceries")

    assert result.id == 1
    assert result.description == "Buy groceries"
    assert result.completed is False


def test_add_task_validates_empty_description() -> None:
    """Test that AddTask raises ValidationError for empty description."""
    repository = InMemoryTaskRepository()
    use_case = AddTask(repository)

    with pytest.raises(ValidationError) as exc_info:
        use_case.execute("")

    assert "cannot be empty" in str(exc_info.value).lower()


def test_add_task_validates_whitespace_only_description() -> None:
    """Test that AddTask raises ValidationError for whitespace-only description."""
    repository = InMemoryTaskRepository()
    use_case = AddTask(repository)

    with pytest.raises(ValidationError) as exc_info:
        use_case.execute("   ")

    assert "cannot be empty" in str(exc_info.value).lower()

