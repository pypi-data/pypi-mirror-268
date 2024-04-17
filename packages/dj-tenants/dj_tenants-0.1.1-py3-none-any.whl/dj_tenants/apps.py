from django.apps import AppConfig


class DjTenantConfig(AppConfig):
    name = "dj_tenants"
    verbose_name = "Django Tenants"

    def ready(self):
        pass
        # from django.contrib.auth import views
        #
        # login_not_required_views = (
        #     views.LoginView,
        # )
        # for view in login_not_required_views:
        #     view.tenant_required = False
