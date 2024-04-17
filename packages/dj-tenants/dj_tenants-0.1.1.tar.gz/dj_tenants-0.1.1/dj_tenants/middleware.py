from django.shortcuts import redirect
from django.urls import reverse

from dj_tenants.conf import settings

from dj_tenants import get_tenant_model, tenant_context, tenant_context_disabled


class DjTenantsMiddleware:
    TenantModel = None
    LoginUrl = 'login'

    def __init__(self, get_response):
        self.get_response = get_response
        self.TenantModel = get_tenant_model()
        self.LoginUrl = settings.DJ_TENANTS_LOGIN_VIEW_NAME

    def __call__(self, request):
        if not request.user.is_authenticated:
            return self.get_response(request)

        if request.path.startswith("/admin/"):
            with tenant_context_disabled():
                return self.get_response(request)

        view_func = None
        if hasattr(request, 'resolver_match') and request.resolver_match:
            view_func = request.resolver_match.func

        if view_func and getattr(view_func, 'tenant_not_required', False):
            return self.get_response(request)

        tenant = self._get_tenant(request)

        if tenant is None:
            return redirect(reverse(self.LoginUrl))

        with tenant_context(tenant):
            request.tenant = tenant
            return self.get_response(request)

    def _get_tenant(self, request):
        tenant_id = request.session.get("tenant_id", None)

        if tenant_id:
            return self.TenantModel.objects.filter(id=tenant_id).first()
        return None
