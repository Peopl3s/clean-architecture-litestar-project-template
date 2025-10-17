from typing import final

from pydantic import Field
from pydantic_settings import BaseSettings


@final
class BrokerSettings(BaseSettings):
    """
    Message broker configuration settings.

    Attributes:
        broker_url (str): Message broker URL.
        broker_new_artifact_queue (str): Queue name for new artifact messages.
        publish_retries (int): Number of retries for publishing operations.
        publish_retry_backoff (float): Backoff factor for publish retries.
    """

    broker_url: str = Field(
        ..., alias="BROKER_URL"
    )  # e.g. amqp://guest:guest@localhost:5672/
    broker_new_artifact_queue: str = Field(
        "new_artifacts", alias="BROKER_NEW_ARTIFACT_QUEUE"
    )

    publish_retries: int = Field(3, alias="PUBLISH_RETRIES")
    publish_retry_backoff: float = Field(0.5, alias="PUBLISH_RETRY_BACKOFF")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"
