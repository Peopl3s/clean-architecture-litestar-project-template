from abc import abstractmethod
from typing import Any, Protocol, TypeVar

T = TypeVar("T")


class CacheProtocol(Protocol):
    """Protocol for cache operations.

    This protocol defines the interface for caching implementations.
    Values are stored as Any type to support various serialization formats.
    """

    @abstractmethod
    async def get(self, key: str) -> dict[str, Any] | None:
        """Retrieve a value from cache by key.

        Args:
            key: Cache key to retrieve

        Returns:
            Cached dictionary data or None if not found
        """
        ...

    @abstractmethod
    async def set(self, key: str, value: dict[str, Any], ttl: int | None = None) -> bool:
        """Store a value in cache with optional TTL.

        Args:
            key: Cache key to store under
            value: Dictionary data to cache
            ttl: Time-to-live in seconds (None for default)

        Returns:
            True if successful, False otherwise
        """
        ...

    @abstractmethod
    async def delete(self, key: str) -> bool:
        """Delete a value from cache.

        Args:
            key: Cache key to delete

        Returns:
            True if key was deleted, False if key didn't exist
        """
        ...

    @abstractmethod
    async def exists(self, key: str) -> bool:
        """Check if a key exists in cache.

        Args:
            key: Cache key to check

        Returns:
            True if key exists, False otherwise
        """
        ...

    @abstractmethod
    async def clear(self, pattern: str) -> int:
        """Clear cache entries matching a pattern.

        Args:
            pattern: Pattern to match keys (e.g., 'user:*')

        Returns:
            Number of keys deleted
        """
        ...
