<!--
Sync Impact Report:
Version change: N/A → 1.0.0
Modified principles: N/A (new constitution)
Added sections: All sections (new constitution)
Removed sections: N/A
Templates requiring updates:
  - .specify/templates/plan-template.md ✅ updated
  - .specify/templates/spec-template.md ✅ updated
  - .specify/templates/tasks-template.md ✅ updated
  - .specify/templates/commands/*.md ⚠ pending
  - README.md ⚠ pending
Follow-up TODOs: None
-->

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

## Scope and Requirements

### Scope:
- Only Phase I features, no extras

### Repository structure requirements:
The GitHub repository must contain:
- CONSTITUTION file (this document)
- specs-history/ folder containing all specification files
- src/ folder containing Python source code
- README.md with setup and run instructions
- CLAUDE.md containing Claude Code operational instructions

### Success criteria:
- All features implemented exactly as specified
- All code generated via Claude Code (no manual edits)
- Full agentic workflow is clearly visible and reviewable
- Application runs successfully from the console
- Clean, readable, and maintainable Python code
- Judges can trace:
  Specs → Plan → Tasks → Implementation
- No rule violations detected during review

**Version**: 1.1.0 | **Ratified**: 2026-01-01 | **Last Amended**: 2026-01-01
