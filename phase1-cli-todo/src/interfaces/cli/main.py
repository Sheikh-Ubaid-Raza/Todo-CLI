#!/usr/bin/env python3
"""
Main CLI application entry point for the todo application.
Implements a menu-driven interface for task management with rich UI.
"""

import sys
from typing import Optional
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich.text import Text
from rich.theme import Theme
from src.core.entities.task import Task
from src.adapters.repositories.task_repository import InMemoryTaskRepository
from src.core.services.todo_service import TodoService
from src.core.exceptions import TaskNotFoundError

# Cyber Slate theme
cyber_theme = Theme({
    "info": "dim cyan",
    "success": "bold green",
    "warning": "bold yellow",
    "error": "bold red",
    "menu.number": "bold cyan",
    "menu.text": "white",
})

console = Console(theme=cyber_theme)


def display_welcome() -> None:
    """Display the branded welcome header."""
    header = Text()
    header.append("AgenTodo", style="bold cyan")
    header.append("\n")
    header.append("The Evolution of Todo - AI-Powered & Spec-Driven", style="italic white")
    console.print(Panel(header, border_style="cyan", padding=(1, 2)))


class CLIMenuSystem:
    """Base class for implementing menu-driven CLI applications"""

    def __init__(self) -> None:
        self.running = True
        # Initialize the repository and service
        repository = InMemoryTaskRepository()
        self.service = TodoService(repository)

    def display_menu(self) -> None:
        """Display the main menu options."""
        menu_items = [
            ("1", "Add Task"),
            ("2", "List Tasks"),
            ("3", "Update Task"),
            ("4", "Mark Complete"),
            ("5", "Delete Task"),
            ("6", "Help"),
            ("7", "Exit"),
        ]
        menu_text = Text()
        for num, label in menu_items:
            menu_text.append(f"  [{num}] ", style="menu.number")
            menu_text.append(f"{label}\n", style="menu.text")
        menu_text.rstrip()
        console.print(Panel(menu_text, title="[bold cyan]Menu[/bold cyan]", border_style="dim cyan", padding=(0, 1)))

    def get_user_choice(self) -> Optional[int]:
        """Get and validate user menu choice"""
        try:
            choice = Prompt.ask("[bold cyan]Choose an option[/bold cyan]", choices=["1", "2", "3", "4", "5", "6", "7"], show_choices=False)
            return int(choice)
        except KeyboardInterrupt:
            console.print("\n[info]Exiting application...[/info]")
            return 7
        except EOFError:
            console.print("\n[info]Exiting application...[/info]")
            return 7

    def run(self) -> None:
        """Main application loop"""
        display_welcome()
        while self.running:
            self.display_menu()
            choice = self.get_user_choice()

            if choice is None:
                continue

            if choice == 1:
                self.handle_add_task()
            elif choice == 2:
                self.handle_list_tasks()
            elif choice == 3:
                self.handle_update_task()
            elif choice == 4:
                self.handle_mark_complete()
            elif choice == 5:
                self.handle_delete_task()
            elif choice == 6:
                self.handle_help()
            elif choice == 7:
                self.handle_exit()

    def handle_add_task(self) -> None:
        """Handle adding a new task"""
        try:
            title = Prompt.ask("[bold cyan]Enter task title[/bold cyan]").strip()

            if not title:
                console.print("[error]Error: Task title cannot be empty[/error]")
                return

            if len(title) > 100:
                console.print(f"[error]Error: Title exceeds maximum length of 100 characters: {len(title)}[/error]")
                return

            task = self.service.add_task(title)
            console.print(f"[success]\u2714 Task Added Successfully![/success] ID: {task.id} - {task.title}")
        except ValueError as e:
            console.print(f"[error]Error: {e}[/error]")
        except Exception as e:
            console.print(f"[error]An unexpected error occurred while adding task: {e}[/error]")

    def handle_list_tasks(self) -> None:
        """Handle listing all tasks"""
        try:
            tasks = self.service.list_tasks()
            if not tasks:
                console.print("[warning]No tasks found[/warning]")
                return

            table = Table(title="Task List", border_style="cyan", header_style="bold cyan", show_lines=True)
            table.add_column("ID", style="bold white", justify="center", width=5)
            table.add_column("Title", style="white", min_width=20)
            table.add_column("Description", style="dim white", min_width=10)
            table.add_column("Status", justify="center", width=12)

            for task in tasks:
                if task.status == "completed":
                    status_display = "[green]Completed[/green]"
                elif task.status == "in progress":
                    status_display = "[blue]In Progress[/blue]"
                else:
                    status_display = "[yellow]Pending[/yellow]"

                table.add_row(
                    str(task.id),
                    task.title,
                    "-",
                    status_display,
                )

            console.print(table)
        except Exception as e:
            console.print(f"[error]An unexpected error occurred while listing tasks: {e}[/error]")

    def handle_update_task(self) -> None:
        """Handle updating an existing task"""
        try:
            task_id_input = Prompt.ask("[bold cyan]Enter task ID to update[/bold cyan]").strip()
            if not task_id_input.isdigit():
                console.print("[error]Error: Task ID must be a number[/error]")
                return

            task_id = int(task_id_input)
            if task_id <= 0:
                console.print("[error]Error: Task ID must be a positive integer[/error]")
                return

            existing_task = self.service.get_task(task_id)
            if existing_task is None:
                console.print(f"[error]Error: Task with ID {task_id} not found[/error]")
                return

            new_title = Prompt.ask(f"[bold cyan]Enter new title for task {task_id}[/bold cyan] (current: '[italic]{existing_task.title}[/italic]')").strip()

            if not new_title:
                console.print("[error]Error: Task title cannot be empty[/error]")
                return

            if len(new_title) > 100:
                console.print(f"[error]Error: Title exceeds maximum length of 100 characters: {len(new_title)}[/error]")
                return

            success = self.service.update_task(task_id, new_title)
            if success:
                console.print(f"[success]\u2714 Task {task_id} updated successfully![/success]")
            else:
                console.print(f"[error]Error: Failed to update task {task_id}[/error]")
        except ValueError as e:
            console.print(f"[error]Error: {e}[/error]")
        except Exception as e:
            console.print(f"[error]An unexpected error occurred while updating task: {e}[/error]")

    def handle_mark_complete(self) -> None:
        """Handle marking a task as complete"""
        try:
            task_id_input = Prompt.ask("[bold cyan]Enter task ID to mark as complete[/bold cyan]").strip()
            if not task_id_input.isdigit():
                console.print("[error]Error: Task ID must be a number[/error]")
                return

            task_id = int(task_id_input)
            if task_id <= 0:
                console.print("[error]Error: Task ID must be a positive integer[/error]")
                return

            existing_task = self.service.get_task(task_id)
            if existing_task is None:
                console.print(f"[error]Error: Task with ID {task_id} not found[/error]")
                return

            success = self.service.mark_complete(task_id)
            if success:
                console.print(f"[success]\u2714 Task {task_id} marked as completed![/success]")
            else:
                console.print(f"[error]Error: Failed to mark task {task_id} as complete[/error]")
        except Exception as e:
            console.print(f"[error]An unexpected error occurred while marking task complete: {e}[/error]")

    def handle_delete_task(self) -> None:
        """Handle deleting a task"""
        try:
            task_id_input = Prompt.ask("[bold cyan]Enter task ID to delete[/bold cyan]").strip()
            if not task_id_input.isdigit():
                console.print("[error]Error: Task ID must be a number[/error]")
                return

            task_id = int(task_id_input)
            if task_id <= 0:
                console.print("[error]Error: Task ID must be a positive integer[/error]")
                return

            existing_task = self.service.get_task(task_id)
            if existing_task is None:
                console.print(f"[error]Error: Task with ID {task_id} not found[/error]")
                return

            success = self.service.delete_task(task_id)
            if success:
                console.print(f"[success]\u2714 Task {task_id} deleted successfully![/success]")
            else:
                console.print(f"[error]Error: Failed to delete task {task_id}[/error]")
        except Exception as e:
            console.print(f"[error]An unexpected error occurred while deleting task: {e}[/error]")

    def handle_help(self) -> None:
        """Display help information"""
        help_items = [
            ("[cyan]1. Add Task[/cyan]", "Create a new task with a title"),
            ("[cyan]2. List Tasks[/cyan]", "Display all tasks with ID, title, and status"),
            ("[cyan]3. Update Task[/cyan]", "Modify the title of an existing task"),
            ("[cyan]4. Mark Complete[/cyan]", "Update a task's status to 'completed'"),
            ("[cyan]5. Delete Task[/cyan]", "Remove a task from the system"),
            ("[cyan]6. Help[/cyan]", "Show this help message"),
            ("[cyan]7. Exit[/cyan]", "Close the application"),
        ]
        help_text = Text()
        for cmd, desc in help_items:
            help_text.append_text(Text.from_markup(f"  {cmd}: {desc}\n"))
        help_text.rstrip()
        console.print(Panel(help_text, title="[bold cyan]Help[/bold cyan]", border_style="dim cyan", padding=(0, 1)))

    def handle_exit(self) -> None:
        """Handle application exit"""
        console.print("[bold cyan]Goodbye![/bold cyan]")
        self.running = False


def main() -> None:
    """Main entry point for the CLI application"""
    app = CLIMenuSystem()
    app.run()


if __name__ == "__main__":
    main()
