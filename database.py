from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
import models

MONGO_DETAILS = "mongodb+srv://naina12345:12345naina@cluster0.vxvxtli.mongodb.net/?retryWrites=true&w=majority"
DATABASE_NAME = "TODO"
COLLECTION_NAME = "tasks"

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client[DATABASE_NAME]
task_collection = database[COLLECTION_NAME]

# Helper function to convert MongoDB document to Pydantic model
def task_helper(task) -> dict:
    return {
        "id": str(task["_id"]),
        "name": task["name"],
        "description": task["description"]
    }

# CRUD operations
async def get_task_by_name(name: str) -> dict:
    task = await task_collection.find_one({"name": name})
    if task:
        return task_helper(task)

async def create_task(task: models.TaskCreate) -> dict:
    task = await task_collection.insert_one(task.dict())
    new_task = await task_collection.find_one({"_id": task.inserted_id})
    return task_helper(new_task)

async def get_tasks() -> list:
    tasks = []
    async for task in task_collection.find():
        tasks.append(task_helper(task))
    return tasks

async def get_task(task_id: str) -> dict:
    task = await task_collection.find_one({"_id": ObjectId(task_id)})
    if task:
        return task_helper(task)

async def update_task(task_id: str, task_data: models.TaskCreate) -> dict:
    task = await task_collection.find_one({"_id": ObjectId(task_id)})
    if task:
        updated_task = await task_collection.update_one(
            {"_id": ObjectId(task_id)},
            {"$set": task_data.dict()}
        )
        if updated_task:
            return task_helper(await task_collection.find_one({"_id": ObjectId(task_id)}))

async def delete_task(task_id: str) -> dict:
    task = await task_collection.find_one({"_id": ObjectId(task_id)})
    if task:
        await task_collection.delete_one({"_id": ObjectId(task_id)})
        return {"status": "Task deleted"}
