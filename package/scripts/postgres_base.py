import os
from time import sleep

import ambari_simplejson as json # simplejson is much faster comparing to Python 2.6 json module and has the same functions set.
from resource_management import *


class PostgresBase(Script):

    postgres_packages = ['postgresql-13']

    def install_postgres(self, env):
        import params
        env.set_params(params)
        Execute('yum install -y https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm')
        Execute('yum install -y postgresql13-server')

    def configure_postgres(self, env):
        import params
        env.set_params(params)
        site_configurations = params.config['configurations']['postgres-site']
        File(format("{conf_dir}/postgresql.conf"),
             content=Template("postgresql.conf.j2", configurations = site_configurations),
             owner=params.postgres_user,
             group=params.postgres_user_group,
             mode=0600
             )
        hba_configurations = params.config['configurations']['postgres-hba']
        File(format("{conf_dir}/pg_hba.conf"),
             content=Template("pg_hba.conf.j2", configurations = hba_configurations),
             owner=params.postgres_user,
             group=params.postgres_user_group,
             mode=0600
             )