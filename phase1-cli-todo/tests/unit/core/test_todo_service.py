"""
Unit tests for the TodoService class.
Tests cover the functionality for adding tasks (US1) and other core operations.
"""

import pytest
from src.core.entities.task import Task
from src.core.services.todo_service import TodoService
from src.adapters.repositories.task_repository import InMemoryTaskRepository
from src.core.exceptions import TaskNotFoundError


class TestTodoService:
    """Test suite for TodoService functionality"""

    def setup_method(self):
        """Set up test fixtures before each test method"""
        self.repository = InMemoryTaskRepository()
        self.service = TodoService(self.repository)

    def test_add_task_success(self):
        """Test creating a new task successfully"""
        # Arrange
        title = "Test task"

        # Act
        result = self.service.add_task(title)

        # Assert
        assert result.id is not None
        assert result.id > 0
        assert result.title == "Test task"
        assert result.status == "pending"
        assert self.repository.get_by_id(result.id) is not None

    def test_add_task_with_whitespace_stripped(self):
        """Test that task titles have whitespace stripped"""
        # Arrange
        title = "  Test task with spaces  "

        # Act
        result = self.service.add_task(title)

        # Assert
        assert result.title == "Test task with spaces"

    def test_add_task_empty_title_raises_error(self):
        """Test that adding a task with empty title raises an error"""
        # Arrange
        title = ""

        # Act & Assert
        with pytest.raises(ValueError, match="Title cannot be empty"):
            self.service.add_task(title)

    def test_add_task_long_title_raises_error(self):
        """Test that adding a task with a too-long title raises an error"""
        # Arrange
        title = "A" * 101  # 101 characters, exceeding the 100 character limit

        # Act & Assert
        with pytest.raises(ValueError, match="Title exceeds maximum length"):
            self.service.add_task(title)

    def test_list_tasks_empty(self):
        """Test getting all tasks when none exist"""
        # Act
        result = self.service.list_tasks()

        # Assert
        assert len(result) == 0

    def test_list_tasks_with_data(self):
        """Test getting all tasks when some exist"""
        # Arrange
        task1 = self.service.add_task("Task 1")
        task2 = self.service.add_task("Task 2")

        # Act
        result = self.service.list_tasks()

        # Assert
        assert len(result) == 2
        titles = [task.title for task in result]
        assert "Task 1" in titles
        assert "Task 2" in titles

    def test_get_task_success(self):
        """Test getting a task by ID when it exists"""
        # Arrange
        original_task = self.service.add_task("Test task")
        task_id = original_task.id

        # Act
        result = self.service.get_task(task_id)

        # Assert
        assert result is not None
        assert result.id == task_id
        assert result.title == "Test task"
        assert result.status == "pending"

    def test_get_task_not_found(self):
        """Test getting a task by ID when it doesn't exist"""
        # Act
        result = self.service.get_task(999)

        # Assert
        assert result is None

    def test_update_task_success(self):
        """Test updating an existing task"""
        # Arrange
        original_task = self.service.add_task("Original task")
        task_id = original_task.id

        # Act
        result = self.service.update_task(task_id, "Updated task")

        # Assert
        assert result is True
        updated_task = self.repository.get_by_id(task_id)
        assert updated_task is not None
        assert updated_task.title == "Updated task"
        assert updated_task.status == "pending"  # Status should remain unchanged

    def test_update_task_not_found(self):
        """Test updating a task that doesn't exist"""
        # Act
        result = self.service.update_task(999, "Updated task")

        # Assert
        assert result is False

    def test_update_task_empty_title_raises_error(self):
        """Test that updating a task with empty title raises an error"""
        # Arrange
        original_task = self.service.add_task("Original task")
        task_id = original_task.id

        # Act & Assert
        with pytest.raises(ValueError, match="Title cannot be empty"):
            self.service.update_task(task_id, "")

    def test_update_task_long_title_raises_error(self):
        """Test that updating a task with a too-long title raises an error"""
        # Arrange
        original_task = self.service.add_task("Original task")
        task_id = original_task.id

        # Act & Assert
        with pytest.raises(ValueError, match="Title exceeds maximum length"):
            self.service.update_task(task_id, "A" * 101)

    def test_mark_complete_success(self):
        """Test marking a task as complete"""
        # Arrange
        original_task = self.service.add_task("Test task")
        task_id = original_task.id
        assert original_task.status == "pending"

        # Act
        result = self.service.mark_complete(task_id)

        # Assert
        assert result is True
        updated_task = self.repository.get_by_id(task_id)
        assert updated_task is not None
        assert updated_task.status == "completed"

    def test_mark_complete_not_found(self):
        """Test marking a task as complete when it doesn't exist"""
        # Act
        result = self.service.mark_complete(999)

        # Assert
        assert result is False

    def test_delete_task_success(self):
        """Test deleting an existing task"""
        # Arrange
        original_task = self.service.add_task("Test task")
        task_id = original_task.id

        # Act
        result = self.service.delete_task(task_id)

        # Assert
        assert result is True
        assert self.repository.get_by_id(task_id) is None

    def test_delete_task_not_found(self):
        """Test deleting a task that doesn't exist"""
        # Act
        result = self.service.delete_task(999)

        # Assert
        assert result is False