from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
import models
import database

app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient(database.MONGO_DETAILS)
    app.mongodb = app.mongodb_client[database.DATABASE_NAME]

@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to the To-Do List API"}

@app.post("/tasks/")
async def create_task(task: models.TaskCreate):
    existing_task = await database.get_task_by_name(task.name)
    if existing_task:
        raise HTTPException(status_code=400, detail="Task with this name already exists")
    new_task = await database.create_task(task)
    return new_task

@app.get("/tasks/")
async def get_tasks():
    tasks = await database.get_tasks()
    return tasks

@app.get("/tasks/{task_id}")
async def get_task(task_id: str):
    task = await database.get_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}")
async def update_task(task_id: str, task: models.TaskCreate):
    updated_task = await database.update_task(task_id, task)
    if updated_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: str):
    result = await database.delete_task(task_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"detail": "Task deleted"}
