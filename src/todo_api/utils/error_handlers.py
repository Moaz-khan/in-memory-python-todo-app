from fastapi import HTTPException
from typing import Optional


class TaskNotFoundException(HTTPException):
    """Exception raised when a task is not found."""

    def __init__(self, user_id: str, task_id: str):
        super().__init__(
            status_code=404,
            detail={
                "success": False,
                "error": "Task not found",
                "details": {
                    "user_id": user_id,
                    "task_id": task_id
                }
            }
        )


class UserNotFoundException(HTTPException):
    """Exception raised when a user is not found."""

    def __init__(self, user_id: str):
        super().__init__(
            status_code=404,
            detail={
                "success": False,
                "error": "User not found",
                "details": {
                    "user_id": user_id
                }
            }
        )


def handle_error(error_msg: str, details: Optional[dict] = None) -> dict:
    """Generic error response handler."""
    error_response = {
        "success": False,
        "error": error_msg
    }
    if details:
        error_response["details"] = details

    return error_response