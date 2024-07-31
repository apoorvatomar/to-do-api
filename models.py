from pydantic import BaseModel

class TaskBase(BaseModel):
    name: str
    description: str

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: str

    class Config:
        orm_mode = True
