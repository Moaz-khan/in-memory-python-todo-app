from fastapi import FastAPI
from .routers import tasks

app = FastAPI(
    title="Todo API",
    description="A simple todo API with user-based task management",
    version="1.0.0"
)

# Include the tasks router
app.include_router(tasks.router, prefix="/api/{user_id}", tags=["tasks"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo API"}