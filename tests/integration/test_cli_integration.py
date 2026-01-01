"""
Integration tests for the CLI application.
Tests verify that the CLI commands work properly with the underlying service layer.
"""

import pytest
from unittest.mock import Mock, patch
from io import StringIO
from src.interfaces.cli.main import CLIMenuSystem


class TestCLIMenuSystem:
    """Test suite for CLI integration"""

    def setup_method(self):
        """Set up test fixtures before each test method"""
        self.cli = CLIMenuSystem()

    def test_add_task_command_integration(self):
        """Test the add task command through the CLI"""
        # Mock user input for adding a task
        with patch('builtins.input', side_effect=['Test task title']):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                # Call the method that handles adding a task
                self.cli.handle_add_task()

                # Check that the output contains the expected success message
                output = mock_stdout.getvalue()
                assert "Task added with ID:" in output
                assert "Test task title" in output

    def test_list_tasks_command_integration_empty(self):
        """Test the list tasks command when no tasks exist"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            # Call the method that handles listing tasks
            self.cli.handle_list_tasks()

            # Check that the output contains the expected message for no tasks
            output = mock_stdout.getvalue()
            assert "No tasks found" in output

    def test_list_tasks_command_integration_with_data(self):
        """Test the list tasks command when tasks exist"""
        # First, add a task to the service
        self.cli.service.add_task("Test task 1")

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            # Call the method that handles listing tasks
            self.cli.handle_list_tasks()

            # Check that the output contains the expected task
            output = mock_stdout.getvalue()
            assert "Test task 1" in output
            assert "ID | Title" in output  # Header should be present

    def test_update_task_command_integration(self):
        """Test the update task command through the CLI"""
        # First, add a task to update
        task = self.cli.service.add_task("Original task title")
        task_id = task.id

        # Mock user input for updating the task
        with patch('builtins.input', side_effect=[str(task_id), 'Updated task title']):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                # Call the method that handles updating a task
                self.cli.handle_update_task()

                # Check that the output contains the expected success message
                output = mock_stdout.getvalue()
                assert f"Task {task_id} updated successfully" in output

    def test_mark_complete_command_integration(self):
        """Test the mark complete command through the CLI"""
        # First, add a task to mark complete
        task = self.cli.service.add_task("Test task to complete")
        task_id = task.id

        # Mock user input for marking task complete
        with patch('builtins.input', side_effect=[str(task_id)]):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                # Call the method that handles marking task complete
                self.cli.handle_mark_complete()

                # Check that the output contains the expected success message
                output = mock_stdout.getvalue()
                assert f"Task {task_id} marked as completed" in output

    def test_delete_task_command_integration(self):
        """Test the delete task command through the CLI"""
        # First, add a task to delete
        task = self.cli.service.add_task("Test task to delete")
        task_id = task.id

        # Mock user input for deleting the task
        with patch('builtins.input', side_effect=[str(task_id)]):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                # Call the method that handles deleting a task
                self.cli.handle_delete_task()

                # Check that the output contains the expected success message
                output = mock_stdout.getvalue()
                assert f"Task {task_id} deleted successfully" in output

    def test_invalid_task_id_handling(self):
        """Test that CLI handles invalid task IDs gracefully"""
        # Mock user input for an invalid task ID
        with patch('builtins.input', side_effect=['999']):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                # Call the method that handles marking task complete with invalid ID
                self.cli.handle_mark_complete()

                # Check that the output contains the expected error message
                output = mock_stdout.getvalue()
                assert "not found" in output.lower()

    def test_empty_task_title_handling(self):
        """Test that CLI handles empty task titles gracefully"""
        # Mock user input for an empty task title
        with patch('builtins.input', side_effect=['']):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                # Call the method that handles adding a task with empty title
                self.cli.handle_add_task()

                # Check that the output contains the expected error message
                output = mock_stdout.getvalue()
                assert "Error:" in output
                assert "cannot be empty" in output.lower()