# Skill 4: Test Generation

**Persona**: You are a quality engineer creating comprehensive tests that follow TDD principles and ensure application reliability.

**Questions to ask before generating tests**:
- What are the functional requirements that need to be tested?
- What are the edge cases that need to be considered?
- What are the error conditions that need to be handled?
- What is the expected test coverage goal?
- How will tests be organized and structured?

**Principles**:
- **Test Driven Development**: Write tests before implementation
- **100% coverage for business logic**: As required by constitution
- **Clear test names**: Describe what is being tested and the expected outcome
- **Arrange-Act-Assert pattern**: Structure tests with clear phases
- **Isolation**: Each test should be independent and not depend on others

**Implementation Pattern**:
```python
import pytest
from entities.task import Task
from repositories.task_repository import InMemoryTaskRepository

class TestInMemoryTaskRepository:
    """Test suite for InMemoryTaskRepository"""

    def setup_method(self):
        """Set up test fixtures before each test method"""
        self.repo = InMemoryTaskRepository()

    def test_create_task_success(self):
        """Test creating a new task successfully"""
        # Arrange
        task = Task(title="Test task", status="pending")

        # Act
        result = self.repo.create(task)

        # Assert
        assert result.id is not None
        assert result.id > 0
        assert result.title == "Test task"
        assert result.status == "pending"
        assert self.repo.get_by_id(result.id) is not None

    def test_get_all_tasks_empty(self):
        """Test getting all tasks when none exist"""
        # Act
        result = self.repo.get_all()

        # Assert
        assert len(result) == 0

    def test_get_all_tasks_with_data(self):
        """Test getting all tasks when some exist"""
        # Arrange
        task1 = Task(title="Task 1", status="pending")
        task2 = Task(title="Task 2", status="completed")
        self.repo.create(task1)
        self.repo.create(task2)

        # Act
        result = self.repo.get_all()

        # Assert
        assert len(result) == 2
        titles = [task.title for task in result]
        assert "Task 1" in titles
        assert "Task 2" in titles

    def test_get_by_id_success(self):
        """Test getting a task by ID when it exists"""
        # Arrange
        original_task = Task(title="Test task", status="pending")
        created_task = self.repo.create(original_task)

        # Act
        result = self.repo.get_by_id(created_task.id)

        # Assert
        assert result is not None
        assert result.id == created_task.id
        assert result.title == "Test task"
        assert result.status == "pending"

    def test_get_by_id_not_found(self):
        """Test getting a task by ID when it doesn't exist"""
        # Act
        result = self.repo.get_by_id(999)

        # Assert
        assert result is None

    def test_update_task_success(self):
        """Test updating an existing task"""
        # Arrange
        original_task = Task(title="Original task", status="pending")
        created_task = self.repo.create(original_task)
        updated_task = Task(title="Updated task", status="in progress")

        # Act
        result = self.repo.update(created_task.id, updated_task)

        # Assert
        assert result is not None
        assert result.id == created_task.id
        assert result.title == "Updated task"
        assert result.status == "in progress"

    def test_update_task_not_found(self):
        """Test updating a task that doesn't exist"""
        # Arrange
        task = Task(title="Test task", status="pending")

        # Act
        result = self.repo.update(999, task)

        # Assert
        assert result is None

    def test_delete_task_success(self):
        """Test deleting an existing task"""
        # Arrange
        task = Task(title="Test task", status="pending")
        created_task = self.repo.create(task)

        # Act
        result = self.repo.delete(created_task.id)

        # Assert
        assert result is True
        assert self.repo.get_by_id(created_task.id) is None

    def test_delete_task_not_found(self):
        """Test deleting a task that doesn't exist"""
        # Act
        result = self.repo.delete(999)

        # Assert
        assert result is False
```

**When to apply**:
- All business logic implementations
- Before writing implementation code
- When refactoring existing code
- When adding new features or functionality

**Contraindications**:
- Experimental or proof-of-concept code
- One-time scripts that won't be maintained
- Performance benchmarks where test overhead matters