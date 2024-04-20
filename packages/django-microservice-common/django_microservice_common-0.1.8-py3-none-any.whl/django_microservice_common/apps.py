from django.apps import AppConfig


class CommonConfig(AppConfig):
    default_auto_field = 'django.db.django_microservice_common.BigAutoField'
    name = "django_microservice_common"
    label = "django_microservice_common"
    verbose_name = "Common"
