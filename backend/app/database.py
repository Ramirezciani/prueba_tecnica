# app/database.py
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env (asegúrate que python-dotenv esté instalado)
load_dotenv()

# Ahora sí obtenemos la variable DATABASE_URL desde el entorno
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://admin:admin@db:5432/taskdb")

# Crear el engine asíncrono
engine = create_async_engine(DATABASE_URL, echo=True)

# Crear la fábrica de sesiones asíncronas
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# Función para usar en dependencia FastAPI para obtener sesión DB
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
