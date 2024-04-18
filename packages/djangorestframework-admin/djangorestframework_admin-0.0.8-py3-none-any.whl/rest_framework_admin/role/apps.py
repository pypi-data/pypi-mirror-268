from django.apps import AppConfig


class RestFrameworkAdminConfig(AppConfig):
    name = 'rest_framework_admin.role'
    verbose_name = "Django REST framework Admin Role"
    label = 'admin_role'

    # def ready(self):
    #     # Add System checks
    #     from .checks import pagination_system_check  # NOQA
