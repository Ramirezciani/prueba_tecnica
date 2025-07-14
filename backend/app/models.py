from sqlalchemy import Column, Integer, String, TIMESTAMP, Text, ForeignKey, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Modelo para la tabla de usuarios
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)  # Identificador único del usuario
    name = Column(String(100), nullable=False)  # Nombre del usuario
    email = Column(String(100), unique=True, nullable=False)  # Correo electrónico único del usuario
    password_hash = Column(String(255), nullable=False)  # Hash de la contraseña del usuario
    role = Column(String(100), nullable=False)  # Rol del usuario (ejemplo: admin, usuario)
    created_at = Column(TIMESTAMP, server_default=func.now())  # Fecha y hora de creación del usuario

# Modelo para la tabla de proyectos
class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)  # Identificador único del proyecto
    name = Column(String(150), nullable=False)  # Nombre del proyecto
    description = Column(Text, nullable=True)  # Descripción del proyecto (opcional)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)  # ID del usuario propietario
    created_at = Column(TIMESTAMP, server_default=func.now())  # Fecha y hora de creación del proyecto

    # Relación con el modelo User (un proyecto pertenece a un usuario)
    owner = relationship("User", backref="projects", passive_deletes=True)
