from polyfactory.factories import BaseFactory
from polyfactory.field_meta import FieldMeta
from dataclasses import fields, is_dataclass
from typing import get_type_hints

from tests.faker import uuid4, word, text, date_time_this_century

from {{cookiecutter.project_slug}}.application.dtos.artifact import (
    ArtifactDTO,
    EraDTO,
    MaterialDTO,
)
from {{cookiecutter.project_slug}}.domain.entities.artifact import (
    ArtifactEntity,
    Material,
    Era,
)


class MaterialDTOFactory(BaseFactory):
    """Factory for MaterialDTO objects."""
    __model__ = MaterialDTO

    @classmethod
    def is_supported_type(cls, model: type) -> bool:
        """Override to support frozen dataclasses"""
        return True

    @classmethod
    def get_model_fields(cls) -> list[FieldMeta]:
        """Override to support frozen dataclasses"""
        if not is_dataclass(cls.__model__):
            return []

        model_fields = []
        type_hints = get_type_hints(cls.__model__)

        for field in fields(cls.__model__):
            field_type = type_hints.get(field.name, field.type)
            model_fields.append(
                FieldMeta(
                    name=field.name,
                    annotation=field_type,
                    default=field.default,
                )
            )

        return model_fields

    @classmethod
    def get_field_value(cls, field_name: str, field_meta: FieldMeta | None = None, **kwargs):
        if field_name == "value":
            return cls.__random__.choice([
                "ceramic", "metal", "stone", "glass", "bone", "wood", "textile", "other"
            ])
        return super().get_field_value(field_name, field_meta)


class EraDTOFactory(BaseFactory):
    """Factory for EraDTO objects."""
    __model__ = EraDTO

    @classmethod
    def is_supported_type(cls, model: type) -> bool:
        """Override to support frozen dataclasses"""
        return True

    @classmethod
    def get_model_fields(cls) -> list[FieldMeta]:
        """Override to support frozen dataclasses"""
        if not is_dataclass(cls.__model__):
            return []

        model_fields = []
        type_hints = get_type_hints(cls.__model__)

        for field in fields(cls.__model__):
            field_type = type_hints.get(field.name, field.type)
            model_fields.append(
                FieldMeta(
                    name=field.name,
                    annotation=field_type,
                    default=field.default,
                )
            )

        return model_fields

    @classmethod
    def get_field_value(cls, field_name: str, field_meta: FieldMeta | None = None, **kwargs):
        if field_name == "value":
            return cls.__random__.choice([
                "paleolithic", "neolithic", "bronze_age", "iron_age", "antiquity",
                "middle_ages", "modern"
            ])
        return super().get_field_value(field_name, field_meta)


class ArtifactDTOFactory(BaseFactory):
    """Factory for ArtifactDTO objects."""
    __model__ = ArtifactDTO

    @classmethod
    def is_supported_type(cls, model: type) -> bool:
        """Override to support frozen dataclasses"""
        return True

    @classmethod
    def get_model_fields(cls) -> list[FieldMeta]:
        """Override to support frozen dataclasses"""
        if not is_dataclass(cls.__model__):
            return []

        model_fields = []
        type_hints = get_type_hints(cls.__model__)

        for field in fields(cls.__model__):
            field_type = type_hints.get(field.name, field.type)
            model_fields.append(
                FieldMeta(
                    name=field.name,
                    annotation=field_type,
                    default=field.default,
                )
            )

        return model_fields

    @classmethod
    def get_field_value(cls, field_name: str, field_meta: FieldMeta | None = None, **kwargs):
        if field_name == "inventory_id":
            return uuid4()
        elif field_name == "acquisition_date":
            return date_time_this_century()
        elif field_name == "name":
            return word()
        elif field_name == "department":
            return word()
        elif field_name == "description":
            return text()
        elif field_name == "created_at":
            return date_time_this_century()
        elif field_name == "era":
            return EraDTOFactory.build()
        elif field_name == "material":
            return MaterialDTOFactory.build()
        return super().get_field_value(field_name, field_meta)


class MaterialFactory(BaseFactory):
    """Factory for Material value objects."""
    __model__ = Material

    @classmethod
    def is_supported_type(cls, model: type) -> bool:
        """Override to support frozen dataclasses"""
        return True

    @classmethod
    def get_model_fields(cls) -> list[FieldMeta]:
        """Override to support frozen dataclasses"""
        if not is_dataclass(cls.__model__):
            return []

        model_fields = []
        type_hints = get_type_hints(cls.__model__)

        for field in fields(cls.__model__):
            field_type = type_hints.get(field.name, field.type)
            model_fields.append(
                FieldMeta(
                    name=field.name,
                    annotation=field_type,
                    default=field.default,
                )
            )

        return model_fields

    @classmethod
    def get_field_value(cls, field_name: str, field_meta: FieldMeta | None = None, **kwargs):
        if field_name == "value":
            return cls.__random__.choice([
                "ceramic", "metal", "stone", "glass", "bone", "wood", "textile", "other"
            ])
        return super().get_field_value(field_name, field_meta)


class EraFactory(BaseFactory):
    """Factory for Era value objects."""
    __model__ = Era

    @classmethod
    def is_supported_type(cls, model: type) -> bool:
        """Override to support frozen dataclasses"""
        return True

    @classmethod
    def get_model_fields(cls) -> list[FieldMeta]:
        """Override to support frozen dataclasses"""
        if not is_dataclass(cls.__model__):
            return []

        model_fields = []
        type_hints = get_type_hints(cls.__model__)

        for field in fields(cls.__model__):
            field_type = type_hints.get(field.name, field.type)
            model_fields.append(
                FieldMeta(
                    name=field.name,
                    annotation=field_type,
                    default=field.default,
                )
            )

        return model_fields

    @classmethod
    def get_field_value(cls, field_name: str, field_meta: FieldMeta | None = None, **kwargs):
        if field_name == "value":
            return cls.__random__.choice([
                "paleolithic", "neolithic", "bronze_age", "iron_age", "antiquity",
                "middle_ages", "modern"
            ])
        return super().get_field_value(field_name, field_meta)


class ArtifactEntityFactory(BaseFactory):
    """Factory for ArtifactEntity objects."""
    __model__ = ArtifactEntity

    @classmethod
    def is_supported_type(cls, model: type) -> bool:
        """Override to support frozen dataclasses"""
        return True

    @classmethod
    def get_model_fields(cls) -> list[FieldMeta]:
        """Override to support frozen dataclasses"""
        if not is_dataclass(cls.__model__):
            return []

        model_fields = []
        type_hints = get_type_hints(cls.__model__)

        for field in fields(cls.__model__):
            field_type = type_hints.get(field.name, field.type)
            model_fields.append(
                FieldMeta(
                    name=field.name,
                    annotation=field_type,
                    default=field.default,
                )
            )

        return model_fields

    @classmethod
    def get_field_value(cls, field_name: str, field_meta: FieldMeta | None = None, **kwargs):
        if field_name == "inventory_id":
            return uuid4()
        elif field_name == "created_at":
            return date_time_this_century()
        elif field_name == "acquisition_date":
            return date_time_this_century()
        elif field_name == "name":
            return word()
        elif field_name == "department":
            return word()
        elif field_name == "description":
            return text()
        elif field_name == "era":
            return EraFactory.build()
        elif field_name == "material":
            return MaterialFactory.build()
        return super().get_field_value(field_name, field_meta)


# Helper functions for backward compatibility
def create_material_dto(value=None):
    """Create a MaterialDTO instance."""
    if value:
        return MaterialDTOFactory.build(value=value)
    return MaterialDTOFactory.build()


def create_era_dto(value=None):
    """Create an EraDTO instance."""
    if value:
        return EraDTOFactory.build(value=value)
    return EraDTOFactory.build()


def create_artifact_dto(**kwargs):
    """Create an ArtifactDTO instance with default or provided values."""
    return ArtifactDTOFactory.build(**kwargs)


def create_material(value=None):
    """Create a Material instance."""
    if value:
        return MaterialFactory.build(value=value)
    return MaterialFactory.build()


def create_era(value=None):
    """Create an Era instance."""
    if value:
        return EraFactory.build(value=value)
    return EraFactory.build()


def create_artifact_entity(**kwargs):
    """Create an ArtifactEntity instance with default or provided values."""
    return ArtifactEntityFactory.build(**kwargs)
