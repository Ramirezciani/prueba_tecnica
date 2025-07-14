from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.projects.crud_project import (create_project, get_project, get_projects, update_project, delete_project)
from app.projects.project import ProjectCreate, ProjectUpdate, ProjectOut
from app.database import get_db  # get_db debe devolver AsyncSession

router = APIRouter(tags=["projects"])

@router.post("/", response_model=ProjectOut, status_code=status.HTTP_201_CREATED)
async def create_project_route(project: ProjectCreate, db: AsyncSession = Depends(get_db)):
    return await create_project(db, project=project)

@router.get("/", response_model=List[ProjectOut])
async def list_projects(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    return await get_projects(db, skip=skip, limit=limit)

@router.get("/{project_id}", response_model=ProjectOut)
async def get_project_route(project_id: int, db: AsyncSession = Depends(get_db)):
    db_project = await get_project(db, project_id)
    if not db_project:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project

@router.put("/{project_id}", response_model=ProjectOut)
async def update_project_route(project_id: int, project_update: ProjectUpdate, db: AsyncSession = Depends(get_db)):
    updated = await update_project(db, project_id, project_update.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Project not found")
    return updated

@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_project_route(project_id: int, db: AsyncSession = Depends(get_db)):
    success = await delete_project(db, project_id)
    if not success:
        raise HTTPException(status_code=404, detail="Project not found")
    return None


