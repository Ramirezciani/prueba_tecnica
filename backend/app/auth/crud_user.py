# crud_user.py
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import User
from typing import List, Optional

# Crear usuario
async def create_user(db: AsyncSession, *, user: User) -> User:
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

# Obtener usuario por ID
async def get_user(db: AsyncSession, user_id: int) -> Optional[User]:
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalars().first()

# Obtener usuario por email
async def get_user_by_email(db: AsyncSession, email: str) -> Optional[User]:
    result = await db.execute(select(User).where(User.email == email))
    return result.scalars().first()

# Listar todos los usuarios
async def get_users(db: AsyncSession, skip: int = 0, limit: int = 100) -> List[User]:
    result = await db.execute(select(User).offset(skip).limit(limit))
    return result.scalars().all()

# Actualizar usuario
async def update_user(db: AsyncSession, user_id: int, new_data: dict) -> Optional[User]:
    user = await get_user(db, user_id)
    if not user:
        return None
    for key, value in new_data.items():
        setattr(user, key, value)
    await db.commit()
    await db.refresh(user)
    return user

# Eliminar usuario
async def delete_user(db: AsyncSession, user_id: int) -> bool:
    user = await get_user(db, user_id)
    if not user:
        return False
    await db.delete(user)
    await db.commit()
    return True
