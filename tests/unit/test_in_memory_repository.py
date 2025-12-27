"""Unit tests for InMemoryTaskRepository."""

import pytest

from src.domain.task import Task
from src.domain.errors import TaskNotFoundError
from src.infrastructure.in_memory_repository import InMemoryTaskRepository


def test_add_task_stores_and_assigns_id() -> None:
    """Test that adding a task stores it and assigns sequential ID."""
    repository = InMemoryTaskRepository()
    task = Task(id=0, description="Test task")

    result = repository.add(task)

    assert result.id == 1
    assert result.description == "Test task"
    assert result.completed is False


def test_add_multiple_tasks_generates_sequential_ids() -> None:
    """Test that adding multiple tasks generates sequential IDs."""
    repository = InMemoryTaskRepository()
    task1 = Task(id=0, description="Task 1")
    task2 = Task(id=0, description="Task 2")

    result1 = repository.add(task1)
    result2 = repository.add(task2)

    assert result1.id == 1
    assert result2.id == 2


def test_get_all_retrieves_all_tasks() -> None:
    """Test that get_all returns all stored tasks."""
    repository = InMemoryTaskRepository()
    task1 = Task(id=0, description="Task 1")
    task2 = Task(id=0, description="Task 2")

    repository.add(task1)
    repository.add(task2)

    all_tasks = repository.get_all()
    assert len(all_tasks) == 2
    assert all_tasks[0].description == "Task 1"
    assert all_tasks[1].description == "Task 2"


def test_get_by_id_retrieves_existing_task() -> None:
    """Test that get_by_id retrieves a task by ID."""
    repository = InMemoryTaskRepository()
    task = Task(id=0, description="Test task")
    added_task = repository.add(task)

    retrieved = repository.get_by_id(added_task.id)

    assert retrieved is not None
    assert retrieved.id == added_task.id
    assert retrieved.description == "Test task"


def test_get_by_id_returns_none_for_nonexistent_task() -> None:
    """Test that get_by_id returns None for non-existent task."""
    repository = InMemoryTaskRepository()

    result = repository.get_by_id(999)

    assert result is None

