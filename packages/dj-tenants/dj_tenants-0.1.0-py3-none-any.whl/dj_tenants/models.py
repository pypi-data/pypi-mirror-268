from django.db import models

from dj_tenants.context import get_current_tenant


class Tenant(models.Model):
    name = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TenantObjectManager(models.Manager):
    def get_queryset(self):
        tenant = get_current_tenant()
        return super().get_queryset().filter(tenant=tenant)

    def bulk_create(self, objs, batch_size=None, ignore_conflicts=False):
        tenant = get_current_tenant()
        for obj in objs:
            obj.tenant = tenant
        return super().bulk_create(objs, batch_size, ignore_conflicts)

    def bulk_update(self, objs, fields, batch_size=None):
        tenant = get_current_tenant()
        for obj in objs:
            obj.tenant = tenant
        return super().bulk_update(objs, fields, batch_size)


class TenantAbstract(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    objects = TenantObjectManager()

    def save(self, *args, **kwargs):
        self.tenant = get_current_tenant()
        super().save(*args, **kwargs)
