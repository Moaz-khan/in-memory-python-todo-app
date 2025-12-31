"""
Task model for the In-Memory Python Console Todo Application
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    """
    Represents a todo task with ID, title, description, and completion status.
    """
    id: int
    title: str
    description: str
    status: bool = False  # False = incomplete, True = complete

    def __post_init__(self):
        """
        Validate the task properties after initialization.
        """
        if not self.title or len(self.title.strip()) == 0:
            raise ValueError("Task title cannot be empty")
        if len(self.title) > 200:
            raise ValueError("Task title cannot exceed 200 characters")
        if len(self.description) > 1000:
            raise ValueError("Task description cannot exceed 1000 characters")