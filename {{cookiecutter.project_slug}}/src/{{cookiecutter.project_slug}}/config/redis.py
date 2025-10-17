from typing import final

from pydantic import Field, RedisDsn
from pydantic_settings import BaseSettings


@final
class RedisSettings(BaseSettings):
    """
    Redis configuration settings.

    Attributes:
        redis_url (RedisDsn): Redis connection URL.
        redis_password (str): Redis password.
        redis_port (int): Redis port.
        redis_host (str): Redis host.
        redis_db (int): Redis database number.
        redis_cache_ttl (int): Time-to-live for Redis cache entries in seconds.
        redis_cache_prefix (str): Prefix for Redis cache keys.
    """

    redis_url: RedisDsn = Field(
        RedisDsn("redis://:redis_password@redis:6379/0"), alias="REDIS_URL"
    )
    redis_password: str = Field("redis_password", alias="REDIS_PASSWORD")
    redis_port: int = Field(6379, alias="REDIS_PORT")
    redis_host: str = Field("redis", alias="REDIS_HOST")
    redis_db: int = Field(0, alias="REDIS_DB")
    redis_cache_ttl: int = Field(3600, alias="REDIS_CACHE_TTL")  # 1 hour default TTL
    redis_cache_prefix: str = Field("antiques:", alias="REDIS_CACHE_PREFIX")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"
