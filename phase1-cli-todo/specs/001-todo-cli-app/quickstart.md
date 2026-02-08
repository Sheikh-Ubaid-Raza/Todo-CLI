# Quickstart Guide: Phase I - Todo In-Memory Python Console App

**Date**: 2026-01-01
**Feature**: Phase I - Todo In-Memory Python Console App

## Getting Started

### Prerequisites
- Python 3.13+
- UV package manager

### Installation
1. Clone the repository
2. Navigate to the project directory
3. Install dependencies: `uv sync` (or `pip install -r requirements.txt`)

### Running the Application
```bash
python src/main.py
```

## Basic Usage

### Starting the Application
When you run the application, you'll see a menu with options:
```
Todo CLI Application
====================
1. Add Task
2. List Tasks
3. Update Task
4. Mark Complete
5. Delete Task
6. Help
7. Exit
Choose an option (1-7):
```

### Adding a Task
- Option 1 or command: `add "Buy groceries"`
- The system will assign an auto-generated ID
- Example: `add "Complete project proposal"`

### Listing Tasks
- Option 2 or command: `list`
- Shows all tasks with ID, title, and status
- Example output:
```
ID | Title                    | Status
---|--------------------------|--------
1  | Buy groceries            | pending
2  | Complete project         | completed
```

### Updating a Task
- Option 3 or command: `update 1 "Updated task title"`
- Updates the title of the task with the specified ID
- Example: `update 1 "Buy groceries and cook dinner"`

### Marking Complete
- Option 4 or command: `complete 1`
- Changes the status of the task to "completed"
- Example: `complete 1`

### Deleting a Task
- Option 5 or command: `delete 1`
- Removes the task with the specified ID
- Example: `delete 1`

### Getting Help
- Option 6 or command: `help`
- Displays available commands and usage

### Exiting the Application
- Option 7 or command: `exit`
- Safely closes the application