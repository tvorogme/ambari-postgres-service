from resource_management import *
from postgres_base import PostgresBase

class PostgresClient(PostgresBase):
    postgres_packages = ['postgresql-13']

    def install(self, env):
        import params
        env.set_params(params)
        self.install(env)
        self.configure(env)

if __name__ == "__main__":
    PostgresClient().execute()
