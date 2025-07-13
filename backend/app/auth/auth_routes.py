from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.database import get_db
from app.models import User
from app.auth.schemas.users.users import UserLogin, UserCreate, UserResponse
from app.auth.auth_utils import verify_password, create_access_token, hash_password

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", summary="Iniciar sesión")
async def login(user: UserLogin, db: AsyncSession = Depends(get_db)):
    # Consultar el usuario en la base de datos por su correo electrónico
    query = select(User).where(User.email == user.email)
    result = await db.execute(query)
    db_user = result.scalar_one_or_none()

    # Verificar si el usuario existe y si la contraseña es válida
    if not db_user or not verify_password(user.password, db_user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas"  # Mensaje de error si las credenciales no son válidas
        )

    # Crear un token de acceso para el usuario autenticado
    token = create_access_token({"sub": db_user.email})
    return {"access_token": token, "token_type": "bearer"}


@router.post("/users", response_model=UserResponse, summary="Crear primer usuario")
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    # Validar si ya existen usuarios en la base de datos
    result = await db.execute(select(User))
    existing_user = result.scalars().first()

    # Si ya existe un usuario, no se permite crear otro sin autenticación
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Solo se permite crear el primer usuario sin autenticación"  # Mensaje de error
        )

    # Crear un nuevo usuario con rol de administrador
    new_user = User(
        name=user.name,
        email=user.email,
        password_hash=hash_password(user.password),  # Hashear la contraseña antes de guardarla
        role="Administrador",  # El primer usuario será administrador
    )
    db.add(new_user)  # Agregar el nuevo usuario a la sesión de la base de datos
    await db.commit()  # Confirmar los cambios en la base de datos
    await db.refresh(new_user)  # Refrescar la instancia del usuario para obtener los datos actualizados
    return new_user  # Retornar el usuario creado
