# Todo In-Memory Python Console App
* For GIAIC Hackathon Phase I </br>
* Roll # 00037391

A simple, in-memory todo list application built with Python 3.13+ following clean architecture principles and Spec-Driven Development.

## Features

- ✅ Add tasks
- 📋 View all tasks
- ✏️ Update task descriptions
- ✓ Mark tasks as complete/incomplete
- 🗑️ Delete tasks

## Requirements

- Python 3.13+
- pytest (for testing)

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Interactive Mode (Recommended)

Run the application in interactive mode with arrow key navigation:

```bash
python -m src.cli.main
```

or

```bash
python todo.py
```

**Interactive Features:**
- Use ↑↓ arrow keys to navigate the menu
- Press Enter to select an option
- Press Q or Ctrl+C to exit
- All operations are performed through an interactive menu

### Command-Line Mode

You can also run commands directly:

```bash
python -m src.cli.main <command> [arguments]
```

**Commands:**

**Add a task:**
```bash
python -m src.cli.main add "Buy groceries"
```

**List all tasks:**
```bash
python -m src.cli.main list
```

**Update a task:**
```bash
python -m src.cli.main update 1 "Buy groceries and milk"
```

**Mark task as complete/incomplete:**
```bash
python -m src.cli.main complete 1
```

**Delete a task:**
```bash
python -m src.cli.main delete 1
```

## Architecture

The application follows clean architecture principles with clear separation of concerns:

- **Domain Layer**: Core business entities (`Task`)
- **Use Cases Layer**: Business logic (AddTask, ViewTasks, UpdateTask, CompleteTask, DeleteTask)
- **Interfaces Layer**: Abstract contracts (`TaskRepository`)
- **Infrastructure Layer**: Concrete implementations (`InMemoryTaskRepository`)
- **CLI Layer**: User interface and command parsing

## Testing

Run tests with pytest:

```bash
pytest tests/ -v
```

## Project Structure

```
.
├── src/
│   ├── domain/          # Domain entities
│   ├── use_cases/       # Business logic
│   ├── interfaces/      # Abstract contracts
│   ├── infrastructure/  # Concrete implementations
│   └── cli/             # Command-line interface
├── tests/
│   ├── unit/            # Unit tests
│   └── integration/     # Integration tests
└── specs/
    └── todo-app/        # Specifications (spec.md, plan.md, tasks.md)
```

## Development

This project follows Spec-Driven Development (SDD) principles. All specifications are documented in `specs/todo-app/`.

## License

MIT

