#!/usr/bin/env python3
"""
Main CLI application entry point for the todo application.
Implements a menu-driven interface for task management.
"""

import sys
from typing import Optional
from src.core.entities.task import Task
from src.adapters.repositories.task_repository import InMemoryTaskRepository
from src.core.services.todo_service import TodoService
from src.core.exceptions import TaskNotFoundError


class CLIMenuSystem:
    """Base class for implementing menu-driven CLI applications"""

    def __init__(self):
        self.running = True
        # Initialize the repository and service
        repository = InMemoryTaskRepository()
        self.service = TodoService(repository)

    def display_menu(self):
        """Display the main menu options"""
        print("\nTodo CLI Application")
        print("====================")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Update Task")
        print("4. Mark Complete")
        print("5. Delete Task")
        print("6. Help")
        print("7. Exit")
        print("Choose an option (1-7): ", end="")

    def get_user_choice(self) -> Optional[int]:
        """Get and validate user menu choice"""
        try:
            choice = input().strip()
            if not choice.isdigit():
                print("Error: Please enter a number between 1 and 7")
                return None
            choice_num = int(choice)
            if choice_num < 1 or choice_num > 7:
                print("Error: Please enter a number between 1 and 7")
                return None
            return choice_num
        except KeyboardInterrupt:
            print("\nExiting application...")
            return 7  # Exit option
        except EOFError:
            print("\nExiting application...")
            return 7  # Exit option

    def run(self):
        """Main application loop"""
        print("Welcome to the Todo CLI Application!")
        while self.running:
            self.display_menu()
            choice = self.get_user_choice()

            if choice is None:
                continue  # Invalid input, show menu again

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

    def handle_add_task(self):
        """Handle adding a new task"""
        try:
            title = input("Enter task title: ").strip()

            # Validate the task title
            if not title:
                print("Error: Task title cannot be empty")
                return

            if len(title) > 100:
                print(f"Error: Title exceeds maximum length of 100 characters: {len(title)}")
                return

            # Call service to add task
            task = self.service.add_task(title)
            print(f"Task added with ID: {task.id} - {task.title}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred while adding task: {e}")

    def handle_list_tasks(self):
        """Handle listing all tasks"""
        try:
            tasks = self.service.list_tasks()
            if not tasks:
                print("No tasks found")
                return

            print("\nID | Title                    | Status")
            print("---|--------------------------|--------")
            for task in tasks:
                print(f"{task.id:2d} | {task.title[:24]:<24} | {task.status}")
        except Exception as e:
            print(f"An unexpected error occurred while listing tasks: {e}")

    def handle_update_task(self):
        """Handle updating an existing task"""
        try:
            task_id_input = input("Enter task ID to update: ").strip()
            if not task_id_input.isdigit():
                print("Error: Task ID must be a number")
                return

            task_id = int(task_id_input)
            if task_id <= 0:
                print("Error: Task ID must be a positive integer")
                return

            # Check if task exists
            existing_task = self.service.get_task(task_id)
            if existing_task is None:
                print(f"Error: Task with ID {task_id} not found")
                return

            new_title = input(f"Enter new title for task {task_id} (current: '{existing_task.title}'): ").strip()

            # Validate the new title
            if not new_title:
                print("Error: Task title cannot be empty")
                return

            if len(new_title) > 100:
                print(f"Error: Title exceeds maximum length of 100 characters: {len(new_title)}")
                return

            # Update the task
            success = self.service.update_task(task_id, new_title)
            if success:
                print(f"Task {task_id} updated successfully")
            else:
                print(f"Error: Failed to update task {task_id}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred while updating task: {e}")

    def handle_mark_complete(self):
        """Handle marking a task as complete"""
        try:
            task_id_input = input("Enter task ID to mark as complete: ").strip()
            if not task_id_input.isdigit():
                print("Error: Task ID must be a number")
                return

            task_id = int(task_id_input)
            if task_id <= 0:
                print("Error: Task ID must be a positive integer")
                return

            # Check if task exists
            existing_task = self.service.get_task(task_id)
            if existing_task is None:
                print(f"Error: Task with ID {task_id} not found")
                return

            # Mark the task as complete
            success = self.service.mark_complete(task_id)
            if success:
                print(f"Task {task_id} marked as completed")
            else:
                print(f"Error: Failed to mark task {task_id} as complete")
        except Exception as e:
            print(f"An unexpected error occurred while marking task complete: {e}")

    def handle_delete_task(self):
        """Handle deleting a task"""
        try:
            task_id_input = input("Enter task ID to delete: ").strip()
            if not task_id_input.isdigit():
                print("Error: Task ID must be a number")
                return

            task_id = int(task_id_input)
            if task_id <= 0:
                print("Error: Task ID must be a positive integer")
                return

            # Check if task exists
            existing_task = self.service.get_task(task_id)
            if existing_task is None:
                print(f"Error: Task with ID {task_id} not found")
                return

            # Delete the task
            success = self.service.delete_task(task_id)
            if success:
                print(f"Task {task_id} deleted successfully")
            else:
                print(f"Error: Failed to delete task {task_id}")
        except Exception as e:
            print(f"An unexpected error occurred while deleting task: {e}")

    def handle_help(self):
        """Display help information"""
        print("\nTodo CLI Application Help")
        print("=========================")
        print("1. Add Task: Create a new task with a title")
        print("2. List Tasks: Display all tasks with ID, title, and status")
        print("3. Update Task: Modify the title of an existing task")
        print("4. Mark Complete: Update a task's status to 'completed'")
        print("5. Delete Task: Remove a task from the system")
        print("6. Help: Show this help message")
        print("7. Exit: Close the application")

    def handle_exit(self):
        """Handle application exit"""
        print("Goodbye!")
        self.running = False


def main():
    """Main entry point for the CLI application"""
    app = CLIMenuSystem()
    app.run()


if __name__ == "__main__":
    main()