from typing import Literal, final

from pydantic import Field
from pydantic_settings import BaseSettings


@final
class AppSettings(BaseSettings):
    """
    Application core settings.

    Attributes:
        app_name (str): Name of the application.
        environment (Literal["local", "dev", "development", "prod"]): Application environment.
        log_level (Literal["DEBUG", "INFO", "WARNING", "ERROR"]): Logging level.
        debug (bool): Debug mode flag.
    """

    app_name: str = "Antiquarium Service"
    environment: Literal["local", "dev", "development", "prod"] = "local"
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR"] = "INFO"
    debug: bool = Field(False, alias="DEBUG")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"
