from typing import final


class RepositorySaveError(Exception):
    """Exception raised when an error occurs during repository save operation."""


@final
class RepositoryConflictError(Exception):
    """Exception raised when a conflict occurs during a repository operation."""
