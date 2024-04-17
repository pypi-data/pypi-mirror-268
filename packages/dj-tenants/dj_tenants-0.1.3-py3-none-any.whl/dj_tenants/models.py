from django.db import models
from django.db.models.expressions import BaseExpression

from dj_tenants.conf import settings
from dj_tenants.context import get_current_tenant, get_dj_state

tenant_field_name = settings.DJ_TENANTS_TENANT_FIELD


class CurrentTenant(BaseExpression):
    def as_sql(self, compiler, connection, *args, **kwargs):
        current_tenant = get_current_tenant()
        tenant_id = str(current_tenant.id)
        value = self.output_field.get_db_prep_value(tenant_id, connection)

        return "%s", [str(value)]


class TenantManager(models.Manager):
    def get_queryset(self):
        state = get_dj_state()
        queryset = super().get_queryset()

        if not state.get("enabled", True):
            return queryset

        field = getattr(self.model, tenant_field_name).field.target_field
        filter_kwargs = {tenant_field_name: CurrentTenant(output_field=field)}

        return queryset.filter(**filter_kwargs)


class TenantAware(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        setattr(self, tenant_field_name, get_current_tenant())
        super().save(*args, **kwargs)

    def get_tenant_instance(self):
        return getattr(self, tenant_field_name)
