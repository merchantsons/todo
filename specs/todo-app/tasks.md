# Tasks: Todo In-Memory Python Console App

**Input**: Design documents from `/specs/todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)

**Tests**: Tests are included for all user stories following TDD principles (Red-Green-Refactor).

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1, US2, US3, US4, US5)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project structure per plan.md

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project structure per implementation plan (src/domain, src/use_cases, src/interfaces, src/infrastructure, src/cli, tests/unit, tests/integration)
- [ ] T002 Initialize Python project with pytest dependency (create requirements.txt, setup.py or pyproject.toml)
- [ ] T003 [P] Configure linting and formatting tools (flake8, black, mypy for type checking)
- [ ] T004 [P] Create __init__.py files in all package directories

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T005 Create Task domain entity in src/domain/task.py with id, description, completed fields
- [ ] T006 Create TaskRepository interface in src/interfaces/task_repository.py with abstract methods (add, get_all, get_by_id, update, delete)
- [ ] T007 Create InMemoryTaskRepository implementation in src/infrastructure/in_memory_repository.py implementing TaskRepository interface
- [ ] T008 [P] Create base error classes (TaskNotFoundError, ValidationError) in src/domain/errors.py or appropriate location
- [ ] T009 [P] Setup basic CLI structure in src/cli/main.py with argparse setup and command routing skeleton

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Task (Priority: P1) 🎯 MVP

**Goal**: Users can add new tasks to their todo list with a description

**Independent Test**: Add a task, verify it appears in the list with correct ID and status

### Tests for User Story 1 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T010 [P] [US1] Unit test for AddTask use case in tests/unit/test_add_task.py (test successful add, test validation errors)
- [ ] T011 [P] [US1] Unit test for InMemoryTaskRepository.add() in tests/unit/test_in_memory_repository.py (test task storage and ID generation)
- [ ] T012 [P] [US1] Integration test for add command in tests/integration/test_cli_integration.py (test CLI add command end-to-end)

### Implementation for User Story 1

- [ ] T013 [US1] Implement AddTask use case in src/use_cases/add_task.py (validates description, calls repository)
- [ ] T014 [US1] Implement add() method in InMemoryTaskRepository (stores task, generates sequential ID)
- [ ] T015 [US1] Implement "add" command in src/cli/main.py (parses arguments, calls use case, displays result)
- [ ] T016 [US1] Add validation for empty task descriptions in AddTask use case
- [ ] T017 [US1] Add error handling and user-friendly messages for add command

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently. Users can add tasks via CLI.

---

## Phase 4: User Story 2 - View Task List (Priority: P1) 🎯 MVP

**Goal**: Users can view all their tasks with ID, description, and completion status

**Independent Test**: Add multiple tasks, view list, verify all tasks are displayed correctly

### Tests for User Story 2 ⚠️

- [ ] T018 [P] [US2] Unit test for ViewTasks use case in tests/unit/test_view_tasks.py (test retrieving all tasks, test empty list)
- [ ] T019 [P] [US2] Unit test for InMemoryTaskRepository.get_all() in tests/unit/test_in_memory_repository.py (test retrieving all stored tasks)
- [ ] T020 [P] [US2] Integration test for list command in tests/integration/test_cli_integration.py (test CLI list command with various task states)

### Implementation for User Story 2

- [ ] T021 [US2] Implement ViewTasks use case in src/use_cases/view_tasks.py (retrieves all tasks from repository)
- [ ] T022 [US2] Implement get_all() method in InMemoryTaskRepository (returns list of all tasks)
- [ ] T023 [US2] Implement "list" command in src/cli/main.py (calls use case, formats output for display)
- [ ] T024 [US2] Add formatting for task display (ID, status, description in human-readable format)
- [ ] T025 [US2] Handle empty list case with appropriate message

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently. Users can add and view tasks.

---

## Phase 5: User Story 3 - Mark Task as Complete/Incomplete (Priority: P2)

**Goal**: Users can toggle task completion status to track progress

**Independent Test**: Add a task, mark it complete, verify status change, mark incomplete, verify status change

### Tests for User Story 3 ⚠️

- [ ] T026 [P] [US3] Unit test for CompleteTask use case in tests/unit/test_complete_task.py (test marking complete, marking incomplete, test task not found)
- [ ] T027 [P] [US3] Unit test for InMemoryTaskRepository.get_by_id() and update() in tests/unit/test_in_memory_repository.py (test retrieving and updating tasks)
- [ ] T028 [P] [US3] Integration test for complete command in tests/integration/test_cli_integration.py (test CLI complete command end-to-end)

### Implementation for User Story 3

- [ ] T029 [US3] Implement CompleteTask use case in src/use_cases/complete_task.py (toggles completion status, validates task exists)
- [ ] T030 [US3] Implement get_by_id() method in InMemoryTaskRepository (retrieves task by ID, returns None if not found)
- [ ] T031 [US3] Implement update() method in InMemoryTaskRepository (updates existing task)
- [ ] T032 [US3] Implement "complete" command in src/cli/main.py (parses task ID, calls use case, displays result)
- [ ] T033 [US3] Add error handling for task not found in CompleteTask use case
- [ ] T034 [US3] Add user-friendly error messages for complete command

**Checkpoint**: At this point, User Stories 1, 2, AND 3 should all work independently. Users can add, view, and complete tasks.

---

## Phase 6: User Story 4 - Update Task (Priority: P2)

**Goal**: Users can update task descriptions to correct mistakes or refine details

**Independent Test**: Add a task, update its description, verify the change is reflected in the list

### Tests for User Story 4 ⚠️

- [ ] T035 [P] [US4] Unit test for UpdateTask use case in tests/unit/test_update_task.py (test updating description, test validation, test task not found)
- [ ] T036 [P] [US4] Integration test for update command in tests/integration/test_cli_integration.py (test CLI update command end-to-end)

### Implementation for User Story 4

- [ ] T037 [US4] Implement UpdateTask use case in src/use_cases/update_task.py (updates task description, validates input and task existence)
- [ ] T038 [US4] Implement "update" command in src/cli/main.py (parses task ID and new description, calls use case, displays result)
- [ ] T039 [US4] Add validation for empty description in UpdateTask use case
- [ ] T040 [US4] Add error handling for task not found in UpdateTask use case
- [ ] T041 [US4] Add user-friendly error messages for update command

**Checkpoint**: At this point, User Stories 1, 2, 3, AND 4 should all work independently. Users can add, view, complete, and update tasks.

---

## Phase 7: User Story 5 - Delete Task (Priority: P3)

**Goal**: Users can delete tasks that are no longer needed

**Independent Test**: Add a task, delete it, verify it no longer appears in the list

### Tests for User Story 5 ⚠️

- [ ] T042 [P] [US5] Unit test for DeleteTask use case in tests/unit/test_delete_task.py (test successful deletion, test task not found)
- [ ] T043 [P] [US5] Unit test for InMemoryTaskRepository.delete() in tests/unit/test_in_memory_repository.py (test task removal from storage)
- [ ] T044 [P] [US5] Integration test for delete command in tests/integration/test_cli_integration.py (test CLI delete command end-to-end)

### Implementation for User Story 5

- [ ] T045 [US5] Implement DeleteTask use case in src/use_cases/delete_task.py (deletes task by ID, validates task exists)
- [ ] T046 [US5] Implement delete() method in InMemoryTaskRepository (removes task from storage, returns success status)
- [ ] T047 [US5] Implement "delete" command in src/cli/main.py (parses task ID, calls use case, displays result)
- [ ] T048 [US5] Add error handling for task not found in DeleteTask use case
- [ ] T049 [US5] Add user-friendly error messages for delete command

**Checkpoint**: All user stories should now be independently functional. Users can perform all 5 basic operations (add, view, update, complete, delete).

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T050 [P] Add comprehensive help text for all CLI commands in src/cli/main.py
- [ ] T051 [P] Add type hints to all functions across all modules
- [ ] T052 Code cleanup and refactoring (ensure consistent error handling patterns)
- [ ] T053 [P] Add additional unit tests for edge cases (empty descriptions, invalid IDs, etc.)
- [ ] T054 [P] Create README.md with usage examples and installation instructions
- [ ] T055 [P] Add docstrings to all public functions and classes
- [ ] T056 Run all tests and ensure 100% pass rate
- [ ] T057 Validate all acceptance criteria from spec.md are met

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-7)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Phase 8)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - Depends on US1 for testing (needs tasks to view)
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - Depends on US1 for testing (needs tasks to complete)
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - Depends on US1 for testing (needs tasks to update)
- **User Story 5 (P3)**: Can start after Foundational (Phase 2) - Depends on US1 for testing (needs tasks to delete)

### Within Each User Story

- Tests (TDD) MUST be written and FAIL before implementation
- Domain entity (Task) before use cases
- Repository interface before implementation
- Use cases before CLI commands
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members (with coordination)

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together:
Task: "Unit test for AddTask use case in tests/unit/test_add_task.py"
Task: "Unit test for InMemoryTaskRepository.add() in tests/unit/test_in_memory_repository.py"
Task: "Integration test for add command in tests/integration/test_cli_integration.py"

# After tests are written (and failing), launch implementation:
Task: "Implement AddTask use case in src/use_cases/add_task.py"
Task: "Implement add() method in InMemoryTaskRepository"
Task: "Implement 'add' command in src/cli/main.py"
```

---

## Implementation Strategy

### MVP First (User Stories 1 & 2 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (Add Task)
4. Complete Phase 4: User Story 2 (View Tasks)
5. **STOP and VALIDATE**: Test User Stories 1 & 2 independently
6. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (Basic MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo (Full MVP!)
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1 (Add Task)
   - Developer B: User Story 2 (View Tasks) - can start after US1 has tasks
   - Developer C: User Story 3 (Complete Task) - can start after US1 has tasks
3. After P1 stories complete:
   - Developer A: User Story 4 (Update Task)
   - Developer B: User Story 5 (Delete Task)
4. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing (TDD Red-Green-Refactor)
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
- All error conditions must be tested
- All user stories must have integration tests

