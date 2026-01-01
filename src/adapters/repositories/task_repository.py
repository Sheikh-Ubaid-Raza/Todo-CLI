"""
In-memory implementation of task repository following the repository pattern.
This implementation stores tasks in memory only (non-persistent).
"""

from typing import List, Optional
from src.core.repositories.task_repository import TaskRepository
from src.core.entities.task import Task


class InMemoryTaskRepository(TaskRepository):
    """In-memory implementation of task repository"""

    def __init__(self):
        self._tasks = {}
        self._next_id = 1

    def create(self, task: Task) -> Task:
        """Create a new task with auto-generated ID and store it in memory"""
        task.id = self._next_id
        self._next_id += 1
        self._tasks[task.id] = task
        return task

    def get_all(self) -> List[Task]:
        """Get all tasks from memory"""
        return list(self._tasks.values())

    def get_by_id(self, task_id: int) -> Optional[Task]:
        """Get a task by ID from memory, return None if not found"""
        return self._tasks.get(task_id)

    def update(self, task_id: int, task: Task) -> Optional[Task]:
        """Update an existing task in memory, return updated task or None if not found"""
        if task_id in self._tasks:
            # Ensure the ID stays consistent
            task.id = task_id
            self._tasks[task_id] = task
            return task
        return None

    def delete(self, task_id: int) -> bool:
        """Delete a task by ID from memory, return True if successful"""
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False