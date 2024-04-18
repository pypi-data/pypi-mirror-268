from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'rest_framework_admin.user'
    verbose_name = "Django REST framework Admin User"
    label = 'admin_user'

    def ready(self):
        # Add System checks
        # from .checks import pagination_system_check  # NOQA
        pass
