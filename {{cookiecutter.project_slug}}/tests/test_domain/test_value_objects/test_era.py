from {{cookiecutter.project_slug}}.domain.exceptions import InvalidEraException
from {{cookiecutter.project_slug}}.domain.value_objects.era import Era


class TestEra:
    def test_create_era_success(self):
        """Test successful creation of Era with valid values"""
        valid_eras = [
            "paleolithic",
            "neolithic",
            "bronze_age",
            "iron_age",
            "antiquity",
            "middle_ages",
            "modern",
        ]

        for era_value in valid_eras:
            era = Era(value=era_value)
            assert era.value == era_value
