from unittest.mock import AsyncMock

import pytest

from {{cookiecutter.project_slug}}.application.dtos.artifact import (
    ArtifactAdmissionNotificationDTO,
    ArtifactCatalogPublicationDTO,
    ArtifactDTO,
)
from {{cookiecutter.project_slug}}.application.exceptions import (
    ArtifactNotFoundError,
    FailedFetchArtifactMuseumAPIException,
    FailedPublishArtifactInCatalogException,
    FailedPublishArtifactMessageBrokerException,
)
from {{cookiecutter.project_slug}}.application.use_cases.process_artifact import ProcessArtifactUseCase
from {{cookiecutter.project_slug}}.domain.entities.artifact import ArtifactEntity


class TestProcessArtifactUseCase:
    @pytest.fixture
    def mock_get_artifact_from_cache_use_case(self) -> AsyncMock:
        return AsyncMock()

    @pytest.fixture
    def mock_get_artifact_from_repo_use_case(self) -> AsyncMock:
        return AsyncMock()

    @pytest.fixture
    def mock_fetch_artifact_from_museum_api_use_case(self) -> AsyncMock:
        return AsyncMock()

    @pytest.fixture
    def mock_save_artifact_to_repo_use_case(self) -> AsyncMock:
        return AsyncMock()

    @pytest.fixture
    def mock_save_artifact_to_cache_use_case(self) -> AsyncMock:
        return AsyncMock()

    @pytest.fixture
    def mock_publish_artifact_to_broker_use_case(self) -> AsyncMock:
        return AsyncMock()

    @pytest.fixture
    def mock_publish_artifact_to_catalog_use_case(self) -> AsyncMock:
        return AsyncMock()

    @pytest.fixture
    def get_artifact_use_case(
        self,
        mock_get_artifact_from_cache_use_case: AsyncMock,
        mock_get_artifact_from_repo_use_case: AsyncMock,
        mock_fetch_artifact_from_museum_api_use_case: AsyncMock,
        mock_save_artifact_to_repo_use_case: AsyncMock,
        mock_save_artifact_to_cache_use_case: AsyncMock,
        mock_publish_artifact_to_broker_use_case: AsyncMock,
        mock_publish_artifact_to_catalog_use_case: AsyncMock,
    ) -> ProcessArtifactUseCase:
        return ProcessArtifactUseCase(
            get_artifact_from_cache_use_case=mock_get_artifact_from_cache_use_case,
            get_artifact_from_repo_use_case=mock_get_artifact_from_repo_use_case,
            fetch_artifact_from_museum_api_use_case=mock_fetch_artifact_from_museum_api_use_case,
            save_artifact_to_repo_use_case=mock_save_artifact_to_repo_use_case,
            save_artifact_to_cache_use_case=mock_save_artifact_to_cache_use_case,
            publish_artifact_to_broker_use_case=mock_publish_artifact_to_broker_use_case,
            publish_artifact_to_catalog_use_case=mock_publish_artifact_to_catalog_use_case,
        )

    @pytest.mark.asyncio
    async def test_execute_artifact_found_in_cache(
        self,
        get_artifact_use_case: ProcessArtifactUseCase,
        mock_get_artifact_from_cache_use_case: AsyncMock,
        sample_artifact_dto: ArtifactDTO,
    ):
        """Test successful execution when artifact is found in cache"""
        inventory_id = str(sample_artifact_dto.inventory_id)
        mock_get_artifact_from_cache_use_case.return_value = sample_artifact_dto

        result = await get_artifact_use_case(inventory_id)

        assert result == sample_artifact_dto
        mock_get_artifact_from_cache_use_case.assert_called_once_with(inventory_id)
        get_artifact_use_case.get_artifact_from_repo_use_case.assert_not_called()
        get_artifact_use_case.fetch_artifact_from_museum_api_use_case.assert_not_called()

    @pytest.mark.asyncio
    async def test_execute_artifact_found_in_repository(
        self,
        get_artifact_use_case: ProcessArtifactUseCase,
        mock_get_artifact_from_cache_use_case: AsyncMock,
        mock_get_artifact_from_repo_use_case: AsyncMock,
        mock_save_artifact_to_cache_use_case: AsyncMock,
        sample_artifact_dto: ArtifactDTO,
    ):
        """Test successful execution when artifact is found in local repository"""
        inventory_id = str(sample_artifact_dto.inventory_id)
        mock_get_artifact_from_cache_use_case.return_value = None
        mock_get_artifact_from_repo_use_case.return_value = sample_artifact_dto

        result = await get_artifact_use_case(inventory_id)

        assert result == sample_artifact_dto
        mock_get_artifact_from_cache_use_case.assert_called_once_with(inventory_id)
        mock_get_artifact_from_repo_use_case.assert_called_once_with(inventory_id)
        mock_save_artifact_to_cache_use_case.assert_called_once_with(
            inventory_id, sample_artifact_dto
        )
        get_artifact_use_case.fetch_artifact_from_museum_api_use_case.assert_not_called()
        get_artifact_use_case.save_artifact_to_repo_use_case.assert_not_called()
        get_artifact_use_case.publish_artifact_to_broker_use_case.assert_not_called()
        get_artifact_use_case.publish_artifact_to_catalog_use_case.assert_not_called()

    @pytest.mark.asyncio
    async def test_execute_artifact_fetched_from_external_api(
        self,
        get_artifact_use_case: ProcessArtifactUseCase,
        mock_get_artifact_from_cache_use_case: AsyncMock,
        mock_get_artifact_from_repo_use_case: AsyncMock,
        mock_fetch_artifact_from_museum_api_use_case: AsyncMock,
        mock_save_artifact_to_repo_use_case: AsyncMock,
        mock_save_artifact_to_cache_use_case: AsyncMock,
        mock_publish_artifact_to_broker_use_case: AsyncMock,
        mock_publish_artifact_to_catalog_use_case: AsyncMock,
        sample_artifact_dto: ArtifactDTO,
    ):
        """Test successful execution when artifact is fetched from external API"""
        inventory_id = str(sample_artifact_dto.inventory_id)
        mock_get_artifact_from_cache_use_case.return_value = None
        mock_get_artifact_from_repo_use_case.return_value = None
        mock_fetch_artifact_from_museum_api_use_case.return_value = sample_artifact_dto

        result = await get_artifact_use_case(inventory_id)

        assert result == sample_artifact_dto
        mock_get_artifact_from_cache_use_case.assert_called_once_with(inventory_id)
        mock_get_artifact_from_repo_use_case.assert_called_once_with(inventory_id)
        mock_fetch_artifact_from_museum_api_use_case.assert_called_once_with(inventory_id)
        mock_save_artifact_to_repo_use_case.assert_called_once_with(sample_artifact_dto)
        mock_save_artifact_to_cache_use_case.assert_called_once_with(
            inventory_id, sample_artifact_dto
        )
        mock_publish_artifact_to_broker_use_case.assert_called_once_with(sample_artifact_dto)
        mock_publish_artifact_to_catalog_use_case.assert_called_once_with(sample_artifact_dto)

    @pytest.mark.asyncio
    async def test_execute_artifact_not_found_in_museum_api(
        self,
        get_artifact_use_case: ProcessArtifactUseCase,
        mock_get_artifact_from_cache_use_case: AsyncMock,
        mock_get_artifact_from_repo_use_case: AsyncMock,
        mock_fetch_artifact_from_museum_api_use_case: AsyncMock,
        sample_artifact_dto: ArtifactDTO,
    ):
        """Test execution when artifact is not found in external museum API"""
        inventory_id = str(sample_artifact_dto.inventory_id)
        mock_get_artifact_from_cache_use_case.return_value = None
        mock_get_artifact_from_repo_use_case.return_value = None
        mock_fetch_artifact_from_museum_api_use_case.side_effect = ArtifactNotFoundError

        with pytest.raises(ArtifactNotFoundError):
            await get_artifact_use_case(inventory_id)

        mock_get_artifact_from_cache_use_case.assert_called_once_with(inventory_id)
        mock_get_artifact_from_repo_use_case.assert_called_once_with(inventory_id)
        mock_fetch_artifact_from_museum_api_use_case.assert_called_once_with(inventory_id)
        get_artifact_use_case.save_artifact_to_repo_use_case.assert_not_called()
        get_artifact_use_case.save_artifact_to_cache_use_case.assert_not_called()
        get_artifact_use_case.publish_artifact_to_broker_use_case.assert_not_called()
        get_artifact_use_case.publish_artifact_to_catalog_use_case.assert_not_called()

    @pytest.mark.asyncio
    async def test_execute_publish_to_broker_fails_but_continues(
        self,
        get_artifact_use_case: ProcessArtifactUseCase,
        mock_get_artifact_from_cache_use_case: AsyncMock,
        mock_get_artifact_from_repo_use_case: AsyncMock,
        mock_fetch_artifact_from_museum_api_use_case: AsyncMock,
        mock_save_artifact_to_repo_use_case: AsyncMock,
        mock_save_artifact_to_cache_use_case: AsyncMock,
        mock_publish_artifact_to_broker_use_case: AsyncMock,
        mock_publish_artifact_to_catalog_use_case: AsyncMock,
        sample_artifact_dto: ArtifactDTO,
    ):
        """Test execution when publishing to broker fails but execution continues"""
        inventory_id = str(sample_artifact_dto.inventory_id)
        mock_get_artifact_from_cache_use_case.return_value = None
        mock_get_artifact_from_repo_use_case.return_value = None
        mock_fetch_artifact_from_museum_api_use_case.return_value = sample_artifact_dto
        mock_publish_artifact_to_broker_use_case.side_effect = FailedPublishArtifactMessageBrokerException

        result = await get_artifact_use_case(inventory_id)

        assert result == sample_artifact_dto
        mock_publish_artifact_to_broker_use_case.assert_called_once_with(sample_artifact_dto)
        mock_publish_artifact_to_catalog_use_case.assert_called_once_with(sample_artifact_dto)

    @pytest.mark.asyncio
    async def test_execute_publish_to_catalog_fails_but_continues(
        self,
        get_artifact_use_case: ProcessArtifactUseCase,
        mock_get_artifact_from_cache_use_case: AsyncMock,
        mock_get_artifact_from_repo_use_case: AsyncMock,
        mock_fetch_artifact_from_museum_api_use_case: AsyncMock,
        mock_save_artifact_to_repo_use_case: AsyncMock,
        mock_save_artifact_to_cache_use_case: AsyncMock,
        mock_publish_artifact_to_broker_use_case: AsyncMock,
        mock_publish_artifact_to_catalog_use_case: AsyncMock,
        sample_artifact_dto: ArtifactDTO,
    ):
        """Test execution when publishing to catalog fails but execution continues"""
        inventory_id = str(sample_artifact_dto.inventory_id)
        mock_get_artifact_from_cache_use_case.return_value = None
        mock_get_artifact_from_repo_use_case.return_value = None
        mock_fetch_artifact_from_museum_api_use_case.return_value = sample_artifact_dto
        mock_publish_artifact_to_catalog_use_case.side_effect = FailedPublishArtifactInCatalogException

        result = await get_artifact_use_case(inventory_id)

        assert result == sample_artifact_dto
        mock_publish_artifact_to_broker_use_case.assert_called_once_with(sample_artifact_dto)
        mock_publish_artifact_to_catalog_use_case.assert_called_once_with(sample_artifact_dto)
