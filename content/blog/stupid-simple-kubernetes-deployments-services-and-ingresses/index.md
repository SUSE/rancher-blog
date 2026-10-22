---
title: "Stupid Simple Kubernetes : Deployments, Services and Ingresses"
date: 2022-04-18T22:12:33
slug: "stupid-simple-kubernetes-deployments-services-and-ingresses"
author: "SUSE"
image: "images/Kubernetes-Logo.wine_.jpg"
products: ["Kubernetes (generic)"]
tags: ["networking"]
content_type: "tutorial"
draft: false
migration:
  wp_id: 91175
  original_url: "https://www.suse.com/c/rancher_blog/stupid-simple-kubernetes%e2%80%8a-deployments-services-and-ingresses/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

![](images/Kubernetes-Logo.wine_.jpg)

In the [**first part**](/blog/91081/)of this series, we learned about the basic concepts used in Kubernetes, its hardware structure, the different software components like **Pods, Deployments, StatefulSets, Services, Ingresses and Persistent Volumes**and saw how to communicate between services and with the outside world.

In this article, we will:

- create a **NodeJS backend**with a MongoDB database
- write the **Dockerfile** to containerize our application
- create the **Kubernetes Deployment scripts** to spin up the Pods
- create the **Kubernetes Service scripts** to define the communication interface between the containers and the outside world
- deploy an **Ingress Controller**for request routing
- write the **Kubernetes Ingress scripts**to define the communication with the outside world.

![](images/190190-1.png)

Because our code can be relocated from one node to another (for example, a node doesn’t have enough memory, so the work will be rescheduled on a different node with enough memory), **data saved on a node is volatile (so our MongoDB data will be volatile, too)**. In the next article, we will talk about the problem of data persistence and how to use **Kubernetes Persistent Volumes** to safely store our persistent data.

In this tutorial, we will use [**NGINX**](https://www.nginx.com/)as an Ingress Controllerand **Azure**[**Container Registry**](https://azure.microsoft.com/en-us/services/container-registry/) to store our custom Docker images. All the scripts written in this article can be found in my [**StupidSimpleKubernetes**](https://github.com/CzakoZoltan08/StupidSimpleKubernetes-AKS)git repository. If you like it, **please leave a star!**

**NOTE:** the scripts are **platform agnostic**, so you can follow the tutorial using other types of cloud providers or a local cluster with [**K3s**](https://k3s.io/)**.**I suggest using **K3s** because it is very lightweight, packed in a single binary less than 40MB. What's more, it's a highly available, certified Kubernetes distribution designed for production workloads in resource-constrained environments. For more information, you can take a look over its well-written and easy-to-follow [**documentation**](https://rancher.com/docs/k3s/latest/en/).

I would like to recommend another great article about basic Kubernetes concepts: [*Explain By Example: Kubernetes*](https://medium.com/swlh/explain-by-example-kubernetes-ea34c60d22ce).

## Requirements

Before starting this tutorial, please make sure that you have installed [**Docker**](https://docs.docker.com/get-docker/). [**Kubectl**](https://kubernetes.io/docs/reference/kubectl/kubectl/)will be installed with Docker. (If not, please install it from [here](https://kubernetes.io/docs/tasks/tools/install-kubectl/#install-kubectl-on-windows)).

The Kubectl commands used throughout this tutorial can be found in the [**Kubectl Cheat Sheet**](https://kubernetes.io/docs/reference/kubectl/cheatsheet/).

Through this tutorial, we will use [**Visual Studio Code**](https://code.visualstudio.com/), but this is not mandatory.

## Creating a Production-Ready Microservices Architecture

### Containerize the app

The first step is to **create the Docker image of our NodeJS backend**. After creating the image, we will **push it in to the container registry**, where it will be accessible and can be **pulled by the Kubernetes service** (in this case, **Azure Kubernetes Service** or **AKS**).

```
The Docker file for NodeJS:
FROM node:13.10.1
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
# Bundle app source
COPY . .
EXPOSE 3000
CMD [ "node", "index.js" ]
```

In the *first line,* we need to define from what image we want to build our backend service. In this case, we will use the official node image with version 13.10.1 from [**Docker Hub**](https://hub.docker.com/_/node).

In *line 3* we create a directory to hold the application code inside the image. This will be the working directory for your application.

This image comes with **Node.js and NPM already installed** so the next thing we need to do is to install your app dependencies using the *npm*command.

Note that to install the required dependencies, we **don’t have to copy the whole directory**, **only the package.json**, which allows us to take advantage of **cached Docker layers** (more info about efficient Dockerfiles [**here**](http://bitjudo.com/blog/2014/03/13/building-efficient-dockerfiles-node-dot-js/)).

In *line 9* we copy our source code into the working directory and on*line 11* we expose it on port 3000 (you can choose another port if you want, but make sure to change in the Kubernetes Service script, too.)

Finally, on *line 13* we define the command to run the application (inside the Docker container). Note that there should **only be one*****CMD*****instruction** in each Dockerfile. If you include more than one, **only the last will take effect**.

Now that we have defined the Dockerfile, we will build an image from it using the following Docker command (using the Terminal of the Visual Studio Code or for example using the CMD on Windows):

```
docker build -t node-user-service:dev .
```

Note the little *dot*from the end of the Docker command, it means that we are building our image from the current directory, so please make sure that you are in the same folder, where the Dockerfile is located (in this case the root folder of the repository).

To run the image locally, we can use the following command:

```
docker run -p 3000:3000 node-user-service:dev
```

To push this image to our Azure Container Registry, we have to tag it using the following format *<container\_registry\_login\_service>/<image\_name>:<tag>*, so in our case:

```
docker tag node-user-service:dev stupidsimplekubernetescontainerregistry.azurecr.io/node-user-service:dev
```

The*last step* is to push it to our container registry using the following Docker command:

```
docker push stupidsimplekubernetescontainerregistry.azurecr.io/node-user-service:dev
```

### Create Pods using Deployment scripts

#### **NodeJs backend**

The next step is to define the **Kubernetes Deployment script**, which automatically manages the Pods for us. (See more in [**this article**](https://community.suse.com/posts/13950530?utm_source=manual))

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: node-user-service-deployment
spec:
  selector:
    matchLabels:
      app: node-user-service-pod
  replicas: 3
  template:
    metadata:
      labels:
        app: node-user-service-pod
    spec:
      containers:
        - name: node-user-service-container
          image: stupidsimplekubernetescontainerregistry.azurecr.io/node-user-service:dev
          resources:
            limits:
              memory: "256Mi"
              cpu: "500m"
          imagePullPolicy: Always
          ports:
            - containerPort: 3000
```

The **Kubernetes API** lets you query and manipulates the state of objects in the Kubernetes Cluster (for example, Pods, Namespaces, ConfigMaps, etc.). The current stable version of this API is 1, as we specified in the *first line*.

In each Kubernetes .yml script we have to define the Kubernetes resource type (Pods, Deployments, Services, etc.) using the *kind*keyword. In this case, in *line 2*we defined that we would like to use the *Deployment*resource.

Kubernetes lets you add some *metadata* to your resources. This way it’s easier to identify, filter and in general to refer to your resources.

From *line 5* we define the **specifications**of this resource. In *line 8* we specified that this Deployment should be applied only to the resources with the label *app:node-user-service-pod*and in *line 9*we said that we want to create *3 replicas* of the **same pod**.

The template (starting from *line 10*) defines the Pods. Here we add the label *app:node-user-service-pod* to each Pod. This way they will be identified by the Deployment. In *lines 16 and 17* we define what kind of Docker Container should be run inside the pod. As you can see in *line 17*, we will use the Docker Image from our *Azure Container Registry* which was built and pushed in the previous section.

We can also define the **resource limits** for the Pods, avoiding **Pod starvation** (when a Pod uses all the resources and other Pods don’t get a chance to use them). Furthermore, when you specify the resource *request* for Containers in a Pod, the scheduler uses this information to decide **which node to place the Pod on**. When you specify a resource *limit* for a Container, the [kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/)enforces those limits so that the running container **is not allowed to use more of that resource than the limit you set**. The kubelet also **reserves at least the*****request*****amount of that system resource** specifically for that container to use. Be aware that if you don’t have enough hardware resources (like CPU or memory), the pod won’t be scheduled -- ever.

The last step is to define the port used for communication. In this case, we used port 3000. **This port number should be the same as the port number exposed in the Dockerfile**.

#### **MongoDB**

The Deployment script for the MongoDB database is quite similar. The only difference is that we have to specify the **volume mounts**(the folder on the node where the data will be saved).

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: user-db-deployment
spec:
  selector:
    matchLabels:
      app: user-db-app
  replicas: 1
  template:
    metadata:
      labels:
        app: user-db-app
    spec:
      containers:
        - name: mongo
          image: mongo:3.6.4
          command:
            - mongod
            - "--bind_ip_all"
            - "--directoryperdb"
          ports:
            - containerPort: 27017
          volumeMounts:
            - name: data
              mountPath: /data/db
          resources:
            limits:
              memory: "256Mi"
              cpu: "500m"
      volumes:
        - name: data
          persistentVolumeClaim:
            claimName: static-persistence-volume-claim-mongo
```

In this case, we used the official MongoDB image directly from the DockerHub (*line 17*). The volume mounts are defined in *line 24*. The last *four lines*will be explained in the **next article** when we will talk about **Kubernetes Persistent Volumes**.

### Create the Services for Network Access

Now that we have the Pods up and running, we should define the communication between the containers and with the outside world. For this, we need to define a **Service**. The relation between a Service and a Deployment is 1-to-1, so for each Deployment, we should have a Service. The Deployment manages the lifecycle of the Pods and it is also responsible for monitoring them, while the **Service is responsible for enabling network access to a set of Pods** (as we saw in [**Part One of this series**](https://community.suse.com/posts/13950530?utm_source=manual)).

```
apiVersion: v1
kind: Service
metadata:
  name: node-user-service
spec:
  type: ClusterIP
  selector:
    app: node-user-service-pod
  ports:
    - port: 3000
      targetPort: 3000
```

The **important part of this .yml script is the selector**, which defines how to identify the Pods (created by the Deployment) to which we want to refer from this Service. As you can see in *line 8*, the selector is *app:node-user-service-pod*, because the Pods from the previously defined Deployment are labeled like this. Another important thing is to define the **mapping between the container port and the Service port**. In this case, the incoming request will use the 3000 port, defined on *line 10* and they will be routed to the port defined in *line 11*.

The Kubernetes Service script for the MongoDB pods is very similar. We just have to update the selector and the ports.

```
apiVersion: v1
kind: Service
metadata:
  name: user-db-service
spec:
  clusterIP: None
  selector:
    app: user-db-app
  ports:
    - port: 27017
      targetPort: 27017
```

### Configure the External Traffic

To communicate with the outside world, we need to define an **Ingress Controller** and **specify the routing rules using an Ingress Kubernetes Resource**.

To configure an **NGINX Ingress Controller** we will use the script that can be found [**here**](https://github.com/CzakoZoltan08/StupidSimpleKubernetes-AKS/blob/master/manifest/ingress-controller/nginx-ingress-controller-deployment.yml).

This is a generic script that can be applied without modifications (explaining the NGINX Ingress Controller is out of scope for this article).

The next step is to define the**Load Balancer**, which will be used to route external traffic using a public IP address (the cloud provider provides the load balancer).

```
kind: Service
apiVersion: v1
metadata:
  name: ingress-nginx
  namespace: ingress-nginx
  labels:
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/part-of: ingress-nginx
spec:
  externalTrafficPolicy: Local
  type: LoadBalancer
  selector:
    app.kubernetes.io/name: ingress-nginx
    app.kubernetes.io/part-of: ingress-nginx
  ports:
    - name: http
      port: 80
      targetPort: http
    - name: https
      port: 443
      targetPort: https
```

Now that we have the Ingress Controller and the Load Balancer up and running, we can define the **Ingress Kubernetes Resource** **for specifying the routing rules**.

```
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: node-user-service-ingress
  annotations:
    kubernetes.io/ingress.class: "nginx"
    nginx.ingress.kubernetes.io/rewrite-target: /$2
spec:
  rules:
    - host: stupid-simple-kubernetes.eastus2.cloudapp.azure.com
      http:
        paths:
          - backend:
              serviceName: node-user-service
              servicePort: 3000
            path: /user-api(/|$)(.*)
          # - backend:
          #     serviceName: nestjs-i-consultant-service
          #     servicePort: 3001
          #   path: /i-consultant-api(/|$)(.*)
```

In *line 6* we define the Ingress Controller type (it’s a Kubernetes predefined value; Kubernetes as a project currently supports and maintains [GCE](https://git.k8s.io/ingress-gce/README.md) and [nginx](https://git.k8s.io/ingress-nginx/README.md) controllers).

In *line 7* we define the rewrite target rules (more information [here](https://github.com/kubernetes/ingress-nginx/tree/master/docs/examples/rewrite)) and in *line 10* we define the hostname.

**For each service that should be accessible from the outside world, we should add an entry in the** **paths list** (starting from*line 13*). In this example, we added only one entry for the NodeJS user service backend, which will be accessible using port 3000. The */user-api* uniquely identifies our service, so any request that starts with *stupid-simple-kubernetes.eastus2.cloudapp.azure.com/user-api*will be routed to this NodeJS backend. If you want to add other services, then you have to update this script (as an example see the commented out code).

#### Apply the .yml scripts

To apply these scripts, we will use the **kubectl**. The kubectl command to apply files is the following:

```
kubectl apply -f <file_name>
```

So in our case, if you are in the *root folder* of the [**StupidSimpleKubernetes**](https://github.com/CzakoZoltan08/StupidSimpleKubernetes-AKS/tree/master/manifest/kubernetes)repository, you will write the following commands:

```
kubectl apply -f .\manifest\kubernetes\deployment.yml
kubectl apply -f .\manifest\kubernetes\service.yml
kubectl apply -f .\manifest\kubernetes\ingress.yml
kubectl apply -f .\manifest\ingress-controller\nginx-ingress-controller-deployment.yml
kubectl apply -f .\manifest\ingress-controller\ngnix-load-balancer-setup.yml
```

After applying these scripts, we will have everything in place, so we can call our backend from the outside world (for example by using Postman).

## Conclusion

In this tutorial, we learned how to create different kinds of resources in Kubernetes, like **Pods, Deployments, Services, Ingresses** and**Ingress Controllers**. We created a **NodeJS backend with a MongoDB database** and we **containerized and deployed** the NodeJS and MongoDB containers using **replication of 3 pods**.

In the next article,we will approach the problem of saving data persistently and we will learn about **Persistent Volumes in Kubernetes**.

You can learn more about the **basic concepts** used in Kubernetes in [***this article***](/blog/91081/).

There is another ongoing **“Stupid Simple AI” series**. The first two articles can be found here: [**SVM and Kernel SVM**](https://towardsdatascience.com/svm-and-kernel-svm-fed02bef1200) and [**KNN in Python**](https://towardsdatascience.com/knn-in-python-835643e2fb53).

## Want to Learn More from our Stupid Simple Series?

Read our eBook: Stupid Simple Kubernetes. Download it [here!](https://more.suse.com/Stupid_Simple_Kubernetes_ebook.html)

[![](images/LinkedIn-Image-Ad_1200x628_SSKubernetes-300x157.png)](https://more.suse.com/Stupid_Simple_Kubernetes_ebook.html)
