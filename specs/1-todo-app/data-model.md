# Data Model: In-Memory Python Console Todo Application

## Task Entity

### Properties
- **id**: Integer (auto-generated unique identifier)
- **title**: String (required, max 200 characters)
- **description**: String (optional, max 1000 characters)
- **status**: Boolean (default: False, represents complete/incomplete)

### Validation Rules
- Title must be provided and not empty
- Title must be between 1 and 200 characters
- Description, if provided, must be between 1 and 1000 characters
- ID must be unique within the application
- Status is a boolean value (True = complete, False = incomplete)

### State Transitions
- **Initial State**: status = False (incomplete)
- **Transition 1**: status = False → status = True (mark complete)
- **Transition 2**: status = True → status = False (mark incomplete)

## Task List Collection

### Properties
- **tasks**: Dictionary mapping ID to Task objects
- **next_id**: Integer (auto-incrementing counter for new tasks)

### Operations
- **Add Task**: Insert new Task object with unique ID
- **Get Task**: Retrieve Task object by ID (returns None if not found)
- **Update Task**: Modify existing Task object by ID
- **Delete Task**: Remove Task object by ID
- **List All Tasks**: Return all Task objects in the collection

### Validation Rules
- Task ID must exist before update/delete operations
- Task ID must be unique when adding new tasks
- Collection size is limited by available memory only