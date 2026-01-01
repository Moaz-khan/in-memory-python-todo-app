# Quickstart Guide: FastAPI Todo API

## Overview
This guide provides instructions for setting up, running, and using the FastAPI Todo API.

## Prerequisites
- Python 3.13+
- pip package manager

## Setup Instructions

### 1. Clone or Navigate to Project Directory
```bash
cd your-project-directory
```

### 2. Install Dependencies
```bash
pip install fastapi uvicorn
```

### 3. Project Structure
```
src/
└── todo_api/
    ├── main.py
    ├── models/
    ├── services/
    └── routers/
```

### 4. Start the Development Server
```bash
cd src/todo_api
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Base URL
`http://localhost:8000/api/{user_id}`

### Available Endpoints

#### 1. List All Tasks
```
GET /api/{user_id}/tasks
```
- Returns all tasks for the specified user
- Response: 200 OK with array of task objects

#### 2. Create New Task
```
POST /api/{user_id}/tasks
```
- Creates a new task for the specified user
- Request body: JSON with `title` (required) and `description` (optional)
- Response: 201 Created with the new task object

#### 3. Get Task Details
```
GET /api/{user_id}/tasks/{id}
```
- Returns details of a specific task
- Response: 200 OK with task object or 404 Not Found

#### 4. Update Task
```
PUT /api/{user_id}/tasks/{id}
```
- Updates an existing task
- Request body: JSON with fields to update
- Response: 200 OK with updated task object or 404 Not Found

#### 5. Delete Task
```
DELETE /api/{user_id}/tasks/{id}
```
- Deletes a specific task
- Response: 204 No Content or 404 Not Found

#### 6. Toggle Task Completion
```
PATCH /api/{user_id}/tasks/{id}/complete
```
- Toggles the completion status of a task
- Response: 200 OK with updated task object or 404 Not Found

## Example Usage

### Create a Task
```bash
curl -X POST "http://localhost:8000/api/user123/tasks" \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy groceries", "description": "Milk, bread, eggs"}'
```

### Get All Tasks
```bash
curl -X GET "http://localhost:8000/api/user123/tasks"
```

### Update a Task
```bash
curl -X PUT "http://localhost:8000/api/user123/tasks/task456" \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy groceries (updated)", "completed": true}'
```

### Toggle Task Completion
```bash
curl -X PATCH "http://localhost:8000/api/user123/tasks/task456/complete"
```

## API Documentation
Interactive API documentation is available at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Development Notes
- The API uses in-memory storage, so data will be lost when the server restarts
- All endpoints validate input using Pydantic models
- Error responses follow a consistent format
- The code follows FastAPI best practices for modularity and type safety