"""
Task entity representing a single todo item with attributes:
ID (auto-generated), Title (user-provided text, max 100 characters),
Status (one of: "pending", "in progress", "completed")
"""

from dataclasses import dataclass
from typing import Literal

TaskStatus = Literal["pending", "in progress", "completed"]

@dataclass
class Task:
    """
    Represents a single todo item with attributes:
    ID (auto-generated), Title (user-provided text, max 100 characters),
    Status (one of: "pending", "in progress", "completed")
    """
    id: int
    title: str
    status: TaskStatus = "pending"

    def __post_init__(self):
        """Validate the task attributes after initialization."""
        if not isinstance(self.title, str):
            raise ValueError("Title must be a string")

        if len(self.title.strip()) == 0:
            raise ValueError("Title cannot be empty")

        if len(self.title) > 100:
            raise ValueError(f"Title exceeds maximum length of 100 characters: {len(self.title)}")

        if self.status not in ["pending", "in progress", "completed"]:
            raise ValueError(f"Status must be one of: 'pending', 'in progress', 'completed'. Got: {self.status}")

    def __str__(self) -> str:
        """String representation of the task."""
        return f"Task(id={self.id}, title='{self.title}', status='{self.status}')"