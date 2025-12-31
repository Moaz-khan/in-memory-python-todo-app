---
description: "Task list for In-Memory Python Console Todo Application implementation"
---

# Tasks: In-Memory Python Console Todo Application

**Input**: Design documents from `/specs/1-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan in src/todo_app/
- [X] T002 Initialize Python 3.13+ project with requirements.txt
- [X] T003 [P] Create requirements.txt with project dependencies
- [X] T004 Create src/ directory structure with models, services, cli subdirectories

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T005 Create Task data model in src/todo_app/models/task.py
- [X] T006 Create in-memory task storage structure in src/todo_app/services/task_storage.py
- [X] T007 [P] Create TaskService class in src/todo_app/services/task_service.py
- [X] T008 Create CLI controller base structure in src/todo_app/cli/cli_controller.py
- [X] T009 Create main application entry point in src/todo_app/main.py
- [X] T010 Setup error handling and validation utilities in src/todo_app/utils/

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new tasks with title and description, assigning unique IDs automatically

**Independent Test**: Can be fully tested by adding tasks with different titles and descriptions and verifying they appear in the system with unique IDs.

### Implementation for User Story 1

- [X] T011 [P] [US1] Implement Task model with id, title, description, status properties in src/todo_app/models/task.py
- [X] T012 [P] [US1] Implement unique ID generation in src/todo_app/services/task_service.py
- [X] T013 [US1] Implement add_task method in TaskService with input validation
- [X] T014 [US1] Create add task CLI command in src/todo_app/cli/cli_controller.py
- [X] T015 [US1] Implement success message display for task creation
- [X] T016 [US1] Add input validation for title and description length

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

**Goal**: Display all tasks in a readable tabular format with status indicators

**Independent Test**: Can be fully tested by adding tasks and then viewing them to verify they display correctly with proper formatting and status indicators.

### Implementation for User Story 2

- [X] T017 [P] [US2] Implement get_all_tasks method in TaskService
- [X] T018 [US2] Create view tasks CLI command in src/todo_app/cli/cli_controller.py
- [X] T019 [US2] Implement tabular display formatting for tasks
- [X] T020 [US2] Add status indicator display (complete/incomplete)
- [X] T021 [US2] Handle case when no tasks exist with appropriate message

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update Task Details (Priority: P2)

**Goal**: Allow users to modify the title or description of existing tasks by ID

**Independent Test**: Can be fully tested by adding tasks, updating their details, and verifying the changes are reflected when viewing tasks.

### Implementation for User Story 3

- [X] T022 [P] [US3] Implement get_task_by_id method in TaskService
- [X] T023 [US3] Implement update_task method in TaskService with validation
- [X] T024 [US3] Create update task CLI command in src/todo_app/cli/cli_controller.py
- [X] T025 [US3] Add success/error message display for update operations
- [X] T026 [US3] Implement validation to ensure task ID exists before update

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Delete Tasks (Priority: P2)

**Goal**: Allow users to remove tasks by ID

**Independent Test**: Can be fully tested by adding tasks, deleting them, and verifying they no longer appear when viewing tasks.

### Implementation for User Story 4

- [X] T027 [P] [US4] Implement delete_task method in TaskService with validation
- [X] T028 [US4] Create delete task CLI command in src/todo_app/cli/cli_controller.py
- [X] T029 [US4] Add success/error message display for delete operations
- [X] T030 [US4] Implement validation to ensure task ID exists before deletion

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Mark Tasks Complete/Incomplete (Priority: P1)

**Goal**: Allow users to toggle the completion status of tasks by ID

**Independent Test**: Can be fully tested by adding tasks, marking them complete/incomplete, and verifying the status changes are reflected when viewing tasks.

### Implementation for User Story 5

- [X] T031 [P] [US5] Implement mark_task_complete method in TaskService
- [X] T032 [US5] Create mark task CLI command in src/todo_app/cli/cli_controller.py
- [X] T033 [US5] Add success/error message display for status change operations
- [X] T034 [US5] Implement validation to ensure task ID exists before status change
- [X] T035 [US5] Add toggle functionality for complete/incomplete status

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T036 [P] Add comprehensive error handling across all operations
- [X] T037 [P] Improve user interface with clear prompts and messages
- [X] T038 Add input validation for all user inputs
- [X] T039 [P] Add documentation strings to all methods and classes
- [X] T040 Implement main menu with numbered options in CLI controller
- [X] T041 Test all functionality against acceptance criteria
- [X] T042 Run quickstart validation to ensure application works as expected

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable

### Within Each User Story

- Core implementation before integration
- Story complete before moving to next priority
- All tasks within a story should work together to deliver the complete functionality

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Different user stories can be worked on in parallel by different team members
- Models within a story marked [P] can run in parallel

---

## Parallel Example: User Story 1

```bash
# Launch all components for User Story 1 together:
Task: "Implement Task model with id, title, description, status properties in src/todo_app/models/task.py"
Task: "Implement unique ID generation in src/todo_app/services/task_service.py"
Task: "Create add task CLI command in src/todo_app/cli/cli_controller.py"
```

---

## Implementation Strategy

### MVP First (User Stories 1, 2, 5 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (Add Task)
4. Complete Phase 4: User Story 2 (View Tasks)
5. Complete Phase 7: User Story 5 (Mark Complete/Incomplete)
6. **STOP and VALIDATE**: Test core functionality independently
7. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (Add Task!)
3. Add User Story 2 → Test independently → Deploy/Demo (View Tasks!)
4. Add User Story 5 → Test independently → Deploy/Demo (Mark Complete!)
5. Add User Story 3 → Test independently → Deploy/Demo (Update Task!)
6. Add User Story 4 → Test independently → Deploy/Demo (Delete Task!)
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence