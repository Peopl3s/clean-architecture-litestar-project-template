from typing import final


@final
class InvalidMaterialException(Exception):
    """Raised when an invalid material is provided."""


@final
class InvalidEraException(Exception):
    """Raised when an invalid era is provided."""


@final
class DomainValidationError(Exception):
    """Raised when domain entity validation fails."""
    ...
