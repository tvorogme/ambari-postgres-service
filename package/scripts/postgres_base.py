from resource_management import *
from resource_management.core.exceptions import ExecutionFailed

class PostgresBase(Script):
    postgres_packages = ['postgresql-13']

    def install_pg(self, env):
        import params
        env.set_params(params)

        try:
            Execute('rpm -Uvh https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm')
        except ExecutionFailed as ef:
            print("Error, maybe installed {0}".format(ef))
        Execute('yum install -y postgresql13-server')

    def config_pg(self, env):
        import params
        env.set_params(params)
        site_configurations = params.config['configurations']['postgres-site']
        File(format("{conf_dir}/postgresql.conf"),
             content=Template("postgresql.conf.j2", configurations=site_configurations),
             owner=params.postgres_user,
             group=params.postgres_user_group,
             mode=0600
             )
        hba_configurations = params.config['configurations']['postgres-hba']
        File(format("{conf_dir}/pg_hba.conf"),
             content=Template("pg_hba.conf.j2", configurations=hba_configurations),
             owner=params.postgres_user,
             group=params.postgres_user_group,
             mode=0600
             )

    def install(self, env):
        self.install_pg(self, env)

    def configure(self, env):
        self.config_pg(self, env)
