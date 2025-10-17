from pydantic import Field
from pydantic_settings import BaseSettings

from {{cookiecutter.project_slug}}.config.app import AppSettings
from {{cookiecutter.project_slug}}.config.broker import BrokerSettings
from {{cookiecutter.project_slug}}.config.cors import CORSSettings
from {{cookiecutter.project_slug}}.config.database import DatabaseSettings
from {{cookiecutter.project_slug}}.config.external_apis import ExternalAPISettings
from {{cookiecutter.project_slug}}.config.redis import RedisSettings


class Settings(BaseSettings):
    """
    Main application settings that combines all configuration objects.

    This class serves as a facade that provides access to all configuration
    sections of the application. Each configuration section is responsible
    for a specific domain (database, redis, cors, etc.).
    """

    app: AppSettings = Field(default_factory=AppSettings)
    database: DatabaseSettings = Field(default_factory=DatabaseSettings)
    redis: RedisSettings = Field(default_factory=RedisSettings)
    external_apis: ExternalAPISettings = Field(default_factory=ExternalAPISettings)
    broker: BrokerSettings = Field(default_factory=BrokerSettings)
    cors: CORSSettings = Field(default_factory=CORSSettings)

    # Convenience properties for backward compatibility
    @property
    def app_name(self) -> str:
        """Get application name."""
        return self.app.app_name

    @property
    def environment(self) -> str:
        """Get application environment."""
        return self.app.environment

    @property
    def log_level(self) -> str:
        """Get log level."""
        return self.app.log_level

    @property
    def debug(self) -> bool:
        """Get debug flag."""
        return self.app.debug

    @property
    def database_url(self) -> str:
        """Get database URL."""
        return str(self.database.database_url)

    @property
    def sqlalchemy_database_uri(self) -> str:
        """Get SQLAlchemy database URI."""
        return str(self.database.sqlalchemy_database_uri)

    @property
    def redis_url(self) -> str:
        """Get Redis URL."""
        return str(self.redis.redis_url)

    @property
    def museum_api_base(self) -> str:
        """Get museum API base URL."""
        return self.external_apis.museum_api_base

    @property
    def catalog_api_base(self) -> str:
        """Get catalog API base URL."""
        return self.external_apis.catalog_api_base

    @property
    def external_api_base_url(self) -> str:
        """Get external API base URL (alias)."""
        return self.external_apis.external_api_base_url

    @property
    def catalog_api_base_url(self) -> str:
        """Get catalog API base URL (alias)."""
        return self.external_apis.catalog_api_base_url

    @property
    def http_timeout(self) -> float:
        """Get HTTP timeout."""
        return self.external_apis.http_timeout

    @property
    def broker_url(self) -> str:
        """Get broker URL."""
        return self.broker.broker_url

    @property
    def broker_new_artifact_queue(self) -> str:
        """Get broker new artifact queue name."""
        return self.broker.broker_new_artifact_queue

    @property
    def publish_retries(self) -> int:
        """Get publish retries count."""
        return self.broker.publish_retries

    @property
    def publish_retry_backoff(self) -> float:
        """Get publish retry backoff."""
        return self.broker.publish_retry_backoff

    @property
    def redis_password(self) -> str:
        """Get Redis password."""
        return self.redis.redis_password

    @property
    def redis_port(self) -> int:
        """Get Redis port."""
        return self.redis.redis_port

    @property
    def redis_host(self) -> str:
        """Get Redis host."""
        return self.redis.redis_host

    @property
    def redis_db(self) -> int:
        """Get Redis database number."""
        return self.redis.redis_db

    @property
    def redis_cache_ttl(self) -> int:
        """Get Redis cache TTL."""
        return self.redis.redis_cache_ttl

    @property
    def redis_cache_prefix(self) -> str:
        """Get Redis cache prefix."""
        return self.redis.redis_cache_prefix

    @property
    def cors_origins(self) -> list[str]:
        """Get CORS origins."""
        return self.cors.cors_origins

    @property
    def cors_allow_credentials(self) -> bool:
        """Get CORS allow credentials flag."""
        return self.cors.cors_allow_credentials

    @property
    def cors_allow_methods(self) -> list[str]:
        """Get CORS allow methods."""
        return self.cors.cors_allow_methods

    @property
    def cors_allow_headers(self) -> list[str]:
        """Get CORS allow headers."""
        return self.cors.cors_allow_headers

    @property
    def postgres_user(self) -> str:
        """Get PostgreSQL username."""
        return self.database.postgres_user

    @property
    def postgres_password(self) -> str:
        """Get PostgreSQL password."""
        return self.database.postgres_password

    @property
    def postgres_server(self) -> str:
        """Get PostgreSQL server."""
        return self.database.postgres_server

    @property
    def postgres_port(self) -> int:
        """Get PostgreSQL port."""
        return self.database.postgres_port

    @property
    def postgres_db(self) -> str:
        """Get PostgreSQL database name."""
        return self.database.postgres_db
