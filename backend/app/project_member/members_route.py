from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Dict, Any
from app.database import get_db
from app.project_member.crud_member import get_kanban_board

router = APIRouter()

@router.get("/kanban", response_model=List[Dict[str, Any]])
async def kanban_dashboard(db: AsyncSession = Depends(get_db)):
    return await get_kanban_board(db)
