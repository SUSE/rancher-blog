---
title: "Creating Microservices Deployments on Kubernetes with Rancher - Part 2"
date: 2016-09-22T10:18:00
slug: "creating-microservices-deployments-on-kubernetes-with-rancher-part-2"
author: "Rancher Admin"
products: ["Kubernetes (generic)"]
tags: ["storage"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 86663
  original_url: "https://www.suse.com/c/rancher_blog/creating-microservices-deployments-on-kubernetes-with-rancher-part-2/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Kubernetes 2016 with Rancher 1.x"
  redirect_target: "rancher.com/blog (hub)"
---

In a [previous
article](https://rancher.com/getting-micro-services-production-kubernetes/)
in this series we looked at the basic
[Kubernetes](https://rancher.com/kubernetes) concepts including
namespaces, pods, deployments and services. Now we will use these
building blocks in a realistic deployment. We will cover how to setup
persistent volumes, how to setup claims for those volumes and then mount
those claims into pods. We will also look at creating and using secrets
using the Kubernetes secrets management system. Lastly, we will look at
service discovery within the cluster as well as exposing services to the
outside world.

## Sample Application

We will be using
[go-auth](https://github.com/usmanismail/go-messenger/tree/master/go-auth)
as a sample application to illustrate the features of Kubernetes. If you
have gone through our [Docker
CI/CD](https://info.rancher.com/cicd-with-docker-ebook) series of
articles then you will be familiar with the application. It is a simple
authentication service consisting of an array of stateless web-servers
and a database cluster. Creating a database inside Kubernetes is
nontrivial as the ephemeral nature of containers conflicts with the
persistent storage requirements of databases.

## Persistent Volumes

Prior to launching our go-auth application we must setup a database for
it to connect to. Prior setting up a database server in Kubernetes we
must provide it with a persistent storage volume. This will help in
making database state persistent across database restarts, and in
migrating storage when containers are moved from one host to another.
The list of currently supported persistent volume types are listed
below:

- GCEPersistentDisk
- AWSElasticBlockStore
- AzureFile
- FC (Fibre Channel)
- NFS
- iSCSI
- RBD (Ceph Block Device)
- CephFS
- Cinder (OpenStack block storage)
- Glusterfs
- VsphereVolume
- HostPath (Testing only will not work in multihost clusters)

We are going to use NFS-based volumes, as NFS is ubiquitous in network
storage systems. If you do not have an NFS server handy, you may want to
use [Amazon Elastic File Store](https://aws.amazon.com/efs/) to quickly
setup a mountable NFS volume. Once you have your NFS volume (or EFS
volume) you can setup a persistent volume in Kubernetes using the
following spec. We specify the hostname or IP of our NFS/EFS server, 1
GB of storage with read, write many access mode.

```
apiVersion: v1
kind: PersistentVolume
metadata:
  name: mysql-volume
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteMany
  nfs:
    server: us-east-1a.fs-f604cbbf.efs.us-east-1.amazonaws.com
    path: "/"
```

Once you create your volume using \*kubectl create -f
persistent-volume.yaml, \*you can use the following command to list your
newly created volume:

```
$kubectl get pv
NAME                CAPACITY   ACCESSMODES   STATUS      CLAIM     REASON    AGE
mysql-volume          1Gi         RWX      Available                         29s
```

## Persistent Volume Claim

Now that we have our volume, we can create a *Persistent Volume Claim*
using the spec below. A persistent volume claim will reserve our
persistent volume, and can then be mounted into a container volume. The
specifications we provide for our claim are used to match available
persistent volumes and bind them if found. For example, we specified
that we only want a ReadWriteMany volume with at least 1 GB of storage
available:

```
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: mysql-claim
spec:
  accessModes:
  - ReadWriteMany
  resources:
    requests:
      storage: 1Gi
```

We can see if our claim was able to bind to a volume using the command
shown below:

```
$kubectl get pvc
NAME          STATUS    VOLUME    CAPACITY   ACCESSMODES   AGE
mysql-claim   Bound     nfs       1Gi       RWX           13s
```

## Secrets Management

Before we start using our persistent volume and claim in a MySQL
container we also need to figure out how to get a secret such as
database password into Kubernetes Pods. Luckily, Kubernetes provides a
[secrets management
system](http://kubernetes.io/docs/user-guide/secrets/) for this purpose.
To create a managed secret for Database password, create a file called
password.txt and add your plain text password here. Make sure there are
no newline characters in this file as they will become part of the
secret. Once you have created your password file, use the following
command to store your secret in Kubernetes:

```
$kubectl create secret generic mysql-pass --from-file=password.txt
secret "mysql-pass" created
```

You can look at a list of all current secrets using the following
command:

```
$kubectl get secret
NAME         TYPE      DATA      AGE
mysql-pass   Opaque    1         3m
```

##

## MySQL Deployment

Now we have all the requisite pieces, we can setup our MySQL deployment
using the spec below. Some interesting things to note: in the spec, we
use the strategy *recreate,* which means that an update of the
deployment will drop all containers and create them again rather than
using a rolling deploy. This is needed because we only want one MySQL
container accessing the persistent volume. However, this also means that
there will be downtime if we redeploy our database. Secondly, we use the
*valueFrom* and *secretKeyRef* parameters to inject the secret we
created earlier into our container as an environment variable. Lastly,
note in the ports section that we can name our port and in downstream
containers we will refer to the port by its name, not its value. This
allows us to change the port in future deployments without having to
update our downstream containers.

```
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: go-auth-mysql
  labels:
    app: go-auth
spec:
  strategy:
    type: Recreate
  template:
    metadata:
      labels:
        app: go-auth
        component: mysql
    spec:
      containers:
      - image: mysql:5.6
      name: mysql
      env:
      - name: MYSQL_ROOT_PASSWORD
        valueFrom:
          secretKeyRef:
            name: mysql-pass
            key: password.txt
      ports:
      - containerPort: 3306
        name: mysql
      volumeMounts:
      - name: mysql-persistent-storage
        mountPath: /var/lib/mysql
      volumes:
      - name: mysql-persistent-storage
        persistentVolumeClaim:
          claimName: mysql-claim
```

##

## MySQL Service

Once we have a MySQL deployment we must attach a service front end to it
so that it is accessible to other services in our application. To create
a service we can use the following spec. Note that we could specify a
cluster IP in this spec if we wanted to statically link our application
layer to this database service. However, we will use the service
discovery mechanisms in Kubernetes to avoid hard-coding IPs.

```
apiVersion: v1
kind: Service
metadata:
  name: go-auth-mysql
  labels:
    app: go-auth
    component: mysql
spec:
  ports:
  - port: 3306
  selector:
    app: go-auth
    component: mysql
  ClusterIP: 10.43.204.178
```

In Kubernetes, service discovery is available through Docker link style
environment variables. All services in a cluster are visible to all
containers/pod in the cluster. Kubernetes uses IP Tables rules to
redirect service requests to the Kube proxy which in turn routes to the
hosts and pods with the requisite service. For example, if you use
*kubectl exec CONTAINER\_NAME bash* into any container and run env, you
can see the service link variables as shown below. We will use this
setup to connect our go-auth web application to the database.

```
$env | grep GO_AUTH_MYSQL_SERVICE
GO_AUTH_MYSQL_SERVICE_PORT=3306
GO_AUTH_MYSQL_SERVICE_HOST=10.43.204.178
```

## Go Auth Deployment

Now that we finally have our database up and exposed, we can finally
bring up our web layer. We will use the spec shown below for our web
layer. We will be using the *usman/go-auth-kubernetes* image, which uses
an [initialization
script](https://github.com/usmanismail/go-messenger/blob/kubernetes/go-auth/run-go-auth.sh#L4-L5)
to add the database service Cluster IP to the /etc/hosts. If you use the
DNS add in Kubernetes, you can skip this step. We also use the secrets
management feature in Kubernetes to mount the mysql-pass secret into the
container. Using the the *args* parameter, we specify the db-host
argument as the mysql host we setup in /etc/hosts. In addition, we
specify *db-password-file* to so that our application connects to the
mysql cluster. We also use the livenessProbe element to monitor our web
service container. If the process has problems, Kubernetes will detect
the failure and replace the pod automatically.

\* \*

```
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: go-auth-web
spec:
  replicas: 2 # We want two pods for this deployment
  template:
    metadata:
      labels:
        app: go-auth
        component: web
    spec:
      containers:
      - name: go-auth-web
        image: usman/go-auth-kubernetes
        ports:
        - containerPort: 8080
        args:
          - "-l debug"
          - run
          - "--db-host mysql"
          - "--db-user root"
          - "--db-password-file /etc/db/password.txt"
          - "-p 8080"
        volumeMounts:
        - name: mysql-password-volume
          mountPath: "/etc/db"
          readOnly: true
        livenessProbe:
          httpGet:
            path: /
            port: 8080
          initialDelaySeconds: 30
          timeoutSeconds: 1
      volumes:
      - name: mysql-password-volume
        secret:
          secretName: mysql-pass
```

## Exposing Public Services

Now that we have setup our go-auth service, we can expose the service
with the following spec. We specify that we are using the service type
NodePort which exposes the service on a given port from Kubernetes range
(30,000-32,767) on every Kubernetes host. The host then uses the
kubeproxy to route traffic to one of the pods in the go-auth deployment.
We can now use round-robin DNS or an external loadbalancer to route
traffic to all Kubernetes nodes for fault tolerance and to spread load.

```
apiVersion: v1
kind: Service
metadata:
  name: go-auth-web
  labels:
    app: go-auth
spec:
  type: NodePort
  ports:
  - port: 8080
    nodePort: 30000
    protocol: TCP
    name: http
  selector:
    app: go-auth
    component: web
```

With our service exposed, we can use the go-auth REST API to create a
user, generate a token for the user, and verify the token using the
following commands. These commands will work even if you kill one of the
go-auth-web containers. They will also still work if you delete the
MySQL container (after a time when it gets replaced).

```
curl -i -X PUT -d userid=USERNAME 
     -d password=PASSWORD KUBERNETES_HOST:30000/user
curl 'http://KUBERNETES_HOST:30000/token?userid=USERNAME&password=PASSWORD'
curl -i -X POST 'KUBERNETES_HOST:30000/token/USERNAME' 
     --data "IHuzUHUuqCk5b5FVesX5LWBsqm8K...."
```

## Wrap up

With our services setup, we have both a persistent MySQL service and
deployment, as well as a stateless web deployment for go-auth service.
We can terminate the MySQL container and it will restart without losing
state (although there will be temporary down time). You may also mount
the same NFS volume as a read-only volume for MySQL slaves to allow
reads even if the master is down and being replaced. In future articles,
we will cover using Pet Sets and Cassandra-style application layer
replicated databases to have persistent layers which are tolerant to
failure without any downtime. For the stateless web layer we already
support failure recovery without downtime. In addition to our services
and deployments, we looked at how to manage secrets in our cluster such
that they can be exposed to the application only at run time. Lastly, we
looked at a mechanism by which services discover each other.

Kubernetes can be daunting with its plethora of terminology and
verbosity. However, if you need to run workloads in production under
load, Kubernetes provides a lot of the plumbing that you would otherwise
have to hand-roll.
