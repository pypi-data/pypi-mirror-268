from django.db.backends.postgresql.base import DatabaseWrapper as PostgresDatabaseWrapper

from dj_tenants.postgres_backend.operations import DatabaseOperations


class DatabaseWrapper(PostgresDatabaseWrapper):
    compiler_module = 'dj_tenants.postgres_backend.compiler'

    def __init__(self, *args, **kwargs):
        super(DatabaseWrapper, self).__init__(*args, **kwargs)

        self.ops = DatabaseOperations(self)
