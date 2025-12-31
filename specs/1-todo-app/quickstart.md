# Quickstart Guide: In-Memory Python Console Todo Application

## Prerequisites
- Python 3.13 or higher
- pip package manager

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Navigate to the project root directory
2. Run the application:
   ```bash
   python -m src.todo_app.main
   ```

   Or if using the installed package:
   ```bash
   python src/todo_app/main.py
   ```

## Using the Application

1. The application will display a menu with the following options:
   - 1. Add Task
   - 2. View Tasks
   - 3. Update Task
   - 4. Delete Task
   - 5. Mark Task Complete/Incomplete
   - 6. Exit

2. Enter the number corresponding to your desired action
3. Follow the prompts to provide required information
4. The application will display results or error messages as appropriate

## Running Tests

To run the unit tests:
```bash
python -m pytest tests/unit/
```

To run the integration tests:
```bash
python -m pytest tests/integration/
```

To run all tests:
```bash
python -m pytest tests/
```

## Example Usage

1. **Add a task**: Select option 1, enter a title and description
2. **View tasks**: Select option 2 to see all tasks with their status
3. **Update a task**: Select option 3, enter the task ID and new information
4. **Delete a task**: Select option 4, enter the task ID to remove
5. **Mark complete/incomplete**: Select option 5, enter task ID and completion status

## Troubleshooting

- If you get a "module not found" error, ensure you're running from the project root
- If the application doesn't start, verify Python 3.13+ is installed
- All data is stored in memory only and will be lost when the application exits