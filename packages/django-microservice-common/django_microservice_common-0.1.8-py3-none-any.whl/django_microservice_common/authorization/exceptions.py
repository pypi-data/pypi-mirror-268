from rest_framework import status
from rest_framework.exceptions import APIException


class CustomApiException(APIException):
    ...


class NotAuthorizedError(CustomApiException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "You are unauthorized"
