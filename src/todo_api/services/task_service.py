from typing import List, Optional
from ..models.task import TaskCreate, TaskUpdate, TaskResponse
from ..utils.id_generator import generate_id, generate_timestamp
from ..utils.error_handlers import TaskNotFoundException
from .storage import storage


class TaskService:
    """Service class to handle task business logic."""

    @staticmethod
    def create_task(user_id: str, task_create: TaskCreate) -> TaskResponse:
        """Create a new task for the given user."""
        from datetime import datetime  # Import here to avoid circular dependencies

        task_data = task_create.model_dump()
        task_id = generate_id()

        # Add required fields
        task_entry = {
            "id": task_id,
            "title": task_data["title"],
            "description": task_data["description"],
            "completed": task_data["completed"],
            "created_at": generate_timestamp(),
            "updated_at": generate_timestamp()
        }

        storage.create_task(user_id, task_entry)

        # Return the created task as a TaskResponse
        return TaskResponse(**task_entry)

    @staticmethod
    def get_task(user_id: str, task_id: str) -> Optional[TaskResponse]:
        """Get a specific task for the given user."""
        task_data = storage.get_task(user_id, task_id)
        if task_data:
            return TaskResponse(**task_data)
        return None

    @staticmethod
    def get_all_tasks(user_id: str) -> List[TaskResponse]:
        """Get all tasks for the given user."""
        tasks_data = storage.get_all_tasks(user_id)
        return [TaskResponse(**task) for task in tasks_data]

    @staticmethod
    def update_task(user_id: str, task_id: str, task_update: TaskUpdate) -> Optional[TaskResponse]:
        """Update a specific task for the given user."""
        task_data = storage.get_task(user_id, task_id)
        if not task_data:
            return None

        # Get the update data, only update fields that are provided
        update_data = task_update.model_dump(exclude_unset=True)

        # Merge with existing data
        updated_task_data = {**task_data, **update_data}
        updated_task_data["updated_at"] = generate_timestamp()

        success = storage.update_task(user_id, task_id, updated_task_data)
        if success:
            return TaskResponse(**updated_task_data)
        return None

    @staticmethod
    def delete_task(user_id: str, task_id: str) -> bool:
        """Delete a specific task for the given user."""
        return storage.delete_task(user_id, task_id)

    @staticmethod
    def toggle_task_completion(user_id: str, task_id: str) -> Optional[TaskResponse]:
        """Toggle the completion status of a task."""
        task_data = storage.get_task(user_id, task_id)
        if not task_data:
            return None

        # Toggle the completion status
        updated_task_data = {**task_data}
        updated_task_data["completed"] = not updated_task_data["completed"]
        updated_task_data["updated_at"] = generate_timestamp()

        success = storage.update_task(user_id, task_id, updated_task_data)
        if success:
            return TaskResponse(**updated_task_data)
        return None


# Create a singleton instance of the service
task_service = TaskService()