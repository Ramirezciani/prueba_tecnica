# app/routes/user_routes.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import User
from app.auth.schemas.users.users import UserCreate, UserResponse, UserUpdate
from app.auth.crud_user import (
    get_user, get_users, get_user_by_email, get_user as get_user_by_id,
    create_user, update_user, delete_user
)
from app.database import get_db

router = APIRouter(
    tags=["users"]
)

@router.get("/", response_model=list[UserResponse])
async def list_users(db: AsyncSession = Depends(get_db)):
    return await get_users(db)

@router.get("/{user_id}", response_model=UserResponse)
async def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_new_user(user_in: UserCreate, db: AsyncSession = Depends(get_db)):
    user = await create_user(db, user=user_in)  # <--- Aquí paso user=user_in
    return user

@router.put("/{user_id}", response_model=UserResponse)
async def update_existing_user(user_id: int, user_in: UserUpdate, db: AsyncSession = Depends(get_db)):
    user = await get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return await update_user(db, user_id, user_in.dict(exclude_unset=True))

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_existing_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    await delete_user(db, user_id)
    return None
