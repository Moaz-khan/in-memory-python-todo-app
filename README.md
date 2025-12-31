# In-Memory Python Console Todo Application

This is a console-based todo application that stores tasks in memory only. It allows users to add, view, update, delete, and mark tasks as complete/incomplete.

## Features

- Add tasks with title and description
- View all tasks in a tabular format with status indicators
- Update task details by ID
- Delete tasks by ID
- Mark tasks as complete or incomplete by ID
- In-memory storage (data resets on program restart)

## Prerequisites

- Python 3.13 or higher

## Setup

1. Clone the repository
2. Install dependencies (if any) using `pip install -r requirements.txt`
3. Run the application with `python src/todo_app/main.py`

## Usage

Run the application and follow the on-screen menu prompts:

1. Add Task - Add a new task with title and description
2. View Tasks - Display all tasks with their status
3. Update Task - Modify an existing task by ID
4. Delete Task - Remove a task by ID
5. Mark Task Complete/Incomplete - Toggle task completion status
6. Exit - Quit the application

## Project Structure

```
src/
├── todo_app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── task.py              # Task data model
│   ├── services/
│   │   ├── __init__.py
│   │   └── task_service.py      # Task business logic
│   ├── cli/
│   │   ├── __init__.py
│   │   └── cli_controller.py    # Command-line interface
│   └── main.py                  # Application entry point
```

## Architecture

The application follows a clean architecture pattern:
- **Models Layer**: Contains the Task data model
- **Services Layer**: Contains business logic for task operations
- **CLI Layer**: Handles user input/output and command routing
- **Main Module**: Orchestrates the application flow