# Skill 1: Data Validation

**Persona**: You are a backend engineer implementing robust data validation to ensure data integrity and prevent application errors.

**Questions to ask before implementing validation**:
- What are the expected data types for each field?
- What are the valid value ranges or patterns?
- What are the required vs optional fields?
- How should validation errors be handled and communicated?
- What are the security implications of invalid data?

**Principles**:
- **Validate early**: Check data at the earliest possible point in the application flow
- **Fail fast**: Stop processing when invalid data is detected
- **Be specific**: Provide clear, actionable error messages
- **Sanitize inputs**: Clean data before processing to prevent injection attacks
- **Validate bounds**: Check length, size, and range limits

**Implementation Pattern**:
```python
def validate_task_title(title: str) -> tuple[bool, str]:
    """Validate task title with specific requirements"""
    if not title or not title.strip():
        return False, "Title cannot be empty"

    if len(title.strip()) > 100:  # Based on spec clarification
        return False, f"Title exceeds maximum length of 100 characters: {len(title.strip())}"

    if not isinstance(title, str):
        return False, "Title must be a string"

    return True, ""

def validate_task_id(task_id: int) -> tuple[bool, str]:
    """Validate task ID with specific requirements"""
    if not isinstance(task_id, int):
        return False, "Task ID must be an integer"

    if task_id <= 0:
        return False, "Task ID must be a positive integer"

    return True, ""
```

**When to apply**:
- All user input processing
- Data from external sources
- API request validation
- Database write operations
- Any data entering the system boundary

**Contraindications**:
- Internal data flows between trusted components
- Pre-validated data from secure sources
- Performance-critical operations where validation overhead is prohibitive