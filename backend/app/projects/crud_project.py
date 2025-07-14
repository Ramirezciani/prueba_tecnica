from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from app.models import Project
from app.projects.project import ProjectCreate, ProjectUpdate

async def create_project(db: AsyncSession, *, project: ProjectCreate) -> Project:
    db_project = Project(**project.dict())
    db.add(db_project)
    await db.commit()
    await db.refresh(db_project)
    return db_project

async def get_project(db: AsyncSession, project_id: int) -> Optional[Project]:
    result = await db.execute(select(Project).where(Project.id == project_id))
    return result.scalars().first()

async def get_projects(db: AsyncSession, skip: int = 0, limit: int = 100) -> List[Project]:
    result = await db.execute(select(Project).offset(skip).limit(limit))
    return result.scalars().all()

async def update_project(db: AsyncSession, project_id: int, new_data: dict) -> Optional[Project]:
    project = await get_project(db, project_id)
    if not project:
        return None
    for key, value in new_data.items():
        setattr(project, key, value)
    await db.commit()
    await db.refresh(project)
    return project

async def delete_project(db: AsyncSession, project_id: int) -> bool:
    project = await get_project(db, project_id)
    if not project:
        return False
    await db.delete(project)  # db.delete sí es awaitable en AsyncSession
    await db.commit()
    return True
