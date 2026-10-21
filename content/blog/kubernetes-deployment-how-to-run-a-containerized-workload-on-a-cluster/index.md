---
title: "Kubernetes Deployment: How to Run a Containerized Workload on a Cluster"
date: 2019-09-12T19:02:52
slug: "kubernetes-deployment-how-to-run-a-containerized-workload-on-a-cluster"
author: "Rancher Admin"
products: ["Kubernetes (generic)"]
tags: ["developer-experience"]
content_type: "tutorial"
draft: false
migration:
  wp_id: 87327
  original_url: "https://www.suse.com/c/rancher_blog/kubernetes-deployment-how-to-run-a-containerized-workload-on-a-cluster/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

## Introduction

In this guide, we will demonstrate how to deploy an application to a Kubernetes cluster. We’ll use a simple demonstration container to walk through how to create a Deployment, how to update the running application with `kubectl`, and how to scale the application out by launching more container instances within the same Deployment.

## Deploying an Application Within Kubernetes

For our example, we will use a pre-built container provided by Rancher. We will perform the following operations to deploy it to a Kubernetes cluster:

- Create a simple YAML file to deploy our our application within Kubernetes
- Modify our spec to reference to a new version and roll over the currently active version to upgrade our deployment
- Scale the application to create a highly available application within Kubernetes

These represent a rather simple set of actions, but will demonstrate the ease and functionality built into Kubernetes’ objects.

### Defining the Application Deployment

To get started, we will define a basic application deployment that Kubernetes can understand by writing a YAML file. YAML is a human-readable data serialization format that Kubernetes can read and interpret.

Our YAML file will define a Deployment object that launches and manages our application container. You can copy the following file, which we’ll call `testdeploy.yaml` to replicate this demonstration on your own cluster:

```
cat testdeploy.yaml
```

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mysite
  labels:
    app: mysite
spec:
  replicas: 1
  selector:
    matchLabels:
      app: mysite
  template:
    metadata:
      labels:
        app: mysite
    spec:
      containers:
        - name: mysite
          image: kellygriffin/hello:v1
          ports:
            - containerPort: 80
```

Let’s take a closer look at this file to describe the specifics of what it defines.

The YAML creates a Kubernetes Deployment object with the name `mysite`, which also uses the label `app: mysite` throughout. The spec for the deployment asks for a single replica spawned from a Pod template that launches a container based on the `kellygriffin/hello:v1` container. The spec indicates that the container will listen on port 80.

Once you’ve saved the file, you can apply it to deploy it to your cluster:

```
kubectl apply -f testdeploy.yaml
```

```
deployment.apps/mysite created
```

You can check the details of the deployed pod by typing:

```
kubectl get pods
```

Record the name of your container. For the deployment we launched, our container was named `mysite-59564d59f5-xz9vd`, but yours will be different.

Once you have the container name, you can query the web server running on the container’s `localhost` by typing:

```
kubectl exec -it <your_container_name> curl localhost
```

You should get a response that verifies the application and version that we deployed:

```
<!DOCTYPE html>
<html>
<head>
<title>Hello World This is Version 1 of our Application</title>
</html>
```

This validates that our deployment was successful and that our application is functioning correctly.

### Modifying the Version of the Application

Now that we have a deployment running on our Kubernetes cluster, we can manage and modify it as circumstances dictate. Kubernetes will take care of a lot of the automated management tasks, but there are still instances where we want to influence the behavior of our applications.

To demonstrate this, we will update the application version associated with our deployment. Editing the deployment YAML file we created earlier won’t help since our application is already running within the cluster. Instead, we need to modify the spec as stored in the actual cluster.

We can edit existing objects with the `kubectl edit` command. The target for the command is the object type and the object name, separated by a forwards slash. For our example, we can edit our deployment’s spec by typing:

```
kubectl edit deploy/mysite
```

The deployment spec will open in the system’s default editor. Once inside, you need to change the following line:

Modify the following line:

- **Original line:** `image: kellygriffin/hello:v1`
- **Replaced with:** `image: kellygriffin/hello:v2`

Assuming the default editor was set to `vim`, you can save and exit after finishing by hitting the escape key and typing `:wq`.

Once you save the file, Kubernetes will recognized the difference in the spec and begin to automatically update the Deployment within the cluster.

You can validate that this process has completed by checking the pods on your cluster again:

```
kubectl get pods
```

As we saw before, this will display information about the Pods on our cluster, including the names of the containers that are deployed withing each pod. Record the name of your container again. If you look closely, you should notice that the container’s name is now different. In our example, our new container is called `mysite-5bcfff5d56-n9zvf`, but again, yours will be different.

We can check the web server operating on port 80 again by asking the container to query `localhost`:

```
kubectl exec -it <your_container_name> curl localhost
```

This time, we should see an updated message associated with version 2 of our container that we specified when we updated our Deployment spec:

```
<!DOCTYPE html>
<html>
<head>
<title>Hello World This is Version 2 and a different Application Tag</title>
</html>
```

This helps us validate that the actual container within our Deployment has been replaced, based on the new image we specified.

### Scaling Applications

Now that we’ve demonstrated how to update our applications by modifying the Deployment spec, we can also discuss how to scale our containerized workload using Kubernetes’ built-in replication primitives.

We can modify the scale of our deployment with the `kubectl scale` command. To complete our request, we need to provide the number of replicas we desire as well as the Kubernetes object we wish to target (in this case, it’s our `deploy/mysite` object).

To scale our Deployment from a single replica to 2, we can type:

```
kubectl scale --replicas=2 deploy/mysite
```

```
deployment.extensions/mysite scaled
```

We can check on the progress of the scaling operation by asking for the details on our Deployment object:

```
kubectl get deploy mysite
```

```
NAME     READY   UP-TO-DATE   AVAILABLE   AGE
mysite   2/2     2            2           91s
```

Here, we can see that 2 out of 2 replicas are ready and operational. The output confirms that each of these replicas is serving the most up-to-date version of the spec and that each is capable of serving traffic currently.

## Cleaning Up the Deployment

We’ve created a deployment, updated it, and scaled it. Since this is not a real production workload, we should remove it from our cluster once we’re done to clean up after ourselves.

To remove the resources we’ve set up, we just need to delete the Deployment object. Kubernetes will automatically remove all other child resources associated with it, like the pods and containers that it manages.

Delete the Deployment by typing:

```
kubectl delete deploy mysite
```

```
deployment.extensions "mysite" deleted
```

You can double check that the resources have been removed by attempting to show the Deployment details or by asking Kubernetes to list the Pods in the default namespace:

```
kubectl get deploy mysite
kubectl get pods
```

These commands should indicate that the Deployment and all of its associated resources are no longer running.

## Conclusion

In this guide, we demonstrated how to run a containerized workload on a Kubernetes cluster. By choosing to wrap our container in a Deployment object, we automatically had access to update and rollback features as well as the scaling capabilities provided by the ReplicaSet object that it controls. While the example we used was simple, it showed some of the standard features available for stateless workloads and how to manage different aspects of your applications.
