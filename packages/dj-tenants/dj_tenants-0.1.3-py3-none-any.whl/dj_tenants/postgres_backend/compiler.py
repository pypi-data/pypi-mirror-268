from django.db.models.sql import compiler

from dj_tenants import get_current_tenant
from dj_tenants.context import get_dj_state
from dj_tenants.utils import count_fields_in_sql


class SQLCompiler(compiler.SQLCompiler):
    def as_sql(self, *args, **kwargs):
        sql, params = super().as_sql(*args, **kwargs)
        has_tenant_id = any(field.column == 'tenant_id' for field in self.query.model._meta.fields)

        dj_state = get_dj_state()
        if has_tenant_id and dj_state.get('enabled', True):
            tenant = get_current_tenant()

            limit_index = sql.find('LIMIT')
            order_by_index = sql.rfind('ORDER BY') if 'ORDER BY' in sql else -1

            insert_index = limit_index if limit_index != -1 else len(sql)

            if order_by_index != -1 and (order_by_index < limit_index or limit_index == -1):
                insert_index = order_by_index

            if 'WHERE' in sql:
                where_clause = f' AND {self.query.model._meta.db_table}.tenant_id = %s '
            else:
                where_clause = f' WHERE {self.query.model._meta.db_table}.tenant_id = %s '

            if insert_index != -1:
                sql = sql[:insert_index].rstrip() + where_clause + sql[insert_index:].lstrip()
            else:
                sql += where_clause

            params += (str(tenant.id),)
        return sql, params


class SQLInsertCompiler(compiler.SQLInsertCompiler, SQLCompiler):
    def as_sql(self, *args, **kwargs):
        sql = super().as_sql(*args, **kwargs)
        has_tenant_id = any(field.column == 'tenant_id' for field in self.query.model._meta.fields)
        dj_state = get_dj_state()

        if has_tenant_id and dj_state.get('enabled', True):
            modified_sql = []
            tenant = get_current_tenant()
            for sql, params in sql:
                if 'INSERT INTO' in sql:
                    count_fields = count_fields_in_sql(sql)
                    for i, p in enumerate(params):
                        if i % count_fields == 0:
                            params = params[:i] + (str(tenant.id),) + params[i + 1:]
                modified_sql.append((sql, params))
            return modified_sql
        return sql


class SQLDeleteCompiler(compiler.SQLDeleteCompiler, SQLCompiler):
    def as_sql(self, *args, **kwargs):
        return super().as_sql(*args, **kwargs)


class SQLUpdateCompiler(compiler.SQLUpdateCompiler, SQLCompiler):
    def as_sql(self, *args, **kwargs):
        sql, params = super().as_sql(*args, **kwargs)
        has_tenant_id = any(field.column == 'tenant_id' for field in self.query.model._meta.fields)

        dj_state = get_dj_state()
        if has_tenant_id and dj_state.get('enabled', True):
            tenant = get_current_tenant()

            where_index = sql.find('WHERE')
            tenant_condition = f' {self.query.model._meta.db_table}.tenant_id = %s'

            if where_index != -1:
                if sql.strip().endswith(';'):
                    sql = sql.strip()[:-1] + f' AND{tenant_condition};'
                else:
                    sql += f' AND{tenant_condition}'
            else:
                if sql.strip().endswith(';'):
                    sql = sql.strip()[:-1] + f' WHERE{tenant_condition};'
                else:
                    sql += f' WHERE{tenant_condition}'

            params += (str(tenant.id),)

        return sql, params


class SQLAggregateCompiler(compiler.SQLAggregateCompiler, SQLCompiler):
    def as_sql(self, *args, **kwargs):
        return super().as_sql(*args, **kwargs)
