"""Interactive CLI entry point with arrow key navigation."""

import sys
from typing import Optional

from prompt_toolkit import prompt
from prompt_toolkit.application import Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout import Layout, Window, FormattedTextControl
from prompt_toolkit.layout.containers import WindowAlign
from prompt_toolkit.styles import Style

from src.domain.errors import TaskNotFoundError, ValidationError
from src.infrastructure.in_memory_repository import InMemoryTaskRepository
from src.use_cases.add_task import AddTask
from src.use_cases.view_tasks import ViewTasks
from src.use_cases.complete_task import CompleteTask
from src.use_cases.update_task import UpdateTask
from src.use_cases.delete_task import DeleteTask


class InteractiveTodoApp:
    """Interactive todo application with arrow key navigation."""

    def __init__(self):
        """Initialize the app with repository and use cases."""
        self.repository = InMemoryTaskRepository()
        self.add_task_use_case = AddTask(self.repository)
        self.view_tasks_use_case = ViewTasks(self.repository)
        self.complete_task_use_case = CompleteTask(self.repository)
        self.update_task_use_case = UpdateTask(self.repository)
        self.delete_task_use_case = DeleteTask(self.repository)
        self.selected_index = 0
        self.menu_options = [
            "Add Task",
            "List Tasks",
            "Update Task",
            "Complete/Uncomplete Task",
            "Delete Task",
            "Exit",
        ]

    def get_tasks_display(self) -> str:
        """Get formatted string of all tasks."""
        tasks = self.view_tasks_use_case.execute()
        if not tasks:
            return "No tasks found."
        lines = []
        for task in tasks:
            status = "✓" if task.completed else " "
            lines.append(f"{task.id}. [{status}] {task.description}")
        return "\n".join(lines)

    def add_task_interactive(self) -> None:
        """Interactive prompt to add a task."""
        try:
            description = prompt("Enter task description: ")
            if description.strip():
                task = self.add_task_use_case.execute(description.strip())
                print(f"\n✓ Task {task.id} added: {task.description}\n")
            else:
                print("\n✗ Task description cannot be empty\n")
        except ValidationError as e:
            print(f"\n✗ Error: {e}\n")
        except Exception as e:
            print(f"\n✗ Unexpected error: {e}\n")

    def update_task_interactive(self) -> None:
        """Interactive prompt to update a task."""
        tasks = self.view_tasks_use_case.execute()
        if not tasks:
            print("\n✗ No tasks found to update.\n")
            return

        print("\nCurrent tasks:")
        print(self.get_tasks_display())
        print()

        try:
            task_id_str = prompt("Enter task ID to update: ")
            task_id = int(task_id_str)
            new_description = prompt("Enter new description: ")
            if new_description.strip():
                task = self.update_task_use_case.execute(task_id, new_description.strip())
                print(f"\n✓ Task {task.id} updated: {task.description}\n")
            else:
                print("\n✗ Task description cannot be empty\n")
        except ValueError:
            print("\n✗ Error: Invalid task ID\n")
        except TaskNotFoundError as e:
            print(f"\n✗ Error: {e}\n")
        except ValidationError as e:
            print(f"\n✗ Error: {e}\n")
        except Exception as e:
            print(f"\n✗ Unexpected error: {e}\n")

    def complete_task_interactive(self) -> None:
        """Interactive prompt to complete/uncomplete a task."""
        tasks = self.view_tasks_use_case.execute()
        if not tasks:
            print("\n✗ No tasks found.\n")
            return

        print("\nCurrent tasks:")
        print(self.get_tasks_display())
        print()

        try:
            task_id_str = prompt("Enter task ID to toggle completion: ")
            task_id = int(task_id_str)
            task = self.complete_task_use_case.execute(task_id)
            status = "completed" if task.completed else "incomplete"
            print(f"\n✓ Task {task.id} marked as {status}: {task.description}\n")
        except ValueError:
            print("\n✗ Error: Invalid task ID\n")
        except TaskNotFoundError as e:
            print(f"\n✗ Error: {e}\n")
        except Exception as e:
            print(f"\n✗ Unexpected error: {e}\n")

    def delete_task_interactive(self) -> None:
        """Interactive prompt to delete a task."""
        tasks = self.view_tasks_use_case.execute()
        if not tasks:
            print("\n✗ No tasks found to delete.\n")
            return

        print("\nCurrent tasks:")
        print(self.get_tasks_display())
        print()

        try:
            task_id_str = prompt("Enter task ID to delete: ")
            task_id = int(task_id_str)
            self.delete_task_use_case.execute(task_id)
            print(f"\n✓ Task {task_id} deleted\n")
        except ValueError:
            print("\n✗ Error: Invalid task ID\n")
        except TaskNotFoundError as e:
            print(f"\n✗ Error: {e}\n")
        except Exception as e:
            print(f"\n✗ Unexpected error: {e}\n")

    def handle_menu_selection(self) -> bool:
        """Handle the selected menu option. Returns False if should exit."""
        option = self.menu_options[self.selected_index]

        if option == "Add Task":
            self.add_task_interactive()
            input("Press Enter to continue...")
            return True
        elif option == "List Tasks":
            print("\n" + "=" * 50)
            print("Tasks:")
            print("=" * 50)
            print(self.get_tasks_display())
            print("=" * 50 + "\n")
            input("Press Enter to continue...")
            return True
        elif option == "Update Task":
            self.update_task_interactive()
            input("Press Enter to continue...")
            return True
        elif option == "Complete/Uncomplete Task":
            self.complete_task_interactive()
            input("Press Enter to continue...")
            return True
        elif option == "Delete Task":
            self.delete_task_interactive()
            input("Press Enter to continue...")
            return True
        elif option == "Exit":
            return False

        return True

    def show_menu(self) -> int:
        """Show menu with arrow key navigation and return selected index."""
        kb = KeyBindings()

        @kb.add("up")
        def go_up(event):
            """Move selection up."""
            if self.selected_index > 0:
                self.selected_index -= 1
            else:
                self.selected_index = len(self.menu_options) - 1
            # Invalidate layout to refresh display
            event.app.invalidate()

        @kb.add("down")
        def go_down(event):
            """Move selection down."""
            if self.selected_index < len(self.menu_options) - 1:
                self.selected_index += 1
            else:
                self.selected_index = 0
            # Invalidate layout to refresh display
            event.app.invalidate()

        @kb.add("enter")
        def select_option(event):
            """Select the current option."""
            event.app.exit(result=self.selected_index)

        @kb.add("q")
        @kb.add("c-c")
        def exit_app(event):
            """Exit the application."""
            self.selected_index = len(self.menu_options) - 1  # Select Exit
            event.app.exit(result=self.selected_index)

        def get_menu_text():
            """Generate menu text with selection indicator."""
            lines = ["Todo App - Use ↑↓ to navigate, Enter to select, Q to exit\n"]
            lines.append("=" * 50)
            for i, option in enumerate(self.menu_options):
                if i == self.selected_index:
                    lines.append(f"> {option} <")
                else:
                    lines.append(f"  {option}")
            lines.append("=" * 50)
            return "\n".join(lines)

        menu_control = FormattedTextControl(get_menu_text)
        menu_window = Window(content=menu_control, align=WindowAlign.LEFT)
        layout = Layout(menu_window)

        style = Style.from_dict({
            "": "#ffffff",
        })

        app = Application(
            layout=layout,
            key_bindings=kb,
            style=style,
            full_screen=False,
        )

        try:
            result = app.run()
            return result if result is not None else self.selected_index
        except KeyboardInterrupt:
            return len(self.menu_options) - 1  # Return Exit index

    def run(self) -> None:
        """Run the interactive application."""
        while True:
            try:
                self.selected_index = self.show_menu()
                should_continue = self.handle_menu_selection()
                if not should_continue:
                    print("\nGoodbye!\n")
                    break
            except KeyboardInterrupt:
                print("\n\nGoodbye!\n")
                break
            except Exception as e:
                print(f"\nError: {e}\n")
                input("Press Enter to continue...")


def main(args: Optional[list[str]] = None) -> int:
    """Main entry point for CLI."""
    # If arguments are provided, use the old command-line interface
    if args and len(args) > 0:
        import argparse
        parser = argparse.ArgumentParser(
            description="Todo In-Memory Python Console App",
            prog="todo",
        )
        subparsers = parser.add_subparsers(dest="command", help="Available commands")

        add_parser = subparsers.add_parser("add", help="Add a new task")
        add_parser.add_argument("description", help="Task description")

        subparsers.add_parser("list", help="List all tasks")

        update_parser = subparsers.add_parser("update", help="Update a task description")
        update_parser.add_argument("id", type=int, help="Task ID")
        update_parser.add_argument("description", help="New task description")

        complete_parser = subparsers.add_parser("complete", help="Mark a task as complete/incomplete")
        complete_parser.add_argument("id", type=int, help="Task ID")

        delete_parser = subparsers.add_parser("delete", help="Delete a task")
        delete_parser.add_argument("id", type=int, help="Task ID")

        parsed_args = parser.parse_args(args)

        if not parsed_args.command:
            parser.print_help()
            return 1

        repository = InMemoryTaskRepository()

        try:
            if parsed_args.command == "add":
                use_case = AddTask(repository)
                task = use_case.execute(parsed_args.description)
                print(f"Task {task.id} added: {task.description}")
                return 0

            elif parsed_args.command == "list":
                use_case = ViewTasks(repository)
                tasks = use_case.execute()
                if not tasks:
                    print("No tasks found.")
                else:
                    for task in tasks:
                        status = "✓" if task.completed else " "
                        print(f"{task.id}. [{status}] {task.description}")
                return 0

            elif parsed_args.command == "complete":
                use_case = CompleteTask(repository)
                task = use_case.execute(parsed_args.id)
                status = "completed" if task.completed else "incomplete"
                print(f"Task {task.id} marked as {status}: {task.description}")
                return 0

            elif parsed_args.command == "update":
                use_case = UpdateTask(repository)
                task = use_case.execute(parsed_args.id, parsed_args.description)
                print(f"Task {task.id} updated: {task.description}")
                return 0

            elif parsed_args.command == "delete":
                use_case = DeleteTask(repository)
                use_case.execute(parsed_args.id)
                print(f"Task {parsed_args.id} deleted")
                return 0

            else:
                print(f"Command '{parsed_args.command}' not yet implemented", file=sys.stderr)
                return 1

        except ValidationError as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1
        except TaskNotFoundError as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1
        except Exception as e:
            print(f"Unexpected error: {e}", file=sys.stderr)
            return 1

    # Otherwise, run interactive mode
    app = InteractiveTodoApp()
    app.run()
    return 0


if __name__ == "__main__":
    sys.exit(main())
