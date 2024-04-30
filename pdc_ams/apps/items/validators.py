from django.core.exceptions import ValidationError


def validate_p_value(value):
    if value < 0 or value > 1:
        error_message = "%(value)s is not between 0 and 1"
        params = {"value": value}
        raise ValidationError(error_message, params=params)
