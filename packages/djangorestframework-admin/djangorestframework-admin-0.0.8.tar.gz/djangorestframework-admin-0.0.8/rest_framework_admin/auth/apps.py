from django.apps import AppConfig


class RestFrameworkAdminConfig(AppConfig):
    name = 'rest_framework_admin.auth'
    verbose_name = "Django REST framework Admin Auth"
    label = 'admin_auth'

    # def ready(self):
    #     # Add System checks
    #     from .checks import pagination_system_check  # NOQA
