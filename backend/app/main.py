from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.future import select
from datetime import datetime

from app.auth.auth_routes import router as auth_router
from app.auth.user_routes import router as user_router
from app.database import AsyncSessionLocal
from app.models import User
from app.auth.auth_utils import hash_password 
from app.projects.project_routes import router as project_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth")
app.include_router(user_router, prefix="/users")
app.include_router(project_router, prefix="/projects")

@app.get("/")
def read_root():
    return {"message": "FastAPI funcionando correctamente ✅"}


# ✅ Función para crear admin
async def create_admin():
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(User).where(User.name == "admin"))  # ← usar name, no username
        admin = result.scalars().first()
        if not admin:
            admin_user = User(
                name="admin",
                email="admin@example.com",
                password_hash=hash_password("admin"),  # ← corrección
                created_at=datetime.utcnow(),
                role="Administrador"
            )
            session.add(admin_user)
            await session.commit()
            print("✅ Usuario admin creado automáticamente")

# ✅ Evento al iniciar
@app.on_event("startup")
async def on_startup():
    await create_admin()
