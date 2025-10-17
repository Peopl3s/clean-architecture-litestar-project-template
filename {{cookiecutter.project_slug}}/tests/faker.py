from datetime import UTC
from faker import Faker


_faker = Faker()


def get_faker() -> Faker:
    """Get the global Faker instance."""
    return _faker


def uuid4() -> str:
    """Generate a random UUID."""
    return _faker.uuid4()


def word() -> str:
    """Generate a random word."""
    return _faker.word()


def text() -> str:
    """Generate random text."""
    return _faker.text()


def date_time_this_century() -> str:
    """Generate a datetime from this century."""
    return _faker.date_time_this_century(tzinfo=UTC)
