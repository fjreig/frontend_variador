from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    POSTGRES_USER: str = os.environ['POSTGRES_USER']
    POSTGRES_PASSWORD: str = os.environ['POSTGRES_PASSWORD']
    POSTGRES_PORT: str = os.environ['POSTGRES_PORT']
    POSTGRES_DB: str = os.environ['POSTGRES_DB']
    POSTGRES_HOST: str = os.environ['POSTGRES_HOST']

    MODBUS_HOST: str = os.environ['MODBUS_host']
    MODBUS_PORT: str = os.environ['MODBUS_port']

    class Config:
        env_file = 'settings.cfg'

settings = Settings()