from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field

class ProjectBase(BaseModel):
    name: str = Field(..., max_length=150)
    description: Optional[str] = None
    owner_id: Optional[int] = None

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=150)
    description: Optional[str] = None
    owner_id: Optional[int] = None

class ProjectOut(ProjectBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
