from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class TaskBase(BaseModel):
    """Base model containing common fields for all task operations."""
    title: str = Field(..., min_length=1, max_length=255, description="Task title")
    description: Optional[str] = Field(None, max_length=1000, description="Task description")
    completed: bool = Field(default=False, description="Task completion status")


class TaskCreate(TaskBase):
    """Model for creating new tasks."""
    pass  # All fields inherited from TaskBase


class TaskUpdate(BaseModel):
    """Model for updating existing tasks. All fields are optional for partial updates."""
    title: Optional[str] = Field(None, min_length=1, max_length=255, description="Task title")
    description: Optional[str] = Field(None, max_length=1000, description="Task description")
    completed: Optional[bool] = Field(None, description="Task completion status")


class TaskResponse(TaskBase):
    """Model for API responses with task details."""
    id: str
    created_at: str
    updated_at: str