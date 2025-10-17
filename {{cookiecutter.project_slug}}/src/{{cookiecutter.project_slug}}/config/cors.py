from typing import final

from pydantic import Field
from pydantic_settings import BaseSettings


@final
class CORSSettings(BaseSettings):
    """
    CORS configuration settings.

    Attributes:
        cors_origins (list[str]): List of allowed CORS origins.
        cors_allow_credentials (bool): Whether CORS requests should support credentials.
        cors_allow_methods (list[str]): List of allowed CORS HTTP methods.
        cors_allow_headers (list[str]): List of allowed CORS HTTP headers.
    """

    cors_origins: list[str] = Field(
        ["http://localhost:3000", "http://localhost:8080"], alias="CORS_ORIGINS"
    )
    cors_allow_credentials: bool = Field(True, alias="CORS_ALLOW_CREDENTIALS")
    cors_allow_methods: list[str] = Field(
        ["GET", "POST", "PUT", "DELETE", "OPTIONS"], alias="CORS_ALLOW_METHODS"
    )
    cors_allow_headers: list[str] = Field(["*"], alias="CORS_ALLOW_HEADERS")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"
