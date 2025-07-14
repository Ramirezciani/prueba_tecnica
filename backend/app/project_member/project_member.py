from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field

class ProjectMemberBase(BaseModel):
    user_id: int
    project_id: int
    task_id: Optional[int] = None
    role: Optional[str] = Field('member', max_length=50)

class ProjectMemberCreate(ProjectMemberBase):
    pass

class ProjectMemberUpdate(BaseModel):
    role: Optional[str] = Field(None, max_length=50)
    task_id: Optional[int] = None

class ProjectMemberOut(ProjectMemberBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
