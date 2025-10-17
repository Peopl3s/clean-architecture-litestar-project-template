from litestar import Request, Response
from litestar.exceptions import HTTPException
from litestar.status_codes import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR

from {{cookiecutter.project_slug}}.application.exceptions import (
    ArtifactNotFoundError,
    FailedFetchArtifactMuseumAPIException,
    FailedPublishArtifactInCatalogException,
    FailedPublishArtifactMessageBrokerException,
)
from {{cookiecutter.project_slug}}.domain.exceptions import (
    DomainValidationError,
    InvalidEraException,
    InvalidMaterialException,
)


def create_exception_handlers() -> dict[type[Exception], callable]:
    """Create exception handlers for the application."""
    return {
        ArtifactNotFoundError: artifact_not_found_exception_handler,
        FailedFetchArtifactMuseumAPIException: failed_fetch_artifact_museum_api_exception_handler,
        FailedPublishArtifactInCatalogException: failed_publish_artifact_in_catalog_exception_handler,
        FailedPublishArtifactMessageBrokerException: failed_publish_artifact_message_broker_exception_handler,
        DomainValidationError: domain_validation_error_handler,
        InvalidEraException: invalid_era_exception_handler,
        InvalidMaterialException: invalid_material_exception_handler,
    }


def artifact_not_found_exception_handler(
    request: Request,
    exc: ArtifactNotFoundError,
) -> Response:
    return Response(
        content={"message": str(exc)},
        status_code=HTTP_404_NOT_FOUND,
    )


def failed_fetch_artifact_museum_api_exception_handler(
    request: Request,
    exc: FailedFetchArtifactMuseumAPIException,
) -> Response:
    return Response(
        content={"message": str(exc)},
        status_code=HTTP_500_INTERNAL_SERVER_ERROR,
    )


def failed_publish_artifact_in_catalog_exception_handler(
    request: Request,
    exc: FailedPublishArtifactInCatalogException,
) -> Response:
    return Response(
        content={"message": str(exc)},
        status_code=HTTP_500_INTERNAL_SERVER_ERROR,
    )


def failed_publish_artifact_message_broker_exception_handler(
    request: Request,
    exc: FailedPublishArtifactMessageBrokerException,
) -> Response:
    return Response(
        content={"message": str(exc)},
        status_code=HTTP_500_INTERNAL_SERVER_ERROR,
    )


def domain_validation_error_handler(
    request: Request,
    exc: DomainValidationError,
) -> Response:
    return Response(
        content={"message": str(exc)},
        status_code=HTTP_400_BAD_REQUEST,
    )


def invalid_era_exception_handler(
    request: Request,
    exc: InvalidEraException,
) -> Response:
    return Response(
        content={"message": str(exc)},
        status_code=HTTP_400_BAD_REQUEST,
    )


def invalid_material_exception_handler(
    request: Request,
    exc: InvalidMaterialException,
) -> Response:
    return Response(
        content={"message": str(exc)},
        status_code=HTTP_400_BAD_REQUEST,
    )
