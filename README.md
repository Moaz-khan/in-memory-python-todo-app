# FastAPI Todo API

A simple and efficient todo API built with FastAPI, featuring user-based task management with full CRUD operations.

## Features

- Create, read, update, delete tasks
- Toggle task completion status
- User-based task organization
- In-memory storage (no database required)
- Automatic OpenAPI/Swagger documentation
- Pydantic model validation
- Comprehensive error handling

## Endpoints

### Task Management

- `GET /api/{user_id}/tasks` - Get all tasks for a user
- `POST /api/{user_id}/tasks` - Create a new task
- `GET /api/{user_id}/tasks/{task_id}` - Get a specific task
- `PUT /api/{user_id}/tasks/{task_id}` - Update a task
- `DELETE /api/{user_id}/tasks/{task_id}` - Delete a task
- `PATCH /api/{user_id}/tasks/{task_id}/complete` - Toggle task completion status

### API Documentation

- `/docs` - Interactive API documentation (Swagger UI)
- `/redoc` - Alternative API documentation (ReDoc)

## Getting Started

### Prerequisites

- Python 3.13+
- pip package manager

### Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   uvicorn src.todo_api.main:app --reload
   ```

### Usage

The API will be available at `http://localhost:8000`. You can access the interactive documentation at `http://localhost:8000/docs`.

## Example Requests

### Create a Task

```bash
curl -X POST "http://localhost:8000/api/user123/tasks" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Buy groceries",
    "description": "Milk, bread, eggs"
  }'
```

### Get All Tasks for a User

```bash
curl -X GET "http://localhost:8000/api/user123/tasks"
```

### Update a Task

```bash
curl -X PUT "http://localhost:8000/api/user123/tasks/task_id" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Buy groceries (updated)",
    "completed": true
  }'
```

### Toggle Task Completion

```bash
curl -X PATCH "http://localhost:8000/api/user123/tasks/task_id/complete"
```

## Project Structure

```
src/
└── todo_api/
    ├── main.py              # FastAPI app instance
    ├── models/              # Pydantic models
    │   └── task.py          # Task-related models
    ├── services/            # Business logic
    │   ├── task_service.py  # Task operations
    │   └── storage.py       # In-memory storage
    ├── routers/             # API routes
    │   └── tasks.py         # Task endpoints
    └── utils/               # Utility functions
        ├── id_generator.py  # ID generation
        ├── error_handlers.py # Error handling
        └── logging.py       # Logging configuration
```

## Architecture

The application follows a clean architecture pattern:

- **Models**: Pydantic models for request/response validation
- **Services**: Business logic and data operations
- **Routers**: API endpoint definitions
- **Storage**: In-memory data persistence

## Error Handling

The API returns consistent error responses in the format:

```json
{
  "success": false,
  "error": "Error message",
  "details": { ... }
}
```

## Validation

All inputs are validated using Pydantic models with the following rules:

- Task title: Required, 1-255 characters
- Task description: Optional, up to 1000 characters
- Task completion: Boolean, defaults to false

## Future Enhancements

- Database integration (PostgreSQL, MongoDB)
- User authentication and authorization
- Task categorization and tagging
- Due dates and reminders
- Search and filtering capabilities