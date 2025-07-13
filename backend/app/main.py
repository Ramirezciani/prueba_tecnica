from fastapi import FastAPI
from app.auth.auth_routes import router as auth_router
from app.auth.user_routes import router as user_router

# Crear una instancia de la aplicación FastAPI
app = FastAPI()

# Definir una ruta raíz con un mensaje de prueba
@app.get("/")
def read_root():
    return {"message": "FastAPI funcionando correctamente ✅"}

# Incluir las rutas del módulo de autenticación con el prefijo "/auth"
app.include_router(auth_router, prefix="/auth")
