from unittest.mock import AsyncMock
from uuid import uuid4

from litestar import status
import pytest

from {{cookiecutter.project_slug}}.application.dtos.artifact import ArtifactDTO, EraDTO, MaterialDTO
from {{cookiecutter.project_slug}}.application.exceptions import (
    ArtifactNotFoundError,
    FailedFetchArtifactMuseumAPIException,
    FailedPublishArtifactInCatalogException,
    FailedPublishArtifactMessageBrokerException,
)
from {{cookiecutter.project_slug}}.application.use_cases.process_artifact import ProcessArtifactUseCase


class TestArtifactController:
    async def _call_controller_with_mock(
        self, inventory_id: str, mock_use_case: ProcessArtifactUseCase
    ):
        """Helper method to call the controller function with a mock use case"""
        try:
            return await mock_use_case(inventory_id)
        except ArtifactNotFoundError as err:
            raise err
        except FailedFetchArtifactMuseumAPIException as err:
            raise err
        except FailedPublishArtifactInCatalogException as err:
            raise err
        except FailedPublishArtifactMessageBrokerException as err:
            raise err

    @pytest.mark.asyncio
    async def test_get_artifact_success(self):
        """Test successful artifact retrieval"""
        inventory_id = str(uuid4())
        expected_dto = ArtifactDTO(
            inventory_id=uuid4(),
            created_at="2023-01-01T00:00:00Z",
            acquisition_date="2023-01-01T00:00:00Z",
            name="Ancient Vase",
            department="Archaeology",
            era=EraDTO(value="antiquity"),
            material=MaterialDTO(value="ceramic"),
            description="A beautiful ancient vase",
        )

        mock_use_case = AsyncMock()
        mock_use_case.return_value = expected_dto

        result = await self._call_controller_with_mock(inventory_id, mock_use_case)

        assert result == expected_dto
        mock_use_case.assert_called_once_with(inventory_id)
