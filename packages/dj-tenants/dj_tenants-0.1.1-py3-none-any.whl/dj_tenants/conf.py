from appconf import AppConf
from django.conf import settings  # NOQA

__all__ = ("settings", "DjTenantsAppConf")


class DjTenantsAppConf(AppConf):
    TENANT_FIELD = "tenant"
    TENANT_MODEL = ""
    LOGIN_VIEW_NAME = "login"

    class Meta:
        prefix = "DJ_TENANTS"
