---
title: "CICD Debates: Drone vs Jenkins"
date: 2018-01-31T11:28:00
slug: "cicd-debates-drone-vs-jenkins"
author: "Rancher Admin"
products: ["Kubernetes (generic)"]
tags: ["ci-cd"]
content_type: "opinion"
draft: true
migration:
  wp_id: 87234
  original_url: "https://www.suse.com/c/rancher_blog/cicd-debates-drone-vs-jenkins/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "2018 CI tool comparison"
  redirect_target: "rancher.com/blog (hub)"
---

[![cicd-dronejenkins](images/rancher_blog_cicd-dronejenkins.jpg)](images/rancher_blog_cicd-dronejenkins.jpg)

## Introduction

Jenkins has been the industry standard CI tool for years. It contains a multitude of functionalities, with almost 1,000 plugins in its ecosystem, this can be daunting to some who appreciate simplicity. Jenkins also came up in a world before containers, though it does fit nicely into the environment. This means that there is not a particular focus on the things that make containers great, though with the inclusion of Blue Ocean and pipelines, that is rapidly changing.

Drone is an open source CI tool that wears simple like a badge of honor. It is truly Docker native; meaning that all actions take place within containers. This makes it a perfect fit for a platform like Kubernetes, where launching containers is an easy task.

Both of these tools walk hand in hand with Rancher, which makes standing up a robust Kubernetes cluster an automatic process. I’ve used Rancher 1.6 to deploy a K8s 1.8 cluster on GCE; as simple as can be.

##### Build a CI/CD Pipeline with Kubernetes and Rancher

![]()
Recorded Online Meetup of best practices and tools for building pipelines with containers and kubernetes.

[Watch the training](https://rancher.com/events/2018/2018-08-07-onlinemeetup-building-a-cicd-pipeline-with-k8s/)

This article will take Drone deployed on Kubernetes (on Rancher), and compare it to Jenkins across three categories:

- Platform installation and management
- Plugin ecosystem
- Pipeline details

In the end, I’ll stack them up side by side and try to give a recommendation. As usually is the case however, there may not be a clear winner. Each tool has its core focus, though by nature there will be overlap.

## Prereqs

Before getting started, we need to do a bit of set up. This involves setting up Drone as an authorized Oauth2 app with a Github account. You can see the settings I’ve used here. All of this is contained within the Drone documentation.

There is one gotcha which I encountered setting up Drone. Drone maintains a passive relationship with the source control repository. In this case, this means that it sets up a webhook with Github for notification of events. The default behavior is to build on push and PR merge events. In order for Github to properly notify Drone, the server must be accessible to the world. With other, on-prem SCMs, this would not be the case, but for the example described here it is. I’ve set up my Rancher server on GCE, so that it is reachable from Github.com.

Drone installs from a container through a set of deployment files, just like any other Kubernetes app. I’ve adapted the deployment files found in this repo. Within the config map spec file, there are several values we need to change. Namely, we need to set the Github-related values to ones specific to our account. We’ll take the client secret and client key from the setup steps and place them into this file, as well as the username of the authorized user. Within the drone-secret file, we can place our Github password in the appropriate slot.

This is a major departure from the way Jenkins interacts with source code. In Jenkins, each job can define its relationship with source control independent of another job. This allows you to pull source from a variety of different repositories, including Github, Gitlab, svn, and others. As of now, Drone only supports git-based repos. A full list is available in the documentation, but all of the most popular choices for git-based development are supported.

We also can’t forget our Kubernetes cluster! Rancher makes it incredibly easy to launch and manage a cluster. I’ve chosen to use latest stable version of Rancher, 1.6. We could’ve used the new Rancher 2.0 tech preview, but constructing this guide worked best with the stable version. however, the information and steps to install should be the same, so if you’d like to try it out with newer Rancher, go ahead!

## Task 1 - Installation and Management

Launching Drone on Kubernetes and Rancher is as simple as copy paste. I used the default K8s dashboard to launch the files. Uploading them one by one, starting with the namespace and config files, will get the ball rolling. [Here are some of the deployment files I used](https://github.com/appleboy/drone-on-kubernetes/tree/master/gke). I pulled from this repository and made my own local edits. This repo is owned by a frequent Drone contributor, and includes instructions on how to launch on GCE, as well as AWS. The Kubernetes yaml files are the only things we need here. To replicate, just edit the ConfigMap file with your specific values. Check out one of my files below.

```
yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: drone-server
namespace: drone
spec:
replicas:  1
template:
metadata:
labels:
app: drone-server
spec:
containers:
- image: drone/drone:0.8
imagePullPolicy:  Always
name:  drone-server
ports:
- containerPort: 8000
protocol:  TCP
- containerPort: 9000
protocol: TCP
volumeMounts:
# Persist our configs in an SQLite DB in here
- name: drone-server-sqlite-db
mountPath: /var/lib/drone
resources:
requests:
cpu: 40m
memory: 32Mi
env:
- name: DRONE_HOST
valueFrom:
configMapKeyRef:
name: drone-config
key: server.host
- name: DRONE_OPEN
valueFrom:
configMapKeyRef:
name: drone-config
key: server.open
- name:DRONE_DATABASE_DRIVER
valueFrom:
configMapKeyRef:
name: drone-config
key: server.database.driver
- name: DRONE_DATABASE_DATASOURCE
valueFrom:
configMapKeyRef:
name: drone-config
key: server.database.datasource
- name: DRONE_SECRET
valueFrom:
secretKeyRef:
name: drone-secrets
key: server.secret
- name: DRONE_ADMIN
valueFrom:
configMapKeyRef:
name: drone-config
key: server.admin
- name: DRONE_GITHUB
valueFrom:
configMapKeyRef:
name: drone-config
key: server.remote.github
- name: DRONE_GITHUB_CLIENT
valueFrom:
configMapKeyRef:
name: drone-config
key: server.remote.github.client
- name: DRONE_GITHUB_SECRET
valueFrom:
configMapKeyRef:
key: server.remote.github.secret
- name: DRONE_DEBUG
valueFrom:
configMapKeyRef:
name: drone-config
key: server.debug

volumes:
- name: drone-server-sqlite-db
hostPath:
path: /var/lib/k8s/drone
- name: docker-socket
hostPath:
path: /var/run/docker.sock
```

Jenkins can be launched in much the same way. Because it is deployable in a Docker container, you can construct a similar deployment file and launch on Kubernetes. Here’s an example below. This file was taken from the GCE examples repo for the Jenkins CI server.

```
yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
name: jenkins
namespace: jenkins
spec:
replicas: 1
template:
metadata:
labels:
app: master
spec:
containers:
- name: master
image: jenkins/jenkins:2.67
ports:
- containerPort: 8080
- containerPort: 50000
readinessProbe:
httpGet:
path: /login
port: 8080
periodSeconds: 10
timeoutSeconds: 5
successThreshold: 2
failureThreshold: 5
env:
- name: JENKINS_OPTS
valueFrom:
secretKeyRef:
name: jenkins
key: options
- name: JAVA_OPTS
value: '-Xmx1400m'
volumeMounts:
- mountPath: /var/jenkins_home
name: jenkins-home
resources:
limits:
cpu: 500m
memory: 1500Mi
requests:
cpu: 500m
memory: 1500Mi
volumes:
- name: jenkins-home
gcePersistentDisk:
pdName: jenkins-home
fsType: ext4
partition: 1
```

Launching Jenkins is similarly easy. Because of the simplicity of Docker and Rancher, all you need to do is take the set of deployment files and paste them into the dashboard. My preferred way is using the Kubernetes dashboard for all management purposes. From here, I can upload the Jenkins files one by one to get the server up and running.

Managing the Drone server comes down to configurations passed when launching. Hooking up to Github involved adding OAuth2 tokens, as well as (in my case) a username and password to access a repository. changing this would involve either granting organization access through GIthub, or relaunching the server with new credentials. This could possibly hamper development, as it means that Drone cannot handle more than one source provider. As mentioned above, Jenkins allows for any number of source repos, with the caveat that each job only uses one.

## Task 2 - Plugins

Plugins in Drone are very simple to configure and manage. In fact, there isn’t much you need to do to get one up and running. The ecosystem is considerably smaller than that for Jenkins, but there are still plugins for almost every major tool available. There are plugins for most major cloud providers, as well as integrations with popular source control repos. As mentioned before, containers in Drone are first class citizens. This means that each plugin and executed task is also a container.
Jenkins is the undisputed king of plugins. If you can think of the task, there is probably a plugin to accomplish it. There are at last glance, almost 1000 plugins available for use. The downside of this is that it can sometimes be difficult to determine, out of a selection of similar looking plugins, which one is the best choice for what you’re trying to accomplish

There are docker plugins for building pushing and images, AWS and K8s plugins for deploying to clusters, and various others. Because of the comparative youth of the Drone platform, there are a great deal fewer plugins available here than for Jenkins. That does not however, take away from their effectiveness and ease of use. A simple stanza in a drone.yml file will automatically download, configure, and run a selected plugin, with no other input needed. And remember, because of Drone’s relationship with containers, each plugin is maintained within an image. There are no extra dependencies to manage; if the plugin creator has done their job correctly, everything will be contained within that container.

When I built the drone.yml file for the simple node app, adding a Docker plugin was a breeze. There were only a few lines needed, and the image was built and pushed to a Dockerhub repo of my choosing. In the next section, you can see the section labeled docker. This stanza is all that’s needed to configure and run the plugin to build and push the Docker image.

## Task 3

The last task is the bread and butter of any CI system. Drone and Jenkins are both designed to build apps. Originally, Jenkins was targeted towards java apps, but over the years the scope has expanded to include anything you could compile and execute as code. Jenkins even excels at new pipelines and cron-job like scheduled tasks. However, it is not container native, though it does fit very well into the container ecosystem.

```
yaml
pipeline:
  build:
    image: node:alpine
    commands:
      - npm install
      - npm run test
      - npm run build
  docker:
    image: plugins/docker
    dockerfile: Dockerfile
    repo: badamsbb/node-example
    tags: v1
```

For comparison, here’s a Jenkinsfile for the same app.

```
groovy
#!/usr/bin/env groovy
pipeline {
 agent {
  node {
   label 'docker'
  }
 }
 tools {
  nodejs 'node8.4.0'
 }
 stages {
  stage ('Checkout Code') {
   steps {
    checkout scm
   }
  }
  stage ('Verify Tools'){
   steps {
    parallel (
     node: {
       sh "npm -v"
     },
     docker: {
       sh "docker -v"
     }
    )
   }
  }
  stage ('Build app') {
   steps {
    sh "npm prune"
    sh "npm install"
   }
  }
  stage ('Test'){
   steps {
    sh "npm test"
   }
  }
  stage ('Build container') {
   steps {
    sh "docker build -t badamsbb/node-example:latest ."
    sh "docker tag badamsbb/node-example:latest badamsbb/node-example:v${env.BUILD_ID}"
   }
  }
  stage ('Verify') {
   steps {
    input "Everything good?"
   }
  }
  stage ('Clean') {
   steps {
    sh "npm prune"
    sh "rm -rf node_modules"
   }
  }
 }
}
```

While this example is verbose for the sake of explanation, you can see that accomplishing the same goal, a built Docker image, can be more involved than with Drone. In addition, what’s not pictured is the set up of the interactions between Jenkins and Docker. Because Jenkins is not Docker native, agent must be configured ahead of time to properly interact with the Docker daemon. This can be confusing to some, which is where Drone comes out ahead. It is already running on top of Docker; this same Docker is used to run its tasks.

## Conclusion

Drone is a wonderful piece of CI software. It has quickly become a very popular choice for wanting to get up and running quickly, looking for a simple container-native CI solution. The simplicity of it is elegant, though as it is still in a pre-release status, there is much more to come. Adventurous engineers may be willing to give it a shot in production, and indeed many have. In my opinion, it is best suited to smaller teams looking to get up and running quickly. Its small footprint and simplicity of use lends itself readily to this kind of development.

However, Jenkins is the tried and true powerhouse of the CI community. It takes a lot to topple the king, especially one so entrenched in his position. Jenkins has been very successful at adapting to the market, with Blue Ocean and container-based pipelines making strong cases for its staying power. Jenkins can be used by teams of all sizes, but excels at scale. Larger organizations love Jenkins due to its history and numerous integrations. It also has distinct support options, either active community support for open source, or enterprise-level support through CloudBees But as with all tools, both Drone and Jenkins have their place within the CI ecosystem.

To learn more about building a CI/CD pipeline on Kubernetes, check out the [video recording](https://rancher.com/events/2018/2018-08-07-onlinemeetup-building-a-cicd-pipeline-with-k8s/ "Video Tutorial on CI/CD on Kubernetes") of our meetup on CI/CICD.

### Bio

**Brandon Adams**
Certified Jenkins Engineer, and Docker enthusiast. I’ve been using Docker since the early days, and love hearing about new applications for the technology. Currently working for a Docker consulting partner in Bethesda, MD.
