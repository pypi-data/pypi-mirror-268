from djangorestframework_camel_case.parser import CamelCaseFormParser, CamelCaseMultiPartParser, CamelCaseJSONParser
from djangorestframework_camel_case.render import CamelCaseJSONRenderer, CamelCaseBrowsableAPIRenderer

from django_microservice_common.api.exception_handlers import errors_exception_handler


class ApiViewV3Mixin:
    renderer_classes = (
        CamelCaseJSONRenderer,
        CamelCaseBrowsableAPIRenderer,
    )
    parser_classes = (
        CamelCaseFormParser,
        CamelCaseMultiPartParser,
        CamelCaseJSONParser,
    )

    def get_exception_handler(self):
        return errors_exception_handler
