from fastapi import FastAPI
from config.settings import settings
from app.core.config import init_db
app = FastAPI(title=settings.app_name, version="1.0.0")


@app.on_event("startup")
def on_startup():
    """Crea la base de datos al iniciar la aplicación."""
    init_db()
    

@app.get("/")
def read_root():
    return {"message": "¡Blog API funcionando!", "status": "running"}