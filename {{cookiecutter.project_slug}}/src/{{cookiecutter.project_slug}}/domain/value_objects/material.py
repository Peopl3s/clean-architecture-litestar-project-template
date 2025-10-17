from dataclasses import dataclass
from typing import ClassVar, final

from {{cookiecutter.project_slug}}.domain.exceptions import InvalidMaterialException


@final
@dataclass(frozen=True, slots=True, kw_only=True, order=True)
class Material:
    """
    Value object representing a material type.

    Ensures that the material value is one of the predefined allowed values.
    """
    _allowed_values: ClassVar[set[str]] = {
        "ceramic",
        "metal",
        "stone",
        "glass",
        "bone",
        "wood",
        "textile",
        "other",
    }
    value: str

    def __post_init__(self) -> None:
        """
        Validates the material value after initialization.

        Raises:
            InvalidMaterialException: If the provided material value is not allowed.
        """
        if self.value not in self._allowed_values:
            raise InvalidMaterialException(f"Invalid material: {self.value}")

    def __str__(self) -> str:
        """
        Returns the string representation of the material.
        """
        return self.value
