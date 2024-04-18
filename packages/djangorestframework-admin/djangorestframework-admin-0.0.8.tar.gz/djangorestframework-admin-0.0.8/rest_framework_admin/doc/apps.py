from django.apps import AppConfig


class DocConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rest_framework_admin.doc'
    verbose_name = "Django REST framework Admin Doc"
    label = 'admin_doc'
