# Todo CLI Application

A command-line interface (CLI) based todo application with in-memory storage, built with Python 3.13+.

## Features

- Add, view, update, mark complete, and delete tasks
- Interactive menu-driven interface
- In-memory storage (data is lost when the application closes)
- Task validation (title length, status values)
- Error handling with user-friendly messages

## Requirements

- Python 3.13+
- UV package manager (optional, for dependency management)

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python -m src.interfaces.cli.main
   ```

## Usage

The application provides a menu-driven interface:

1. **Add Task**: Create a new task with a title
2. **List Tasks**: Display all tasks with ID, title, and status
3. **Update Task**: Modify the title of an existing task
4. **Mark Complete**: Update a task's status to 'completed'
5. **Delete Task**: Remove a task from the system
6. **Help**: Show help information
7. **Exit**: Close the application

## Architecture

The application follows a layered architecture:

- **Core Layer**: Contains entities and business logic
- **Adapters Layer**: Contains infrastructure code (repositories)
- **Interfaces Layer**: Contains the CLI interface

## Project Structure

```
src/
├── core/                 # Pure business logic (Entities, Use Cases)
│   ├── entities/
│   │   └── task.py       # Task entity definition
│   ├── repositories/
│   │   └── task_repository.py  # Repository interface
│   └── services/
│       └── todo_service.py  # Business logic service
├── adapters/             # Infrastructure code (Repositories)
│   └── repositories/
│       └── task_repository.py  # In-memory repository implementation
└── interfaces/           # Entry points (CLI)
    └── cli/
        └── main.py       # CLI application entry point
```

## Development

### Running Tests

```bash
pytest
```

### Code Formatting

```bash
black .
```

### Linting

```bash
pylint src/
```

### Type Checking

```bash
mypy src/
```

### Running command

```bash
python3 -m src.interfaces.cli.main
```