---
id: 1
title: Create Constitution
stage: constitution
date: 2026-01-01
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: user
command: sp.constitution
labels: [constitution,spec-driven-development,todo-app]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

```text
Project:
In-Memory Python Console Todo Application (Phase I – Basic Level)

Objective:
Develop a command-line based Todo application that stores tasks in memory only, following strict Spec-Driven Development using Claude Code and Spec-Kit Plus. The project must demonstrate an agentic development workflow and clean, maintainable Python code.

Core principles:

Spec-first development: No implementation without an approved specification

Agentic workflow compliance: All code must be generated via Claude Code

Process transparency: Every decision must be traceable through specs and plans

Simplicity & clarity: Console-first, minimal dependencies, readable code

Documentation accuracy: All libraries and tools must follow official documentation

Key standards:

Development must strictly follow Agentic Dev Stack workflow:

Write specification

Generate plan

Break into tasks

Implement using Claude Code

Manual coding is strictly forbidden

All Python code must follow clean code principles

Each feature must be mapped to a clear spec requirement

Code must be modular and easy to review

Console output must be user-friendly and consistent

Technology & tooling rules:

Python version: 3.13+

Environment & tooling: UV

AI coding assistant: Claude Code only

Specification system: Spec-Kit Plus

Documentation source:

For every library, framework, or tool installation and usage, Claude Code must use MCP server context7

No assumptions or outdated knowledge allowed

All implementations must align with the latest official documentation fetched via context7

Functional requirements (Basic Level – Mandatory):

The application must support all five features:

Add a task (with title and description)

View all tasks with status indicators

Update task details

Delete task by ID

Mark task as complete or incomplete

Constraints:

Storage: In-memory only (no database, no file persistence)

Interface: Command-line / console application only

Frameworks: No unnecessary frameworks

Persistence: Data resets on program restart

Scope:
```

## Response snapshot

Constitution file created at `.specify/memory/constitution.md` with the following content:

# In-Memory Python Console Todo Application Constitution

## Core Principles

### I. Spec-First Development
No implementation without an approved specification. All features must be clearly defined in specifications before any code is written. This ensures alignment between requirements and implementation.

### II. Agentic Workflow Compliance
All code must be generated via Claude Code following Spec-Kit Plus methodology. Manual coding is strictly forbidden. All development must follow the agentic development workflow: Write specification → Generate plan → Break into tasks → Implement using Claude Code.

### III. Test-First (NON-NEGOTIABLE)
TDD mandatory: Tests written → User approved → Tests fail → Then implement; Red-Green-Refactor cycle strictly enforced. Every feature must have corresponding tests before implementation.

### IV. Clean Code Standards
All Python code must follow clean code principles. Each feature must be mapped to a clear spec requirement. Code must be modular, easy to review, and maintainable with consistent, readable formatting.

### V. Console-First Interface
Command-line / console application only. User-friendly and consistent console output required. No GUI or web interface - focus on terminal-based interaction with clear, intuitive commands.

### VI. In-Memory Storage Constraint
Storage: In-memory only (no database, no file persistence). Data resets on program restart. This constraint ensures simplicity and focuses on core application logic without persistence complexity.

## Technology & Tooling Standards

Python version: 3.13+ required. Environment & tooling: UV package manager. AI coding assistant: Claude Code only. Specification system: Spec-Kit Plus. For every library, framework, or tool installation and usage, Claude Code must use MCP server context7 - no assumptions or outdated knowledge allowed.

## Development Workflow

Development must strictly follow Agentic Dev Stack workflow: Write specification → Generate plan → Break into tasks → Implement using Claude Code. All implementations must align with the latest official documentation fetched via context7. Process transparency: Every decision must be traceable through specs and plans.

## Governance

This constitution supersedes all other development practices. All implementation work must verify compliance with these principles. Amendments require formal documentation, approval, and migration plan. Every feature must support all five core todo operations: Add task, View tasks, Update task details, Delete task by ID, Mark task as complete/incomplete.

**Version**: 1.0.0 | **Ratified**: 2026-01-01 | **Last Amended**: 2026-01-01

## Outcome

- ✅ Impact: Constitution created for In-Memory Python Console Todo Application project
- 🧪 Tests: No tests required for constitution creation
- 📁 Files: Updated .specify/memory/constitution.md with project-specific principles
- 🔁 Next prompts: Generate specification for the todo application
- 🧠 Reflection: Constitution properly reflects the project requirements and constraints

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS - Constitution properly created with all required principles
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Create the specification document based on the constitution