from dotenv import find_dotenv
from pydantic import BaseSettings, Field


class Base(BaseSettings):
    class Config:
        env_file = find_dotenv()
        env_file_encoding = "utf-8"


class CognitiveSearchSettings(Base):
    rabbitmq_broker: str = Field(env="CELERY_RABBITMQ_BROKER")
    app_name: str = Field(env="CELERY_APP_NAME")
