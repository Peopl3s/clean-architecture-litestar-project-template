from dishka import Provider

from {{cookiecutter.project_slug}}.config.ioc.providers import (
    BrokerProvider,
    CacheProvider,
    DatabaseProvider,
    HTTPClientProvider,
    MapperProvider,
    RepositoryProvider,
    ServiceProvider,
    SettingsProvider,
    UseCaseProvider,
    UnitOfWorkProvider,
)


def get_providers() -> list[Provider]:
    """
    Returns a list of Dishka providers for dependency injection.

    Returns:
        list[Provider]: A list of configured providers.
    """
    return [
        SettingsProvider(),
        DatabaseProvider(),
        HTTPClientProvider(),
        BrokerProvider(),
        RepositoryProvider(),
        ServiceProvider(),
        MapperProvider(),
        CacheProvider(),
        UseCaseProvider(),
        UnitOfWorkProvider(),
    ]
