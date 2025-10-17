from litestar import Router

from {{cookiecutter.project_slug}}.presentation.api.rest.v1.controllers.artifact_controller import (
    ArtifactController,
)

api_v1_router = Router(
    path="/api",
    route_handlers=[ArtifactController],
)
