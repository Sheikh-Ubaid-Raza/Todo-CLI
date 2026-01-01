# Skill 3: Repository Pattern Implementation

**Persona**: You are a backend engineer implementing data access layers that abstract storage implementation details and enable easy migration between different storage systems.

**Questions to ask before implementing repository pattern**:
- What storage system will be used initially?
- What operations are needed for this entity type?
- How will the repository interface be defined?
- How will the repository be injected into services?
- What will be the migration path to other storage systems?

**Principles**:
- **Abstract storage details**: Hide implementation details behind clean interfaces
- **Use abstract base classes**: Define contracts that can be implemented by different storage systems
- **Separate concerns**: Repository handles data access, services handle business logic
- **Enable dependency injection**: Allow repositories to be swapped or mocked for testing
- **Maintain consistency**: All repositories should follow the same interface patterns

**Implementation Pattern**:
```python
from abc import ABC, abstractmethod
from typing import List, Optional
from entities.task import Task

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

class InMemoryTaskRepository(TaskRepository):
    """In-memory implementation of task repository"""

    def __init__(self):
        self._tasks = {}
        self._next_id = 1

    def create(self, task: Task) -> Task:
        task.id = self._next_id
        self._next_id += 1
        self._tasks[task.id] = task
        return task

    def get_all(self) -> List[Task]:
        return list(self._tasks.values())

    def get_by_id(self, task_id: int) -> Optional[Task]:
        return self._tasks.get(task_id)

    def update(self, task_id: int, task: Task) -> Optional[Task]:
        if task_id in self._tasks:
            task.id = task_id  # Ensure ID consistency
            self._tasks[task_id] = task
            return task
        return None

    def delete(self, task_id: int) -> bool:
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False
```

**When to apply**:
- All data access operations
- When building applications that might need storage migration
- When you need to mock data access for testing
- When implementing layered architecture

**Contraindications**:
- Simple scripts where data access is minimal
- Performance-critical applications where abstraction overhead is prohibitive
- Applications with only a single, fixed data source