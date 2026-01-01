# API Contract: FastAPI Todo API

## Overview
This document defines the API contracts for the FastAPI Todo API, specifying the endpoints, request/response formats, and error handling.

## Base URL
```
/api/{user_id}
```

## Common Headers
- Content-Type: application/json
- Accept: application/json

## Authentication
None required (for this implementation phase)

## API Endpoints

### 1. List All Tasks
```
GET /api/{user_id}/tasks
```

#### Request
- Path Parameters:
  - user_id (string): Unique identifier for the user
- Query Parameters: None
- Request Body: None

#### Response
- Success Response (200):
```json
{
  "success": true,
  "data": [
    {
      "id": "task-uuid",
      "title": "Task title",
      "description": "Task description (optional)",
      "completed": false,
      "created_at": "2026-01-01T10:00:00Z",
      "updated_at": "2026-01-01T10:00:00Z"
    }
  ],
  "message": "Tasks retrieved successfully"
}
```

### 2. Create New Task
```
POST /api/{user_id}/tasks
```

#### Request
- Path Parameters:
  - user_id (string): Unique identifier for the user
- Request Body:
```json
{
  "title": "Task title (required)",
  "description": "Task description (optional)"
}
```

#### Response
- Success Response (201):
```json
{
  "success": true,
  "data": {
    "id": "new-task-uuid",
    "title": "Task title",
    "description": "Task description",
    "completed": false,
    "created_at": "2026-01-01T10:00:00Z",
    "updated_at": "2026-01-01T10:00:00Z"
  },
  "message": "Task created successfully"
}
```

- Validation Error Response (422):
```json
{
  "success": false,
  "error": "Validation error",
  "details": {
    "loc": ["body", "title"],
    "msg": "Field required",
    "type": "value_error.missing"
  }
}
```

### 3. Get Task Details
```
GET /api/{user_id}/tasks/{id}
```

#### Request
- Path Parameters:
  - user_id (string): Unique identifier for the user
  - id (string): Unique identifier for the task
- Request Body: None

#### Response
- Success Response (200):
```json
{
  "success": true,
  "data": {
    "id": "task-uuid",
    "title": "Task title",
    "description": "Task description",
    "completed": false,
    "created_at": "2026-01-01T10:00:00Z",
    "updated_at": "2026-01-01T10:00:00Z"
  },
  "message": "Task retrieved successfully"
}
```

- Not Found Response (404):
```json
{
  "success": false,
  "error": "Task not found",
  "details": {
    "user_id": "user-uuid",
    "task_id": "task-uuid"
  }
}
```

### 4. Update Task
```
PUT /api/{user_id}/tasks/{id}
```

#### Request
- Path Parameters:
  - user_id (string): Unique identifier for the user
  - id (string): Unique identifier for the task
- Request Body:
```json
{
  "title": "Updated task title (optional)",
  "description": "Updated task description (optional)",
  "completed": true (optional)
}
```

#### Response
- Success Response (200):
```json
{
  "success": true,
  "data": {
    "id": "task-uuid",
    "title": "Updated task title",
    "description": "Updated task description",
    "completed": true,
    "created_at": "2026-01-01T10:00:00Z",
    "updated_at": "2026-01-01T11:00:00Z"
  },
  "message": "Task updated successfully"
}
```

### 5. Delete Task
```
DELETE /api/{user_id}/tasks/{id}
```

#### Request
- Path Parameters:
  - user_id (string): Unique identifier for the user
  - id (string): Unique identifier for the task
- Request Body: None

#### Response
- Success Response (204): No content

- Not Found Response (404):
```json
{
  "success": false,
  "error": "Task not found",
  "details": {
    "user_id": "user-uuid",
    "task_id": "task-uuid"
  }
}
```

### 6. Toggle Task Completion
```
PATCH /api/{user_id}/tasks/{id}/complete
```

#### Request
- Path Parameters:
  - user_id (string): Unique identifier for the user
  - id (string): Unique identifier for the task
- Request Body: None

#### Response
- Success Response (200):
```json
{
  "success": true,
  "data": {
    "id": "task-uuid",
    "title": "Task title",
    "description": "Task description",
    "completed": true,
    "created_at": "2026-01-01T10:00:00Z",
    "updated_at": "2026-01-01T11:00:00Z"
  },
  "message": "Task completion status updated"
}
```

## Error Handling

### Standard Error Response Format
```json
{
  "success": false,
  "error": "Error message",
  "details": { ... } (optional)
}
```

### Common HTTP Status Codes
- 200: Success (GET, PUT, PATCH)
- 201: Created (POST)
- 204: No Content (DELETE)
- 400: Bad Request
- 404: Not Found
- 422: Validation Error
- 500: Internal Server Error

## Data Validation Rules

### Task Title
- Required field
- Minimum length: 1 character
- Maximum length: 255 characters

### Task Description
- Optional field
- Maximum length: 1000 characters

### Task Completion
- Boolean value
- Default: false