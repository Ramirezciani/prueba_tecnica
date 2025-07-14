from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.database import get_db 
from app.models import Task
from app.task.task import TaskCreate, TaskUpdate, TaskOut
import app.task.crud_task as task_crud

router = APIRouter()

@router.post("/", response_model=TaskOut)
async def create_task(task: TaskCreate, db: AsyncSession = Depends(get_db)):
    return await task_crud.create_task(db, task=task)

@router.get("/{task_id}", response_model=TaskOut)
async def read_task(task_id: int, db: AsyncSession = Depends(get_db)):
    task = await task_crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.get("/", response_model=List[TaskOut])
async def read_tasks(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    return await task_crud.get_tasks(db, skip=skip, limit=limit)

@router.get("/project/{project_id}", response_model=List[TaskOut])
async def read_tasks_by_project(project_id: int, skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    return await task_crud.get_tasks_by_project(db, project_id, skip=skip, limit=limit)

@router.put("/{task_id}", response_model=TaskOut)
async def update_task(task_id: int, task_update: TaskUpdate, db: AsyncSession = Depends(get_db)):
    updated_task = await task_crud.update_task(db, task_id, task_update.dict(exclude_unset=True))
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

@router.delete("/{task_id}", response_model=bool)
async def delete_task(task_id: int, db: AsyncSession = Depends(get_db)):
    success = await task_crud.delete_task(db, task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return success