from fastapi import FastAPI
from config.settings import settings

app = FastAPI(title=settings.app_name, version="1.0.0")

@app.get("/")
def read_root():
    return {"message": "¡Blog API funcionando!", "status": "running"}