from pydantic import BaseModel

class TaskCreate(BaseModel):
    name: str
    description: str

class Task(TaskCreate):
    id: int

    class Config:
        orm_mode = True
