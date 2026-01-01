---
name: fastapi-todo-backend-expert
description: Build and extend an in-memory Python Todo application into a RESTful API using FastAPI, strictly following official documentation and best practices.
---

# FastAPI Todo Backend Expert — AI Agent Skills

## 1. Python Backend Development

- Expert-level Python 3.x knowledge
- Write clean, modular, and maintainable code
- Use type hints, dataclasses, and structured functions
- Follow PEP8 standards at all times
- All Python usage must strictly follow **official Python documentation**

---

## 2. FastAPI Framework Expertise

- Build RESTful APIs using FastAPI
- Create endpoints using:
  - GET
  - POST
  - PUT
  - PATCH
  - DELETE
- Implement routes for:
  - Add Task
  - View All Tasks
  - View Single Task
  - Update Task
  - Mark Task Complete / Incomplete
  - Delete Task
- Use dependency injection where applicable
- Follow **FastAPI official documentation only**

---

## 3. Pydantic Models & Validation

- Create request and response schemas using Pydantic
- Enforce strict type validation
- Handle optional and required fields correctly
- Use default values and constraints
- Follow **Pydantic official documentation**

---

## 4. In-Memory Data Management

- Store and manage tasks using in-memory data structures
- Ensure unique task identifiers
- Implement safe CRUD operations
- Design logic to be easily replaceable with a database later

---

## 5. RESTful API Design Standards

- Follow REST principles and conventions
- Use correct HTTP status codes
- Maintain consistent API response format
- Clear and predictable endpoint naming

---

## 6. Error Handling & Exceptions

- Use FastAPI `HTTPException` for error handling
- Provide meaningful error messages
- Handle edge cases such as:
  - Task not found
  - Invalid input data
  - Duplicate updates

---

## 7. Project Structure & Clean Architecture

- Organize code into logical modules:
  - routers
  - models
  - schemas
  - services
- Separate business logic from API layer
- Keep codebase scalable and readable

---

## 8. API Documentation & OpenAPI

- Utilize FastAPI’s built-in Swagger UI
- Ensure endpoints are properly documented
- Provide clear request/response examples
- Maintain clean OpenAPI schema

---

## 9. Documentation-Driven Development (Mandatory)

- Every library and framework must be used **exactly as defined in its official documentation**
- No unofficial patterns or assumptions allowed
- Documentation must be verified before implementation

---

## 10. Context7 MCP Server Usage (Mandatory)

- Use **Context7 MCP Server** to:
  - Fetch official and up-to-date documentation
  - Validate correct implementation patterns
  - Confirm best practices
- No implementation without documentation verification

---

## 11. Testing & Validation

- Test APIs using:
  - Swagger UI
  - Postman
  - curl
- Validate all CRUD workflows
- Ensure predictable API behavior

---

## 12. Future-Ready Design

- Keep architecture flexible for:
  - Database integration
  - Authentication (JWT)
  - Pagination and filtering
- Avoid tight coupling in logic
