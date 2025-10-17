from collections.abc import AsyncIterator

from dishka import Provider, Scope, provide
from faststream.kafka import KafkaBroker
from httpx import AsyncClient
import redis.asyncio as redis
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
)

from {{cookiecutter.project_slug}}.application.interfaces.cache import CacheProtocol
from {{cookiecutter.project_slug}}.application.interfaces.http_clients import (
    ExternalMuseumAPIProtocol,
    PublicCatalogAPIProtocol,
)
from {{cookiecutter.project_slug}}.application.interfaces.mappers import DtoEntityMapperProtocol
from {{cookiecutter.project_slug}}.application.interfaces.message_broker import MessageBrokerPublisherProtocol
from {{cookiecutter.project_slug}}.application.interfaces.repositories import ArtifactRepositoryProtocol
from {{cookiecutter.project_slug}}.application.interfaces.serialization import SerializationMapperProtocol
from {{cookiecutter.project_slug}}.application.interfaces.uow import UnitOfWorkProtocol
from {{cookiecutter.project_slug}}.application.mappers import ArtifactMapper
from {{cookiecutter.project_slug}}.application.use_cases.fetch_artifact_from_museum_api import (
    FetchArtifactFromMuseumAPIUseCase,
)
from {{cookiecutter.project_slug}}.application.use_cases.process_artifact import ProcessArtifactUseCase
from {{cookiecutter.project_slug}}.application.use_cases.get_artifact_from_cache import (
    GetArtifactFromCacheUseCase,
)
from {{cookiecutter.project_slug}}.application.use_cases.get_artifact_from_repo import (
    GetArtifactFromRepoUseCase,
)
from {{cookiecutter.project_slug}}.application.use_cases.publish_artifact_to_broker import (
    PublishArtifactToBrokerUseCase,
)
from {{cookiecutter.project_slug}}.application.use_cases.publish_artifact_to_catalog import (
    PublishArtifactToCatalogUseCase,
)
from {{cookiecutter.project_slug}}.application.use_cases.save_artifact_to_cache import (
    SaveArtifactToCacheUseCase,
)
from {{cookiecutter.project_slug}}.application.use_cases.save_artifact_to_repo import (
    SaveArtifactToRepoUseCase,
)
from {{cookiecutter.project_slug}}.config.base import Settings
from {{cookiecutter.project_slug}}.infrastructures.broker.publisher import KafkaPublisher
from {{cookiecutter.project_slug}}.infrastructures.cache.redis_client import RedisCacheClient
from {{cookiecutter.project_slug}}.infrastructures.db.mappers.artifact_db_mapper import ArtifactDBMapper
from {{cookiecutter.project_slug}}.infrastructures.db.repositories.artifact import ArtifactRepositorySQLAlchemy
from {{cookiecutter.project_slug}}.infrastructures.db.session import create_engine, get_session_factory
from {{cookiecutter.project_slug}}.infrastructures.db.uow import UnitOfWorkSQLAlchemy
from {{cookiecutter.project_slug}}.infrastructures.http.clients import (
    ExternalMuseumAPIClient,
    PublicCatalogAPIClient,
)
from {{cookiecutter.project_slug}}.infrastructures.mappers.artifact import InfrastructureArtifactMapper
from {{cookiecutter.project_slug}}.presentation.api.rest.v1.mappers.artifact_mapper import ArtifactPresentationMapper


class SettingsProvider(Provider):
    """
    Provides application settings.
    """

    @provide(scope=Scope.APP)
    def get_settings(self) -> Settings:
        """
        Provides the Settings instance.
        """
        return Settings()


class DatabaseProvider(Provider):
    """
    Provides database-related dependencies, such as session factory and sessions.
    """

    @provide(scope=Scope.APP)
    async def get_session_factory(
        self, settings: Settings
    ) -> AsyncIterator[async_sessionmaker[AsyncSession]]:
        """
        Provides an asynchronous session factory for SQLAlchemy.
        """
        engine = create_engine(str(settings.database_url), is_echo=settings.debug)
        session_factory = get_session_factory(engine)
        try:
            yield session_factory
        finally:
            await engine.dispose()

    @provide(scope=Scope.REQUEST)
    async def get_session(
        self, factory: async_sessionmaker[AsyncSession]
    ) -> AsyncIterator[AsyncSession]:
        """
        Provides an asynchronous SQLAlchemy session.
        """
        async with factory() as session:
            yield session


class HTTPClientProvider(Provider):
    """
    Provides an asynchronous HTTP client.
    """

    @provide(scope=Scope.APP)
    async def get_http_client(self, settings: Settings) -> AsyncIterator[AsyncClient]:
        """
        Provides an AsyncClient instance with configured timeout.
        """
        client = AsyncClient(timeout=settings.http_timeout)
        try:
            yield client
        finally:
            await client.aclose()


class BrokerProvider(Provider):
    """
    Provides a Kafka message broker instance.
    """

    @provide(scope=Scope.APP)
    async def get_broker(self, settings: Settings) -> AsyncIterator[KafkaBroker]:
        """
        Provides a KafkaBroker instance.
        """
        broker = KafkaBroker(settings.broker_url)
        try:
            yield broker
        finally:
            await broker.stop()


class RepositoryProvider(Provider):
    """
    Provides repository implementations.
    """

    @provide(scope=Scope.REQUEST)
    def get_artifact_repository(
        self, session: AsyncSession, db_mapper: ArtifactDBMapper
    ) -> ArtifactRepositoryProtocol:
        """
        Provides an ArtifactRepositoryProtocol implementation.
        """
        return ArtifactRepositorySQLAlchemy(session=session, mapper=db_mapper)


class UnitOfWorkProvider(Provider):
    """
    Provides Unit of Work implementations.
    """

    @provide(scope=Scope.REQUEST)
    def get_unit_of_work(
        self,
        session: AsyncSession,
        repository: ArtifactRepositoryProtocol,
    ) -> UnitOfWorkProtocol:
        """
        Provides a UnitOfWorkProtocol implementation.
        """
        return UnitOfWorkSQLAlchemy(session=session, repository=repository)


class ServiceProvider(Provider):
    """
    Provides service clients for external integrations.
    """

    @provide(scope=Scope.REQUEST)
    def get_external_museum_api_client(
        self,
        client: AsyncClient,
        settings: Settings,
        infrastructure_mapper: SerializationMapperProtocol,
    ) -> ExternalMuseumAPIProtocol:
        """
        Provides an ExternalMuseumAPIProtocol implementation.
        """
        return ExternalMuseumAPIClient(
            base_url=settings.museum_api_base,
            client=client,
            mapper=infrastructure_mapper,
        )

    @provide(scope=Scope.REQUEST)
    def get_public_catalog_api_client(
        self,
        client: AsyncClient,
        settings: Settings,
        infrastructure_mapper: SerializationMapperProtocol,
    ) -> PublicCatalogAPIProtocol:
        """
        Provides a PublicCatalogAPIProtocol implementation.
        """
        return PublicCatalogAPIClient(
            base_url=settings.catalog_api_base_url,
            client=client,
            mapper=infrastructure_mapper,
        )

    @provide(scope=Scope.REQUEST)
    def get_message_broker(
        self,
        broker: KafkaBroker,
        infrastructure_mapper: SerializationMapperProtocol,
    ) -> MessageBrokerPublisherProtocol:
        """
        Provides a MessageBrokerPublisherProtocol implementation.
        """
        return KafkaPublisher(
            broker=broker,
            mapper=infrastructure_mapper,
        )


class MapperProvider(Provider):
    """
    Provides various mapper implementations for different layers.
    """

    @provide(scope=Scope.APP)
    def get_artifact_mapper(self) -> DtoEntityMapperProtocol:
        """
        Provides the Application layer mapper (Domain Entity <-> Application DTO).
        """
        return ArtifactMapper()

    @provide(scope=Scope.REQUEST)
    def get_db_mapper(self) -> ArtifactDBMapper:
        """
        Provides the Database mapper (Domain Entity <-> SQLAlchemy Model).
        """
        return ArtifactDBMapper()

    @provide(scope=Scope.REQUEST)
    def get_infrastructure_artifact_mapper(self) -> SerializationMapperProtocol:
        """
        Provides the Infrastructure mapper (Application DTO <-> Pydantic/JSON).
        """
        return InfrastructureArtifactMapper()

    @provide(scope=Scope.REQUEST)
    def get_presentation_artifact_mapper(self) -> ArtifactPresentationMapper:
        """
        Provides the Presentation mapper (Application DTO -> Response Schema).
        """
        return ArtifactPresentationMapper()


class CacheProvider(Provider):
    """
    Provides caching services using Redis.
    """

    @provide(scope=Scope.APP)
    async def get_cache_service(
        self, settings: Settings
    ) -> AsyncIterator[CacheProtocol]:
        """
        Provides a CacheProtocol implementation.
        """
        redis_client = await redis.from_url(
            str(settings.redis_url),
            encoding="utf-8",
            decode_responses=True,
            health_check_interval=30,
            max_connections=10,
            retry_on_timeout=True,
            socket_connect_timeout=5,
            socket_timeout=5,
        )
        cache_service = RedisCacheClient(
            client=redis_client, ttl=settings.redis_cache_ttl
        )
        try:
            yield cache_service
        finally:
            await cache_service.close()


class UseCaseProvider(Provider):
    """
    Provides application use cases.
    """

    @provide(scope=Scope.REQUEST)
    def get_get_artifact_from_cache_use_case(
        self,
        cache_client: CacheProtocol,
        serialization_mapper: SerializationMapperProtocol,
    ) -> GetArtifactFromCacheUseCase:
        """
        Provides a GetArtifactFromCacheUseCase instance.
        """
        return GetArtifactFromCacheUseCase(
            cache_client=cache_client, serialization_mapper=serialization_mapper
        )

    @provide(scope=Scope.REQUEST)
    def get_get_artifact_from_repo_use_case(
        self, uow: UnitOfWorkProtocol, artifact_mapper: DtoEntityMapperProtocol
    ) -> GetArtifactFromRepoUseCase:
        """
        Provides a GetArtifactFromRepoUseCase instance.
        """
        return GetArtifactFromRepoUseCase(uow=uow, artifact_mapper=artifact_mapper)

    @provide(scope=Scope.REQUEST)
    def get_fetch_artifact_from_museum_api_use_case(
        self,
        museum_api_client: ExternalMuseumAPIProtocol,
    ) -> FetchArtifactFromMuseumAPIUseCase:
        """
        Provides a FetchArtifactFromMuseumAPIUseCase instance.
        """
        return FetchArtifactFromMuseumAPIUseCase(museum_api_client=museum_api_client)

    @provide(scope=Scope.REQUEST)
    def get_save_artifact_to_repo_use_case(
        self, uow: UnitOfWorkProtocol, artifact_mapper: DtoEntityMapperProtocol
    ) -> SaveArtifactToRepoUseCase:
        """
        Provides a SaveArtifactToRepoUseCase instance.
        """
        return SaveArtifactToRepoUseCase(uow=uow, artifact_mapper=artifact_mapper)

    @provide(scope=Scope.REQUEST)
    def get_save_artifact_to_cache_use_case(
        self,
        cache_client: CacheProtocol,
        serialization_mapper: SerializationMapperProtocol,
    ) -> SaveArtifactToCacheUseCase:
        """
        Provides a SaveArtifactToCacheUseCase instance.
        """
        return SaveArtifactToCacheUseCase(
            cache_client=cache_client, serialization_mapper=serialization_mapper
        )

    @provide(scope=Scope.REQUEST)
    def get_publish_artifact_to_broker_use_case(
        self,
        message_broker: MessageBrokerPublisherProtocol,
        artifact_mapper: DtoEntityMapperProtocol,
    ) -> PublishArtifactToBrokerUseCase:
        """
        Provides a PublishArtifactToBrokerUseCase instance.
        """
        return PublishArtifactToBrokerUseCase(
            message_broker=message_broker, artifact_mapper=artifact_mapper
        )

    @provide(scope=Scope.REQUEST)
    def get_publish_artifact_to_catalog_use_case(
        self,
        catalog_api_client: PublicCatalogAPIProtocol,
        artifact_mapper: DtoEntityMapperProtocol,
    ) -> PublishArtifactToCatalogUseCase:
        """
        Provides a PublishArtifactToCatalogUseCase instance.
        """
        return PublishArtifactToCatalogUseCase(
            catalog_api_client=catalog_api_client, artifact_mapper=artifact_mapper
        )

    @provide(scope=Scope.REQUEST)
    def get_register_artifact_use_case(
        self,
        get_artifact_from_cache_use_case: GetArtifactFromCacheUseCase,
        get_artifact_from_repo_use_case: GetArtifactFromRepoUseCase,
        fetch_artifact_from_museum_api_use_case: FetchArtifactFromMuseumAPIUseCase,
        save_artifact_to_repo_use_case: SaveArtifactToRepoUseCase,
        save_artifact_to_cache_use_case: SaveArtifactToCacheUseCase,
        publish_artifact_to_broker_use_case: PublishArtifactToBrokerUseCase,
        publish_artifact_to_catalog_use_case: PublishArtifactToCatalogUseCase,
    ) -> ProcessArtifactUseCase:
        """
        Provides a ProcessArtifactUseCase instance.
        """
        return ProcessArtifactUseCase(
            get_artifact_from_cache_use_case=get_artifact_from_cache_use_case,
            get_artifact_from_repo_use_case=get_artifact_from_repo_use_case,
            fetch_artifact_from_museum_api_use_case=fetch_artifact_from_museum_api_use_case,
            save_artifact_to_repo_use_case=save_artifact_to_repo_use_case,
            save_artifact_to_cache_use_case=save_artifact_to_cache_use_case,
            publish_artifact_to_broker_use_case=publish_artifact_to_broker_use_case,
            publish_artifact_to_catalog_use_case=publish_artifact_to_catalog_use_case,
        )
