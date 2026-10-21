---
title: "Stateful Kubernetes Workloads on vSphere with RKE"
date: 2020-05-01T10:10:00
slug: "stateful-kubernetes-workloads-on-vsphere-with-rke"
authors: ["Gaurav Mehta"]
image: "images/rancher_blog_stateful-workload-featured.png"
products: ["RKE1"]
tags: ["storage", "cloud"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 86409
  original_url: "https://www.suse.com/c/rancher_blog/stateful-kubernetes-workloads-on-vsphere-with-rke/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "RKE1 vSphere how-to, RKE1 EOL"
  redirect_target: "docs.rancher.com"
---

Read our free white paper: How to Build a Kubernetes Strategy[Download Now](https://more.suse.com/fy21-global-web-landing-page-how-to-build-enterprise-kubernetes-strategy)

## Introduction

Stateful workloads in Kubernetes need to be able to access persistent volumes across the cluster. Storage Classes represent different storage types in Kubernetes. A storage provisioner backs each storage class. Most commonly used cloud providers have storage provisioners, which offer different capabilities based on the underlying cloud.

There are also a wide variety of storage provisioners available to Kubernetes, based on the cloud provider in use. Some storage providers such as Portworx, Longhorn, Ceph and Local are cloud agnostic.

In this blog, we’ll look at setting up your Rancher Kubernetes Engine (RKE) Kubernetes cluster running on VMware vSphere ready for stateful workloads. The CPI/CSI manifests are upstream VMware vSphere manifests, which have a few minor tweaks to factor in how RKE applies custom taints and run the various components making Kubernetes. VMware vSphere provides the persistent volumes for this workload.

## Background: Types of Cloud Providers

Kubernetes allows native integration with a wide variety of cloud providers. There are two types of cloud providers:

- in-tree cloud providers (providers we develop and release in the main Kubernetes repository)
- out-of-tree cloud providers (providers that can be developed, built and released independent of Kubernetes core)

Originally, kube-controller-manager handled the implementation of cloud-provider control loops. This meant that changes to cloud providers were coupled with Kubernetes.

Kubernetes v1.6 introduced a component called cloud-controller-manager to offload the cloud management control loops from kube-controller-manager. The idea was to decouple cloud provider logic from core Kubernetes and allow cloud providers to write their own out-of-tree cloud providers, which implemented the Cloud Provider Interface (CPI).

Similarly, Storage Classes perform storage management. Traditionally, in-tree volume plugins managed volume provisioning. Kubernetes introduced the concept of Container Storage Interface (CSI) in v1.9 as Alpha. This reached GA in v1.13. Using CSI, third-party vendors can write volume plugins that can be deployed and managed outside the Kubernetes lifecycle.

VMware introduced its out-of-tree CPI/CSI in May 2019, which allows users to decouple cloud management capabilities from underlying Kubernetes.

## Prerequisites

- VMware environment with vCenter 6.7U3+, ESXi v6.7.0+
- Kubernetes cluster provisioned using RKE. Kubernetes version 1.14+
- Virtual machines with hardware version 15 or later.
- vmtools on each virtual machine.

## How To Set Up vSphere on RKE

We will look at setting up the VMware vSphere CPI/CSI on an RKE provisioned Kubernetes cluster.

The process for setting up the CPI/CSI on an RKE managed cluster is as follows:

**1. Additions to RKE cluster.yml**

We need to provision the RKE cluster with cloud-provider set to external.

In addition, we need to add the the extra volume mount for the VMware vSphere CSI plugin to the extra\_binds on the kubelet.

The sample config should look something like this:

```
kubelet:
    extra_binds:
    - /var/lib/csi/sockets/pluginproxy/csi.vsphere.vmware.com:/var/lib/csi/sockets/pluginproxy/csi.vsphere.vmware.com:rshared
    - /csi:/csi:rshared
    extra_args:
    cloud-provider: external
```

**2. Handling extra taint toleration**

RKE already taints the Master nodes with the following taints:

```
node-role.kubernetes.io/controlplane=true:NoSchedule
```

```
node-role.kubernetes.io/etcd=true:NoExecute
```

If you are running dedicated nodes for etcd, please tweak the taint toleration accordingly.

**3. Setup CPI conf and secrets**

CPI setup is mandatory before using CSI.

- Create the vsphere-cpi.conf for setting up the CPI.

```
tee $HOME/cpi-vsphere.conf > /dev/null <<EOF
[Global]
port = "443"
insecure-flag = "true" #Optional. Please tweak based on setup.
secret-name = "cpi-global-secret"
secret-namespace = "kube-system"
[VirtualCenter "vc.domain.com"]
datacenters = "dc1"
EOF
```

- Create a configmap from this file

```
kubectl create configmap cloud-config --from-file=$HOME/cpi-vsphere.conf --namespace=kube-system
```

- Verify that configmap exists

`kubectl get cm cloud-config -n kube-system`

- Create a CPI secret

```
tee $HOME/cpi-secret.conf > /dev/null <<EOF
apiVersion: v1
kind: Secret
metadata:
  name: cpi-global-secret
  namespace: kube-system
stringData:
  vc.domain.com.username: "USERNAME"
  vc.domain.com.password: "PASSWORD"
EOF
```

- Create the secret

```
kubectl create -f $HOME/cpi-secret.conf
```

- Verify the secret was created

```
kubectl get secret cpi-global-secret -n kube-system
```

*Users can now remove the cpi-secret.conf file*

**4. Deploy CPI manifests**

Deploy the RBAC manifests for CPI.

```
kubectl apply -f https://raw.githubusercontent.com/kubernetes/cloud-provider-vsphere/master/manifests/controller-manager/cloud-controller-manager-roles.yaml
kubectl apply -f https://raw.githubusercontent.com/kubernetes/cloud-provider-vsphere/master/manifests/controller-manager/cloud-controller-manager-role-bindings.yaml
```

The CPI manifest needs a few minor tweaks to allow it to handle the RKE taints:

```
tee $HOME/cloud-provider.yaml > /dev/null <<EOF
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: cloud-controller-manager
  namespace: kube-system
---
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: vsphere-cloud-controller-manager
  namespace: kube-system
  labels:
    k8s-app: vsphere-cloud-controller-manager
spec:
  selector:
    matchLabels:
      k8s-app: vsphere-cloud-controller-manager
  updateStrategy:
    type: RollingUpdate
  template:
    metadata:
      labels:
        k8s-app: vsphere-cloud-controller-manager
    spec:
      nodeSelector:
        node-role.kubernetes.io/controlplane: "true"
      securityContext:
        runAsUser: 0
      tolerations:
      - key: node.cloudprovider.kubernetes.io/uninitialized
        value: "true"
        effect: NoSchedule
      - key: node-role.kubernetes.io/controlplane
        value: "true"
        effect: NoSchedule
      - key: node-role.kubernetes.io/etcd
        value: "true"
        effect: NoExecute
      serviceAccountName: cloud-controller-manager
      containers:
        - name: vsphere-cloud-controller-manager
          image: gcr.io/cloud-provider-vsphere/cpi/release/manager:latest
          args:
            - --v=2
            - --cloud-provider=vsphere
            - --cloud-config=/etc/cloud/cpi-vsphere.conf
          volumeMounts:
            - mountPath: /etc/cloud
              name: vsphere-config-volume
              readOnly: true
          resources:
            requests:
              cpu: 200m
      hostNetwork: true
      volumes:
      - name: vsphere-config-volume
        configMap:
          name: cloud-config
---
apiVersion: v1
kind: Service
metadata:
  labels:
    component: cloud-controller-manager
  name: vsphere-cloud-controller-manager
  namespace: kube-system
spec:
  type: NodePort
  ports:
    - port: 43001
      protocol: TCP
      targetPort: 43001
  selector:
    component: cloud-controller-manager
---
EOF
```

Apply this manifest

```
kubectl apply -f $HOME/cloud-provider.yaml
```

Once this is complete, we should see the vsphere-cloud-controller-manager pod in the kube-system namespace.

**5. Setup CSI secrets**

- Create the vsphere.conf file to create the secrets

```
tee $HOME/csi-vsphere.conf >/dev/null <<EOF
[Global]
cluster-id = "dc1-$unique-cluster-id-from-vcenter"
[VirtualCenter "vc.domain.com"]
insecure-flag = "true"
user = "username"
password = "password"
port = "443"
datacenters = "dc1"
EOF
```

- Create the credential secret

```
kubectl create secret generic vsphere-config-secret --from-file=$HOME/csi-vsphere.conf --namespace=kube-system
```

- Verify the secret

```
kubectl get secret vsphere-config-secret -n kube-ssytem
```

Now you can remove the csi-vsphere.conf.

**6. Setting up CSI manifests**

- Set up RBAC for CSI provider:

```
tee csi-driver-rbac.yaml >/dev/null <<EOF
kind: ServiceAccount
apiVersion: v1
metadata:
  name: vsphere-csi-controller
  namespace: kube-system
---
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: vsphere-csi-controller-role
rules:
  - apiGroups: [""]
    resources: ["secrets"]
    verbs: ["get", "list", "watch"]
  - apiGroups: ["storage.k8s.io"]
    resources: ["csidrivers"]
    verbs: ["create", "delete"]
  - apiGroups: [""]
    resources: ["nodes"]
    verbs: ["get", "list", "watch"]
  - apiGroups: [""]
    resources: ["persistentvolumes"]
    verbs: ["get", "list", "watch", "update", "create", "delete"]
  - apiGroups: ["storage.k8s.io"]
    resources: ["csinodes"]
    verbs: ["get", "list", "watch"]
  - apiGroups: ["storage.k8s.io"]
    resources: ["volumeattachments"]
    verbs: ["get", "list", "watch", "update"]
  - apiGroups: [""]
    resources: ["persistentvolumeclaims"]
    verbs: ["get", "list", "watch", "update"]
  - apiGroups: ["storage.k8s.io"]
    resources: ["storageclasses"]
    verbs: ["get", "list", "watch"]
  - apiGroups: [""]
    resources: ["events"]
    verbs: ["list", "watch", "create", "update", "patch"]
  - apiGroups: ["snapshot.storage.k8s.io"]
    resources: ["volumesnapshots"]
    verbs: ["get", "list"]
  - apiGroups: ["snapshot.storage.k8s.io"]
    resources: ["volumesnapshotcontents"]
    verbs: ["get", "list"]
  - apiGroups: [""]
    resources: ["pods"]
    verbs: ["get", "list", "watch"]
---
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: vsphere-csi-controller-binding
subjects:
  - kind: ServiceAccount
    name: vsphere-csi-controller
    namespace: kube-system
roleRef:
  kind: ClusterRole
  name: vsphere-csi-controller-role
  apiGroup: rbac.authorization.k8s.io
---
EOF
```

- Apply the manifest to the cluster

kubectl apply -f csi-driver-rbac.yaml

- Install the CSI controller
  This involves deploying the controller and node drivers.
  Copy the following content to a csi-controller.yaml

```
kind: StatefulSet
apiVersion: apps/v1
metadata:
  name: vsphere-csi-controller
  namespace: kube-system
spec:
  serviceName: vsphere-csi-controller
  replicas: 1
  updateStrategy:
    type: "RollingUpdate"
  selector:
    matchLabels:
      app: vsphere-csi-controller
  template:
    metadata:
      labels:
        app: vsphere-csi-controller
        role: vsphere-csi
    spec:
      serviceAccountName: vsphere-csi-controller
      nodeSelector:
        node-role.kubernetes.io/controlplane: "true"
      tolerations:
        - key: node-role.kubernetes.io/controlplane
          value: "true"
          effect: NoSchedule
        - key: node-role.kubernetes.io/etcd
          value: "true"
          effect: NoExecute
      dnsPolicy: "Default"
      containers:
        - name: csi-attacher
          image: quay.io/k8scsi/csi-attacher:v1.1.1
          args:
            - "--v=4"
            - "--timeout=300s"
            - "--csi-address=$(ADDRESS)"
          env:
            - name: ADDRESS
              value: /csi/csi.sock
          volumeMounts:
            - mountPath: /csi
              name: socket-dir
        - name: vsphere-csi-controller
          image: gcr.io/cloud-provider-vsphere/csi/release/driver:v1.0.1
          lifecycle:
            preStop:
              exec:
                command: ["/bin/sh", "-c", "rm -rf /var/lib/csi/sockets/pluginproxy/csi.vsphere.vmware.com"]
          args:
            - "--v=4"
          imagePullPolicy: "Always"
          env:
            - name: CSI_ENDPOINT
              value: unix:///var/lib/csi/sockets/pluginproxy/csi.sock
            - name: X_CSI_MODE
              value: "controller"
            - name: VSPHERE_CSI_CONFIG
              value: "/etc/cloud/csi-vsphere.conf"
          volumeMounts:
            - mountPath: /etc/cloud
              name: vsphere-config-volume
              readOnly: true
            - mountPath: /var/lib/csi/sockets/pluginproxy/
              name: socket-dir
          ports:
            - name: healthz
              containerPort: 9808
              protocol: TCP
          livenessProbe:
            httpGet:
              path: /healthz
              port: healthz
            initialDelaySeconds: 10
            timeoutSeconds: 3
            periodSeconds: 5
            failureThreshold: 3
        - name: liveness-probe
          image: quay.io/k8scsi/livenessprobe:v1.1.0
          args:
            - "--csi-address=$(ADDRESS)"
          env:
            - name: ADDRESS
              value: /var/lib/csi/sockets/pluginproxy/csi.sock
          volumeMounts:
            - mountPath: /var/lib/csi/sockets/pluginproxy/
              name: socket-dir
        - name: vsphere-syncer
          image: gcr.io/cloud-provider-vsphere/csi/release/syncer:v1.0.1
          args:
            - "--v=2"
          imagePullPolicy: "Always"
          env:
            - name: FULL_SYNC_INTERVAL_MINUTES
              value: "30"
            - name: VSPHERE_CSI_CONFIG
              value: "/etc/cloud/csi-vsphere.conf"
          volumeMounts:
            - mountPath: /etc/cloud
              name: vsphere-config-volume
              readOnly: true
        - name: csi-provisioner
          image: quay.io/k8scsi/csi-provisioner:v1.2.2
          args:
            - "--v=4"
            - "--timeout=300s"
            - "--csi-address=$(ADDRESS)"
            - "--feature-gates=Topology=true"
            - "--strict-topology"
          env:
            - name: ADDRESS
              value: /csi/csi.sock
          volumeMounts:
            - mountPath: /csi
              name: socket-dir
      volumes:
        - name: vsphere-config-volume
          secret:
            secretName: vsphere-config-secret
        - name: socket-dir
          hostPath:
            path: /var/lib/csi/sockets/pluginproxy/csi.vsphere.vmware.com
            type: DirectoryOrCreate
---
apiVersion: storage.k8s.io/v1beta1
kind: CSIDriver
metadata:
  name: csi.vsphere.vmware.com
spec:
  attachRequired: true
  podInfoOnMount: false
```

Apply the manifest:

```
kubectl create -f csi-controller.yaml
```

- Install the CSI node driver

Copy the following content to a csi-driver.yaml file:

```
kind: DaemonSet
apiVersion: apps/v1
metadata:
  name: vsphere-csi-node
  namespace: kube-system
spec:
  selector:
    matchLabels:
      app: vsphere-csi-node
  updateStrategy:
    type: "RollingUpdate"
  template:
    metadata:
      labels:
        app: vsphere-csi-node
        role: vsphere-csi
    spec:
      dnsPolicy: "Default"
      containers:
        - name: node-driver-registrar
          image: quay.io/k8scsi/csi-node-driver-registrar:v1.1.0
          lifecycle:
            preStop:
              exec:
                command: ["/bin/sh", "-c", "rm -rf /registration/csi.vsphere.vmware.com /var/lib/kubelet/plugins_registry/csi.vsphere.vmware.com /var/lib/kubelet/plugins_registry/csi.vsphere.vmware.com-reg.sock"]
          args:
            - "--v=5"
            - "--csi-address=$(ADDRESS)"
            - "--kubelet-registration-path=$(DRIVER_REG_SOCK_PATH)"
          env:
            - name: ADDRESS
              value: /csi/csi.sock
            - name: DRIVER_REG_SOCK_PATH
              value: /var/lib/kubelet/plugins_registry/csi.vsphere.vmware.com/csi.sock
          securityContext:
            privileged: true
          volumeMounts:
            - name: plugin-dir
              mountPath: /csi
            - name: registration-dir
              mountPath: /registration
        - name: vsphere-csi-node
          image: gcr.io/cloud-provider-vsphere/csi/release/driver:v1.0.1
          imagePullPolicy: "Always"
          env:
            - name: NODE_NAME
              valueFrom:
                fieldRef:
                  fieldPath: spec.nodeName
            - name: CSI_ENDPOINT
              value: unix:///csi/csi.sock
            - name: X_CSI_MODE
              value: "node"
            - name: X_CSI_SPEC_REQ_VALIDATION
              value: "false"
            - name: VSPHERE_CSI_CONFIG
              value: "/etc/cloud/csi-vsphere.conf" # here csi-vsphere.conf is the name of the file used for creating secret using "--from-file" flag
          args:
            - "--v=4"
          securityContext:
            privileged: true
            capabilities:
              add: ["SYS_ADMIN"]
            allowPrivilegeEscalation: true
          volumeMounts:
            - name: vsphere-config-volume
              mountPath: /etc/cloud
              readOnly: true
            - name: plugin-dir
              mountPath: /csi
            - name: pods-mount-dir
              mountPath: /var/lib/kubelet
              # needed so that any mounts setup inside this container are
              # propagated back to the host machine.
              mountPropagation: "Bidirectional"
            - name: device-dir
              mountPath: /dev
          ports:
            - name: healthz
              containerPort: 9808
              protocol: TCP
          livenessProbe:
            httpGet:
              path: /healthz
              port: healthz
            initialDelaySeconds: 10
            timeoutSeconds: 3
            periodSeconds: 5
            failureThreshold: 3
        - name: liveness-probe
          image: quay.io/k8scsi/livenessprobe:v1.1.0
          args:
            - "--csi-address=$(ADDRESS)"
          env:
            - name: ADDRESS
              value: /csi/csi.sock
          volumeMounts:
            - name: plugin-dir
              mountPath: /csi
      volumes:
        - name: vsphere-config-volume
          secret:
            secretName: vsphere-config-secret
        - name: registration-dir
          hostPath:
            path: /var/lib/kubelet/plugins_registry
            type: DirectoryOrCreate
        - name: plugin-dir
          hostPath:
            path: /var/lib/kubelet/plugins_registry/csi.vsphere.vmware.com
            type: DirectoryOrCreate
        - name: pods-mount-dir
          hostPath:
            path: /var/lib/kubelet
            type: Directory
        - name: device-dir
          hostPath:
            path: /dev
```

Apply the manifest

```
kubectl apply -f csi-driver.yaml
```

- Verify that the components are deployed

Check csi daemonset pods are running and the CSINode CRD’s are set up

```
▶ kubectl get CSINode
NAME              CREATED AT
gm-csi-worker-1   2020-01-16T05:24:38Z
gm-csi-worker-2   2020-01-16T05:24:40Z
gm-csi-worker-3   2020-01-16T05:24:38Z
```

**7. Set up a storage class**

The sample manifest defines the storage class, where datastore url is the uuid for the datastore that can be referenced from vCenter.

```
tee storage-class.yaml > /dev/null <<EOF
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: vsphere-csi
  annotations:
    storageclass.kubernetes.io/is-default-class: "true"
provisioner: csi.vsphere.vmware.com
parameters:
  fstype: ext4
  DatastoreURL: "ds:///vmfs/volumes/5c59dcb0-c26630e3-3ae6-b8ca3aeefe3f/"
EOF
```

Apply this storage class

```
kubectl apply -f storage-class.yaml
```

## Conclusion

After performing these steps, you should be able to provision persistent volumes on VMware vSphere using the newly created Storage Class.

Now, persistent volume requests will not be managed by the out-of-tree CPI/CSI provider.

Read our free white paper: How to Build a Kubernetes Strategy[Download Now](https://more.suse.com/fy21-global-web-landing-page-how-to-build-enterprise-kubernetes-strategy)
