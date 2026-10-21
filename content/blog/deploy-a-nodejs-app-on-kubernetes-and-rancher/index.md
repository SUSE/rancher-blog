---
title: "Deploy a NodeJS App on Kubernetes and Rancher"
date: 2016-05-04T11:26:00
slug: "deploy-a-nodejs-app-on-kubernetes-and-rancher"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: ["developer-experience"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 87104
  original_url: "https://www.suse.com/c/rancher_blog/deploy-a-nodejs-app-on-kubernetes-and-rancher/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher 1.x Kubernetes environment, 2016"
  redirect_target: "rancher.com/blog (hub)"
---

![Kubernetes
ghost](images/rancher_blog_Kubernetes-ghost-183x300.png)Rancher recently
shipped 1.0 which [added support for the Kubernetes
orchestration](https://rancher.com/rancher-now-supports-kubernetes/)
framework. Now, you can leverage the capabilities of Kubernetes with
your Rancher environments. Kubernetes is an open-source cluster
management framework for application containers started by Google; it’s
designed to provide a simple way to deploy, schedule, scale, and roll
out new features of applications by providing a container-centric
environment without depending on the underlying infrastructure. The
native support for [Kubernetes](https://rancher.com/kubernetes/)in
Rancher gives you the ability to launch multiple Kubernetes clusters and
Rancher will take care of deploying these clusters into your
environment, also, it adds several features including:

- Node provisioning through Docker Machine.
- UI to manage Kubernetes cluster from Rancher.
- Leveraging Rancher Load balancers to route traffic to Kubernetes
  services and pods.
- One-click deployments for applications and microservices using
  Rancher catalog templates for Kubernetes.

Today I will provide an overview of using Kubernetes in Rancher by
deploying a NodeJS application on the Kubernetes environment.

### Starting Kubernetes Cluster within Rancher

After Installing Rancher platform
and adding a few hosts, you should be able to access the Rancher
environments by navigating to **Manage Environments** by clicking on the
environment name: **[![HG
1](images/rancher_blog_HG-1-1024x492.png)](https://cdn.rancher.com/wp-content/uploads/2016/03/25113209/HG-1.png)**
Click on “Add new environment,” or simply edit the current environment.
Now, you will have the option to choose between different cluster
management platforms for your hosts. The default is the Rancher native
Cattle clustering. Also, you will have two more options: Kubernetes and
Docker Swarm. After choosing Kubernetes and clicking on save, you will
notice new menu items including Kubernetes, which will provide a UI to
manage the kubernetes cluster. **[![HG
2](images/rancher_blog_HG-2-1024x510.png)](https://cdn.rancher.com/wp-content/uploads/2016/03/25113254/HG-2.png)**
Rancher will start to deploy containers to get the Kubernetes cluster
running. These containers include core functions such as etcd and the
kubernetes API server, as well as kubelets and proxys on each computing
host.: **[![HG
3](images/rancher_blog_HG-3-1024x414.png)](https://cdn.rancher.com/wp-content/uploads/2016/03/25113322/HG-3.png)**

### **KubeCTL in Rancher**

Rancher includes full access to Kubectl, which is a command line
interface to manage the Kubernetes cluster. Also, Rancher adds the
ability to generate and copy the configuration file for kubectl to add
to your own local machine: **[![HG
4](images/rancher_blog_HG-4-1024x518.png)](https://cdn.rancher.com/wp-content/uploads/2016/03/25113347/HG-4.png)**
Kubectl is installed using
[gcloud](https://cloud.google.com/container-engine/docs/before-you-begin#install_kubectl).
You can copy the configuration for kubectl and add it to
~/.kube/config, and start using kubectl from your local computer:

```
$ kubectl get nodes
NAME      LABELS    STATUS    AGE

node-1    beta.kubernetes.io/instance-type=rancher,failure-domain.alpha.kubernetes.io/region=Region1,failure-domain.alpha.kubernetes.io/zone=FailureDomain1,kubernetes.io/hostname=node-1   Ready     1h
```

### **Getting the NodeJS Application Ready**

Now that I have Kubernetes in place, I will start building my app by
creating the Docker image for the NodeJS application. I am going to use
the blogging application Ghost, which already has an official Docker
image. But, we will do minor tweaks to this image to add support for a
MySQL database. The Docker image is based on the [official ghost
image](https://hub.docker.com/_/ghost/); in addition, it
adds a custom entry point, and configuration file:

```
FROM ghost: latest

COPY docker-entrypoint.sh /entrypoint.sh

RUN chmod u+x /entrypoint.sh

COPY config-example.js /config-example.js

ENTRYPOINT ["/entrypoint.sh"]

CMD ["npm", "start", "--production"]
```

The custom configuration file for ghost will add placeholders to be
replaced with values of Ghost database and username/password:

```
database: {

client: 'mysql',

connection: {

host     : 'mysql',

user     : 'GHOST_USER',

password : 'GHOST_PASSWORD',

database : 'GHOST_DB',

charset  : 'utf8'

}

}
```

Then the entry point will be responsible to replace these placeholders
with the actual values parsed from the environment variables passed to
the image. Here is a snippet from the entry point:

```
if [ ! -e "$GHOST_CONTENT/config.js" ]; then

sed -r "

s/GHOST_DB/$GHOST_DB/g;

s/GHOST_USER/$GHOST_USER/g;

s/GHOST_PASSWORD/$GHOST_PASSWORD/g;

s!path.join(__dirname, (.)/content!path.join(process.env.GHOST_CONTENT, 1!g;

" "/config-example.js" > "$GHOST_CONTENT/config.js"

fi
```

You can build and push the image to an accessible registry, which will
be available to your kubernetes cluster:

```
$ docker build -t husseingalal/ghost ghost/

$ docker push husseingalal/ghost
```

### Creating Pods and Services for Ghost

I will create simple pods to serve the ghost application and mysql. Pods
are the smallest deployable units of computing that can be set up and
managed in Kubernetes, which represents a group of containers that are
related to each other. In our example, I will create a pod for MySQL and
another one for the nodejs application, the pod configuration MySQL will
look like this:

```
apiVersion: v1

kind: Pod

metadata:

name: mysql

labels:

name: mysql

spec:

containers:

- image: mysql

name: mysql

env:

- name: MYSQL_ROOT_PASSWORD

value: mysqlrootpassword

- name: MYSQL_DATABASE

value: ghost

- name: MYSQL_USER

value: ghost_user

- name: MYSQL_PASSWORD

value: ghost_pass

ports:

- containerPort: 3306

name: mysql

volumeMounts:

- name: mysql-vol

mountPath: /var/lib/mysql

livenessProbe:

tcpSocket:

port: "mysql"

initialDelaySeconds: 5

timeoutSeconds: 1

readinessProbe:

exec:

command: ["mysqladmin", "status", "-pmysqlrootpassword"]

volumes:

- name: mysql-vol

hostPath:

path: /var/lib/mysql
```

The services in Kubernetes are an abstraction that defines a logical
set of Pods. We will create a service for each set of pods in
Kubernetes. The MySQL service will look like this:

```
apiVersion: v1

kind: Service

metadata:

labels:

name: mysql

name: mysql

spec:

ports:

- port: 3306

selector:

name: mysql
```

The ghost pod and service will look similar to both the pod and the
service for MySQL:

```
apiVersion: v1

kind: Pod

metadata:

name: ghost

labels:

name: ghost

spec:

restartPolicy: Always

containers:

- image: "husseingalal/ghost"

imagePullPolicy: Always

name: "ghost"

ports:

- containerPort: 2368

env:

- name: GHOST_USER

value: ghost_user

- name: GHOST_PASSWORD

value: ghost_pass

- name: GHOST_DB

value: ghost

volumeMounts:

- name: ghost-vol

mountPath: /var/lib/ghost

volumes:

- name: ghost-vol

hostPath:

path: /var/lib/ghost

ghost-service.yaml
```

```
apiVersion: v1

kind: Service

metadata:

labels:

name: ghost-lb

name: ghost-lb

spec:

ports:

- port: 2368

selector:

name: ghost

type: LoadBalancer
```

You may notice the type in the ghost-service.yaml file to be
**LoadBalancer**, Rancher will provide a load balancer to distribute the
requests to defined pods. You can create the pods and services using
kubectl:

```
$ for i in *.yaml; do kubectl create -f $i; done

service "ghost-lb" created

pod "ghost" created

service "mysql" created

pod "mysql" created
```

You can see in Rancher UI for kubernetes the new services and pods are
being created: **[![HG
5](images/rancher_blog_HG-5-1024x512.png)](https://cdn.rancher.com/wp-content/uploads/2016/03/25113409/HG-5.png)**
In addition, you can check for the pods and services using the command
line:

```
$ kubectl get pods

NAME      READY     STATUS    RESTARTS   AGE

ghost       1/1             Running     0                   15m

mysql      1/1              Running     0                   20m
```

```
kubectl get services

NAME         CLUSTER_IP     EXTERNAL_IP   PORT(S)    SELECTOR     AGE

ghost-lb     10.43.27.14                  2368/TCP   name=ghost   22m

kubernetes   10.43.0.1      <none>        443/TCP    <none>       2h

mysql        10.43.51.244   <none>        3306/TCP   name=mysql   22m
```

You can test the previous setup by accessing the ghost application
directly: **[![HG
6](images/rancher_blog_HG-6-1024x557.png)](https://cdn.rancher.com/wp-content/uploads/2016/03/25113424/HG-6.png)**

## Conclusion

Kubernetes is a great addition to the Rancher management platform. It
leverages a lot of features and services for your own customized
environment. You can learn more about using Kubernetes by visiting the
[official documentation](http://kubernetes.io/docs/). You
can now start creating your own Kubernetes
cluster within your Rancher
environment. To learn more about running containers with Kubernetes,
view a recording of our recent meetup on deploying Kubernetes environments,
or download a copy of our eBook on modernizing CI/CD with Docker and
Rancher.
