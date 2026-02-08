"""
Abstract base class for task data access following the repository pattern.
This interface defines the contract for all task repository implementations.
"""

from abc import ABC, abstractmethod
from typing import List, Optional
from src.core.entities.task import Task


class TaskRepository(ABC):
    """Abstract base class for task data access"""

    @abstractmethod
    def create(self, task: Task) -> Task:
        """Create a new task and return it with any generated fields"""
        pass

    @abstractmethod
    def get_all(self) -> List[Task]:
        """Get all tasks"""
        pass

    @abstractmethod
    def get_by_id(self, task_id: int) -> Optional[Task]:
        """Get a task by ID, return None if not found"""
        pass

    @abstractmethod
    def update(self, task_id: int, task: Task) -> Optional[Task]:
        """Update an existing task, return updated task or None if not found"""
        pass

    @abstractmethod
    def delete(self, task_id: int) -> bool:
        """Delete a task by ID, return True if successful"""
        pass