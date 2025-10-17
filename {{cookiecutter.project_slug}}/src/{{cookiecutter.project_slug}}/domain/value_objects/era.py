from dataclasses import dataclass
from typing import ClassVar, final

from {{cookiecutter.project_slug}}.domain.exceptions import InvalidEraException


@final
@dataclass(frozen=True, slots=True, kw_only=True, order=True)
class Era:
    """
    Value object representing a historical era.

    Ensures that the era value is one of the predefined allowed values.
    """
    _allowed_values: ClassVar[set[str]] = {
        "paleolithic",
        "neolithic",
        "bronze_age",
        "iron_age",
        "antiquity",
        "middle_ages",
        "modern",
    }
    value: str

    def __post_init__(self) -> None:
        """
        Validates the era value after initialization.

        Raises:
            InvalidEraException: If the provided era value is not allowed.
        """
        if self.value not in self._allowed_values:
            raise InvalidEraException(f"Invalid era: {self.value}")

    def __str__(self) -> str:
        """
        Returns the string representation of the era.
        """
        return self.value
