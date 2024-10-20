import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    PROJECT_NAME: str = "EasyCare App"
    PROJECT_DESCRIPTION: str = "EasyCare API"
    DB_URL: str = os.getenv("DB_URL")
    DB_API_KEY: str = os.getenv("DB_API_KEY")
    DB_EMAIL: str = os.getenv("DB_EMAIL")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    ROOT_PATH: str = os.getenv("ROOT_PATH")
    model_config = SettingsConfigDict(env_file=".env")
    API_VERSION: str = "/api/v1"
    ROOT: str = os.getenv("ROOT_PATH")
    BUCKET_NAME: str = os.getenv("BUCKET_NAME")

settings = Settings()
