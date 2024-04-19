from ..authorization.exceptions import NotAuthorizedError


def is_allowed(*_, **__):
    return True


def is_not_allowed(*_, **__):
    raise NotAuthorizedError
