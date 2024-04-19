from django.core.exceptions import ValidationError

from .roles import UserRoles


def validate_user_roles(value):
    if value not in UserRoles.values:
        raise ValidationError("Invalid roles!!")
