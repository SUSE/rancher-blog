---
title: "Project Longhorn Now Available on Kubernetes"
date: 2018-03-27T11:13:00
slug: "project-longhorn-now-available-on-kubernetes"
author: "Rancher Admin"
products: ["Longhorn"]
tags: ["storage"]
content_type: "release"
draft: false
migration:
  wp_id: 86867
  original_url: "https://www.suse.com/c/rancher_blog/project-longhorn-now-available-on-kubernetes/"
  disposition: migrate
  commercial: false
  outdated_reason: "Longhorn v0.2 early announcement"
  redirect_target: ""
---

Take a Deep dive into Date Storage Options for Kubernetes and Rancher 2.0Without the ability to persist data, containers might seem to have limited use in many workloads. Join Rancher Labs for a deep dive into storage solutions for Docker containers and Kubernetes as we discuss best practices for a wide variety of storage use cases.[Watch the Training](https://rancher.com/events/2018/2018-09-18-building-data-storage-solution-with-k8s/)

[![](images/rancher_blog_project-longhorn-logo-blue-1-300x87.png)](https://cdn.rancher.com/wp-content/uploads/2018/03/26212907/project-longhorn-logo-blue-1.png)Since we announced Project Longhorn [last year](https://rancher.com/microservices-block-storage/), there has been a great deal of interest in running Longhorn storage on a Kubernetes cluster.

Today, I am very excited to announce the availability of Project Longhorn v0.2, which is a persistent storage implementation for any Kubernetes cluster. Once deployed on a Kubernetes cluster, Longhorn automatically clusters all available local storage from all the nodes in the cluster to form replicated and distributed block storage. You can perform snapshot and backup operations on Longhorn volumes, and they will be synchronously replicated onto multiple nodes. We have ported Longhorn Manager to work as a Kubernetes controller. All Longhorn states are stored as Custom Resource Definitions (CRDs). There’s no need for a separate etcd server for Longhorn. Longhorn Manager exposes APIs to perform Longhorn volume operations and snapshot/backup operations, which would be used by the Longhorn UI and Kubernetes Flexvolume driver during the operation.

Run this one command to deploy the whole Longhorn storage system on your Kubernetes cluster.

```
kubectl create -f https://raw.githubusercontent.com/rancher/longhorn/v0.2/deploy/longhorn.yaml
```

(for GKE, see [here](https://github.com/rancher/longhorn/blob/master/README.md#google-kubernetes-engine)) After deployment, you can use the UI by looking into Kubernetes services to find the proper IP: `kubectl -n longhorn-system get svc`

```
  NAME                TYPE           CLUSTER-IP      EXTERNAL-IP      PORT(S)        AGE
  longhorn-backend    ClusterIP      10.20.248.250   <none>           9500/TCP       58m
  longhorn-frontend   LoadBalancer   10.20.245.110   100.200.200.123   80:12345/TCP   58m
```

So now you can access the UI using `100.200.200.123`, or `<node_ip>:12345`. Longhorn provides full integration with Kubernetes. You can create a pod with a volume backing by Longhorn like this.

```
apiVersion: v1
kind: Pod
metadata:
  name: volume-test
  namespace: default
spec:
  containers:
  - name: volume-test
    image: nginx:stable-alpine
    imagePullPolicy: IfNotPresent
    volumeMounts:
    - name: voll
      mountPath: /data
    ports:
    - containerPort: 80
  volumes:
  - name: voll
    flexVolume:
      driver: "rancher.io/longhorn"
      fsType: "ext4"
      options:
        size: "2Gi"
        numberOfReplicas: "3"
        staleReplicaTimeout: "20"
        fromBackup: ""
```

Longhorn also supports dynamic provisioner. For example, you can define a StorageClass in Kubernetes like this:

```
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: longhorn
provisioner: rancher.io/longhorn
parameters:
  numberOfReplicas: "3"
  staleReplicaTimeout: "30"
  fromBackup: ""
```

Then create a PVC and use it with a Pod:

```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: longhorn-volv-pvc
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: longhorn
  resources:
    requests:
      storage: 2Gi
---
apiVersion: v1
kind: Pod
metadata:
  name: volume-test
  namespace: default
spec:
  containers:
  - name: volume-test
    image: nginx:stable-alpine
    imagePullPolicy: IfNotPresent
    volumeMounts:
    - name: volv
      mountPath: /data
    ports:
    - containerPort: 80
  volumes:
  - name: volv
    persistentVolumeClaim:
      claimName: longhorn-volv-pvc
```

**Want expert guidance on Longhorn? Sign up for a demo.**

[![Schedule a Demo](https://no-cache.hubspot.com/cta/default/468859/aa0477dc-3583-4bf0-ab24-5c008977aa82.png)](https://cta-redirect.hubspot.com/cta/redirect/468859/aa0477dc-3583-4bf0-ab24-5c008977aa82)

Longhorn is a 100% open-source project. To this day, it’s still a work in progress. We appreciate your comments as we continue to work on it!

If you find any bugs or have advice, feel free to contact us through [GitHub issues](https://github.com/rancher/longhorn/issues) or join the [forum](https://forums.rancher.com/) to discuss the project.

[![Sheng Yang](images/rancher_blog_sheng-yang-150x150.jpg)](https://cdn.rancher.com/wp-content/uploads/2018/03/26214349/sheng-yang.jpg)

### Sheng Yang

Twitter: @yasker

Github: https://github.com/yasker

Take a Deep dive into Date Storage Options for Kubernetes and Rancher 2.0Without the ability to persist data, containers might seem to have limited use in many workloads. Join Rancher Labs for a deep dive into storage solutions for Docker containers and Kubernetes as we discuss best practices for a wide variety of storage use cases.[Watch the Training](https://rancher.com/events/2018/2018-09-18-building-data-storage-solution-with-k8s/)
