---
title: "Native Kubernetes Monitoring, Part 2: Scaling and Life Cycle Management"
date: 2019-04-05T09:08:00
slug: "native-kubernetes-monitoring-part-2-scaling-and-life-cycle-management"
author: "Rancher Admin"
image: "images/rancher_blog_featured-images_monitoring.svg"
products: ["Kubernetes (generic)"]
tags: ["observability"]
content_type: "tutorial"
draft: false
migration:
  wp_id: 85908
  original_url: "https://www.suse.com/c/rancher_blog/native-kubernetes-monitoring-part-2-scaling-and-life-cycle-management/"
  disposition: migrate_refresh
  commercial: false
  outdated_reason: "Old Rancher UI and versions"
  redirect_target: ""
---

This article is a follow up to [Native Kubernetes Monitoring, Part One](/blog/2019/native-kubernetes-monitoring-tools-part-1). In this chapter we’ll finish the two remaining demos for the other built-in tools, Probes and Horizontal Pod Autoscaler (HPA).

## Prerequisites for the Demo

If you were following [previous chapter](/blog/2019/native-kubernetes-monitoring-tools-part-1) then your Rancher instance and Kubernetes cluster should be both up and running. If not, please check the [article](/blog/2019/native-kubernetes-monitoring-tools-part-1/#prerequisites-for-the-demo) in order to setup the environment.

As a short reminder, we previously mentioned that Kubernetes ships with some built-in tools to monitor the cluster and the many moving parts that form a deployment:

- **Kubernetes dashboard:** gives an overview of the resources running on your cluster. It also gives a very basic means of deploying and interacting with those resources.
- **cAdvisor:** is an open source agent that monitors resource usage and analyzes the performance of containers.
- **Liveness and Readiness Probes:** actively monitor the health of a container.
- **Horizontal Pod Autoscaler:** increases the number of pods if needed based on information gathered by analyzing different metrics.

We’ve seen the first two in action, so let’s take a look at the remaining tools.

## Probes

There are two kind of health checks: liveness and readiness probes.

**Readiness probes** let Kubernetes know when an app is ready to serve traffic. Kubernetes will only allow a service to send traffic to the pod once the probe passes. If the probe fails, Kubernetes will stop sending traffic to that Pod until it passes again.

These kinds of probes are useful when you have an application which takes some appreciable amount of time to start. The service won’t work until the probe completes successfully even when the process has already started. Be default, Kubernetes will start sending traffic as soon as the process inside the container is started, but with a readiness probe, Kubernetes will wait until the app is fully started before allowing services to route traffic.

**Liveness probes** let Kubernetes know if an app is alive or not. If it is alive, no action is taken. If the app is dead, Kubernetes will remove the pod and start a new one to replace it. These probes are useful when you have an app that may hang indefinitely and stop serving requests. Because the process is still running, by default, Kubernetes will continue sending requests to the pod. With these probes, Kubernetes will detect that the app is no longer serving requests and will restart the pod.

For both liveness and readiness checks, the following types of probes are available:

- **http:** The most command type of custom probe. Kubernetes pings a path and if it gets a http response in 200-300 range, it will mark the pod as healthy.
- **command:** When using this probe, Kubernetes will run a command inside of one of the pod’s containers. If the command returns an exit code of 0, the container will be marked healthy.
- **tcp:** Kubernetes will try to establish a TCP connection on a specified port. If it’s able to establish the connection, the container is marked healthy.

When configuring probes, the following parameters can be provide:

- **`initialDelaySeconds`:** the time to wait before sending a readiness/liveness probe when first starting a container. For liveness checks, make sure that the probe will start only after the app is ready or else your app will keep restarting.
- **`periodSeconds`:** how often the probe is performed (default is 10).
- **`timeoutSeconds`:** the number of seconds for a probe to timeout (default is 1).
- **`successThreshold`:** the minimum consecutive successful checks for a probe to be considered successful.
- **`failureThreshold`:** the amount of failed probe attempts before giving up. Giving up on a liveness probe causes Kubernetes to restart the pod. For readiness probes, the pod will be marked as unready.

### Demonstrating a Readiness Probe

In this section, we will be playing with a readiness probe, configured using the `command` check. We will have a deployment of two replicas using the default `nginx` container. No traffic will be sent to the pods until a file called `/tmp/healthy` is found within the containers.

First, create a `readiness.yaml` file with the following contents:

```
cat readiness.yaml
```

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: readiness-demo
spec:
  selector:
    matchLabels:
      app: nginx
  replicas: 2
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - image: nginx
        name: nginx
        ports:
          - containerPort: 80
        readinessProbe:
          exec:
            command:
            - ls
            - /tmp/healthy
          initialDelaySeconds: 5
          periodSeconds: 5
---
apiVersion: v1
kind: Service
metadata:
  name: lb
spec:
  type: LoadBalancer
  ports:
  - port: 80
    protocol: TCP
    targetPort: 80
  selector:
      app: nginx
```

Next, apply the YAML file:

```
kubectl apply -f readiness.yml
```

We will see a deployment and a service being created:

```
deployment.apps "readiness-demo" created
service "lb" created
```

The pods won’t enter the `READY` state unless the readiness probe passes. In this case, since there is no file called `/tmp/healthy`, it will be marked as failed, so no traffic will be sent by the Service.

```
kubectl get deployments
kubectl get pods
```

```
NAME             DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
readiness-demo   2         2         2            0           20s

NAME                              READY     STATUS    RESTARTS   AGE
readiness-demo-6c48bbb79f-xvgsk   0/1       Running   0          23s
readiness-demo-6c48bbb79f-xvr4x   0/1       Running   0          23s
```

For a better understanding of what is happening, we will modify the default `nginx` index page for the two pods. When requested, the first one will show `1` as response and the second one will show `2` as a response.

Replace the specific pod names in the commands below with the ones created by the deployment on your machine:

```
kubectl exec -it readiness-demo-6c48bbb79f-xvgsk -- bash -c "echo 1 > /usr/share/nginx/html/index.html"
kubectl exec -it readiness-demo-6c48bbb79f-xvr4x -- bash -c "echo 2 > /usr/share/nginx/html/index.html"
```

Let’s create the required file in our first pod so that it transitions into the `READY` state and can be routed there:

```
kubectl exec  -it readiness-demo-6c48bbb79f-xvgsk -- touch /tmp/healthy
```

The probe runs every 5 seconds, so we might need to wait a bit before seeing the result:

```
kubectl get pods
kubectl get pods
```

```
NAME                              READY     STATUS    RESTARTS   AGE
readiness-demo-6c48bbb79f-xvgsk   0/1       Running   0          23m
readiness-demo-6c48bbb79f-xvr4x   0/1       Running   0          23m

kubectl get pods
NAME                              READY     STATUS    RESTARTS   AGE
readiness-demo-6c48bbb79f-xvgsk   1/1       Running   0          23m
readiness-demo-6c48bbb79f-xvr4x   0/1       Running   0          23m
```

As soon as the state changes we can start hitting the external IP of our load balancer:

```
curl 35.204.202.158
```

We should see our modified Nginx page, which consists of a single digit identifier:

```
1
```

Creating the file for the second pod will cause that pod to enter the `READY` state as well. Traffic will be redirected here too:

```
kubectl exec -it readiness-demo-6c48bbb79f-xvr4x -- touch /tmp/healthy
kubectl get pods
```

```
NAME                              READY     STATUS    RESTARTS   AGE
readiness-demo-6c48bbb79f-xvgsk   1/1       Running   0          25m
readiness-demo-6c48bbb79f-xvr4x   1/1       Running   0          25m
```

As second pod is now marked as `READY`, the service will send traffic to both:

```
curl 35.204.145.38
curl 35.204.145.38
```

The output should indicate that traffic is being split between the two pods:

```
2
1
```

### Demonstrating a Liveness Probe

In this section, we will demo a liveness probe configured with a `tcp` check. Just as above, we will use a deployment of two replicas using the default `nginx` container. If port 80 inside the container is not be listening, traffic will not be sent to the container and it will be restarted.

First, let’s take a look at the liveness probe demo file:

```
cat liveness.yaml
```

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: liveness-demo
spec:
  selector:
    matchLabels:
      app: nginx
  replicas: 2
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - image: nginx
        name: nginx
        ports:
          - containerPort: 80
        livenessProbe:
          tcpSocket:
            port: 80
          initialDelaySeconds: 15
          periodSeconds: 5
---
apiVersion: v1
kind: Service
metadata:
  name: lb
spec:
  type: LoadBalancer
  ports:
  - port: 80
    protocol: TCP
    targetPort: 80
  selector:
      app: nginx
```

We can apply the YAML with a single command:

```
kubectl apply -f liveness.yaml
```

Afterwards, we can check the pods and, like above, modify the default Nginx page to respond with a simple `1` or `2`.

First, find the names given to the pods by your Nginx deployment:

```
kubectl get pods
```

```
NAME                              READY     STATUS    RESTARTS   AGE
liveness-demo-7bdcdd47d9-l8wj8   1/1       Running   0          2m
liveness-demo-7bdcdd47d9-m825b   1/1       Running   0          2m
```

Next, replace the default index page within each pod with a numerical identifier:

```
kubectl exec -ti liveness-demo-7bdcdd47d9-l8wj8 -- bash -c "echo 1 > /usr/share/nginx/html/index.html"
kubectl exec -ti liveness-demo-7bdcdd47d9-m825b -- bash -c "echo 2 > /usr/share/nginx/html/index.html"
```

Traffic is already being redirected by the Service, so we can get responses from both pods immediately:

```
curl 35.204.202.158
curl 35.204.202.158
```

Again, the response should indicate that the traffic is being split between our two pods:

```
2
1
```

Now we’re ready to stop the Nginx process in the first pod to see the liveness probe in action. As soon as Kubernetes notices that the container is no longer listening on port `80`, the pod’s status will change and it will be restarted. We can observe some of the statuses it transitions through until it’s running correctly again.

First, stop the web server process in one of your pods:

```
kubectl exec -ti liveness-demo-7bdcdd47d9-l8wj8 -- service nginx stop
```

```
command terminated with exit code 137
```

Now, audit the status of your pods as Kubernetes notices the probe failure and takes action to restart the pod:

```
kubectl get pods
kubectl get pods
kubectl get pods
```

You will likely see the pod transition through a number of statuses until it becomes healthy again:

```
NAME                              READY     STATUS      RESTARTS   AGE
liveness-demo-7bdcdd47d9-l8wj8   0/1       Completed   2          7m
liveness-demo-7bdcdd47d9-m825b   1/1       Running     0          7m

NAME                              READY     STATUS             RESTARTS   AGE
liveness-demo-7bdcdd47d9-l8wj8   0/1       CrashLoopBackOff   2          7m
liveness-demo-7bdcdd47d9-m825b   1/1       Running            0          7m

NAME                              READY     STATUS    RESTARTS   AGE
liveness-demo-7bdcdd47d9-l8wj8   1/1       Running   3          8m
liveness-demo-7bdcdd47d9-m825b   1/1       Running   0          8m
```

If we request the page through our service, we will see the correct response, the modified identifier of “2”, from our second pod. However, the pod that was just created we will return the default Nginx page from the container image:

```
curl 35.204.202.158
curl 35.204.202.158
```

```
2

<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```

This demonstrates that Kubernetes deployed an entirely new pod to replace the failed pod we customized earlier.

## Horizontal Pod Autoscaler

The Horizontal Pod Autoscaler, or HPA, is a feature of Kubernetes that enables us to automatically scale the number of pods needed for a deployment, replication controller, or replica set based on observed metrics. In practice, CPU metrics are often the primary trigger, but custom metrics are also possible too.

Each part of the process is automated and based on measured resource usage, so no human intervention is required. The metrics are fetched from APIs like `metrics.k8s.io`, `custom.metrics.k8s.io` or `external.metrics.k8s.io`.

In this example, we will run a demo based on CPU metrics. A useful command that we can use in this scenario is `kubectl top pods`, which shows CPU and memory usage for pods.

First, let’s create a YAML file that will create a deployment with a single replica:

```
cat hpa.yaml
```

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hpa-demo
spec:
  selector:
    matchLabels:
      app: stress
  replicas: 1
  template:
    metadata:
      labels:
        app: stress
    spec:
      containers:
      - image: nginx
        name: stress
```

Apply the deployment by typing:

```
kubectl apply -f hpa.yaml
```

```
horizontalpodautoscaler.autoscaling "hpa-demo" created
```

This is a simple deployment with the same Nginx image and a single replica:

```
kubectl get deployment
```

```
NAME       DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
hpa-demo   1         1         1            1           38s
```

Next, let’s see how we can implement an autoscaling mechanism. We can list the currently defined autoscalers with `kubectl get/describe hpa`. To define a new autoscaler, we could use a `kubectl create` command. However, the easiest way to create an autoscaler is to target an existing deployment, like this:

```
kubectl autoscale deployment hpa-demo --cpu-percent=50 --min=1 --max=10
```

```
deployment.apps "hpa-demo" autoscaled
```

This will create an autoscaler for our `hpa-demo` deployment that we created earlier with the target CPU utilization set to 50%. The replica number is set here to be between one and ten, so maximum number of pods the autoscaler will create when there is high load is ten.

You can confirm the autoscaler’s configuration by typing:

```
kubectl get hpa
```

```
NAME       REFERENCE             TARGETS   MINPODS   MAXPODS   REPLICAS   AGE
hpa-demo   Deployment/hpa-demo   0%/50%    1         10        1          23s
```

We can alternatively define this in a YAML format to allow for easier review and change management:

```
apiVersion: autoscaling/v1
kind: HorizontalPodAutoscaler
metadata:
  name: hpa-demo
  namespace: default
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: hpa-demo
  minReplicas: 1
  maxReplicas: 10
  targetCPUUtilizationPercentage: 50
```

In order to see HPA in action, we need to run a command which creates load on the CPU. There are numerous ways to achieve this, but one very simple example is:

```
while true; do sleep 1 && date & done
```

First, let’s check the load on our only pod. As it currently sits idle, there is not much going:

```
kubectl top pods
```

```
NAME                        CPU(cores)   MEMORY(bytes)
hpa-demo-7c68555d8b-6hjvj   0m           1Mi
```

Now, let’s generate some load on the current pod. As soon as load increases we should see the HPA begin to automatically create some additional pods to handle the increased load. Let the following command run for few seconds before stopping it:

```
kubectl exec -it hpa-demo-7c68555d8b-6hjvj  -- bash -c "while true; do sleep 1 && date & done"
```

Check the current load on the current pod:

```
kubectl top pods
```

```
NAME                        CPU(cores)   MEMORY(bytes)
hpa-demo-7c68555d8b-6hjvj   104m         3Mi
```

The HPA kicks in and starts creating extra pods. Kubernetes indicates that the deployment has been automatically scaled and now has three replicas:

```
kubectl get deployments
kubectl get pods
```

```
NAME       DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
hpa-demo   3         3         3            2           4m

NAME                        READY     STATUS    RESTARTS   AGE
hpa-demo-7c68555d8b-6hjvj   1/1       Running   0          5m
hpa-demo-7c68555d8b-9b7dn   1/1       Running   0          58s
hpa-demo-7c68555d8b-lt7t2   1/1       Running   0          58s
```

We can see the details of our HPA and the reason why this has been scaled to three replicas:

```
kubectl describe hpa hpa-demo
```

```
Name:                                                  hpa-demo
Namespace:                                             default
Labels:                                                <none>
Annotations:                                           kubectl.kubernetes.io/last-applied-configuration={"apiVersion":"autoscaling/v1","kind":"HorizontalPodAutoscaler","metadata":{"annotations":{},"name":"hpa-demo","namespace":"default"},"spec":{"maxRepli...
CreationTimestamp:                                     Sat, 30 Mar 2019 17:43:50 +0200
Reference:                                             Deployment/hpa-demo
Metrics:                                               ( current / target )
  resource cpu on pods  (as a percentage of request):  104% (104m) / 50%
Min replicas:                                          1
Max replicas:                                          10
Conditions:
  Type            Status  Reason              Message
  ----            ------  ------              -------
  AbleToScale     True    ReadyForNewScale    recommended size matches current size
  ScalingActive   True    ValidMetricFound    the HPA was able to successfully calculate a replica count from cpu resource utilization (percentage of request)
  ScalingLimited  False   DesiredWithinRange  the desired count is within the acceptable range
Events:
  Type    Reason             Age   From                       Message
  ----    ------             ----  ----                       -------
  Normal  SuccessfulRescale  15s   horizontal-pod-autoscaler  New size: 3; reason: cpu resource utilization (percentage of request) above target
```

Since we stopped our load-generating command, if we wait a few minutes, the HPA should notice the decreased load and scale down the number of replicas. Without high load, there is no need for the additional two pods that were created.

Five minutes is the default amount time autoscalers wait before performing a downscale operation in Kubernetes. This limit can be overridden by adjusting the `--horizontal-pod-autoscaler-downscale-delay` setting, which you can learn more about in [the autoscaler documentation](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/).

Once the wait time is over, the pods for the deployment should decrease from the high-load mark:

```
kubectl get pods
```

```
NAME                        READY     STATUS    RESTARTS   AGE
hpa-demo-7c68555d8b-6hjvj   1/1       Running   0          9m
hpa-demo-7c68555d8b-9b7dn   1/1       Running   0          5m
hpa-demo-7c68555d8b-lt7t2   1/1       Running   0          5m
```

They should return to the baseline number:

```
kubectl get pods
```

```
NAME                        READY     STATUS    RESTARTS   AGE
hpa-demo-7c68555d8b-6hjvj   1/1       Running   0          9m
```

If you check the description for the HPA again, you should we see the reason for decreasing the number of replicas:

```
kubectl describe hpa hpa-demo
```

```
Name:                                                  hpa-demo
Namespace:                                             default
Labels:                                                <none>
Annotations:                                           kubectl.kubernetes.io/last-applied-configuration={"apiVersion":"autoscaling/v1","kind":"HorizontalPodAutoscaler","metadata":{"annotations":{},"name":"hpa-demo","namespace":"default"},"spec":{"maxRepli...
CreationTimestamp:                                     Sat, 30 Mar 2019 17:43:50 +0200
Reference:                                             Deployment/hpa-demo
Metrics:                                               ( current / target )
  resource cpu on pods  (as a percentage of request):  0% (0) / 50%
Min replicas:                                          1
Max replicas:                                          10
Conditions:
  Type            Status  Reason            Message
  ----            ------  ------            -------
  AbleToScale     True    SucceededRescale  the HPA controller was able to update the target scale to 1
  ScalingActive   True    ValidMetricFound  the HPA was able to successfully calculate a replica count from cpu resource utilization (percentage of request)
  ScalingLimited  True    TooFewReplicas    the desired replica count is increasing faster than the maximum scale rate
Events:
  Type    Reason             Age   From                       Message
  ----    ------             ----  ----                       -------
  Normal  SuccessfulRescale  5m    horizontal-pod-autoscaler  New size: 3; reason: cpu resource utilization (percentage of request) above target
  Normal  SuccessfulRescale  13s   horizontal-pod-autoscaler  New size: 1; reason: All metrics below target
```

## Conclusion

We’ve seen how Kubernetes helps us using the built-in tools to set up monitoring for our cluster. We’ve seen how it works nonstop behind the scenes to keep our apps running, but this doesn’t mean that we shouldn’t be aware of what’s happening.

Gathering all the data from the dashboard and the probes, and having all these container resources exposed by cAdvisor can help us investigate resource limitations and/or capacity planning. Monitoring Kubernetes is vital as it helps us understand the health and performance of a cluster and the applications running on top of it.

## Kubernetes Monitoring in Rancher

In Rancher, you can easily monitor and graph everything in your cluster, from nodes to pods to applications. The advanced monitoring tooling, powered by Prometheus, gives you real-time data about the performance of every aspect of your cluster. [Watch our online meetup on advanced Kubernetes monitoring in Rancher](https://info.rancher.com/meetup-introducing-rancher-2.2) to see these features demoed and discussed.
