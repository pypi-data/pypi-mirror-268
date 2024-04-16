from django.apps import AppConfig


class DjTenantConfig(AppConfig):
    name = "dj_tenants"
    verbose_name = "Django Tenants"

    def ready(self):
        pass
