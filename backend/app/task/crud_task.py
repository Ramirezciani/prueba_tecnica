from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from app.models import Task
from app.task import TaskCreate, TaskUpdate

async def create_task(db: AsyncSession, *, task: TaskCreate) -> Task:
    # Excluir campos adicionales que no existen en el modelo SQLAlchemy
    task_data = task.dict()
    db_task = Task(**task_data)
    db.add(db_task)
    await db.commit()
    await db.refresh(db_task)
    return db_task

async def get_task(db: AsyncSession, task_id: int) -> Optional[Task]:
    result = await db.execute(select(Task).where(Task.id == task_id))
    return result.scalars().first()

async def get_tasks_by_project(db: AsyncSession, project_id: int, skip: int = 0, limit: int = 100) -> List[Task]:
    result = await db.execute(select(Task).where(Task.project_id == project_id).offset(skip).limit(limit))
    return result.scalars().all()

async def get_tasks(db: AsyncSession, skip: int = 0, limit: int = 100) -> List[Task]:
    result = await db.execute(select(Task).offset(skip).limit(limit))
    return result.scalars().all()

async def update_task(db: AsyncSession, task_id: int, new_data: dict) -> Optional[Task]:
    task = await get_task(db, task_id)
    if not task:
        return None
    for key, value in new_data.items():
        setattr(task, key, value)
    await db.commit()
    await db.refresh(task)
    return task

async def delete_task(db: AsyncSession, task_id: int) -> bool:
    task = await get_task(db, task_id)
    if not task:
        return False
    await db.delete(task)  # db.delete sí es awaitable en AsyncSession
    await db.commit()
    return True