# Data Model: FastAPI Todo API

## Overview
This document defines the data structures and models for the FastAPI Todo API, focusing on the core entities and their relationships.

## Core Entities

### Task Entity
The Task entity represents a single todo item with the following attributes:

- **id**: Unique identifier (UUID or auto-generated string)
- **title**: String, required, represents the task title
- **description**: String, optional, provides details about the task
- **completed**: Boolean, default false, indicates completion status
- **created_at**: DateTime, automatically set when created
- **updated_at**: DateTime, automatically updated when modified

### User Entity
The User entity represents a user account that owns tasks:

- **id**: Unique identifier (UUID or auto-generated string)
- **tasks**: List of Task entities owned by the user

## Pydantic Model Definitions

### Task Models

#### TaskBase
Base model containing common fields for all task operations:
- title: str (required)
- description: str (optional)
- completed: bool (optional, default false)

#### TaskCreate
Model for creating new tasks:
- Inherits from TaskBase
- No additional fields (all fields from TaskBase)

#### TaskUpdate
Model for updating existing tasks:
- Inherits from TaskBase
- All fields are optional to allow partial updates

#### TaskResponse
Model for API responses:
- Inherits from TaskBase
- id: str (required)
- created_at: datetime
- updated_at: datetime

### User Model

#### UserResponse
Model for user data in API responses:
- id: str (required)
- task_count: int (computed field showing number of tasks)

## In-Memory Storage Structure

### Data Storage Approach
```python
# Structure for in-memory storage
users_data: Dict[str, Dict] = {
    "user_id": {
        "id": "user_id",
        "tasks": {
            "task_id": {
                "id": "task_id",
                "title": "Task Title",
                "description": "Task description",
                "completed": False,
                "created_at": datetime,
                "updated_at": datetime
            }
        }
    }
}
```

## API Response Format

### Success Responses
All successful API operations return a consistent structure:
```json
{
    "success": true,
    "data": { ... },
    "message": "Optional message"
}
```

### Error Responses
All error responses follow a consistent structure:
```json
{
    "success": false,
    "error": "Error message",
    "details": { ... }
}
```

## Validation Rules

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

## Future-Proofing Considerations

The data model is designed with future database integration in mind:
- Unique identifiers can easily map to database primary keys
- DateTime fields align with standard database timestamp types
- Structure supports additional fields for authentication/authorization
- Separation of user and task data supports future user management features