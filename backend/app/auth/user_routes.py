from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import User
from app.auth.crud_user import get_user_by_id, get_users, create_user, update_user, delete_user
from app.database import get_async_session

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/", response_model=list[UserRead])
async def list_users(db: AsyncSession = Depends(get_async_session)):
    users = await get_users(db)
    return users

@router.get("/{user_id}", response_model=UserRead)
async def read_user(user_id: int, db: AsyncSession = Depends(get_async_session)):
    user = await get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_new_user(user_in: UserCreate, db: AsyncSession = Depends(get_async_session)):
    user = await create_user(db, user_in)
    return user

@router.put("/{user_id}", response_model=UserRead)
async def update_existing_user(user_id: int, user_in: UserUpdate, db: AsyncSession = Depends(get_async_session)):
    user = await get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    updated_user = await update_user(db, user, user_in)
    return updated_user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_existing_user(user_id: int, db: AsyncSession = Depends(get_async_session)):
    user = await get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    await delete_user(db, user)
    return None
