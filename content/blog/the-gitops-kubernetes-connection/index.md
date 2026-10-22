---
title: "The GitOps Kubernetes Connection"
date: 2020-02-28T09:49:00
slug: "the-gitops-kubernetes-connection"
author: "Rancher Admin"
image: "images/rancher_blog_gitops-kubernetes-featured-image.svg"
products: ["Kubernetes (generic)"]
tags: ["gitops"]
content_type: "explainer"
draft: false
migration:
  wp_id: 86109
  original_url: "https://www.suse.com/c/rancher_blog/the-gitops-kubernetes-connection/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

In the first article in this series, we talked about [making Kubernetes essential to your DevOps pipeline](/blog/kubernetes-devops-a-powerful-pair/). We reviewed CI/CD and DevOps and why their relationship with Kubernetes is so powerful.

In this article, I’m going to dive into another term in the application development and management mix: **GitOps**. We’ll cover what GitOps is, how it affects an organization and how it aligns with Kubernetes.

## What is GitOps?

GitOps is a process that leverages the Git developer toolset for operations and management of cloud-native applications. Git is the single source of truth when deploying applications to Kubernetes. When developers make changes to the application, Git automatically pushes them to Kubernetes for deployment. Further, if there are changes to the running state within Kubernetes that are inconsistent with the state within Git, they are reverted to the known state from within Git.

## GitOps and CI/CD: What’s the Connection?

GitOps and CI/CD (continuous integration/continuous delivery or deployment) have an important working relationship. As a refresher, CI/CD lets developers continuously iterate, develop and deploy applications. Often the iteration is through a Git repository (although there can be other repositories) that flows through a toolset for pipelines. During the deployment/delivery phase, the built container-based application is “pushed” to Kubernetes for deployment. The operation of GitOps enhances the CI/CD model by using a “pull” method via Kubernetes, bringing the operational aspect into deployment/delivery.

But what happens if someone changes something running within the Kubernetes cluster? We’d use Git as the primary source of truth as a declarative deployment tool and leverage additional tools to alert us when there is divergence. By leveraging tools that can identify differences between running and declared state, Kubernetes remediates to the known/declared operating state.

**Note:** Continuous integration and continuous development are complementary but separate processes. In an optimal state, GitOps enables batch size as single-piece-flow, where work happens one unit at a time. However, since CI and CD processes occur in different groups, the process may vary from one organization to another.

## GitOps and the Application Lifecycle

Let’s look at this through the application lifecycle lens. During a typical lifecycle, an application goes through multiple states. These include:

- code
- build
- image creation
- test
- release

With GitOps, we extend that list to include:

- deploy
- monitor changes within git repository
- log changes and events
- alert when a change has occurred and integrate with existing monitoring/alerting systems
- update

Under the GitOps operating model, when an application is released, Kubernetes ensures that it operates as intended. Kubernetes also manages the operation of the application by ensuring its stability and availability. If a developer changes the application via Git, Kubernetes takes the declaration and applies it as required.

## What GitOps Brings to the Table

In summary, here’s what GitOps is, and what it can do for you:

- GitOps provides an operating model for applications that ensures Git provides the framework to unify the running, operating and continuous development of an application.
- As part of the CI/CD pipeline, GitOps provides the glue between the application build/delivery and the operations of where to run it.
- Git provides a single source of truth for both the development and operations of the application within a Kubernetes platform.
- Application delivery and ongoing platform management are declarative and can be version controlled.
- Git controls rollback, upgrades and changes.
- Developers don’t need to know or operate the operational platform (such as Kubernetes).
- Git controls and remediates divergence, or “drift.”
- GitOps leverages auditing, monitoring and rollback capabilities to increase reliability and stability of application releases.

In closing, while there’s a lot more to operating in GitOps mode, there’s a clear synergy between GitOps, DevOps and existing CI/CD patterns. GitOps provides a model for delivering applications to a Kubernetes platform that ensures a single source of truth and leverages all of the operational features of Kubernetes. GitOps is not a tool replacement. Quite the opposite: GitOps augments your processes, increases maturity and helps teams deliver (and operate) applications by leveraging declarative processes and tools.

## See GitOps In Action: FluxCD Demo

FluxCD (or Flux) is a great tool for integrating Kubernetes and Git. Flux is a Kubernetes Operator that you, as the administrator, install into Kubernetes to manage the integration between Git and native Kubernetes. Within Kubernetes, an Operator is an extension of the native Kubernetes platform as a pattern for custom resources that are used to manage applications and their components. This means that, with the aid of the Operator inside Kubernetes, the desired state – as represented within the running state – will continually check and adjust to align with what the Git repository declares. Flux can integrate with your existing CI/CD toolsets for additional workflow, permissions and auditing. Within Kubernetes, Flux monitors Git repositories that you declare (through configuration) for changes and will update Kubernetes to that desired running state, should changes occur locally on a Kubernetes pod that shouldn’t be changed. Remember, Git is the source of truth. The Flux Operator will detect this and change the running configuration back to the declared state from Git.

In the following demo, I’ll show you how to install and implement Flux.

### Pre-Requisites

You Will Need

- a Docker hub repository where you can upload the Flaskapp docker image
- A Git Repo that you can connect to replace anything within “< >” with your settings as required throughout this demonstration

### Steps

- Install Kubernetes
- Install and configure fluxctl, the native installer for Flux deployment
- Configure Flux to connect to Git Repo
- Update deployment manifest in Git Repo
- Update Container image and Sync
- Configuration drift and Sync

You can use the following configuration for testing/demonstration purposes. It includes the Docker file for the Flask application, as well as the Kubernetes deployment/configuration files. You will need these as part of the demonstration and can uploaded them to your nominated GIT repository.

### Docker File

```
    FROM python:3

    RUN pip install flask

    RUN mkdir -p /corp/app
    WORKDIR /corp/app
    COPY main.py .
    ENV FLASK_APP=/corp/app/main.py

    ENV APP_NAME=MyApp.DevOps
    ENV APP_VERSION=v1.0.0

    CMD ["flask", "run", "--host=127.0.0.1"]
```

### `main.py` Python Script File

```
import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    appname = os.environ['APP_NAME']
    appversion = os.environ['APP_VERSION']

    response = "%s - %s.%sn" %('Hello World', appname, appversion)
    return response
```

### Kubernetes Deployment File

```
apiVersion: v1
kind: Namespace
metadata:
  name: my-demo
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: fluxdemo
  namespace: my-demo
  annotations:
    flux.weave.works/tag.flask: glob:develop-v*
    flux.weave.works/automated: 'true'
  labels:
    role: fluxdemo
    env: demo
    app: flux
spec:
  replicas: 1
  selector:
    matchLabels:
      role: fluxdemo
  template:
    metadata:
      labels:
        role: fluxdemo
    spec:
      containers:
      - name: nginx
        image: nginx:1.16-perl
        imagePullPolicy: IfNotPresent
        ports:
        - name: http
          containerPort: 80
        volumeMounts:
        - name: nginx-proxy-config
          mountPath: /etc/nginx/conf.d/default.conf
          subPath: nginx.conf
      - name: flask
        image: docker.io/<your docker repo>/flaskapp:develop-v1.8.0
        imagePullPolicy: IfNotPresent
        ports:
        - name: http
          containerPort: 5000
        env:
        - name: APP_NAME
          value: myfluxdemo.K8s.GitOps
        - name: APP_VERSION
          value: v1.0.5
      volumes:
      - name: nginx-proxy-config
        configMap:
          name: nginx-conf
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: nginx-conf
  namespace: my-demo
data:
  nginx.conf: |-
    #CODE1.0:
    #add the nginx.conf configuration - this will be referenced within the deployment.yaml
    server {
        listen 80;
        server_name localhost;

        location / {
            proxy_pass http://localhost:5000/;
            proxy_set_header Host "localhost";
        }
    }
```

### Install Flux

- [Install Fluxctl](https://docs.fluxcd.io/en/1.18.0/references/fluxctl.html)
- [Install Fluxcd](https://docs.fluxcd.io/en/1.18.0/tutorials/get-started.html)

### Configure Flux for Repo

#### Create a Namespace

```
kubectl create ns <namespace>
export FLUX_FORWARD_NAMESPACE= <namespace>
fluxctl list-workloads
```

#### Install Fluxcd to create connection to your Git Repo

```
export GHUSER=""
export REPO="gitops-demo"
export NS="flux"
fluxctl install 
--git-user=${GHUSER} 
--git-email=${GHUSER}@users.noreply.github.com 
--git-url=git@github.com:
Image download failed.
{REPO} 
--namespace=${NS} | kubectl apply -f -
```

### Create SSH Key for Adding to Your GitHub Repository

Type the following in your terminal to obtain the key you will need for the next step.

```
fluxctl identity
```

Open GitHub, navigate to the Repository added when you installed Fluxcd, go to Setting > Deploy keys, click on Add deploy key, give it a title, check Allow write access, paste the public key and click Add key.

### Update Deployment Manifest in Git Repo

- Open up your GitRepo that has the `deployment.yaml` file
- Scroll down to the section as below and change the APP\_VERSION number

```
    env:
    - name: APP_NAME
      value: myfluxdemo.K8s.GitOps
    - name: APP_VERSION
      value: v1.0.5
```

- Save and Commit the change to your repo

Flux will (within 5 minutes) update your deployment

To test from a localhost, use the “Port-forward” command within Kubernetes:

```
kubectl get pods -n  copy the pod name kubectl port-forward  8080:80 -n
```

Open another terminal:

```
curl -s -i http://localhost:8080
```

### Update Container Image and Sync

Now let’s now make a modification to the Docker image and upload to our Docker hub repository. For this, we will modify the `main.py` file within the `flaskapp` directory.

- Update the `main.py` file. Change `Hello World` to something else

```
response = "%s - %s.%sn" %('Flux World', appname, appversion)
```

- Create a new Docker file and upload to Docker (with another incremental version number)
- Wait 5 minutes - Flux will now automatically deploy new Image

### Configuration Drift and Sync

Now let’s test what happens when there is a manual change to the running configuration

```
kubectl scale deployment/fluxdemo --replicas=4 -n
```

Now let’s watch the pods for a few minutes and see what happens. We will see the additional pods for a short period, but within 5 minutes, we will see the excess number of pods terminate. Therefore, Flux has brought the configuration back to the declared state of deployment currently held within Git.

```
kubectl get po -n  --watch
```

Re-run the same command again and you can see that this view has now filtered down to the just one running pod.

Don’t forget to clean up and remove the deployment and Git connection (if you wish). Otherwise, start adding more repositories and keep on building.

## More Resources

Rancher makes it easier to operate and manage of multi-cluster, hybrid-cloud Kubernetes. It also has built-in tools for developers and other consumers of Kubernetes and computing power.

New to Rancher? [Learn how Rancher works in the technical architecture guide.](https://more.suse.com/fy21-global-web-landing-page-rancher2-technical-architecture)
