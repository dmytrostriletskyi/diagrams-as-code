## On-Premise

Table of Content:

* [Aggregator](#aggregator)
* [Analytics](#analytics)
* [Auth](#auth)
* [Cd](#cd)
* [Certificates](#certificates)
* [Ci](#ci)
* [Client](#client)
* [Compute](#compute)
* [Container](#container)
* [Database](#database)
* [Dns](#dns)
* [Etl](#etl)
* [Gitops](#gitops)
* [Groupware](#groupware)
* [Iac](#iac)
* [Identity](#identity)
* [Inmemory](#inmemory)
* [Logging](#logging)
* [Messaging](#messaging)
* [Mlops](#mlops)
* [Monitoring](#monitoring)
* [Network](#network)
* [Proxmox](#proxmox)
* [Queue](#queue)
* [Registry](#registry)
* [Search](#search)
* [Security](#security)
* [Storage](#storage)
* [Tracing](#tracing)
* [Vcs](#vcs)
* [Workflow](#workflow)

### Aggregator

| Type                        | Alias | Image                                                                            |
|-----------------------------|-------|----------------------------------------------------------------------------------|
| `onprem.aggregator.Fluentd` | `-`   | <img width="90" src="../../docs/images/resources/onprem/aggregator/fluentd.png"> |
| `onprem.aggregator.Vector`  | `-`   | <img width="90" src="../../docs/images/resources/onprem/aggregator/vector.png">  |

### Analytics

| Type                          | Alias                      | Image                                                                              |
|-------------------------------|----------------------------|------------------------------------------------------------------------------------|
| `onprem.analytics.Beam`       | `-`                        | <img width="90" src="../../docs/images/resources/onprem/analytics/beam.png">       |
| `onprem.analytics.Databricks` | `-`                        | <img width="90" src="../../docs/images/resources/onprem/analytics/databricks.png"> |
| `onprem.analytics.Dbt`        | `-`                        | <img width="90" src="../../docs/images/resources/onprem/analytics/dbt.png">        |
| `onprem.analytics.Dremio`     | `-`                        | <img width="90" src="../../docs/images/resources/onprem/analytics/dremio.png">     |
| `onprem.analytics.Flink`      | `-`                        | <img width="90" src="../../docs/images/resources/onprem/analytics/flink.png">      |
| `onprem.analytics.Hadoop`     | `-`                        | <img width="90" src="../../docs/images/resources/onprem/analytics/hadoop.png">     |
| `onprem.analytics.Hive`       | `-`                        | <img width="90" src="../../docs/images/resources/onprem/analytics/hive.png">       |
| `onprem.analytics.Metabase`   | `-`                        | <img width="90" src="../../docs/images/resources/onprem/analytics/metabase.png">   |
| `onprem.analytics.Norikra`    | `-`                        | <img width="90" src="../../docs/images/resources/onprem/analytics/norikra.png">    |
| `onprem.analytics.Powerbi`    | `onprem.analytics.PowerBI` | <img width="90" src="../../docs/images/resources/onprem/analytics/powerbi.png">    |
| `onprem.analytics.Presto`     | `-`                        | <img width="90" src="../../docs/images/resources/onprem/analytics/presto.png">     |
| `onprem.analytics.Singer`     | `-`                        | <img width="90" src="../../docs/images/resources/onprem/analytics/singer.png">     |
| `onprem.analytics.Spark`      | `-`                        | <img width="90" src="../../docs/images/resources/onprem/analytics/spark.png">      |
| `onprem.analytics.Storm`      | `-`                        | <img width="90" src="../../docs/images/resources/onprem/analytics/storm.png">      |
| `onprem.analytics.Superset`   | `-`                        | <img width="90" src="../../docs/images/resources/onprem/analytics/superset.png">   |
| `onprem.analytics.Tableau`    | `-`                        | <img width="90" src="../../docs/images/resources/onprem/analytics/tableau.png">    |

### Auth

| Type                      | Alias | Image                                                                           |
|---------------------------|-------|---------------------------------------------------------------------------------|
| `onprem.auth.Boundary`    | `-`   | <img width="90" src="../../docs/images/resources/onprem/auth/boundary.png">     |
| `onprem.auth.BuzzfeedSso` | `-`   | <img width="90" src="../../docs/images/resources/onprem/auth/buzzfeed-sso.png"> |
| `onprem.auth.Oauth2Proxy` | `-`   | <img width="90" src="../../docs/images/resources/onprem/auth/oauth2-proxy.png"> |

### Cd

| Type                  | Alias | Image                                                                       |
|-----------------------|-------|-----------------------------------------------------------------------------|
| `onprem.cd.Spinnaker` | `-`   | <img width="90" src="../../docs/images/resources/onprem/cd/spinnaker.png">  |
| `onprem.cd.TektonCli` | `-`   | <img width="90" src="../../docs/images/resources/onprem/cd/tekton-cli.png"> |
| `onprem.cd.Tekton`    | `-`   | <img width="90" src="../../docs/images/resources/onprem/cd/tekton.png">     |

### Certificates

| Type                              | Alias | Image                                                                                   |
|-----------------------------------|-------|-----------------------------------------------------------------------------------------|
| `onprem.certificates.CertManager` | `-`   | <img width="90" src="../../docs/images/resources/onprem/certificates/cert-manager.png"> |
| `onprem.certificates.LetsEncrypt` | `-`   | <img width="90" src="../../docs/images/resources/onprem/certificates/lets-encrypt.png"> |

### Ci

| Type                      | Alias                   | Image                                                                           |
|---------------------------|-------------------------|---------------------------------------------------------------------------------|
| `onprem.ci.Circleci`      | `onprem.ci.CircleCI`    | <img width="90" src="../../docs/images/resources/onprem/ci/circleci.png">       |
| `onprem.ci.Concourseci`   | `onprem.ci.ConcourseCI` | <img width="90" src="../../docs/images/resources/onprem/ci/concourseci.png">    |
| `onprem.ci.Droneci`       | `onprem.ci.DroneCI`     | <img width="90" src="../../docs/images/resources/onprem/ci/droneci.png">        |
| `onprem.ci.GithubActions` | `-`                     | <img width="90" src="../../docs/images/resources/onprem/ci/github-actions.png"> |
| `onprem.ci.Gitlabci`      | `onprem.ci.GitlabCI`    | <img width="90" src="../../docs/images/resources/onprem/ci/gitlabci.png">       |
| `onprem.ci.Jenkins`       | `-`                     | <img width="90" src="../../docs/images/resources/onprem/ci/jenkins.png">        |
| `onprem.ci.Teamcity`      | `onprem.ci.TC`          | <img width="90" src="../../docs/images/resources/onprem/ci/teamcity.png">       |
| `onprem.ci.Travisci`      | `onprem.ci.TravisCI`    | <img width="90" src="../../docs/images/resources/onprem/ci/travisci.png">       |
| `onprem.ci.Zuulci`        | `onprem.ci.ZuulCI`      | <img width="90" src="../../docs/images/resources/onprem/ci/zuulci.png">         |

### Client

| Type                   | Alias | Image                                                                       |
|------------------------|-------|-----------------------------------------------------------------------------|
| `onprem.client.Client` | `-`   | <img width="90" src="../../docs/images/resources/onprem/client/client.png"> |
| `onprem.client.User`   | `-`   | <img width="90" src="../../docs/images/resources/onprem/client/user.png">   |
| `onprem.client.Users`  | `-`   | <img width="90" src="../../docs/images/resources/onprem/client/users.png">  |

### Compute

| Type                    | Alias | Image                                                                        |
|-------------------------|-------|------------------------------------------------------------------------------|
| `onprem.compute.Nomad`  | `-`   | <img width="90" src="../../docs/images/resources/onprem/compute/nomad.png">  |
| `onprem.compute.Server` | `-`   | <img width="90" src="../../docs/images/resources/onprem/compute/server.png"> |

### Container

| Type                           | Alias                  | Image                                                                               |
|--------------------------------|------------------------|-------------------------------------------------------------------------------------|
| `onprem.container.Containerd`  | `-`                    | <img width="90" src="../../docs/images/resources/onprem/container/containerd.png">  |
| `onprem.container.Crio`        | `-`                    | <img width="90" src="../../docs/images/resources/onprem/container/crio.png">        |
| `onprem.container.Docker`      | `-`                    | <img width="90" src="../../docs/images/resources/onprem/container/docker.png">      |
| `onprem.container.Firecracker` | `-`                    | <img width="90" src="../../docs/images/resources/onprem/container/firecracker.png"> |
| `onprem.container.Gvisor`      | `-`                    | <img width="90" src="../../docs/images/resources/onprem/container/gvisor.png">      |
| `onprem.container.K3S`         | `-`                    | <img width="90" src="../../docs/images/resources/onprem/container/k3s.png">         |
| `onprem.container.Lxc`         | `onprem.container.LXC` | <img width="90" src="../../docs/images/resources/onprem/container/lxc.png">         |
| `onprem.container.Rkt`         | `onprem.container.RKT` | <img width="90" src="../../docs/images/resources/onprem/container/rkt.png">         |

### Database

| Type                          | Alias                         | Image                                                                              |
|-------------------------------|-------------------------------|------------------------------------------------------------------------------------|
| `onprem.database.Cassandra`   | `-`                           | <img width="90" src="../../docs/images/resources/onprem/database/cassandra.png">   |
| `onprem.database.Clickhouse`  | `onprem.database.ClickHouse`  | <img width="90" src="../../docs/images/resources/onprem/database/clickhouse.png">  |
| `onprem.database.Cockroachdb` | `onprem.database.CockroachDB` | <img width="90" src="../../docs/images/resources/onprem/database/cockroachdb.png"> |
| `onprem.database.Couchbase`   | `-`                           | <img width="90" src="../../docs/images/resources/onprem/database/couchbase.png">   |
| `onprem.database.Couchdb`     | `onprem.database.CouchDB`     | <img width="90" src="../../docs/images/resources/onprem/database/couchdb.png">     |
| `onprem.database.Dgraph`      | `-`                           | <img width="90" src="../../docs/images/resources/onprem/database/dgraph.png">      |
| `onprem.database.Druid`       | `-`                           | <img width="90" src="../../docs/images/resources/onprem/database/druid.png">       |
| `onprem.database.Hbase`       | `onprem.database.HBase`       | <img width="90" src="../../docs/images/resources/onprem/database/hbase.png">       |
| `onprem.database.Influxdb`    | `onprem.database.InfluxDB`    | <img width="90" src="../../docs/images/resources/onprem/database/influxdb.png">    |
| `onprem.database.Janusgraph`  | `onprem.database.JanusGraph`  | <img width="90" src="../../docs/images/resources/onprem/database/janusgraph.png">  |
| `onprem.database.Mariadb`     | `onprem.database.MariaDB`     | <img width="90" src="../../docs/images/resources/onprem/database/mariadb.png">     |
| `onprem.database.Mongodb`     | `onprem.database.MongoDB`     | <img width="90" src="../../docs/images/resources/onprem/database/mongodb.png">     |
| `onprem.database.Mssql`       | `onprem.database.MSSQL`       | <img width="90" src="../../docs/images/resources/onprem/database/mssql.png">       |
| `onprem.database.Mysql`       | `onprem.database.MySQL`       | <img width="90" src="../../docs/images/resources/onprem/database/mysql.png">       |
| `onprem.database.Neo4J`       | `-`                           | <img width="90" src="../../docs/images/resources/onprem/database/neo4j.png">       |
| `onprem.database.Oracle`      | `-`                           | <img width="90" src="../../docs/images/resources/onprem/database/oracle.png">      |
| `onprem.database.Postgresql`  | `onprem.database.PostgreSQL`  | <img width="90" src="../../docs/images/resources/onprem/database/postgresql.png">  |
| `onprem.database.Scylla`      | `-`                           | <img width="90" src="../../docs/images/resources/onprem/database/scylla.png">      |

### Dns

| Type                  | Alias | Image                                                                      |
|-----------------------|-------|----------------------------------------------------------------------------|
| `onprem.dns.Coredns`  | `-`   | <img width="90" src="../../docs/images/resources/onprem/dns/coredns.png">  |
| `onprem.dns.Powerdns` | `-`   | <img width="90" src="../../docs/images/resources/onprem/dns/powerdns.png"> |

### Etl

| Type                | Alias | Image                                                                    |
|---------------------|-------|--------------------------------------------------------------------------|
| `onprem.etl.Embulk` | `-`   | <img width="90" src="../../docs/images/resources/onprem/etl/embulk.png"> |

### Gitops

| Type                    | Alias                  | Image                                                                        |
|-------------------------|------------------------|------------------------------------------------------------------------------|
| `onprem.gitops.Argocd`  | `onprem.gitops.ArgoCD` | <img width="90" src="../../docs/images/resources/onprem/gitops/argocd.png">  |
| `onprem.gitops.Flagger` | `-`                    | <img width="90" src="../../docs/images/resources/onprem/gitops/flagger.png"> |
| `onprem.gitops.Flux`    | `-`                    | <img width="90" src="../../docs/images/resources/onprem/gitops/flux.png">    |

### Groupware

| Type                         | Alias | Image                                                                             |
|------------------------------|-------|-----------------------------------------------------------------------------------|
| `onprem.groupware.Nextcloud` | `-`   | <img width="90" src="../../docs/images/resources/onprem/groupware/nextcloud.png"> |

### Iac

| Type                   | Alias | Image                                                                       |
|------------------------|-------|-----------------------------------------------------------------------------|
| `onprem.iac.Ansible`   | `-`   | <img width="90" src="../../docs/images/resources/onprem/iac/ansible.png">   |
| `onprem.iac.Atlantis`  | `-`   | <img width="90" src="../../docs/images/resources/onprem/iac/atlantis.png">  |
| `onprem.iac.Awx`       | `-`   | <img width="90" src="../../docs/images/resources/onprem/iac/awx.png">       |
| `onprem.iac.Puppet`    | `-`   | <img width="90" src="../../docs/images/resources/onprem/iac/puppet.png">    |
| `onprem.iac.Terraform` | `-`   | <img width="90" src="../../docs/images/resources/onprem/iac/terraform.png"> |

### Identity

| Type                  | Alias | Image                                                                      |
|-----------------------|-------|----------------------------------------------------------------------------|
| `onprem.identity.Dex` | `-`   | <img width="90" src="../../docs/images/resources/onprem/identity/dex.png"> |

### Inmemory

| Type                        | Alias | Image                                                                            |
|-----------------------------|-------|----------------------------------------------------------------------------------|
| `onprem.inmemory.Aerospike` | `-`   | <img width="90" src="../../docs/images/resources/onprem/inmemory/aerospike.png"> |
| `onprem.inmemory.Hazelcast` | `-`   | <img width="90" src="../../docs/images/resources/onprem/inmemory/hazelcast.png"> |
| `onprem.inmemory.Memcached` | `-`   | <img width="90" src="../../docs/images/resources/onprem/inmemory/memcached.png"> |
| `onprem.inmemory.Redis`     | `-`   | <img width="90" src="../../docs/images/resources/onprem/inmemory/redis.png">     |

### Logging

| Type                       | Alias                      | Image                                                                           |
|----------------------------|----------------------------|---------------------------------------------------------------------------------|
| `onprem.logging.Fluentbit` | `onprem.logging.FluentBit` | <img width="90" src="../../docs/images/resources/onprem/logging/fluentbit.png"> |
| `onprem.logging.Graylog`   | `-`                        | <img width="90" src="../../docs/images/resources/onprem/logging/graylog.png">   |
| `onprem.logging.Loki`      | `-`                        | <img width="90" src="../../docs/images/resources/onprem/logging/loki.png">      |
| `onprem.logging.Rsyslog`   | `onprem.logging.RSyslog`   | <img width="90" src="../../docs/images/resources/onprem/logging/rsyslog.png">   |
| `onprem.logging.SyslogNg`  | `-`                        | <img width="90" src="../../docs/images/resources/onprem/logging/syslog-ng.png"> |

### Messaging

| Type                          | Alias | Image                                                                              |
|-------------------------------|-------|------------------------------------------------------------------------------------|
| `onprem.messaging.Centrifugo` | `-`   | <img width="90" src="../../docs/images/resources/onprem/messaging/centrifugo.png"> |

### Mlops

| Type                    | Alias | Image                                                                        |
|-------------------------|-------|------------------------------------------------------------------------------|
| `onprem.mlops.Mlflow`   | `-`   | <img width="90" src="../../docs/images/resources/onprem/mlops/mlflow.png">   |
| `onprem.mlops.Polyaxon` | `-`   | <img width="90" src="../../docs/images/resources/onprem/mlops/polyaxon.png"> |

### Monitoring

| Type                                   | Alias | Image                                                                                        |
|----------------------------------------|-------|----------------------------------------------------------------------------------------------|
| `onprem.monitoring.Cortex`             | `-`   | <img width="90" src="../../docs/images/resources/onprem/monitoring/cortex.png">              |
| `onprem.monitoring.Datadog`            | `-`   | <img width="90" src="../../docs/images/resources/onprem/monitoring/datadog.png">             |
| `onprem.monitoring.Dynatrace`          | `-`   | <img width="90" src="../../docs/images/resources/onprem/monitoring/dynatrace.png">           |
| `onprem.monitoring.Grafana`            | `-`   | <img width="90" src="../../docs/images/resources/onprem/monitoring/grafana.png">             |
| `onprem.monitoring.Humio`              | `-`   | <img width="90" src="../../docs/images/resources/onprem/monitoring/humio.png">               |
| `onprem.monitoring.Mimir`              | `-`   | <img width="90" src="../../docs/images/resources/onprem/monitoring/mimir.png">               |
| `onprem.monitoring.Nagios`             | `-`   | <img width="90" src="../../docs/images/resources/onprem/monitoring/nagios.png">              |
| `onprem.monitoring.Newrelic`           | `-`   | <img width="90" src="../../docs/images/resources/onprem/monitoring/newrelic.png">            |
| `onprem.monitoring.PrometheusOperator` | `-`   | <img width="90" src="../../docs/images/resources/onprem/monitoring/prometheus-operator.png"> |
| `onprem.monitoring.Prometheus`         | `-`   | <img width="90" src="../../docs/images/resources/onprem/monitoring/prometheus.png">          |
| `onprem.monitoring.Sentry`             | `-`   | <img width="90" src="../../docs/images/resources/onprem/monitoring/sentry.png">              |
| `onprem.monitoring.Splunk`             | `-`   | <img width="90" src="../../docs/images/resources/onprem/monitoring/splunk.png">              |
| `onprem.monitoring.Thanos`             | `-`   | <img width="90" src="../../docs/images/resources/onprem/monitoring/thanos.png">              |
| `onprem.monitoring.Zabbix`             | `-`   | <img width="90" src="../../docs/images/resources/onprem/monitoring/zabbix.png">              |

### Network

| Type                             | Alias                     | Image                                                                                   |
|----------------------------------|---------------------------|-----------------------------------------------------------------------------------------|
| `onprem.network.Ambassador`      | `-`                       | <img width="90" src="../../docs/images/resources/onprem/network/ambassador.png">        |
| `onprem.network.Apache`          | `-`                       | <img width="90" src="../../docs/images/resources/onprem/network/apache.png">            |
| `onprem.network.Bind9`           | `-`                       | <img width="90" src="../../docs/images/resources/onprem/network/bind-9.png">            |
| `onprem.network.Caddy`           | `-`                       | <img width="90" src="../../docs/images/resources/onprem/network/caddy.png">             |
| `onprem.network.Consul`          | `-`                       | <img width="90" src="../../docs/images/resources/onprem/network/consul.png">            |
| `onprem.network.Envoy`           | `-`                       | <img width="90" src="../../docs/images/resources/onprem/network/envoy.png">             |
| `onprem.network.Etcd`            | `onprem.network.ETCD`     | <img width="90" src="../../docs/images/resources/onprem/network/etcd.png">              |
| `onprem.network.Glassfish`       | `-`                       | <img width="90" src="../../docs/images/resources/onprem/network/glassfish.png">         |
| `onprem.network.Gunicorn`        | `-`                       | <img width="90" src="../../docs/images/resources/onprem/network/gunicorn.png">          |
| `onprem.network.Haproxy`         | `onprem.network.HAProxy`  | <img width="90" src="../../docs/images/resources/onprem/network/haproxy.png">           |
| `onprem.network.Internet`        | `-`                       | <img width="90" src="../../docs/images/resources/onprem/network/internet.png">          |
| `onprem.network.Istio`           | `-`                       | <img width="90" src="../../docs/images/resources/onprem/network/istio.png">             |
| `onprem.network.Jbossas`         | `-`                       | <img width="90" src="../../docs/images/resources/onprem/network/jbossas.png">           |
| `onprem.network.Jetty`           | `-`                       | <img width="90" src="../../docs/images/resources/onprem/network/jetty.png">             |
| `onprem.network.Kong`            | `-`                       | <img width="90" src="../../docs/images/resources/onprem/network/kong.png">              |
| `onprem.network.Linkerd`         | `-`                       | <img width="90" src="../../docs/images/resources/onprem/network/linkerd.png">           |
| `onprem.network.Nginx`           | `-`                       | <img width="90" src="../../docs/images/resources/onprem/network/nginx.png">             |
| `onprem.network.Ocelot`          | `-`                       | <img width="90" src="../../docs/images/resources/onprem/network/ocelot.png">            |
| `onprem.network.OpenServiceMesh` | `onprem.network.OSM`      | <img width="90" src="../../docs/images/resources/onprem/network/open-service-mesh.png"> |
| `onprem.network.Opnsense`        | `onprem.network.OPNSense` | <img width="90" src="../../docs/images/resources/onprem/network/opnsense.png">          |
| `onprem.network.Pfsense`         | `onprem.network.PFSense`  | <img width="90" src="../../docs/images/resources/onprem/network/pfsense.png">           |
| `onprem.network.Pomerium`        | `-`                       | <img width="90" src="../../docs/images/resources/onprem/network/pomerium.png">          |
| `onprem.network.Powerdns`        | `-`                       | <img width="90" src="../../docs/images/resources/onprem/network/powerdns.png">          |
| `onprem.network.Tomcat`          | `-`                       | <img width="90" src="../../docs/images/resources/onprem/network/tomcat.png">            |
| `onprem.network.Traefik`         | `-`                       | <img width="90" src="../../docs/images/resources/onprem/network/traefik.png">           |
| `onprem.network.Tyk`             | `-`                       | <img width="90" src="../../docs/images/resources/onprem/network/tyk.png">               |
| `onprem.network.Vyos`            | `onprem.network.VyOS`     | <img width="90" src="../../docs/images/resources/onprem/network/vyos.png">              |
| `onprem.network.Wildfly`         | `-`                       | <img width="90" src="../../docs/images/resources/onprem/network/wildfly.png">           |
| `onprem.network.Yarp`            | `-`                       | <img width="90" src="../../docs/images/resources/onprem/network/yarp.png">              |
| `onprem.network.Zookeeper`       | `-`                       | <img width="90" src="../../docs/images/resources/onprem/network/zookeeper.png">         |

### Proxmox

| Type                 | Alias                      | Image                                                                     |
|----------------------|----------------------------|---------------------------------------------------------------------------|
| `onprem.proxmox.Pve` | `onprem.proxmox.ProxmoxVE` | <img width="90" src="../../docs/images/resources/onprem/proxmox/pve.png"> |

### Queue

| Type                    | Alias                   | Image                                                                        |
|-------------------------|-------------------------|------------------------------------------------------------------------------|
| `onprem.queue.Activemq` | `onprem.queue.ActiveMQ` | <img width="90" src="../../docs/images/resources/onprem/queue/activemq.png"> |
| `onprem.queue.Celery`   | `-`                     | <img width="90" src="../../docs/images/resources/onprem/queue/celery.png">   |
| `onprem.queue.Emqx`     | `onprem.queue.EMQX`     | <img width="90" src="../../docs/images/resources/onprem/queue/emqx.png">     |
| `onprem.queue.Kafka`    | `-`                     | <img width="90" src="../../docs/images/resources/onprem/queue/kafka.png">    |
| `onprem.queue.Nats`     | `-`                     | <img width="90" src="../../docs/images/resources/onprem/queue/nats.png">     |
| `onprem.queue.Rabbitmq` | `onprem.queue.RabbitMQ` | <img width="90" src="../../docs/images/resources/onprem/queue/rabbitmq.png"> |
| `onprem.queue.Zeromq`   | `onprem.queue.ZeroMQ`   | <img width="90" src="../../docs/images/resources/onprem/queue/zeromq.png">   |

### Registry

| Type                     | Alias | Image                                                                         |
|--------------------------|-------|-------------------------------------------------------------------------------|
| `onprem.registry.Harbor` | `-`   | <img width="90" src="../../docs/images/resources/onprem/registry/harbor.png"> |
| `onprem.registry.Jfrog`  | `-`   | <img width="90" src="../../docs/images/resources/onprem/registry/jfrog.png">  |

### Search

| Type                 | Alias | Image                                                                     |
|----------------------|-------|---------------------------------------------------------------------------|
| `onprem.search.Solr` | `-`   | <img width="90" src="../../docs/images/resources/onprem/search/solr.png"> |

### Security

| Type                        | Alias | Image                                                                            |
|-----------------------------|-------|----------------------------------------------------------------------------------|
| `onprem.security.Bitwarden` | `-`   | <img width="90" src="../../docs/images/resources/onprem/security/bitwarden.png"> |
| `onprem.security.Trivy`     | `-`   | <img width="90" src="../../docs/images/resources/onprem/security/trivy.png">     |
| `onprem.security.Vault`     | `-`   | <img width="90" src="../../docs/images/resources/onprem/security/vault.png">     |

### Storage

| Type                       | Alias                     | Image                                                                           |
|----------------------------|---------------------------|---------------------------------------------------------------------------------|
| `onprem.storage.CephOsd`   | `onprem.storage.CEPH_OSD` | <img width="90" src="../../docs/images/resources/onprem/storage/ceph-osd.png">  |
| `onprem.storage.Ceph`      | `onprem.storage.CEPH`     | <img width="90" src="../../docs/images/resources/onprem/storage/ceph.png">      |
| `onprem.storage.Glusterfs` | `-`                       | <img width="90" src="../../docs/images/resources/onprem/storage/glusterfs.png"> |
| `onprem.storage.Portworx`  | `-`                       | <img width="90" src="../../docs/images/resources/onprem/storage/portworx.png">  |

### Tracing

| Type                    | Alias | Image                                                                        |
|-------------------------|-------|------------------------------------------------------------------------------|
| `onprem.tracing.Jaeger` | `-`   | <img width="90" src="../../docs/images/resources/onprem/tracing/jaeger.png"> |
| `onprem.tracing.Tempo`  | `-`   | <img width="90" src="../../docs/images/resources/onprem/tracing/tempo.png">  |

### Vcs

| Type                | Alias | Image                                                                    |
|---------------------|-------|--------------------------------------------------------------------------|
| `onprem.vcs.Git`    | `-`   | <img width="90" src="../../docs/images/resources/onprem/vcs/git.png">    |
| `onprem.vcs.Gitea`  | `-`   | <img width="90" src="../../docs/images/resources/onprem/vcs/gitea.png">  |
| `onprem.vcs.Github` | `-`   | <img width="90" src="../../docs/images/resources/onprem/vcs/github.png"> |
| `onprem.vcs.Gitlab` | `-`   | <img width="90" src="../../docs/images/resources/onprem/vcs/gitlab.png"> |
| `onprem.vcs.Svn`    | `-`   | <img width="90" src="../../docs/images/resources/onprem/vcs/svn.png">    |

### Workflow

| Type                       | Alias                      | Image                                                                           |
|----------------------------|----------------------------|---------------------------------------------------------------------------------|
| `onprem.workflow.Airflow`  | `-`                        | <img width="90" src="../../docs/images/resources/onprem/workflow/airflow.png">  |
| `onprem.workflow.Digdag`   | `-`                        | <img width="90" src="../../docs/images/resources/onprem/workflow/digdag.png">   |
| `onprem.workflow.Kubeflow` | `onprem.workflow.KubeFlow` | <img width="90" src="../../docs/images/resources/onprem/workflow/kubeflow.png"> |
| `onprem.workflow.Nifi`     | `onprem.workflow.NiFi`     | <img width="90" src="../../docs/images/resources/onprem/workflow/nifi.png">     |
