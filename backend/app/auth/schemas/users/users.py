# app/schemas/users/users.py
from pydantic import BaseModel
from typing import Optional

# Esquema para la creación de un usuario
class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    role: str

# Esquema para el inicio de sesión de un usuario
class UserLogin(BaseModel):
    email: str
    password: str

# Esquema para la respuesta de un usuario
class UserResponse(BaseModel):
    id: int
    email: str
    role: str

    class Config:
        from_attributes = True  # reemplazo de orm_mode

# Esquema para la actualización de un usuario
class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    role: Optional[str] = None
