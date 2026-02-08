"""
Integration tests for the CLI application.
Tests verify that the CLI commands work properly with the underlying service layer.
"""

import pytest
from unittest.mock import Mock, patch
from io import StringIO
from src.interfaces.cli.main import CLIMenuSystem, console


class TestCLIMenuSystem:
    """Test suite for CLI integration"""

    def setup_method(self):
        """Set up test fixtures before each test method"""
        self.cli = CLIMenuSystem()

    def _capture_output(self, method, prompt_inputs=None):
        """Helper to capture rich console output and optionally mock Prompt.ask."""
        buf = StringIO()
        console.file = buf
        try:
            if prompt_inputs is not None:
                side_effects = list(prompt_inputs)
                with patch('src.interfaces.cli.main.Prompt.ask', side_effect=side_effects):
                    method()
            else:
                method()
        finally:
            console.file = None  # reset to default stdout
        return buf.getvalue()

    def test_add_task_command_integration(self):
        """Test the add task command through the CLI"""
        output = self._capture_output(self.cli.handle_add_task, ['Test task title'])
        assert "Task Added Successfully" in output
        assert "Test task title" in output

    def test_list_tasks_command_integration_empty(self):
        """Test the list tasks command when no tasks exist"""
        output = self._capture_output(self.cli.handle_list_tasks)
        assert "No tasks found" in output

    def test_list_tasks_command_integration_with_data(self):
        """Test the list tasks command when tasks exist"""
        self.cli.service.add_task("Test task 1")
        output = self._capture_output(self.cli.handle_list_tasks)
        assert "Test task 1" in output
        assert "Task List" in output

    def test_update_task_command_integration(self):
        """Test the update task command through the CLI"""
        task = self.cli.service.add_task("Original task title")
        task_id = task.id
        output = self._capture_output(self.cli.handle_update_task, [str(task_id), 'Updated task title'])
        assert f"Task {task_id} updated successfully" in output

    def test_mark_complete_command_integration(self):
        """Test the mark complete command through the CLI"""
        task = self.cli.service.add_task("Test task to complete")
        task_id = task.id
        output = self._capture_output(self.cli.handle_mark_complete, [str(task_id)])
        assert f"Task {task_id} marked as completed" in output

    def test_delete_task_command_integration(self):
        """Test the delete task command through the CLI"""
        task = self.cli.service.add_task("Test task to delete")
        task_id = task.id
        output = self._capture_output(self.cli.handle_delete_task, [str(task_id)])
        assert f"Task {task_id} deleted successfully" in output

    def test_invalid_task_id_handling(self):
        """Test that CLI handles invalid task IDs gracefully"""
        output = self._capture_output(self.cli.handle_mark_complete, ['999'])
        assert "not found" in output.lower()

    def test_empty_task_title_handling(self):
        """Test that CLI handles empty task titles gracefully"""
        output = self._capture_output(self.cli.handle_add_task, [''])
        assert "cannot be empty" in output.lower()
