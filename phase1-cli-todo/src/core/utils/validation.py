"""
Validation functions for task data following the validation requirements.
"""


def validate_task_title(title: str) -> tuple[bool, str]:
    """
    Validate task title with specific requirements.

    Returns:
        tuple[bool, str]: (is_valid, error_message)
    """
    if not title or not title.strip():
        return False, "Title cannot be empty"

    if len(title.strip()) > 100:  # Based on spec clarification
        return False, f"Title exceeds maximum length of 100 characters: {len(title.strip())}"

    if not isinstance(title, str):
        return False, "Title must be a string"

    return True, ""


def validate_task_id(task_id: int) -> tuple[bool, str]:
    """
    Validate task ID with specific requirements.

    Returns:
        tuple[bool, str]: (is_valid, error_message)
    """
    if not isinstance(task_id, int):
        return False, "Task ID must be an integer"

    if task_id <= 0:
        return False, "Task ID must be a positive integer"

    return True, ""