## Kubernetes

Table of Content:

* [Chaos](#chaos)
* [ClusterConfig](#clusterconfig)
* [Compute](#compute)
* [Control Plane](#control-plane)
* [Ecosystem](#ecosystem)
* [Group](#group)
* [Infra](#infra)
* [Network](#network)
* [Others](#others)
* [PodConfig](#podconfig)
* [RBAC](#rbac)
* [Storage](#storage)

### Chaos

| Type                    | Alias | Image                                                                         |
|-------------------------|-------|-------------------------------------------------------------------------------|
| `k8s.chaos.ChaosMesh`   | `-`   | <img width="90" src="../../docs/images/resources/k8s/chaos/chaos-mesh.png">   |
| `k8s.chaos.LitmusChaos` | `-`   | <img width="90" src="../../docs/images/resources/k8s/chaos/litmus-chaos.png"> |

### ClusterConfig

| Type                       | Alias                                       | Image                                                                           |
|----------------------------|---------------------------------------------|---------------------------------------------------------------------------------|
| `k8s.clusterconfig.HPA`    | `k8s.clusterconfig.HorizontalPodAutoscaler` | <img width="90" src="../../docs/images/resources/k8s/clusterconfig/hpa.png">    |
| `k8s.clusterconfig.Limits` | `k8s.clusterconfig.LimitRange`              | <img width="90" src="../../docs/images/resources/k8s/clusterconfig/limits.png"> |
| `k8s.clusterconfig.Quota`  | `-`                                         | <img width="90" src="../../docs/images/resources/k8s/clusterconfig/quota.png">  |

### Compute

| Type                  | Alias                     | Image                                                                      |
|-----------------------|---------------------------|----------------------------------------------------------------------------|
| `k8s.compute.Cronjob` | `-`                       | <img width="90" src="../../docs/images/resources/k8s/compute/cronjob.png"> |
| `k8s.compute.Deploy`  | `k8s.compute.Deployment`  | <img width="90" src="../../docs/images/resources/k8s/compute/deploy.png">  |
| `k8s.compute.DS`      | `k8s.compute.DaemonSet`   | <img width="90" src="../../docs/images/resources/k8s/compute/ds.png">      |
| `k8s.compute.Job`     | `-`                       | <img width="90" src="../../docs/images/resources/k8s/compute/job.png">     |
| `k8s.compute.Pod`     | `-`                       | <img width="90" src="../../docs/images/resources/k8s/compute/pod.png">     |
| `k8s.compute.RS`      | `k8s.compute.ReplicaSet`  | <img width="90" src="../../docs/images/resources/k8s/compute/rs.png">      |
| `k8s.compute.STS`     | `k8s.compute.StatefulSet` | <img width="90" src="../../docs/images/resources/k8s/compute/sts.png">     |

### Control Plane

| Type                       | Alias                                | Image                                                                           |
|----------------------------|--------------------------------------|---------------------------------------------------------------------------------|
| `k8s.controlplane.API`     | `k8s.controlplane.APIServer`         | <img width="90" src="../../docs/images/resources/k8s/controlplane/api.png">     |
| `k8s.controlplane.CCM`     | `-`                                  | <img width="90" src="../../docs/images/resources/k8s/controlplane/c-c-m.png">   |
| `k8s.controlplane.CM`      | `k8s.controlplane.ControllerManager` | <img width="90" src="../../docs/images/resources/k8s/controlplane/c-m.png">     |
| `k8s.controlplane.KProxy`  | `k8s.controlplane.KubeProxy`         | <img width="90" src="../../docs/images/resources/k8s/controlplane/k-proxy.png"> |
| `k8s.controlplane.Kubelet` | `-`                                  | <img width="90" src="../../docs/images/resources/k8s/controlplane/kubelet.png"> |
| `k8s.controlplane.Sched`   | `k8s.controlplane.Scheduler`         | <img width="90" src="../../docs/images/resources/k8s/controlplane/sched.png">   |

### Ecosystem

| Type                        | Alias | Image                                                                             |
|-----------------------------|-------|-----------------------------------------------------------------------------------|
| `k8s.ecosystem.ExternalDns` | `-`   | <img width="90" src="../../docs/images/resources/k8s/ecosystem/external-dns.png"> |
| `k8s.ecosystem.Helm`        | `-`   | <img width="90" src="../../docs/images/resources/k8s/ecosystem/helm.png">         |
| `k8s.ecosystem.Krew`        | `-`   | <img width="90" src="../../docs/images/resources/k8s/ecosystem/krew.png">         |
| `k8s.ecosystem.Kustomize`   | `-`   | <img width="90" src="../../docs/images/resources/k8s/ecosystem/kustomize.png">    |

### Group

| Type           | Alias                 | Image                                                               |
|----------------|-----------------------|---------------------------------------------------------------------|
| `k8s.group.NS` | `k8s.group.Namespace` | <img width="90" src="../../docs/images/resources/k8s/group/ns.png"> |

### Infra

| Type               | Alias | Image                                                                   |
|--------------------|-------|-------------------------------------------------------------------------|
| `k8s.infra.ETCD`   | `-`   | <img width="90" src="../../docs/images/resources/k8s/infra/etcd.png">   |
| `k8s.infra.Master` | `-`   | <img width="90" src="../../docs/images/resources/k8s/infra/master.png"> |
| `k8s.infra.Node`   | `-`   | <img width="90" src="../../docs/images/resources/k8s/infra/node.png">   |

### Network

| Type                 | Alias                       | Image                                                                     |
|----------------------|-----------------------------|---------------------------------------------------------------------------|
| `k8s.network.Ep`     | `k8s.network.Endpoint`      | <img width="90" src="../../docs/images/resources/k8s/network/ep.png">     |
| `k8s.network.Ing`    | `k8s.network.Ingress`       | <img width="90" src="../../docs/images/resources/k8s/network/ing.png">    |
| `k8s.network.Netpol` | `k8s.network.NetworkPolicy` | <img width="90" src="../../docs/images/resources/k8s/network/netpol.png"> |
| `k8s.network.SVC`    | `k8s.network.Service`       | <img width="90" src="../../docs/images/resources/k8s/network/svc.png">    |

### Others

| Type             | Alias | Image                                                                 |
|------------------|-------|-----------------------------------------------------------------------|
| `k8s.others.CRD` | `-`   | <img width="90" src="../../docs/images/resources/k8s/others/crd.png"> |
| `k8s.others.PSP` | `-`   | <img width="90" src="../../docs/images/resources/k8s/others/psp.png"> |

### PodConfig

| Type                   | Alias                     | Image                                                                       |
|------------------------|---------------------------|-----------------------------------------------------------------------------|
| `k8s.podconfig.CM`     | `k8s.podconfig.ConfigMap` | <img width="90" src="../../docs/images/resources/k8s/podconfig/cm.png">     |
| `k8s.podconfig.Secret` | `-`                       | <img width="90" src="../../docs/images/resources/k8s/podconfig/secret.png"> |

### RBAC

| Type             | Alias                         | Image                                                                  |
|------------------|-------------------------------|------------------------------------------------------------------------|
| `k8s.rbac.CRole` | `k8s.rbac.ClusterRole`        | <img width="90" src="../../docs/images/resources/k8s/rbac/c-role.png"> |
| `k8s.rbac.CRB`   | `k8s.rbac.ClusterRoleBinding` | <img width="90" src="../../docs/images/resources/k8s/rbac/crb.png">    |
| `k8s.rbac.Group` | `-`                           | <img width="90" src="../../docs/images/resources/k8s/rbac/group.png">  |
| `k8s.rbac.RB`    | `k8s.rbac.RoleBinding`        | <img width="90" src="../../docs/images/resources/k8s/rbac/rb.png">     |
| `k8s.rbac.Role`  | `-`                           | <img width="90" src="../../docs/images/resources/k8s/rbac/role.png">   |
| `k8s.rbac.SA`    | `k8s.rbac.ServiceAccount`     | <img width="90" src="../../docs/images/resources/k8s/rbac/sa.png">     |
| `k8s.rbac.User`  | `-`                           | <img width="90" src="../../docs/images/resources/k8s/rbac/user.png">   |

### Storage

| Type              | Alias                               | Image                                                                  |
|-------------------|-------------------------------------|------------------------------------------------------------------------|
| `k8s.storage.PV`  | `k8s.storage.PersistentVolume`      | <img width="90" src="../../docs/images/resources/k8s/storage/pv.png">  |
| `k8s.storage.PVC` | `k8s.storage.PersistentVolumeClaim` | <img width="90" src="../../docs/images/resources/k8s/storage/pvc.png"> |
| `k8s.storage.SC`  | `k8s.storage.StorageClass`          | <img width="90" src="../../docs/images/resources/k8s/storage/sc.png">  |
| `k8s.storage.Vol` | `k8s.storage.Volume`                | <img width="90" src="../../docs/images/resources/k8s/storage/vol.png"> |
