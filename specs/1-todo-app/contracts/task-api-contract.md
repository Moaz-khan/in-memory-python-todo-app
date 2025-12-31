# Task API Contract: In-Memory Python Console Todo Application

## Overview
This document defines the API contracts for the task management operations in the console todo application. These contracts represent the internal interfaces between different components of the application.

## Task Service Interface

### add_task(title: str, description: str) -> dict
**Purpose**: Add a new task to the in-memory storage
**Parameters**:
- title: String, required, 1-200 characters
- description: String, optional, 0-1000 characters
**Returns**: Dictionary containing:
- success: Boolean indicating operation success
- task_id: Integer ID of the created task (if successful)
- message: String describing the result
**Errors**:
- If title is empty or exceeds length limits, returns success=False with error message

### get_all_tasks() -> dict
**Purpose**: Retrieve all tasks from in-memory storage
**Parameters**: None
**Returns**: Dictionary containing:
- success: Boolean indicating operation success
- tasks: List of task dictionaries with id, title, description, and status
- count: Number of tasks returned
**Errors**: No errors expected

### get_task_by_id(task_id: int) -> dict
**Purpose**: Retrieve a specific task by its ID
**Parameters**:
- task_id: Integer ID of the task to retrieve
**Returns**: Dictionary containing:
- success: Boolean indicating operation success
- task: Task dictionary if found, None otherwise
- message: String describing the result
**Errors**:
- If task_id does not exist, returns success=False with error message

### update_task(task_id: int, title: str = None, description: str = None) -> dict
**Purpose**: Update an existing task's title or description
**Parameters**:
- task_id: Integer ID of the task to update
- title: String, optional, 1-200 characters
- description: String, optional, 0-1000 characters
**Returns**: Dictionary containing:
- success: Boolean indicating operation success
- message: String describing the result
**Errors**:
- If task_id does not exist, returns success=False with error message
- If title exceeds length limits, returns success=False with error message

### delete_task(task_id: int) -> dict
**Purpose**: Remove a task from in-memory storage
**Parameters**:
- task_id: Integer ID of the task to delete
**Returns**: Dictionary containing:
- success: Boolean indicating operation success
- message: String describing the result
**Errors**:
- If task_id does not exist, returns success=False with error message

### mark_task_complete(task_id: int, complete: bool) -> dict
**Purpose**: Update the completion status of a task
**Parameters**:
- task_id: Integer ID of the task to update
- complete: Boolean indicating whether task is complete (True) or incomplete (False)
**Returns**: Dictionary containing:
- success: Boolean indicating operation success
- message: String describing the result
**Errors**:
- If task_id does not exist, returns success=False with error message