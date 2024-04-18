from django.apps import AppConfig


class TenantConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = 'rest_framework_admin.tenant'
    verbose_name = "Django REST framework Admin Tenant"
    label = 'admin_tenant'
