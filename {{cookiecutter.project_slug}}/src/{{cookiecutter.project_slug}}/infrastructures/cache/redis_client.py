from dataclasses import dataclass
import json
from typing import Any, final

import structlog
from redis.asyncio import Redis
import redis.exceptions

from {{cookiecutter.project_slug}}.application.interfaces.cache import CacheProtocol

logger = structlog.get_logger(__name__)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class RedisCacheClient(CacheProtocol):
    """
    Redis implementation of the CacheProtocol for caching operations.
    """
    client: Redis
    ttl: int | None = None

    async def get(self, key: str) -> dict[str, Any] | None:
        """
        Retrieves a value from Redis cache by key.

        Args:
            key: Cache key to retrieve.

        Returns:
            Cached dictionary data or None if not found or an error occurs.
        """
        try:
            value = await self.client.get(key)
            if value is None:
                return None
            return json.loads(value)
        except (ConnectionError, redis.exceptions.RedisError) as e:
            logger.error(
                "Redis get operation failed", key=key, error=str(e)
            )
            return None
        except (json.JSONDecodeError, TypeError) as e:
            logger.warning(
                "Failed to decode cached value", key=key, error=str(e)
            )
            return None

    async def set(self, key: str, value: dict[str, Any], ttl: int | None = None) -> bool:
        """
        Stores a value in Redis cache with an optional TTL.

        Args:
            key: Cache key to store under.
            value: Dictionary data to cache.
            ttl: Time-to-live in seconds (None for default or no expiration).

        Returns:
            True if successful, False otherwise.
        """
        try:
            serialized_value = json.dumps(value, default=str)
            if ttl is not None:
                await self.client.setex(key, ttl, serialized_value)
            elif self.ttl is not None:
                await self.client.setex(key, self.ttl, serialized_value)
            else:
                await self.client.set(key, serialized_value)
            return True
        except (ConnectionError, redis.exceptions.RedisError) as e:
            logger.error(
                "Redis set operation failed", key=key, error=str(e)
            )
            return False
        except (TypeError, ValueError) as e:
            logger.error(
                "Failed to serialize value for cache",
                key=key,
                error=str(e),
            )
            return False

    async def delete(self, key: str) -> bool:
        """
        Deletes a value from Redis cache.

        Args:
            key: Cache key to delete.

        Returns:
            True if key was deleted, False if key didn't exist or an error occurs.
        """
        try:
            result = await self.client.delete(key)
            return result > 0
        except (ConnectionError, redis.exceptions.RedisError) as e:
            logger.error(
                "Redis delete operation failed", key=key, error=str(e)
            )
            return False

    async def exists(self, key: str) -> bool:
        """
        Checks if a key exists in Redis cache.

        Args:
            key: Cache key to check.

        Returns:
            True if key exists, False otherwise or if an error occurs.
        """
        try:
            return bool(await self.client.exists(key))
        except (ConnectionError, redis.exceptions.RedisError) as e:
            logger.error(
                "Redis exists operation failed", key=key, error=str(e)
            )
            return False

    async def clear(self, pattern: str) -> int:
        """
        Clears cache entries matching a pattern in Redis.

        Args:
            pattern: Pattern to match keys (e.g., 'user:*').

        Returns:
            Number of keys deleted.
        """
        try:
            keys = []
            async for key in self.client.scan_iter(match=pattern):
                keys.append(key)
            if keys:
                deleted_count = await self.client.delete(*keys)
                logger.info(
                    "Cleared cache keys matching pattern",
                    pattern=pattern,
                    count=deleted_count,
                )
                return deleted_count
            return 0
        except (ConnectionError, redis.exceptions.RedisError) as e:
            logger.error(
                "Redis clear pattern operation failed",
                pattern=pattern,
                error=str(e),
            )
            return 0

    async def close(self) -> None:
        """
        Closes the Redis client connection.
        """
        try:
            await self.client.close()
            logger.info("Redis connection closed")
        except (ConnectionError, redis.exceptions.RedisError) as e:
            logger.error("Failed to close Redis connection", error=str(e))
