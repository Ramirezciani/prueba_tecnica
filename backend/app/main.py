from fastapi import FastAPI
from app.auth.auth_routes import router as auth_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI funcionando correctamente ✅"}

app.include_router(auth_router, prefix="/auth")
