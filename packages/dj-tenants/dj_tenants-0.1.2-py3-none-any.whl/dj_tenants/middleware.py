from django.shortcuts import redirect
from django.urls import reverse, resolve

from dj_tenants.conf import settings

from dj_tenants import get_tenant_model, tenant_context, tenant_context_disabled

allowed_paths = settings.DJ_TENANTS_URLS_ALLOW_WITHOUT_TENANT

login_url = settings.DJ_TENANTS_LOGIN_VIEW_NAME


class DjTenantsMiddleware:
    TenantModel = None

    def __init__(self, get_response):
        self.get_response = get_response
        self.TenantModel = get_tenant_model()

    def __call__(self, request):
        if not request.user.is_authenticated:
            return self.get_response(request)

        if request.path.startswith("/admin/"):
            with tenant_context_disabled():
                return self.get_response(request)

        ignored_path = any(
            resolve(request.path).view_name == ignored for ignored in allowed_paths
        )
        if ignored_path:
            return self.get_response(request)

        tenant = self._get_tenant(request)

        if tenant is None:
            return redirect(reverse(login_url))

        with tenant_context(tenant):
            request.tenant = tenant
            return self.get_response(request)

    def _get_tenant(self, request):
        tenant_id = request.session.get("tenant_id", None)

        if tenant_id:
            return self.TenantModel.objects.filter(id=tenant_id).first()
        return None
