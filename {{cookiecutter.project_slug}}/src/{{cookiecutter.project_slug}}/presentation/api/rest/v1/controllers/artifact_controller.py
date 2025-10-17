from uuid import UUID

from dishka.integrations.litestar import FromDishka, inject
from litestar import Controller, get
from litestar.params import Parameter

from {{cookiecutter.project_slug}}.application.use_cases.process_artifact import ProcessArtifactUseCase
from {{cookiecutter.project_slug}}.presentation.api.rest.v1.mappers.artifact_mapper import ArtifactPresentationMapper
from {{cookiecutter.project_slug}}.presentation.api.rest.v1.schemas.responses import ArtifactResponseSchema


class ArtifactController(Controller):
    """Controller for handling artifact-related requests."""

    path = "/v1/artifacts"
    tags = ["Artifacts"]

    @get(
        "/{inventory_id:str}",
        summary="Get artifact by inventory ID",
    )
    @inject
    async def get_artifact(
        self,
        inventory_id: UUID = Parameter(
            title="inventory_id",
            description="Artifact UUID",
        ),
        use_case: FromDishka[ProcessArtifactUseCase] = None,
        presentation_mapper: FromDishka[ArtifactPresentationMapper] = None,
    ) -> ArtifactResponseSchema:
        """Get artifact by inventory ID."""
        artifact_dto = await use_case(str(inventory_id))
        return presentation_mapper.to_response(artifact_dto)
