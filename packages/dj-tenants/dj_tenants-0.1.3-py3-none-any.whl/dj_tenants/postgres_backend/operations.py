from django.db.backends.postgresql.operations import DatabaseOperations as PostgresDatabaseOperations


class DatabaseOperations(PostgresDatabaseOperations):
    compiler_module = 'dj_tenants.postgres_backend.compiler'
