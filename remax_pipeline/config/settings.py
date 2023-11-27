from dotenv import find_dotenv
from pydantic import BaseSettings


class Base(BaseSettings):
    class Config:
        env_file = find_dotenv()
        env_file_encoding = "utf-8"


class CelerySettings(Base):
    rabbitmq_broker: str
    app_name: str

    class Config:
        env_prefix = "CELERY_"

class PostegresSettings:
    dbname: str
    user: str
    passsword: str
    host: str
    post: str

    class Config:
        env_prefix = "POSTGRES_"
