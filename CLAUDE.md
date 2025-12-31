# Claude Code Operational Instructions

This file contains operational instructions for using Claude Code with this project.

## Project Overview

This is an In-Memory Python Console Todo Application built following Spec-Driven Development using Claude Code and Spec-Kit Plus. The project demonstrates an agentic development workflow and clean, maintainable Python code.

## Development Workflow

The project follows the Spec-Driven Development workflow:

1. **Specification** - Requirements are defined in `specs/1-todo-app/spec.md`
2. **Planning** - Architecture and approach defined in `specs/1-todo-app/plan.md`
3. **Tasks** - Implementation steps defined in `specs/1-todo-app/tasks.md`
4. **Implementation** - Code generated via Claude Code following the tasks

## Project Structure

- `.specify/` - Contains templates and scripts for the Spec-Kit Plus workflow
- `specs/1-todo-app/` - Contains all specification documents
- `src/todo_app/` - Contains the Python source code
- `history/prompts/` - Contains Prompt History Records (PHRs)
- `.gitignore` - Git ignore file
- `requirements.txt` - Python dependencies
- `README.md` - Project documentation
- `CLAUDE.md` - This file
- `.specify/memory/constitution.md` - Project constitution

## Agentic Workflow Compliance

All code in this project was generated via Claude Code following the Spec-Kit Plus methodology. Manual coding is strictly forbidden. The development followed the agentic development workflow: Write specification → Generate plan → Break into tasks → Implement using Claude Code.

## Code Standards

- Python 3.13+ syntax only
- Console-only interface, no GUI
- In-memory storage only (no file or database persistence)
- Modular, clean, maintainable code
- Follows full agentic workflow: Spec → Plan → Tasks → Implementation

## Running the Application

To run the application:

```bash
python src/todo_app/main.py
```

## Testing

The application can be tested by running through all the user stories defined in the specification:
1. Add tasks with title and description
2. View all tasks with status indicators
3. Update task details by ID
4. Delete tasks by ID
5. Mark tasks as complete/incomplete by ID