from typing import final

from pydantic import Field
from pydantic_settings import BaseSettings


@final
class ExternalAPISettings(BaseSettings):
    """
    External API configuration settings.

    Attributes:
        museum_api_base (str): Base URL for the external museum API.
        catalog_api_base (str): Base URL for the public catalog API.
        external_api_base_url (str): Alias for museum_api_base.
        catalog_api_base_url (str): Alias for catalog_api_base.
        http_timeout (float): HTTP request timeout in seconds.
    """

    museum_api_base: str = Field(
        "https://api.antiquarium-museum.ru", alias="MUSEUM_API_BASE"
    )
    catalog_api_base: str = Field(
        "https://catalog.antiquarium-museum.ru", alias="CATALOG_API_BASE"
    )

    # Aliases for compatibility
    external_api_base_url: str = Field(
        "https://api.antiquarium-museum.ru", alias="EXTERNAL_API_BASE_URL"
    )
    catalog_api_base_url: str = Field(
        "https://catalog.antiquarium-museum.ru", alias="CATALOG_API_BASE_URL"
    )

    http_timeout: float = Field(10.0, alias="HTTP_TIMEOUT")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"
