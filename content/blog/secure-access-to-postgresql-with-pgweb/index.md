---
title: "Secure Access to PostgreSQL with Pgweb"
date: 2020-08-05T11:50:00
slug: "secure-access-to-postgresql-with-pgweb"
author: "Rancher Admin"
image: "images/rancher_blog_postgres-featured.png"
products: ["Kubernetes (generic)"]
tags: ["developer-experience", "security"]
content_type: "tutorial"
draft: false
migration:
  wp_id: 87344
  original_url: "https://www.suse.com/c/rancher_blog/secure-access-to-postgresql-with-pgweb/"
  disposition: migrate_refresh
  commercial: false
  outdated_reason: "Old versions and manifests"
  redirect_target: ""
---

Read our free white paper: How to Build a Kubernetes Strategy [Download Now](https://more.suse.com/fy21-global-web-landing-page-how-to-build-enterprise-kubernetes-strategy)

## Introduction to PostgreSQL and Pgweb

PostgreSQL is an open source database known for its reliability and performance. It’s used across many industries and applications, and is especially a favorite of web developers. All major web frameworks support PostgreSQL natively, from node.js and Django to Rails and Spring, so its adaptation is relatively broad across the internet for site backend systems.

As with any database, developers need tools to work with them. [Pgweb](http://sosedoff.github.io/pgweb/) is an open source, web-based client for PostgreSQL. It has an incredibly clean interface that lets you connect to any PostgreSQL instance to browse tables, run queries and export data. It’s much more lightweight and convenient for light database work than apps like pgAdmin.

On the security side, opening up a database port to the internet is always a terrible idea. Devs who need quick access to debug production databases running on their Kubernetes cluster can set up Pgweb in several ways to keep databases secure and maintain their security posture. One example is to deploy Pgweb into the same cluster as your database and expose it publicly while keeping the database ports accessible only inside the network. Put Pgweb behind an [Oauth2 proxy](https://kubernetes.github.io/ingress-nginx/examples/auth/oauth-external-auth/) for an extra layer of authentication and voilà, super easy and super secure database access from anywhere.

Pgweb can run locally on Linux, macOS or Windows, but we’re going to explore deploying it into your Kubernetes cluster today. In this blog, we’ll deploy the Pgweb image as a pod into our cluster, expose it using a Kubernetes service, deploy PostgreSQL and expose it (but only within the cluster for max security), then connect to the database. Finally, we will redeploy everything via Rancher as a workload and see how much easier Rancher makes getting your applications up and running.

![Image 01](images/rancher_blog_image-01.jpg)

## Prerequisites

To complete this guide, you will need the following:

- A Rancher deployment (check out the [Quick Start guide](https://rancher.com/quick-start/) to get Rancher up and running)
- A Kubernetes cluster, managed by Rancher (follow [this guide](https://rancher.com/docs/rancher/v2.x/en/cluster-provisioning/) to either import or provision a cluster)

## Deploy Pgweb

Create a new file called `pgweb.yaml`, paste the following into it, then apply the file to deploy your pod and service.

```
apiVersion: v1
kind: Pod
metadata:
  labels:
    run: pgweb
  name: pgweb
spec:
  containers:
    - image: sosedoff/pgweb
      name: pgweb
      ports:
        - containerPort: 8081
---
apiVersion: v1
kind: Service
metadata:
  labels:
    run: pgweb
  name: pgweb-svc
spec:
  ports:
    - port: 8081
      targetPort: 8081
      protocol: TCP
  type: NodePort
  selector:
    run: pgweb
```

```
kubectl apply -f pgweb.yaml
pod/pgweb created
service/pgweb-svc created
```

Then get information on the service to find which node port is in use; in this case, it is 31338. Yours will probably differ but will be in the 30000-32767 range.

```
kubectl get svc pgweb-svc
NAME            TYPE       CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
pgweb-svc       NodePort   10.96.47.248   <none>        8081:31338/TCP   9s
```

Now go to a public IP of one of your nodes on that port in a browser. Finding your public IP and how to open necessary firewall ports varies greatly depending on your setup, but if all is well you should be greeted by the Pgweb login page:

![Image 02](images/rancher_blog_image-02.jpg)

If you have problems accessing the node port, [port forwarding](https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/) works in a pinch.

Now we need a database to access.

## Deploy a PostgreSQL with Sample Data

Just like with Pgweb, we’re going to deploy PostgreSQL in Kubernetes using a YAML manifest. This one is slightly different. We’ll be keeping the default service type of ClusterIP, as we do not want the database accessible from outside of the cluster. Otherwise, all our security-conscience setup is for nothing.

[The image we’re using](https://hub.docker.com/r/ghusta/postgres-world-db) is a standard PostgreSQL image, but with sample country data already preloaded.

Copy the following to `postgres.yaml` and apply the manifest:

```
apiVersion: v1
kind: Pod
metadata:
  labels:
    run: postgres
  name: postgres
spec:
  containers:
    - image: ghusta/postgres-world-db
      name: postgres
      ports:
        - containerPort: 5432
---
apiVersion: v1
kind: Service
metadata:
  labels:
    run: postgres
  name: postgres-svc
spec:
  ports:
    - port: 5432
      targetPort: 5432
      protocol: TCP
  selector:
    run: postgres
```

```
kubectl apply -f postgres.yaml
pod/postgres created
service/postgres-svc created
```

## Connect to the Database via Cluster DNS

Now go back to our Pgweb login page and login with the following info:

Host: postgres-svc.default.svc.cluster.local

Username: world

Password: world123

Database: world-db

SSL Mode: Disable

Now you’re connected to the database. Click “city” under the list of tables of the left:

![Image 03](images/rancher_blog_image-03.jpg)

Notice the host name we used. This is [Kubernetes’ internal DNS at work](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/), allowing you to connect to services by name instead of pod IP. The first part is the service name, which we defined in the `postgres.yaml` file. The second part is the namespace your service is deployed in – `default` in this case. Next, `svc` explicitly states that we’re using a service name (you can also specify a pod by name). Finally, `cluster.local` is the cluster’s default DNS name. This structure makes it easy to wire together pods and take advantage of how services gracefully handle replicas and isolate pods that go offline.

Back to Pgweb, click “Query” at the top and try querying the database for cities in New Zealand:

```
SELECT * FROM city WHERE country_code like 'NZL'
```

Or cities with a life expectancy over 80 years:

```
SELECT * FROM country WHERE life_expectancy > 80
```

Take as much time as you would like to play with the data, as if you were a developer troubleshooting an application connecting to this database. When you are ready to continue, delete the resources from your cluster for the next section:

```
kubectl delete -f pgweb.yaml
kubectl delete -f postgres.yaml
```

## Redeploy Using Rancher

Now we’re going to redeploy the same configuration, but this time use Rancher to deploy the workloads instead of Kubernetes manifest files.

1. From the Global view, open the project that you want to deploy the workload to (default is fine if you don’t have other projects already).
2. We could import our YAML files, but let’s walk through using the GUI to build out our configuration instead, click **Deploy**.
3. **Name** it `pgweb` and set the **Docker Image** to `sosedoff/pgweb`.
4. Click **Add Port**, name it `pgweb-svc` and set the container port to `8080`.
5. Click **Launch**, and Rancher will deploy your pod into the cluster.
6. Now repeat for the PostgreSQL pod, naming it appropriately and using `ghusta/postgres-world-db` for the image. The **container port** will be 5432 and change the service type to `Cluster IP.`
7. On the page listing your workloads, you will see the node port assigned to the Pgweb cluster, use that to access the Pgweb login page and login with the same credentials.
8. Back on your terminal, run `kubectl get pods` and `kubectl get svc` to see the pods and services Rancher deployed.

Accessing Pgweb on your cluster’s public IP and connecting to the database will work the same as when deployed both through Kubernetes manifest files.

## Conclusion

In this blog, we’ve learned about PostgreSQL as a database of choice for web developers and the Pgweb client. We deployed it to our Kubernetes cluster manually using manifest files, then redeployed it using Rancher. We saw how Rancher eliminated some of the overhead involved in deploying and editing application pods. Hopefully, you can take what you’ve learned from deploying these resources and further practice by setting up other applications that communicate between multiple pods, such as WordPress or your custom web app.Read our free white paper: How to Build a Kubernetes Strategy [Download Now](https://more.suse.com/fy21-global-web-landing-page-how-to-build-enterprise-kubernetes-strategy)
