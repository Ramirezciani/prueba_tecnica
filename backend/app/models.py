from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from sqlalchemy.ext.declarative import declarative_base

# Se define la base para los modelos de SQLAlchemy
Base = declarative_base()

class User(Base):
    __tablename__ = "users"  # Nombre de la tabla en la base de datos

    # Definición de las columnas de la tabla
    id = Column(Integer, primary_key=True, index=True)  # Identificador único para cada usuario
    name = Column(String(100), nullable=False)  # Nombre del usuario (obligatorio)
    email = Column(String(100), unique=True, nullable=False)  # Correo electrónico único (obligatorio)
    password_hash = Column(String(255), nullable=False)  # Hash de la contraseña del usuario (obligatorio)
    role =  Column(String(100), nullable=False)  # Rol del usuario (obligatorio)
    created_at = Column(TIMESTAMP, server_default=func.now())  # Fecha y hora de creación del registro
