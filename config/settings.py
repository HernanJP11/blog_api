from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Blog API"
    database_url: str = "sqlite:///./blog.db"
    environment: str = "development"
    
    class Config:
        env_file = ".env"

settings = Settings()