# crud_user.py
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from app.models import User
from app.auth.schemas.users.users import UserCreate, UserUpdate
from app.auth.auth_utils import hash_password  # Asegúrate de tener esta función

async def create_user(db: AsyncSession, *, user: UserCreate) -> User:
    db_user = User(
        name=user.name,
        email=user.email,
        password_hash=hash_password(user.password),  # Hashea la contraseña antes de guardar
        role=user.role
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

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