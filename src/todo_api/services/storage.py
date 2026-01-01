from typing import Dict, Optional, List
from datetime import datetime


class InMemoryStorage:
    """
    In-memory storage for tasks, organized by user ID.
    This class provides methods to store, retrieve, update, and delete tasks.
    """

    def __init__(self):
        # Structure: {user_id: {task_id: task_data}}
        self._data: Dict[str, Dict[str, dict]] = {}

    def create_user(self, user_id: str) -> None:
        """Create a new user space in storage if it doesn't exist."""
        if user_id not in self._data:
            self._data[user_id] = {}

    def create_task(self, user_id: str, task_data: dict) -> str:
        """Create a new task for the given user and return its ID."""
        if user_id not in self._data:
            self.create_user(user_id)

        task_id = task_data["id"]
        self._data[user_id][task_id] = task_data
        return task_id

    def get_task(self, user_id: str, task_id: str) -> Optional[dict]:
        """Get a specific task for the given user."""
        if user_id in self._data and task_id in self._data[user_id]:
            return self._data[user_id][task_id]
        return None

    def get_all_tasks(self, user_id: str) -> List[dict]:
        """Get all tasks for the given user."""
        if user_id in self._data:
            return list(self._data[user_id].values())
        return []

    def update_task(self, user_id: str, task_id: str, task_data: dict) -> bool:
        """Update a specific task for the given user."""
        if user_id in self._data and task_id in self._data[user_id]:
            # Preserve the original id and creation time
            original_task = self._data[user_id][task_id]
            task_data["id"] = original_task["id"]
            task_data["created_at"] = original_task["created_at"]
            task_data["updated_at"] = datetime.now().isoformat()

            self._data[user_id][task_id] = task_data
            return True
        return False

    def delete_task(self, user_id: str, task_id: str) -> bool:
        """Delete a specific task for the given user."""
        if user_id in self._data and task_id in self._data[user_id]:
            del self._data[user_id][task_id]
            return True
        return False

    def task_exists(self, user_id: str, task_id: str) -> bool:
        """Check if a task exists for the given user."""
        return user_id in self._data and task_id in self._data[user_id]


# Global instance of the storage
storage = InMemoryStorage()