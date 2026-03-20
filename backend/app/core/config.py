from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Yelen Import API"
    DATABASE_URL: str = "postgresql://postgres:Ouma%40218@localhost:5432/YelenImport"
    SECRET_KEY: str = "your_secret_key_here"
    DEBUG: bool = False

    class Config:
        env_file = ".env"

settings = Settings()