"""
Custom exception classes for the todo application.
"""


class TaskError(Exception):
    """Base exception for all task-related errors"""
    def __init__(self, message: str, error_code: str = None):
        self.message = message
        self.error_code = error_code
        super().__init__(self.message)


class TaskNotFoundError(TaskError):
    """Raised when a task with the specified ID is not found"""
    def __init__(self, task_id: int):
        super().__init__(f"Task with ID {task_id} not found", "TASK_NOT_FOUND")


class InvalidTaskTitleError(TaskError):
    """Raised when a task title is invalid"""
    def __init__(self, message: str):
        super().__init__(message, "INVALID_TASK_TITLE")


class InvalidTaskStatusError(TaskError):
    """Raised when a task status is invalid"""
    def __init__(self, status: str):
        super().__init__(
            f"Invalid task status: {status}. Must be one of: 'pending', 'in progress', 'completed'",
            "INVALID_TASK_STATUS"
        )