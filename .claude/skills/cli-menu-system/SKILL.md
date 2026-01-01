# Skill 5: CLI Menu System Implementation

**Persona**: You are a frontend engineer designing intuitive command-line interfaces with menu-driven interactions that provide excellent user experience.

**Questions to ask before implementing CLI menu system**:
- What are the main operations users need to perform?
- How should the menu be structured for optimal user experience?
- What error handling is needed for user inputs?
- How should the application behave after each operation?
- What feedback should be provided to users?

**Principles**:
- **Clear navigation**: Menu options should be clearly numbered and described
- **Intuitive flow**: User journey should be logical and predictable
- **Error resilience**: Handle invalid inputs gracefully without crashing
- **Consistent feedback**: Provide clear confirmation of operations
- **Easy exit**: Allow users to exit cleanly at any point

**Implementation Pattern**:
```python
class CLIMenuSystem:
    """Base class for implementing menu-driven CLI applications"""

    def __init__(self):
        self.running = True

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

    def get_user_choice(self):
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
            # Use validation skill here
            is_valid, error_msg = validate_task_title(title)
            if not is_valid:
                print(f"Error: {error_msg}")
                return

            # Call service to add task
            task = self.service.add_task(title)
            print(f"Task added with ID: {task.id} - {task.title}")
        except Exception as e:
            print(handle_operation_error("add task", e))

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
            print(handle_operation_error("list tasks", e))

    def handle_exit(self):
        """Handle application exit"""
        print("Goodbye!")
        self.running = False
```

**When to apply**:
- All CLI applications requiring user interaction
- Menu-driven interfaces
- Applications with multiple operation types
- Any application where users need to choose from options

**Contraindications**:
- Command-line tools that accept arguments directly
- Non-interactive batch processing applications
- Performance-critical applications where menu overhead matters