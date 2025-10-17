from {{cookiecutter.project_slug}}.config.app import AppSettings
from {{cookiecutter.project_slug}}.config.base import Settings
from {{cookiecutter.project_slug}}.config.broker import BrokerSettings
from {{cookiecutter.project_slug}}.config.cors import CORSSettings
from {{cookiecutter.project_slug}}.config.database import DatabaseSettings
from {{cookiecutter.project_slug}}.config.external_apis import ExternalAPISettings
from {{cookiecutter.project_slug}}.config.redis import RedisSettings
from {{cookiecutter.project_slug}}.config.settings import Settings as NewSettings

__all__ = [
    "AppSettings",
    "Settings",  # Backward compatibility
    "NewSettings",  # New modular settings
    "DatabaseSettings",
    "RedisSettings",
    "ExternalAPISettings",
    "BrokerSettings",
    "CORSSettings",
]
