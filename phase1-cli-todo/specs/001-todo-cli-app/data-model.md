# Data Model: Phase I - Todo In-Memory Python Console App

**Date**: 2026-01-01
**Feature**: Phase I - Todo In-Memory Python Console App

## Task Entity

### Attributes
- **id**: Integer (auto-generated, unique, required)
  - Auto-incrementing integer identifier
  - Primary identifier for the task
  - Generated automatically when a new task is created

- **title**: String (user-provided, required)
  - The main content/description of the task
  - Must be non-empty string
  - Maximum length: 500 characters (to prevent display issues)

- **status**: String/Enum (required)
  - Values: "pending", "completed"
  - Default value: "pending"
  - Represents the completion state of the task

### Validation Rules
- Title must not be empty or contain only whitespace
- ID must be unique within the system
- Status must be one of the allowed values ("pending", "completed")
- Title length should be between 1 and 500 characters

### State Transitions
- Default state: "pending"
- "pending" → "completed" (when task is marked complete)
- No reverse transition allowed in this phase (completed tasks remain completed)

## Repository Interface

### Abstract Base Class: TaskRepository
- **create(task: Task) -> Task**: Creates a new task with auto-generated ID
- **get_all() -> List[Task]**: Returns all tasks
- **get_by_id(id: int) -> Task | None**: Returns task with given ID or None
- **update(id: int, task: Task) -> Task | None**: Updates existing task, returns updated task or None if not found
- **delete(id: int) -> bool**: Deletes task by ID, returns True if successful, False if not found

## Service Layer

### TodoService
- **add_task(title: str) -> Task**: Creates a new task with the provided title
- **list_tasks() -> List[Task]**: Returns all tasks
- **get_task(id: int) -> Task | None**: Returns task with given ID
- **update_task(id: int, title: str) -> bool**: Updates the title of an existing task
- **mark_complete(id: int) -> bool**: Marks a task as completed
- **delete_task(id: int) -> bool**: Removes a task from the system
- **validate_task(title: str) -> bool**: Validates task data before creation/updating