"""
CLI controller for the In-Memory Python Console Todo Application
"""
from typing import Dict
from todo_app.services.task_service import TaskService


class CLIController:
    """
    Controller for CLI operations.
    """
    def __init__(self):
        self.task_service = TaskService()

    def add_task(self, title: str, description: str) -> Dict:
        """
        Add a new task via CLI.
        """
        return self.task_service.add_task(title, description)

    def view_tasks(self) -> Dict:
        """
        View all tasks via CLI.
        """
        return self.task_service.get_all_tasks()

    def get_task(self, task_id: int) -> Dict:
        """
        Get a specific task by ID via CLI.
        """
        return self.task_service.get_task_by_id(task_id)

    def update_task(self, task_id: int, title: str = None, description: str = None) -> Dict:
        """
        Update a task via CLI.
        """
        return self.task_service.update_task(task_id, title, description)

    def delete_task(self, task_id: int) -> Dict:
        """
        Delete a task via CLI.
        """
        return self.task_service.delete_task(task_id)

    def mark_task_complete(self, task_id: int, complete: bool) -> Dict:
        """
        Mark a task as complete/incomplete via CLI.
        """
        return self.task_service.mark_task_complete(task_id, complete)

    def display_tasks(self, tasks: list) -> str:
        """
        Format and display tasks in a readable table format.
        """
        if not tasks:
            return "No tasks found."

        # Create table header
        table = f"{'ID':<5} {'Title':<30} {'Description':<40} {'Status':<12}\n"
        table += "-" * 90 + "\n"

        # Add each task as a row
        for task in tasks:
            status = "Complete" if task.status else "Incomplete"
            title = task.title if len(task.title) <= 28 else task.title[:27] + "…"
            description = task.description if len(task.description) <= 38 else task.description[:37] + "…"
            table += f"{task.id:<5} {title:<30} {description:<40} {status:<12}\n"

        return table