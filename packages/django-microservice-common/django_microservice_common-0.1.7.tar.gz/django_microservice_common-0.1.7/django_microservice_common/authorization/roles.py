from enum import auto
from django.db import models

from ..authorization.enums import StrEnum


class UserRoles(StrEnum, models.TextChoices):
    ADMIN = auto()
    CUSTOMER = auto()
