# Skill 2: Error Handling

**Persona**: You are a backend engineer designing resilient applications that handle errors gracefully and provide actionable information to users.

**Questions to ask before implementing error handling**:
- What error categories exist in this system? (user errors, system errors, network errors)
- Should errors be retryable or terminal?
- What information helps debugging without exposing security details?
- How do errors propagate through layers (CLI → Service → Repository)?
- How should the application behave after an error occurs?

**Principles**:
- **Never fail silently**: Always handle or propagate errors appropriately
- **Provide clear messages**: Give users actionable information to resolve issues
- **Maintain application flow**: Return to main menu after errors rather than exiting
- **Log for debugging**: Record sufficient information for troubleshooting
- **Separate concerns**: Differentiate between user-facing messages and internal logs

**Implementation Pattern**:
```python
class TaskError(Exception):
    """Base exception for all task-related errors"""

    def __init__(self, message: str, error_code: str = None):
        self.message = message
        self.error_code = error_code
        super().__init__(self.message)

def handle_operation_error(operation_name: str, error: Exception) -> str:
    """Handle errors during operations and return user-friendly message"""
    if isinstance(error, TaskError):
        return f"Error during {operation_name}: {error.message}"
    else:
        # Log the full error for debugging
        logger.error(f"Unexpected error during {operation_name}: {str(error)}")
        # Return generic message to user
        return f"An unexpected error occurred during {operation_name}. Please try again."
```

**When to apply**:
- All user-facing operations
- Data access operations
- Input processing
- Any operation that could fail
- External system interactions

**Contraindications**:
- Performance-critical operations where error handling overhead is prohibitive
- Internal system monitoring (may need different error patterns)