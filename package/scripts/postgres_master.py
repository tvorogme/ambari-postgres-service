from resource_management import *
from postgres_base import PostgresBase
from resource_management.core.exceptions import ExecutionFailed

class PostgresServer(PostgresBase):
    postgres_packages = ['postgresql-13']

    def install(self, env):
        import params
        env.set_params(params)
        self.install_pg(env)
        print("Initializing Postgress DB")
        init_cmd = format('/usr/pgsql-13/bin/postgresql-13-setup initdb')
        try:
            Execute(init_cmd)
        except ExecutionFailed as ef:
            print("Error {0}".format(ef))
        self.config_pg(env)

    def configure(self, env):
        import params
        env.set_params(params)
        self.config_pg(env)
        reload_cmd = format("systemctl reload postgresql-13")
        Execute(reload_cmd)

    def start(self, env):
        print("Starting postgres")
        self.config_pg(env)
        start_cmd = format("systemctl start postgresql-13")
        Execute(start_cmd)

    def stop(self, env):
        print("Stopping postgres")
        stop_cmd = format("systemctl stop postgresql-13")
        Execute(stop_cmd)

    def restart(self, env):
        print("Restartarting postgres")
        self.config_pg(env)
        Execute('systemctl restart postgresql-13')

    def status(self, env):
        print("Checking postgres status...")
        try:
            Execute('systemctl status postgresql-13')
        except ExecutionFailed:
            return False

if __name__ == "__main__":
    PostgresServer().execute()
