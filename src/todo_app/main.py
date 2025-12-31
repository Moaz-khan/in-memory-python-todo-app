"""
Main entry point for the In-Memory Python Console Todo Application
"""
from todo_app.cli.cli_controller import CLIController


def main():
    """
    Main function to run the todo application.
    """
    controller = CLIController()
    print("Welcome to the In-Memory Python Console Todo Application!")
    print("Type 'help' for available commands or 'exit' to quit.\n")

    while True:
        try:
            # Display main menu
            print("\n--- Main Menu ---")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Update Task")
            print("4. Delete Task")
            print("5. Mark Task Complete/Incomplete")
            print("6. Exit")
            print("------------------")

            choice = input("Enter your choice (1-6): ").strip()

            if choice == "1":
                # Add Task
                title = input("Enter task title: ").strip()
                description = input("Enter task description: ").strip()
                result = controller.add_task(title, description)
                print(result["message"])

            elif choice == "2":
                # View Tasks
                result = controller.view_tasks()
                if result["success"]:
                    if result["count"] == 0:
                        print("No tasks found.")
                    else:
                        print("\nAll Tasks:")
                        print(controller.display_tasks(result["tasks"]))
                else:
                    print(result["message"])

            elif choice == "3":
                # Update Task
                try:
                    task_id = int(input("Enter task ID to update: ").strip())
                    title = input("Enter new title (or press Enter to skip): ").strip()
                    description = input("Enter new description (or press Enter to skip): ").strip()

                    # Only pass non-empty values
                    update_data = {}
                    if title:
                        update_data["title"] = title
                    if description:
                        update_data["description"] = description

                    if not title and not description:
                        print("No updates provided.")
                        continue

                    result = controller.update_task(task_id, **update_data)
                    print(result["message"])
                except ValueError:
                    print("Invalid task ID. Please enter a number.")

            elif choice == "4":
                # Delete Task
                try:
                    task_id = int(input("Enter task ID to delete: ").strip())
                    result = controller.delete_task(task_id)
                    print(result["message"])
                except ValueError:
                    print("Invalid task ID. Please enter a number.")

            elif choice == "5":
                # Mark Task Complete/Incomplete
                try:
                    task_id = int(input("Enter task ID: ").strip())
                    status = input("Mark as complete? (y/n): ").strip().lower()
                    complete = status in ['y', 'yes', 'true', '1']
                    result = controller.mark_task_complete(task_id, complete)
                    print(result["message"])
                except ValueError:
                    print("Invalid task ID. Please enter a number.")

            elif choice == "6":
                # Exit
                print("Thank you for using the Todo Application. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

        except KeyboardInterrupt:
            print("\n\nApplication interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()