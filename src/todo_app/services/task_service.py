"""
Task service for the In-Memory Python Console Todo Application
"""
from typing import Dict, Optional, List
from todo_app.models.task import Task
from todo_app.services.task_storage import TaskStorage


class TaskService:
    """
    Service layer for task operations.
    """
    def __init__(self):
        self.storage = TaskStorage()

    def add_task(self, title: str, description: str) -> Dict:
        """
        Add a new task.
        """
        try:
            # Validate inputs
            if not title or len(title.strip()) == 0:
                return {"success": False, "message": "Task title cannot be empty"}
            if len(title) > 200:
                return {"success": False, "message": "Task title cannot exceed 200 characters"}
            if len(description) > 1000:
                return {"success": False, "message": "Task description cannot exceed 1000 characters"}

            # Generate unique ID
            task_id = self.storage.get_next_id()

            # Create task
            task = Task(id=task_id, title=title.strip(), description=description.strip())

            # Add to storage
            self.storage.add_task(task)

            return {
                "success": True,
                "task_id": task_id,
                "message": f"Task '{title}' added successfully with ID {task_id}"
            }
        except ValueError as e:
            return {"success": False, "message": str(e)}
        except Exception as e:
            return {"success": False, "message": f"An error occurred: {str(e)}"}

    def get_all_tasks(self) -> Dict:
        """
        Get all tasks.
        """
        try:
            tasks = self.storage.get_all_tasks()
            return {
                "success": True,
                "tasks": list(tasks.values()),
                "count": len(tasks)
            }
        except Exception as e:
            return {"success": False, "message": f"An error occurred: {str(e)}"}

    def get_task_by_id(self, task_id: int) -> Dict:
        """
        Get a specific task by ID.
        """
        try:
            task = self.storage.get_task(task_id)
            if task is not None:
                return {"success": True, "task": task}
            else:
                return {"success": False, "message": f"Task with ID {task_id} not found"}
        except Exception as e:
            return {"success": False, "message": f"An error occurred: {str(e)}"}

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Dict:
        """
        Update a task by ID.
        """
        try:
            # Get existing task
            existing_task = self.storage.get_task(task_id)
            if existing_task is None:
                return {"success": False, "message": f"Task with ID {task_id} not found"}

            # Prepare updated values
            new_title = title if title is not None else existing_task.title
            new_description = description if description is not None else existing_task.description

            # Validate inputs
            if not new_title or len(new_title.strip()) == 0:
                return {"success": False, "message": "Task title cannot be empty"}
            if len(new_title) > 200:
                return {"success": False, "message": "Task title cannot exceed 200 characters"}
            if len(new_description) > 1000:
                return {"success": False, "message": "Task description cannot exceed 1000 characters"}

            # Create updated task
            updated_task = Task(
                id=task_id,
                title=new_title.strip(),
                description=new_description.strip(),
                status=existing_task.status
            )

            # Update in storage
            success = self.storage.update_task(task_id, updated_task)

            if success:
                return {"success": True, "message": f"Task with ID {task_id} updated successfully"}
            else:
                return {"success": False, "message": "Failed to update task"}

        except ValueError as e:
            return {"success": False, "message": str(e)}
        except Exception as e:
            return {"success": False, "message": f"An error occurred: {str(e)}"}

    def delete_task(self, task_id: int) -> Dict:
        """
        Delete a task by ID.
        """
        try:
            success = self.storage.delete_task(task_id)
            if success:
                return {"success": True, "message": f"Task with ID {task_id} deleted successfully"}
            else:
                return {"success": False, "message": f"Task with ID {task_id} not found"}
        except Exception as e:
            return {"success": False, "message": f"An error occurred: {str(e)}"}

    def mark_task_complete(self, task_id: int, complete: bool) -> Dict:
        """
        Mark a task as complete or incomplete.
        """
        try:
            # Get existing task
            existing_task = self.storage.get_task(task_id)
            if existing_task is None:
                return {"success": False, "message": f"Task with ID {task_id} not found"}

            # Create updated task with new status
            updated_task = Task(
                id=task_id,
                title=existing_task.title,
                description=existing_task.description,
                status=complete
            )

            # Update in storage
            success = self.storage.update_task(task_id, updated_task)

            if success:
                status_text = "complete" if complete else "incomplete"
                return {"success": True, "message": f"Task with ID {task_id} marked as {status_text}"}
            else:
                return {"success": False, "message": "Failed to update task status"}

        except Exception as e:
            return {"success": False, "message": f"An error occurred: {str(e)}"}