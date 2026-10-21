---
title: "Deploy an Ingress Controller on K3s"
date: 2020-07-28T09:46:00
slug: "deploy-an-ingress-controller-on-k3s"
author: "Rancher Admin"
image: "images/rancher_blog_ingress-featured.png"
products: ["K3s"]
tags: ["networking"]
content_type: "tutorial"
draft: false
migration:
  wp_id: 86028
  original_url: "https://www.suse.com/c/rancher_blog/deploy-an-ingress-controller-on-k3s/"
  disposition: migrate_refresh
  commercial: false
  outdated_reason: "Ingress details tied to 2020 K3s defaults"
  redirect_target: ""
---

The certified Kubernetes distribution built for IoT & Edge computing[Download K3S](https://k3s.io/)

Kubernetes provides a powerful networking model for microservices. One of the pillars of this model is that each pod has its own IP address and is directly addressable within the cluster. As a consequence, each Kubernetes cluster usually has a flat virtual network that external hosts can’t reach directly. That means routing traffic from clients outside the cluster to services deployed inside the cluster requires some additional work. There are [various strategies for routing traffic into a Kubernetes cluster](https://blog.getambassador.io/kubernetes-ingress-nodeport-load-balancers-and-ingress-controllers-6e29f1c44f2d) – the most common approach is to use an ingress controller.

## Ingress Controllers

An ingress controller routes traffic from outside the cluster, and is responsible for routing traffic to individual services inside the cluster. An ingress controller gets its name from the fact that it can process [Ingress resources](https://kubernetes.io/docs/concepts/services-networking/ingress/), which are a special type of Kubernetes resource that specify these routing rules.

Ingress controllers are built on proxies such as HAProxy, NGINX, Traefik, and, most recently, [Envoy Proxy](https://www.envoyproxy.io/). Originally written and deployed at Lyft, Envoy Proxy today is a Cloud Native Computing Foundation (CNCF) project with dozens of organizations contributing, including Amazon, Airbnb, Google, Pinterest and VMware.

## K3s, Rancher and Ambassador

[K3s](https://www.envoyproxy.io/) is a lightweight Kubernetes distribution that runs in resource-constrained environments, such as IoT or edge devices and development laptops. Rancher is a complete software stack for teams deploying containers built on Kubernetes. Both K3s and Rancher support a variety of ingress controllers, with different capabilities.

In this post, we’ll walk through how to deploy Ambassador on K3s. [Ambassador](https://www.getambassador.io) is an open source ingress controller and API Gateway built on Envoy Proxy. Ambassador exposes many of Envoy Proxy’s core features to Kubernetes users, including zero-downtime reloads, advanced traffic management, service mesh integrations (with support for Consul, Linkerd and Istio), observability, TLS termination and flexible APIs for rate limiting and authentication. Ambassador has been extensively [tuned for maximum performance on Kubernetes](https://www.getambassador.io/resources/envoyproxy-performance-on-k8s/) and is designed to run with minimal resources.

## Deploying K3s with Ambassador

By default, K3s deploys with Traefik as an ingress controller. To use Ambassador and Envoy Proxy, follow these steps. (These steps assume you’ve installed K3s already; if you haven’t, [this quick start](https://rancher.com/docs/k3s/latest/en/quick-start/) will get you going.)

1. Start K3s with the `--disable traefik` option. You can do this by editing `/etc/systemd/system/k3s.service` and editing the `ExecStart` line:

   ```
   ExecStart=/usr/local/bin/k3s 
   server 
   --disable traefik
   ```
2. Restart K3s

   ```
   sudo systemctl daemon-reload
   sudo systemctl restart k3s.service
   ```
3. Install Ambassador by applying the standard Ambassador Kubernetes manifests. ([Ambassador also supports Helm](https://www.getambassador.io/docs/latest/topics/install/helm/)).

   ```
   kubectl apply -f https://www.getambassador.io/yaml/ambassador/ambassador-crds.yaml
   kubectl apply -f https://www.getambassador.io/yaml/ambassador/ambassador-rbac.yaml
   kubectl apply -f https://www.getambassador.io/yaml/ambassador/ambassador-service.yaml
   ```
4. Now we’ll deploy a sample service. Save the below Kubernetes YAML into a file called `quote.yaml.`

   ```
   ---
   apiVersion: v1
   kind: Service
   metadata:
       name: quote
   spec:
       ports:
       -   name: http
           port: 80
           targetPort: 8080
       selector:
           app: quote
   ---
   apiVersion: apps/v1
   kind: Deployment
   metadata:
       name: quote
   spec:
       replicas: 1
       selector:
           matchLabels:
               app: quote
       strategy:
           type: RollingUpdate
       template:
           metadata:
               labels:
                   app: quote
           spec:
               containers:
               -   name: backend
                   image: docker.io/datawire/quote:0.4.1
                   ports:
                   -   containerPort: 8080
   ---
   apiVersion: getambassador.io/v2
   kind: Mapping
   metadata:
       name: quote-backend
   spec:
       prefix: /give-me-a-quote/
       service: quote
   ```
5. Deploy the quote service to K3s: `kubectl apply -f quote.yaml`
6. Ambassador supports the standard Kubernetes ingress resource for routing. Ingress resources are monolithic objects that include both configuration for the ingress itself (e.g., TLS configuration) as well as routes. The official ingress standard is fairly limited, however, so most Ambassador users rely on a [Mapping](https://www.getambassador.io/docs/latest/topics/using/intro-mappings/), which is an Ambassador-specific Custom Resource Definition. Mapping resources are fully decoupled from Ambassador deployment, enabling Mapping resources just to describe request routes. Save the below YAML configuration into a file called quote-mapping.yaml.

   ```
   ---
   apiVersion: getambassador.io/v2
   kind: Mapping
   metadata:
   name: quote-backend
   spec:
   prefix: /give-me-a-quote/
   service: quote
   ```
7. Apply the configuration to the cluster: `kubectl apply -f quote-mapping.yaml`
8. Get the IP address of the Ambassador LoadBalancer service:

   ```
   $ sudo kubectl get svc
   NAME               TYPE           CLUSTER-IP      EXTERNAL-IP    PORT(S)          AGE
   kubernetes         ClusterIP      10.43.0.1       <none>         443/TCP          60m
   ambassador-admin   NodePort       10.43.134.74    <none>         8877:31032/TCP   5m15s
   ambassador         LoadBalancer   10.43.61.86     10.128.0.111   80:31347/TCP     89s
   quote              ClusterIP      10.43.129.249   <none>         80/TCP           31s
   ```
9. Copy the IP address, and test the configuration: `curl http://<IP address>/give-me-a-quote/:`

   ```
   $ curl 10.128.0.111/give-me-a-quote/
   {
   "server": "harmonious-strawberry-z6onbsu2",
   "quote": "A small mercy is nothing at all?",
   "time": "2020-07-15T13:59:50.716712445Z"
   }
   ```

Congratulations! You’ve successfully used Ambassador to route an HTTP request to the quote service.

## Conclusion

Ambassador provides a broad set of capabilities, including [authentication](https://www.getambassador.io/products/edge-stack/api-gateway/security-authentication/), rate limiting and broad protocol support (e.g., TCP, WebSockets, gRPC, HTTP). Ambassador also has a set of tested integrations with other cloud-native infrastructures, such as monitoring systems and service mesh. Together, K3s and Ambassador are a powerful lightweight Kubernetes solution for both development and production.

The certified Kubernetes distribution built for IoT & Edge computing[Download K3S](https://k3s.io/)
