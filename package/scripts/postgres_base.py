import os
from time import sleep

import ambari_simplejson as json # simplejson is much faster comparing to Python 2.6 json module and has the same functions set.
from resource_management import *


class PostgresBase(Script):

    postgres_packages = []

    def install_postgres(self, env):
        import params
        env.set_params(params)
        Execute('yum -y remove postgresql92-server-9.2.15-1.57.amzn1.x86_64')
        Execute('yum -y remove postgresql92-9.2.15-1.57.amzn1.x86_64')
        Execute('yum -y remove postgresql92-libs-9.2.15-1.57.amzn1.x86_64')
        Execute('yum -y install https://download.postgresql.org/pub/repos/yum/9.6/redhat/rhel-6-x86_64/pgdg-ami201503-96-9.6-2.noarch.rpm')
        print "Installing postgres..."
        for pack in self.postgres_packages:
            Package(pack)

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