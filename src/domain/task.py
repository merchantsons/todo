"""Task domain entity."""

from dataclasses import dataclass


@dataclass
class Task:
    """Represents a todo task."""

    id: int
    description: str
    completed: bool = False

    def __post_init__(self) -> None:
        """Validate task after initialization."""
        if not self.description or not self.description.strip():
            raise ValueError("Task description cannot be empty")


