from django.apps import AppConfig


class SystemConfig(AppConfig):
    name = 'rest_framework_admin.system'
    verbose_name = "Django REST framework Admin System"

    # def ready(self):
    #     # Add System checks
    #     from .checks import pagination_system_check  # NOQA
