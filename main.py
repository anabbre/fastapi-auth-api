from fastapi import FastAPI
from auth import router as auth_router

# Inicializar la aplicación
app = FastAPI(title="API de Autenticación con JWT")

# Registrar los endpoints de autenticación
app.include_router(auth_router)

# Ruta de prueba
@app.get("/")
def home():
    return {"message": "Bienvenido a la API de Autenticación con FastAPI"}
