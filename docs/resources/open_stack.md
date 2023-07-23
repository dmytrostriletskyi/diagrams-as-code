## OpenStack

Table of Content:

* [API Proxies](#api-proxies)
* [Application Life Cycle](#application-life-cycle)
* [Bare Metal](#bare-metal)
* [Billing](#billing)
* [Compute](#compute)
* [Container Services](#container-services)
* [Deployment](#deployment)
* [Front-end](#front-end)
* [Monitoring](#monitoring)
* [Multiregion](#multiregion)
* [Networking](#networking)
* [NFV](#nfv)
* [Optimization](#optimization)
* [Orchestration](#orchestration)
* [Packaging](#packaging)
* [Shared Services](#shared-services)
* [Storage](#storage)
* [User](#user)
* [Workload Provisioning](#workload-provisioning)

### API Proxies

| Type                          | Alias | Image                                                                              |
|-------------------------------|-------|------------------------------------------------------------------------------------|
| `openstack.apiproxies.EC2API` | `-`   | <img width="90" src="../../docs/images/resources/openstack/apiproxies/ec2api.png"> |

### Application Life Cycle

| Type                                      | Alias | Image                                                                                          |
|-------------------------------------------|-------|------------------------------------------------------------------------------------------------|
| `openstack.applicationlifecycle.Freezer`  | `-`   | <img width="90" src="../../docs/images/resources/openstack/applicationlifecycle/freezer.png">  |
| `openstack.applicationlifecycle.Masakari` | `-`   | <img width="90" src="../../docs/images/resources/openstack/applicationlifecycle/masakari.png"> |
| `openstack.applicationlifecycle.Murano`   | `-`   | <img width="90" src="../../docs/images/resources/openstack/applicationlifecycle/murano.png">   |
| `openstack.applicationlifecycle.Solum`    | `-`   | <img width="90" src="../../docs/images/resources/openstack/applicationlifecycle/solum.png">    |

### Bare Metal

| Type                         | Alias | Image                                                                             |
|------------------------------|-------|-----------------------------------------------------------------------------------|
| `openstack.baremetal.Cyborg` | `-`   | <img width="90" src="../../docs/images/resources/openstack/baremetal/cyborg.png"> |
| `openstack.baremetal.Ironic` | `-`   | <img width="90" src="../../docs/images/resources/openstack/baremetal/ironic.png"> |

### Billing

| Type                           | Alias                          | Image                                                                               |
|--------------------------------|--------------------------------|-------------------------------------------------------------------------------------|
| `openstack.billing.Cloudkitty` | `openstack.billing.CloudKitty` | <img width="90" src="../../docs/images/resources/openstack/billing/cloudkitty.png"> |

### Compute

| Type                        | Alias | Image                                                                            |
|-----------------------------|-------|----------------------------------------------------------------------------------|
| `openstack.compute.Nova`    | `-`   | <img width="90" src="../../docs/images/resources/openstack/compute/nova.png">    |
| `openstack.compute.Qinling` | `-`   | <img width="90" src="../../docs/images/resources/openstack/compute/qinling.png"> |
| `openstack.compute.Zun`     | `-`   | <img width="90" src="../../docs/images/resources/openstack/compute/zun.png">     |

### Container Services

| Type                                | Alias | Image                                                                                    |
|-------------------------------------|-------|------------------------------------------------------------------------------------------|
| `openstack.containerservices.Kuryr` | `-`   | <img width="90" src="../../docs/images/resources/openstack/containerservices/kuryr.png"> |

### Deployment

| Type                           | Alias                               | Image                                                                               |
|--------------------------------|-------------------------------------|-------------------------------------------------------------------------------------|
| `openstack.deployment.Ansible` | `-`                                 | <img width="90" src="../../docs/images/resources/openstack/deployment/ansible.png"> |
| `openstack.deployment.Charms`  | `-`                                 | <img width="90" src="../../docs/images/resources/openstack/deployment/charms.png">  |
| `openstack.deployment.Chef`    | `-`                                 | <img width="90" src="../../docs/images/resources/openstack/deployment/chef.png">    |
| `openstack.deployment.Helm`    | `-`                                 | <img width="90" src="../../docs/images/resources/openstack/deployment/helm.png">    |
| `openstack.deployment.Kolla`   | `openstack.deployment.KollaAnsible` | <img width="90" src="../../docs/images/resources/openstack/deployment/kolla.png">   |
| `openstack.deployment.Tripleo` | `openstack.deployment.TripleO`      | <img width="90" src="../../docs/images/resources/openstack/deployment/tripleo.png"> |

### Front-end

| Type                         | Alias | Image                                                                             |
|------------------------------|-------|-----------------------------------------------------------------------------------|
| `openstack.frontend.Horizon` | `-`   | <img width="90" src="../../docs/images/resources/openstack/frontend/horizon.png"> |

### Monitoring

| Type                             | Alias | Image                                                                                 |
|----------------------------------|-------|---------------------------------------------------------------------------------------|
| `openstack.monitoring.Monasca`   | `-`   | <img width="90" src="../../docs/images/resources/openstack/monitoring/monasca.png">   |
| `openstack.monitoring.Telemetry` | `-`   | <img width="90" src="../../docs/images/resources/openstack/monitoring/telemetry.png"> |

### Multiregion

| Type                              | Alias | Image                                                                                  |
|-----------------------------------|-------|----------------------------------------------------------------------------------------|
| `openstack.multiregion.Tricircle` | `-`   | <img width="90" src="../../docs/images/resources/openstack/multiregion/tricircle.png"> |

### Networking

| Type                             | Alias | Image                                                                                 |
|----------------------------------|-------|---------------------------------------------------------------------------------------|
| `openstack.networking.Designate` | `-`   | <img width="90" src="../../docs/images/resources/openstack/networking/designate.png"> |
| `openstack.networking.Neutron`   | `-`   | <img width="90" src="../../docs/images/resources/openstack/networking/neutron.png">   |
| `openstack.networking.Octavia`   | `-`   | <img width="90" src="../../docs/images/resources/openstack/networking/octavia.png">   |

### NFV

| Type                   | Alias | Image                                                                       |
|------------------------|-------|-----------------------------------------------------------------------------|
| `openstack.nfv.Tacker` | `-`   | <img width="90" src="../../docs/images/resources/openstack/nfv/tacker.png"> |

### Optimization

| Type                              | Alias | Image                                                                                  |
|-----------------------------------|-------|----------------------------------------------------------------------------------------|
| `openstack.optimization.Congress` | `-`   | <img width="90" src="../../docs/images/resources/openstack/optimization/congress.png"> |
| `openstack.optimization.Rally`    | `-`   | <img width="90" src="../../docs/images/resources/openstack/optimization/rally.png">    |
| `openstack.optimization.Vitrage`  | `-`   | <img width="90" src="../../docs/images/resources/openstack/optimization/vitrage.png">  |
| `openstack.optimization.Watcher`  | `-`   | <img width="90" src="../../docs/images/resources/openstack/optimization/watcher.png">  |

### Orchestration

| Type                              | Alias | Image                                                                                  |
|-----------------------------------|-------|----------------------------------------------------------------------------------------|
| `openstack.orchestration.Blazar`  | `-`   | <img width="90" src="../../docs/images/resources/openstack/orchestration/blazar.png">  |
| `openstack.orchestration.Heat`    | `-`   | <img width="90" src="../../docs/images/resources/openstack/orchestration/heat.png">    |
| `openstack.orchestration.Mistral` | `-`   | <img width="90" src="../../docs/images/resources/openstack/orchestration/mistral.png"> |
| `openstack.orchestration.Senlin`  | `-`   | <img width="90" src="../../docs/images/resources/openstack/orchestration/senlin.png">  |
| `openstack.orchestration.Zaqar`   | `-`   | <img width="90" src="../../docs/images/resources/openstack/orchestration/zaqar.png">   |

### Packaging

| Type                         | Alias | Image                                                                             |
|------------------------------|-------|-----------------------------------------------------------------------------------|
| `openstack.packaging.LOCI`   | `-`   | <img width="90" src="../../docs/images/resources/openstack/packaging/loci.png">   |
| `openstack.packaging.Puppet` | `-`   | <img width="90" src="../../docs/images/resources/openstack/packaging/puppet.png"> |
| `openstack.packaging.RPM`    | `-`   | <img width="90" src="../../docs/images/resources/openstack/packaging/rpm.png">    |

### Shared Services

| Type                                   | Alias | Image                                                                                       |
|----------------------------------------|-------|---------------------------------------------------------------------------------------------|
| `openstack.sharedservices.Barbican`    | `-`   | <img width="90" src="../../docs/images/resources/openstack/sharedservices/barbican.png">    |
| `openstack.sharedservices.Glance`      | `-`   | <img width="90" src="../../docs/images/resources/openstack/sharedservices/glance.png">      |
| `openstack.sharedservices.Karbor`      | `-`   | <img width="90" src="../../docs/images/resources/openstack/sharedservices/karbor.png">      |
| `openstack.sharedservices.Keystone`    | `-`   | <img width="90" src="../../docs/images/resources/openstack/sharedservices/keystone.png">    |
| `openstack.sharedservices.Searchlight` | `-`   | <img width="90" src="../../docs/images/resources/openstack/sharedservices/searchlight.png"> |

### Storage

| Type                       | Alias | Image                                                                           |
|----------------------------|-------|---------------------------------------------------------------------------------|
| `openstack.storage.Cinder` | `-`   | <img width="90" src="../../docs/images/resources/openstack/storage/cinder.png"> |
| `openstack.storage.Manila` | `-`   | <img width="90" src="../../docs/images/resources/openstack/storage/manila.png"> |
| `openstack.storage.Swift`  | `-`   | <img width="90" src="../../docs/images/resources/openstack/storage/swift.png">  |

### User

| Type                             | Alias                            | Image                                                                                 |
|----------------------------------|----------------------------------|---------------------------------------------------------------------------------------|
| `openstack.user.Openstackclient` | `openstack.user.OpenStackClient` | <img width="90" src="../../docs/images/resources/openstack/user/openstackclient.png"> |

### Workload Provisioning

| Type                                    | Alias | Image                                                                                        |
|-----------------------------------------|-------|----------------------------------------------------------------------------------------------|
| `openstack.workloadprovisioning.Magnum` | `-`   | <img width="90" src="../../docs/images/resources/openstack/workloadprovisioning/magnum.png"> |
| `openstack.workloadprovisioning.Sahara` | `-`   | <img width="90" src="../../docs/images/resources/openstack/workloadprovisioning/sahara.png"> |
| `openstack.workloadprovisioning.Trove`  | `-`   | <img width="90" src="../../docs/images/resources/openstack/workloadprovisioning/trove.png">  |
