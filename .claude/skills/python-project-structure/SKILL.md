# Skill 6: Python Project Scaffolding

**Persona**: You are a Python architect creating project structures that follow best practices for maintainability, testability, and scalability.

**Questions to ask before implementing project structure**:
- What are the main components of the application?
- How should concerns be separated (entities, services, data access, interfaces)?
- What testing approach will be used?
- How will dependencies be managed?
- What documentation is needed?

**Principles**:
- **Modularity**: Separate concerns into distinct layers
- **Testability**: Structure should enable easy testing
- **Maintainability**: Clear organization that's easy to navigate
- **Scalability**: Structure should support growth
- **Consistency**: Follow consistent patterns across the project

**Implementation Pattern**:
```python
# Project structure following the constitution guidelines:
project-root/
├── src/
│   ├── core/                 # Pure business logic (Entities, Use Cases)
│   │   ├── __init__.py
│   │   ├── entities/
│   │   │   ├── __init__.py
│   │   │   └── task.py       # Entity definition
│   │   └── use_cases/
│   │       ├── __init__.py
│   │       └── task_use_cases.py  # Business logic
│   ├── adapters/             # Infrastructure code (Repositories, etc.)
│   │   ├── __init__.py
│   │   ├── repositories/
│   │   │   ├── __init__.py
│   │   │   └── task_repository.py  # Data access implementation
│   │   └── __init__.py
│   └── interfaces/           # Entry points (CLI, APIs, etc.)
│       ├── __init__.py
│       ├── cli/
│       │   ├── __init__.py
│       │   └── main.py       # CLI application entry point
│       └── __init__.py
├── tests/
│   ├── __init__.py
│   ├── unit/
│   │   ├── __init__.py
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   └── test_entities.py
│   │   └── adapters/
│   │       ├── __init__.py
│   │       └── test_repositories.py
│   ├── integration/
│   │   ├── __init__.py
│   │   └── test_cli_integration.py
│   └── __init__.py
├── requirements.txt          # Dependencies
├── pyproject.toml           # Project configuration
└── README.md               # Documentation

# Example __init__.py files to make packages:
# src/__init__.py
"""
Application source code package.
"""

# src/core/__init__.py
"""
Core business logic package.
"""

# src/adapters/__init__.py
"""
Infrastructure adapters package.
"""

# src/interfaces/__init__.py
"""
Interface layer package.
"""
```

**When to apply**:
- Starting any new Python project
- Refactoring existing projects for better organization
- When following layered architecture principles
- When testability is a priority

**Contraindications**:
- Simple scripts or one-off tools
- Projects with specific framework requirements that conflict
- Performance-critical applications where import overhead matters