# CLI Command Contracts: Phase I - Todo In-Memory Python Console App

**Date**: 2026-01-01
**Feature**: Phase I - Todo In-Memory Python Console App

## Command Interface Specification

### Add Task Command
- **Command**: `add <title>`
- **Input**: Title as string argument
- **Success Response**:
  - Returns: New task with auto-generated ID
  - Format: "Task added with ID: {id} - {title}"
- **Error Responses**:
  - Empty title: "Error: Task title cannot be empty"
  - Invalid format: "Error: Please provide a task title"

### List Tasks Command
- **Command**: `list` or `ls`
- **Input**: None
- **Success Response**:
  - Returns: List of all tasks
  - Format:
    ```
    ID | Title                    | Status
    ---|--------------------------|--------
    1  | Buy groceries            | pending
    2  | Complete project         | completed
    ```
- **Error Responses**:
  - No tasks: "No tasks found"

### Update Task Command
- **Command**: `update <id> <new_title>`
- **Input**: Task ID (integer) and new title (string)
- **Success Response**:
  - Returns: Updated task
  - Format: "Task {id} updated: {new_title}"
- **Error Responses**:
  - Invalid ID: "Error: Task with ID {id} not found"
  - Empty title: "Error: Task title cannot be empty"
  - Invalid format: "Error: Usage: update <id> <new_title>"

### Mark Complete Command
- **Command**: `complete <id>` or `done <id>`
- **Input**: Task ID (integer)
- **Success Response**:
  - Returns: Confirmation message
  - Format: "Task {id} marked as completed"
- **Error Responses**:
  - Invalid ID: "Error: Task with ID {id} not found"

### Delete Task Command
- **Command**: `delete <id>`
- **Input**: Task ID (integer)
- **Success Response**:
  - Returns: Confirmation message
  - Format: "Task {id} deleted"
- **Error Responses**:
  - Invalid ID: "Error: Task with ID {id} not found"

### Help Command
- **Command**: `help` or `--help` or `-h`
- **Input**: None
- **Success Response**:
  - Returns: List of available commands with usage
  - Format: Display help text with all available commands

### Exit Command
- **Command**: `exit` or `quit` or `q`
- **Input**: None
- **Success Response**:
  - Returns: Exit confirmation
  - Format: "Goodbye!" and exits application