#!/usr/bin/env python
"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from resource_management import *

config = Script.get_config()

conf_dir = "/var/lib/pgsql/13/data"

# env settings
postgres_user = config['configurations']['postgres-env']['postgres_user']
postgres_user_group = config['configurations']['postgres-env']['postgres_user_group']
postgres_pid_dir = config['configurations']['postgres-env']['postgres_pid_dir']

# site settings
listen_addresses = config['configurations']['postgres-site']['listen_addresses']
tcp_port = config['configurations']['postgres-site']['tcp_port']
max_connections = config['configurations']['postgres-site']['max_connections']
shared_buffers = config['configurations']['postgres-site']['shared_buffers']
effective_cache_size = config['configurations']['postgres-site']['effective_cache_size']
work_mem = config['configurations']['postgres-site']['work_mem']
maintenance_work_mem = config['configurations']['postgres-site']['maintenance_work_mem']
min_wal_size = config['configurations']['postgres-site']['min_wal_size']
max_wal_size = config['configurations']['postgres-site']['max_wal_size']
wal_buffers = config['configurations']['postgres-site']['wal_buffers']
checkpoint_completion_target = config['configurations']['postgres-site']['checkpoint_completion_target']
default_statistics_target = config['configurations']['postgres-site']['default_statistics_target']

# client hba setting
client_type = config['configurations']['postgres-hba']['client_type']
client_database = config['configurations']['postgres-hba']['client_database']
client_user = config['configurations']['postgres-hba']['client_user']
client_address = config['configurations']['postgres-hba']['client_address']
client_method = config['configurations']['postgres-hba']['client_method']

postgres_host = default('/clusterHostInfo/postgres_server_hosts', ['unknown'])[0]
