import logging
from pydantic import BaseSettings, Field


def generate_redis_url(host, port):
    return f"redis://{host}:{port}/"


def generate_logging_level(level):
    level_map = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR,
        'CRITICAL': logging.CRITICAL,
    }
    return level_map.get(f'{level}')


class Settings(BaseSettings):
    REDIS_HOST: str = Field(env="REDIS_HOST")
    REDIS_PORT: int = Field(env="REDIS_PORT")

    LOGGING_LEVEL: str = Field(env='LOGGING_LEVEL')

    BOT_TOKEN: str = Field(env='BOT_TOKEN')

    @property
    def redis_url(self):
        return generate_redis_url(host=self.REDIS_HOST, port=self.REDIS_PORT)

    @property
    def logging_level(self):
        return generate_logging_level(level=self.LOGGING_LEVEL)

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
