"""
In-memory task storage for the In-Memory Python Console Todo Application
"""
from typing import Dict, Optional
from todo_app.models.task import Task


class TaskStorage:
    """
    In-memory storage for tasks using a dictionary.
    """
    def __init__(self):
        self._tasks: Dict[int, Task] = {}
        self._next_id: int = 1

    def add_task(self, task: Task) -> None:
        """
        Add a task to storage.
        """
        self._tasks[task.id] = task

    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Get a task by ID.
        """
        return self._tasks.get(task_id)

    def get_all_tasks(self) -> Dict[int, Task]:
        """
        Get all tasks.
        """
        return self._tasks.copy()

    def update_task(self, task_id: int, updated_task: Task) -> bool:
        """
        Update a task by ID.
        """
        if task_id in self._tasks:
            self._tasks[task_id] = updated_task
            return True
        return False

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by ID.
        """
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False

    def get_next_id(self) -> int:
        """
        Get the next available task ID and increment the counter.
        """
        current_id = self._next_id
        self._next_id += 1
        return current_id