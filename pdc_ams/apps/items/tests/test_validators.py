import pytest
from django.core.exceptions import ValidationError

from pdc_ams.apps.items.validators import validate_p_value


class TestPValueValidator:
    def test_valid_p_value(self):
        # Test that valid p values pass
        for p in [0, 0.5, 1]:
            try:
                validate_p_value(p)
            except ValidationError:
                pytest.fail(f"{p} failed validation when it should have passed")

    def test_invalid_p_value(self):
        # Test that invalid p values fail
        for p in [-1, 1.5, 2]:
            with pytest.raises(ValidationError):
                validate_p_value(p)
