from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

import structlog
from dishka import AsyncContainer, make_async_container
from dishka.integrations.litestar import setup_dishka
from litestar import Litestar
from litestar.config.cors import CORSConfig
from litestar.plugins.pydantic import PydanticPlugin
from litestar.openapi import OpenAPIConfig

from {{cookiecutter.project_slug}}.config.ioc.di import get_providers
from {{cookiecutter.project_slug}}.config.logging import setup_logging
from {{cookiecutter.project_slug}}.presentation.api.rest.error_handling import create_exception_handlers
from {{cookiecutter.project_slug}}.presentation.api.rest.v1.routers import api_v1_router

setup_logging()
logger = structlog.get_logger(__name__)


@asynccontextmanager
async def lifespan(app: Litestar) -> AsyncIterator[None]:
    """
    Asynchronous context manager for managing the lifespan of the Litestar application.

    Args:
        app: The Litestar application instance.

    Yields:
        None
    """
    logger.info("Starting application...")
    yield
    logger.info("Shutting down application...")


def create_app() -> Litestar:
    """
    Creates and configures the Litestar application.

    Returns:
        Litestar: The configured Litestar application instance.
    """
    cors_config = CORSConfig(
        allow_origins=[
            "http://localhost",
            "http://localhost:8080",
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    container: AsyncContainer = make_async_container(*get_providers())

    openapi_config = OpenAPIConfig(
        title="{{ cookiecutter.api_title }}",
        version="{{ cookiecutter.api_version }}",
        description="{{ cookiecutter.api_description }}",
    )

    app = Litestar(
        lifespan=[lifespan],
        route_handlers=[api_v1_router],
        cors_config=cors_config,
        plugins=[PydanticPlugin()],
        exception_handlers=create_exception_handlers(),
        openapi_config=openapi_config,
    )

    setup_dishka(container, app)

    return app


app = create_app()
