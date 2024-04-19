import uuid

from django.conf import settings

from ..authorization.grants import PermissionGrants, GRANT_MAPPER
from ..authorization.roles import UserRoles


def get_permission_setting(acl_mapper: dict[settings.RoutesEnum, dict[UserRoles, PermissionGrants]]):
    for router in acl_mapper:
        acl_mapper[router][UserRoles.ADMIN] = PermissionGrants.IS_ALLOWED
    return acl_mapper


def check_permission(
        user_rule: UserRoles,
        user_id: uuid.uuid4,
        route: settings.RoutesEnum,
        permission_setting: dict[settings.RoutesEnum, dict[UserRoles, PermissionGrants]],
        **kwargs,
):
    permission_for_endpoint = permission_setting.get(route)
    assert permission_for_endpoint is not None
    _permission_grant = permission_for_endpoint.get(user_rule)
    permission_grant = _permission_grant or PermissionGrants.NOT_ALLOWED
    permission_func = GRANT_MAPPER.get(permission_grant)
    assert permission_func is not None
    permission_func(user_id, **kwargs)


def get_permission_callable():
    return check_permission
