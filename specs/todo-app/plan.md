# Implementation Plan: Todo In-Memory Python Console App

**Branch**: `todo-app` | **Date**: 2025-12-28 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/todo-app/spec.md`

## Summary

This plan implements a Python in-memory Todo CLI application following clean architecture principles. The application supports 5 core features (Add, View, Update, Complete/Incomplete, Delete) using Python 3.13+, in-memory storage, and a console-based interface. The architecture separates domain logic from infrastructure, enabling future extensibility while maintaining simplicity for the current requirements.

## Technical Context

**Language/Version**: Python 3.13+  
**Primary Dependencies**: Standard library only (argparse for CLI, dataclasses for entities, typing for type hints)  
**Storage**: In-memory (Python dictionaries/lists) - NO database, NO file persistence  
**Testing**: pytest (standard Python testing framework)  
**Target Platform**: Command-line interface (Windows, Linux, macOS)  
**Project Type**: Single application (CLI tool)  
**Performance Goals**: Sub-second response times for all operations, handle 1000+ tasks in memory  
**Constraints**: In-memory only (no persistence), console I/O only, minimal dependencies  
**Scale/Scope**: Single-user application, up to 1000 tasks in memory, console-based interaction

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

✅ **I. Spec-Driven Development**: Specifications created first (spec.md, plan.md, tasks.md)  
✅ **II. Clean Architecture**: Architecture follows clean architecture with domain, use cases, interfaces, and infrastructure layers  
✅ **III. Technology Constraints**: Python 3.13+, in-memory storage, console-based interface  
✅ **IV. Feature Completeness**: All 5 Basic Level features specified  
✅ **V. Specification Quality**: Complete, unambiguous, testable specifications  
✅ **VI. Knowledge Capture**: PHR files will be created for all development interactions

**All constitution gates PASSED** - Proceeding with implementation planning.

## Project Structure

### Documentation (this feature)

```text
specs/todo-app/
├── spec.md              # Feature specification (user stories, requirements)
├── plan.md              # This file (architectural design)
├── tasks.md             # Task breakdown (to be created)
└── [future: research.md, data-model.md, quickstart.md, contracts/]
```

### Source Code (repository root)

```text
src/
├── domain/
│   ├── __init__.py
│   └── task.py          # Task entity (domain model)
├── use_cases/
│   ├── __init__.py
│   ├── add_task.py      # AddTask use case
│   ├── view_tasks.py    # ViewTasks use case
│   ├── update_task.py   # UpdateTask use case
│   ├── complete_task.py # CompleteTask use case
│   └── delete_task.py   # DeleteTask use case
├── interfaces/
│   ├── __init__.py
│   └── task_repository.py  # TaskRepository interface (abstract base class)
├── infrastructure/
│   ├── __init__.py
│   └── in_memory_repository.py  # InMemoryTaskRepository implementation
└── cli/
    ├── __init__.py
    └── main.py          # CLI entry point and command parsing

tests/
├── unit/
│   ├── __init__.py
│   ├── test_task.py
│   ├── test_add_task.py
│   ├── test_view_tasks.py
│   ├── test_update_task.py
│   ├── test_complete_task.py
│   ├── test_delete_task.py
│   └── test_in_memory_repository.py
└── integration/
    ├── __init__.py
    └── test_cli_integration.py
```

**Structure Decision**: Single project structure with clean architecture layers (domain, use_cases, interfaces, infrastructure, cli). This structure supports future extensibility (e.g., adding file persistence, database storage) while maintaining clear separation of concerns for the current in-memory implementation.

## Architecture Design

### Clean Architecture Layers

#### 1. Domain Layer (`src/domain/`)
- **Purpose**: Core business entities and domain logic
- **Components**:
  - `Task` entity: Represents a todo task with id, description, completed status
  - Domain validation rules (e.g., description cannot be empty)
- **Dependencies**: None (pure Python, no external dependencies)

#### 2. Use Cases Layer (`src/use_cases/`)
- **Purpose**: Business logic and application-specific rules
- **Components**:
  - `AddTask`: Creates new tasks with validation
  - `ViewTasks`: Retrieves and formats task list
  - `UpdateTask`: Updates task descriptions
  - `CompleteTask`: Toggles task completion status
  - `DeleteTask`: Removes tasks from repository
- **Dependencies**: Domain layer, Interfaces layer
- **Input/Output**: Each use case takes repository interface and input parameters, returns result objects

#### 3. Interfaces Layer (`src/interfaces/`)
- **Purpose**: Abstract contracts for infrastructure implementations
- **Components**:
  - `TaskRepository`: Abstract base class defining storage operations
    - `add(task: Task) -> Task`
    - `get_all() -> List[Task]`
    - `get_by_id(task_id: int) -> Optional[Task]`
    - `update(task: Task) -> Task`
    - `delete(task_id: int) -> bool`
- **Dependencies**: Domain layer
- **Note**: Uses Python's `abc` module for abstract base classes

#### 4. Infrastructure Layer (`src/infrastructure/`)
- **Purpose**: Concrete implementations of interfaces
- **Components**:
  - `InMemoryTaskRepository`: In-memory storage using Python dictionary
    - Stores tasks in dictionary keyed by task ID
    - Auto-generates sequential task IDs
    - Provides thread-safe operations (if needed in future)
- **Dependencies**: Domain layer, Interfaces layer

#### 5. Presentation Layer (`src/cli/`)
- **Purpose**: User interface and command parsing
- **Components**:
  - `main.py`: Entry point, command-line argument parsing using `argparse`
    - Commands: `add`, `list`, `update`, `complete`, `delete`
    - Error handling and user-friendly messages
    - Output formatting (human-readable and optionally JSON)
- **Dependencies**: Use Cases layer, Infrastructure layer

### Data Flow

```
CLI (main.py)
  ↓
Use Case (e.g., AddTask)
  ↓
Repository Interface (TaskRepository)
  ↓
Infrastructure (InMemoryTaskRepository)
  ↓
Domain (Task entity)
```

### Interface Contracts

#### TaskRepository Interface

```python
class TaskRepository(ABC):
    @abstractmethod
    def add(self, task: Task) -> Task:
        """Add a new task. Returns the task with assigned ID."""
        
    @abstractmethod
    def get_all(self) -> List[Task]:
        """Retrieve all tasks. Returns list of all tasks."""
        
    @abstractmethod
    def get_by_id(self, task_id: int) -> Optional[Task]:
        """Retrieve task by ID. Returns task or None if not found."""
        
    @abstractmethod
    def update(self, task: Task) -> Task:
        """Update an existing task. Returns updated task or raises error if not found."""
        
    @abstractmethod
    def delete(self, task_id: int) -> bool:
        """Delete a task by ID. Returns True if deleted, False if not found."""
```

#### Error Handling

- **TaskNotFoundError**: Raised when operations reference non-existent task IDs
- **ValidationError**: Raised when input validation fails (e.g., empty description)
- **Error Messages**: User-friendly messages displayed to console via stderr

### Non-Functional Requirements

#### Performance
- **Response Time**: All operations complete in < 1 second for up to 1000 tasks
- **Memory**: Efficient in-memory storage using dictionary (O(1) lookup by ID)
- **Scalability**: Handles up to 1000 tasks without performance degradation

#### Reliability
- **Error Handling**: All error conditions are caught and reported with clear messages
- **Input Validation**: All user input is validated before processing
- **Idempotency**: Operations like "mark complete" are idempotent (safe to repeat)

#### Security
- **Input Validation**: All user input is validated to prevent injection or malformed data
- **No External Dependencies**: Minimal attack surface (standard library only)
- **No Persistence**: No sensitive data stored on disk

#### Maintainability
- **Clean Architecture**: Clear separation of concerns enables future changes
- **Type Hints**: All functions use Python type hints for better IDE support and documentation
- **Testability**: Each layer can be tested independently with dependency injection

## Key Decisions and Rationale

### Decision 1: Clean Architecture Structure
**Options Considered**:
- A) Monolithic single file
- B) Simple module structure (models, services, cli)
- C) Clean architecture with layers

**Chosen**: Option C - Clean architecture with layers

**Rationale**: 
- Enables future extensibility (e.g., adding file persistence, database storage)
- Clear separation of concerns makes code easier to test and maintain
- Follows constitution principle II (Clean Architecture)
- Minimal overhead for current requirements, significant benefit for future changes

**Trade-offs**: Slightly more complex structure than needed for MVP, but aligns with project principles and future needs.

### Decision 2: In-Memory Storage Implementation
**Options Considered**:
- A) Python list with linear search
- B) Python dictionary keyed by task ID
- C) Custom data structure

**Chosen**: Option B - Python dictionary keyed by task ID

**Rationale**:
- O(1) lookup by ID (vs O(n) for list)
- Simple implementation using standard library
- Efficient for up to 1000 tasks
- Easy to extend to other storage backends via interface

**Trade-offs**: Dictionary provides fast lookups but requires ID management. Sequential ID generation is simple and sufficient.

### Decision 3: Command-Line Interface Library
**Options Considered**:
- A) Manual argument parsing (sys.argv)
- B) argparse (standard library)
- C) click or other third-party library

**Chosen**: Option B - argparse

**Rationale**:
- Standard library (no external dependencies)
- Provides help text generation
- Handles argument validation
- Sufficient for console CLI requirements

**Trade-offs**: More verbose than click, but avoids external dependencies per constitution.

### Decision 4: Task ID Generation
**Options Considered**:
- A) Sequential integers (1, 2, 3...)
- B) UUIDs
- C) Timestamp-based IDs

**Chosen**: Option A - Sequential integers

**Rationale**:
- Simple and human-readable
- Easy to reference in CLI commands
- Sufficient for in-memory single-user application
- Can be extended to UUIDs in future if needed

**Trade-offs**: Sequential IDs are simpler but less robust for distributed systems (not needed for current scope).

## Risk Analysis and Mitigation

### Risk 1: Memory Constraints with Large Task Lists
**Blast Radius**: Application performance degradation or crashes
**Mitigation**: 
- Design for 1000 tasks (well within Python memory limits)
- Use efficient data structures (dictionary)
- Document memory constraints in user documentation

### Risk 2: Input Validation Gaps
**Blast Radius**: Application errors or unexpected behavior
**Mitigation**:
- Comprehensive input validation in use cases
- Clear error messages for all error conditions
- Integration tests covering edge cases

### Risk 3: Future Extensibility Challenges
**Blast Radius**: Difficult to add features like persistence or GUI
**Mitigation**:
- Clean architecture enables easy extension
- Interface-based design allows swapping implementations
- Well-documented architecture decisions

## Evaluation and Validation

### Definition of Done
- [ ] All 5 features implemented and tested
- [ ] All unit tests passing
- [ ] Integration tests passing
- [ ] Code follows clean architecture structure
- [ ] Type hints on all functions
- [ ] Error handling for all error conditions
- [ ] User-friendly CLI with help text
- [ ] Documentation complete (README, usage examples)

### Output Validation
- Specifications are complete and unambiguous
- Architecture follows clean architecture principles
- All technology constraints met (Python 3.13+, in-memory, console-based)
- Code generation ready (specifications enable AI code generation)

## Follow-ups and Risks

### Future Work (Out of Scope for Phase I)
- File persistence (save/load tasks to JSON file)
- Task categories or tags
- Task priorities and sorting
- Search and filtering capabilities
- Task export/import functionality

### Areas Requiring More Detail
- Specific CLI command syntax and examples (to be refined in tasks.md)
- Error message exact wording (to be refined during implementation)
- Output formatting details (to be refined during implementation)

### Architectural Risks
- **Low Risk**: Current architecture is well-suited for requirements
- **Medium Risk**: Future persistence requirements may require additional abstraction layers
- **Low Risk**: Performance is sufficient for in-memory operations

