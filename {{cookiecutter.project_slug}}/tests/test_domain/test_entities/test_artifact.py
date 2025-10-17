from datetime import UTC, datetime
from uuid import uuid4

from {{cookiecutter.project_slug}}.domain.entities.artifact import ArtifactEntity
from {{cookiecutter.project_slug}}.domain.value_objects.era import Era
from {{cookiecutter.project_slug}}.domain.value_objects.material import Material


class TestArtifactEntity:
    def test_create_artifact_entity_success(self):
        """Test successful creation of ArtifactEntity"""
        inventory_id = uuid4()
        acquisition_date = datetime(2023, 1, 1, tzinfo=UTC)

        artifact = ArtifactEntity(
            inventory_id=inventory_id,
            acquisition_date=acquisition_date,
            name="Ancient Vase",
            department="Archaeology",
            era=Era(value="antiquity"),
            material=Material(value="ceramic"),
            description="A beautiful ancient vase",
        )

        assert artifact.inventory_id == inventory_id
        assert artifact.acquisition_date == acquisition_date
        assert artifact.name == "Ancient Vase"
        assert artifact.department == "Archaeology"
        assert artifact.era.value == "antiquity"
        assert artifact.material.value == "ceramic"
        assert artifact.description == "A beautiful ancient vase"
        assert isinstance(artifact.created_at, datetime)
