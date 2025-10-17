from typing import cast, final

from pydantic import Field, PostgresDsn, computed_field
from pydantic_settings import BaseSettings


@final
class DatabaseSettings(BaseSettings):
    """
    Database configuration settings.

    Attributes:
        postgres_user (str): PostgreSQL username.
        postgres_password (str): PostgreSQL password.
        postgres_server (str): PostgreSQL server host.
        postgres_port (int): PostgreSQL server port.
        postgres_db (str): PostgreSQL database name.
    """

    postgres_user: str = Field(..., alias="POSTGRES_USER")
    postgres_password: str = Field(..., alias="POSTGRES_PASSWORD")
    postgres_server: str = Field(..., alias="POSTGRES_SERVER")
    postgres_port: int = Field(5432, alias="POSTGRES_PORT")
    postgres_db: str = Field(..., alias="POSTGRES_DB")

    @computed_field
    def database_url(self) -> PostgresDsn:
        """
        Constructs the PostgreSQL database URL.

        Returns:
            PostgresDsn: The constructed database URL.
        """
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            username=self.postgres_user,
            password=self.postgres_password,
            host=self.postgres_server,
            port=self.postgres_port,
            path=self.postgres_db,
        )

    @computed_field
    def sqlalchemy_database_uri(self) -> PostgresDsn:
        """
        Returns the SQLAlchemy compatible database URI.

        Returns:
            PostgresDsn: The SQLAlchemy database URI.
        """
        return cast("PostgresDsn", self.database_url)

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"
