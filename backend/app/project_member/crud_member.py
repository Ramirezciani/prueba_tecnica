from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from collections import defaultdict

from app.models import Project, Task, ProjectMember

async def get_kanban_board(db: AsyncSession) -> List[dict]:
    # Traer todos los proyectos con sus miembros cargados
    projects_res = await db.execute(
        select(Project).options(
            selectinload(Project.members).selectinload(ProjectMember.user)
        )
    )
    projects = projects_res.scalars().all()

    # Traer todas las tareas con usuario asignado
    tasks_res = await db.execute(
        select(Task).options(
            selectinload(Task.assigned_user)
        )
    )
    tasks = tasks_res.scalars().all()

    # Agrupar tareas y miembros por proyecto_id
    tasks_by_project = defaultdict(list)
    for task in tasks:
        tasks_by_project[task.project_id].append(task)

    members_by_project = defaultdict(list)
    for project in projects:
        members_by_project[project.id] = project.members

    kanban_data = []
    for project in projects:
        kanban_data.append({
            "project_id": project.id,
            "project_name": project.name,
            "tasks": [
                {
                    "id": task.id,
                    "title": task.title,
                    "description": task.description,
                    "status": task.status,
                    "due_date": task.due_date.isoformat() if task.due_date else None,
                    "completed": bool(task.completed),
                    "assigned_to": {
                        "id": task.assigned_user.id,
                        "name": task.assigned_user.name
                    } if task.assigned_user else None
                }
                for task in tasks_by_project.get(project.id, [])
            ],
            "members": [
                {
                    "id": member.user.id,
                    "name": member.user.name
                }
                for member in members_by_project.get(project.id, [])
            ]
        })

    return kanban_data
