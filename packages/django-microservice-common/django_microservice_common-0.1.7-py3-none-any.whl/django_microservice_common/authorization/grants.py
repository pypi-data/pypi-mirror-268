from enum import auto

from ..authorization.enums import StrEnum
from ..authorization.grants_func import is_allowed, is_not_allowed


class PermissionGrants(StrEnum):
    IS_ALLOWED = auto()
    NOT_ALLOWED = auto()


GRANT_MAPPER = {
    PermissionGrants.IS_ALLOWED: is_allowed,
    PermissionGrants.NOT_ALLOWED: is_not_allowed,
}
