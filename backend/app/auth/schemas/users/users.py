#app/schemas/users/users.py
from pydantic import BaseModel, EmailStr

# Esquema para la creación de un usuario
class UserCreate(BaseModel):
    name: str  # Nombre del usuario
    email: EmailStr  # Correo electrónico del usuario (validado como email)
    password: str  # Contraseña del usuario
    role: str # Rol del usuario
# Esquema para el inicio de sesión de un usuario
class UserLogin(BaseModel):
    email: EmailStr  # Correo electrónico del usuario (validado como email)
    password: str  # Contraseña del usuario

# Esquema para la respuesta de un usuario
class UserResponse(BaseModel):
    id: int  # Identificador único del usuario
    email: EmailStr  # Correo electrónico del usuario
    role: str  # Rol del usuario en el sistema

    # Configuración para habilitar el modo ORM (Object-Relational Mapping)
    class Config:
        from_attributes = True
