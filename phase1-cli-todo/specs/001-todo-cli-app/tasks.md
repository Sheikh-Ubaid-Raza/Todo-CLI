---
description: "Task list template for feature implementation"
---

# Tasks: Phase I - Todo In-Memory Python Console App

**Input**: Design documents from `/specs/001-todo-cli-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/` or `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan
- [X] T002 Initialize Python 3.13+ project with UV dependencies
- [X] T003 [P] Configure linting and formatting tools (pylint, black, mypy)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [X] T004 Create Task entity with id, title (max 100 chars), status (pending/in progress/completed) in src/core/entities/task.py
- [X] T005 [P] Create abstract TaskRepository interface in src/core/repositories/task_repository.py
- [X] T006 [P] Create InMemoryTaskRepository implementation in src/adapters/repositories/task_repository.py
- [X] T007 Create TodoService with all required methods in src/core/services/todo_service.py
- [X] T008 Setup CLI menu system in src/interfaces/cli/main.py
- [X] T009 Create validation functions for task data in src/core/utils/validation.py
- [X] T010 Create custom exception classes in src/core/exceptions.py
- [X] T011 Setup pytest configuration in pyproject.toml
- [X] T012 Create requirements.txt with dependencies (pytest for testing)

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Tasks (Priority: P1) 🎯 MVP

**Goal**: User can create new tasks in the todo application with auto-generated IDs

**Independent Test**: Can be fully tested by running the CLI app, entering the add task command with a title, and verifying that a new task with an ID is created and stored in memory

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T013 [P] [US1] Unit test for add_task functionality in tests/unit/core/test_todo_service.py
- [X] T014 [P] [US1] Integration test for CLI add command in tests/integration/test_cli_integration.py

### Implementation for User Story 1

- [X] T015 [P] [US1] Implement Task entity with proper validation in src/core/entities/task.py
- [X] T016 [P] [US1] Implement add_task method in TodoService in src/core/services/todo_service.py
- [X] T017 [US1] Implement CLI command for adding tasks in src/interfaces/cli/main.py
- [X] T018 [US1] Add input validation for task titles (max 100 chars) in src/core/utils/validation.py
- [X] T019 [US1] Add error handling for empty titles in src/core/exceptions.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View All Tasks (Priority: P2)

**Goal**: User can see all tasks they have created to understand their current todo list

**Independent Test**: Can be fully tested by adding some tasks, then running the view command, and verifying that all tasks are displayed with their ID, title, and completion status

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [X] T020 [P] [US2] Unit test for list_tasks functionality in tests/unit/core/test_todo_service.py
- [X] T021 [P] [US2] Integration test for CLI list command in tests/integration/test_cli_integration.py

### Implementation for User Story 2

- [X] T022 [P] [US2] Implement list_tasks method in TodoService in src/core/services/todo_service.py
- [X] T023 [US2] Implement CLI command for listing tasks in src/interfaces/cli/main.py
- [X] T024 [US2] Add formatting for task display with ID, title, and status in src/interfaces/cli/main.py
- [X] T025 [US2] Add handling for empty task list in src/interfaces/cli/main.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update Task Content (Priority: P3)

**Goal**: User can modify the content of existing tasks by specifying the task ID

**Independent Test**: Can be fully tested by adding a task, then running the update command with the task ID and new content, and verifying that the task title is updated

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [X] T026 [P] [US3] Unit test for update_task functionality in tests/unit/core/test_todo_service.py
- [X] T027 [P] [US3] Integration test for CLI update command in tests/integration/test_cli_integration.py

### Implementation for User Story 3

- [X] T028 [P] [US3] Implement update_task method in TodoService in src/core/services/todo_service.py
- [X] T029 [US3] Implement CLI command for updating tasks in src/interfaces/cli/main.py
- [X] T030 [US3] Add validation for existing task ID in src/core/services/todo_service.py
- [X] T031 [US3] Add error handling for non-existent task IDs in src/core/exceptions.py

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Mark Task as Complete (Priority: P4)

**Goal**: User can mark tasks as completed to track progress

**Independent Test**: Can be fully tested by adding a task, then running the mark complete command with the task ID, and verifying that the task status is updated to 'Completed'

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [X] T032 [P] [US4] Unit test for mark_complete functionality in tests/unit/core/test_todo_service.py
- [X] T033 [P] [US4] Integration test for CLI complete command in tests/integration/test_cli_integration.py

### Implementation for User Story 4

- [X] T034 [P] [US4] Implement mark_complete method in TodoService in src/core/services/todo_service.py
- [X] T035 [US4] Implement CLI command for marking tasks as complete in src/interfaces/cli/main.py
- [X] T036 [US4] Add validation for existing task ID in src/core/services/todo_service.py
- [X] T037 [US4] Add error handling for non-existent task IDs in src/core/exceptions.py

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Delete Task (Priority: P5)

**Goal**: User can remove tasks that are no longer needed

**Independent Test**: Can be fully tested by adding a task, then running the delete command with the task ID, and verifying that the task is removed from memory

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [X] T038 [P] [US5] Unit test for delete_task functionality in tests/unit/core/test_todo_service.py
- [X] T039 [P] [US5] Integration test for CLI delete command in tests/integration/test_cli_integration.py

### Implementation for User Story 5

- [X] T040 [P] [US5] Implement delete_task method in TodoService in src/core/services/todo_service.py
- [X] T041 [US5] Implement CLI command for deleting tasks in src/interfaces/cli/main.py
- [X] T042 [US5] Add validation for existing task ID in src/core/services/todo_service.py
- [X] T043 [US5] Add error handling for non-existent task IDs in src/core/exceptions.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T044 [P] Add comprehensive docstrings to all public methods and classes
- [X] T045 Add error handling for invalid user inputs in CLI menu system
- [X] T046 [P] Add help command implementation in src/interfaces/cli/main.py
- [X] T047 [P] Add exit command implementation in src/interfaces/cli/main.py
- [X] T048 Add consistent error message formatting across all operations
- [X] T049 [P] Documentation updates in README.md
- [X] T050 Code cleanup and refactoring
- [X] T051 [P] Additional unit tests in tests/unit/ (if requested)
- [X] T052 Run quickstart validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3 → P4 → P5)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "T013 [P] [US1] Unit test for add_task functionality in tests/unit/core/test_todo_service.py"
Task: "T014 [P] [US1] Integration test for CLI add command in tests/integration/test_cli_integration.py"

# Launch all implementation tasks for User Story 1 together:
Task: "T015 [P] [US1] Implement Task entity with proper validation in src/core/entities/task.py"
Task: "T016 [P] [US1] Implement add_task method in TodoService in src/core/services/todo_service.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence