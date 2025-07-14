from pydantic import BaseModel
from typing import Optional
from datetime import date

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False
    status: Optional[str] = "pendiente"
    due_date: Optional[date] = None

class TaskCreate(TaskBase):
    project_id: int
    assigned_to: Optional[int] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    due_date: Optional[date] = None
    completed: Optional[bool] = None
    assigned_to: Optional[int] = None

class TaskOut(TaskBase):
    id: int

    class Config:
        orm_mode = True
