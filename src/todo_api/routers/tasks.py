from fastapi import APIRouter, HTTPException, Path, Body
from typing import List
from ..models.task import TaskCreate, TaskUpdate, TaskResponse
from ..services.task_service import task_service
from ..utils.error_handlers import TaskNotFoundException, handle_error

router = APIRouter()


@router.post("/tasks", response_model=dict, status_code=201, summary="Create a new task")
async def create_task(
    user_id: str = Path(..., description="User ID"),
    task: TaskCreate = Body(..., description="Task data")
):
    """
    Create a new task for the specified user.

    - **user_id**: The ID of the user who owns the task
    - **title**: Task title (required)
    - **description**: Task description (optional)
    - **completed**: Task completion status (default: false)
    """
    try:
        created_task = task_service.create_task(user_id, task)
        return {
            "success": True,
            "data": created_task,
            "message": "Task created successfully"
        }
    except Exception as e:
        return handle_error(f"Failed to create task: {str(e)}")


@router.get("/tasks", response_model=dict, summary="Get all tasks for a user")
async def get_all_tasks(
    user_id: str = Path(..., description="User ID")
):
    """
    Retrieve all tasks for the specified user.

    - **user_id**: The ID of the user whose tasks to retrieve
    """
    try:
        tasks = task_service.get_all_tasks(user_id)
        return {
            "success": True,
            "data": tasks,
            "message": "Tasks retrieved successfully"
        }
    except Exception as e:
        return handle_error(f"Failed to retrieve tasks: {str(e)}")


@router.get("/tasks/{task_id}", response_model=dict, summary="Get a specific task")
async def get_task(
    user_id: str = Path(..., description="User ID"),
    task_id: str = Path(..., description="Task ID")
):
    """
    Retrieve a specific task for the specified user.

    - **user_id**: The ID of the user who owns the task
    - **task_id**: The ID of the task to retrieve
    """
    try:
        task = task_service.get_task(user_id, task_id)
        if not task:
            raise TaskNotFoundException(user_id, task_id)

        return {
            "success": True,
            "data": task,
            "message": "Task retrieved successfully"
        }
    except TaskNotFoundException:
        raise
    except Exception as e:
        return handle_error(f"Failed to retrieve task: {str(e)}")


@router.put("/tasks/{task_id}", response_model=dict, summary="Update a specific task")
async def update_task(
    user_id: str = Path(..., description="User ID"),
    task_id: str = Path(..., description="Task ID"),
    task_update: TaskUpdate = Body(..., description="Task update data")
):
    """
    Update a specific task for the specified user.

    - **user_id**: The ID of the user who owns the task
    - **task_id**: The ID of the task to update
    - **title**: New task title (optional)
    - **description**: New task description (optional)
    - **completed**: New task completion status (optional)
    """
    try:
        updated_task = task_service.update_task(user_id, task_id, task_update)
        if not updated_task:
            raise TaskNotFoundException(user_id, task_id)

        return {
            "success": True,
            "data": updated_task,
            "message": "Task updated successfully"
        }
    except TaskNotFoundException:
        raise
    except Exception as e:
        return handle_error(f"Failed to update task: {str(e)}")


@router.delete("/tasks/{task_id}", response_model=dict, summary="Delete a specific task")
async def delete_task(
    user_id: str = Path(..., description="User ID"),
    task_id: str = Path(..., description="Task ID")
):
    """
    Delete a specific task for the specified user.

    - **user_id**: The ID of the user who owns the task
    - **task_id**: The ID of the task to delete
    """
    try:
        success = task_service.delete_task(user_id, task_id)
        if not success:
            raise TaskNotFoundException(user_id, task_id)

        return {
            "success": True,
            "message": "Task deleted successfully"
        }
    except TaskNotFoundException:
        raise
    except Exception as e:
        return handle_error(f"Failed to delete task: {str(e)}")


@router.patch("/tasks/{task_id}/complete", response_model=dict, summary="Toggle task completion status")
async def toggle_task_completion(
    user_id: str = Path(..., description="User ID"),
    task_id: str = Path(..., description="Task ID")
):
    """
    Toggle the completion status of a specific task for the specified user.

    - **user_id**: The ID of the user who owns the task
    - **task_id**: The ID of the task to toggle
    """
    try:
        updated_task = task_service.toggle_task_completion(user_id, task_id)
        if not updated_task:
            raise TaskNotFoundException(user_id, task_id)

        return {
            "success": True,
            "data": updated_task,
            "message": "Task completion status updated"
        }
    except TaskNotFoundException:
        raise
    except Exception as e:
        return handle_error(f"Failed to toggle task completion: {str(e)}")