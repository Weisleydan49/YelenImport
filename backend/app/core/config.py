from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME = "Yelen Import API"
    DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/yelenimport"
    SECRET_KEY = str 
    DEBUG: bool = False

    class Config:
        env_file = ".env"

        settings = Settings()