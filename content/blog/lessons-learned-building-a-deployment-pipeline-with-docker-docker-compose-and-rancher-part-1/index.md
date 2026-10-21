---
title: "Lessons Learned Building a Deployment Pipeline with Docker, Docker-Compose, and Rancher (Part 1)"
date: 2016-04-04T11:11:00
slug: "lessons-learned-building-a-deployment-pipeline-with-docker-docker-compose-and-rancher-part-1"
author: "Rancher Admin"
products: ["Docker/containers (generic)"]
tags: ["ci-cd"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 86786
  original_url: "https://www.suse.com/c/rancher_blog/lessons-learned-building-a-deployment-pipeline-with-docker-docker-compose-and-rancher-part-1/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Docker Compose pipeline series, 2016"
  redirect_target: "rancher.com/blog (hub)"
---

Build a CI/CD Pipeline with Kubernetes and RancherRecorded Online Meetup of best practices and tools for building pipelines with containers and kubernetes.[Watch the training](https://rancher.com/events/2018/2018-08-07-onlinemeetup-building-a-cicd-pipeline-with-k8s/)

*John Patterson ([@cantrobot](https://twitter.com/cantrobot)) and Chris
Lunsford run This End Out, an operations and infrastructure services
company. You can find them online at*
[*https://www.thisendout.com*](https://thisendout.com/) \*and follow them
on twitter [@thisendout](https://twitter.com/thisendout). \* *Update:
All four parts of the series are now live, you can find them here: [Part
1: Getting started with CI/CD and
Docker](https://rancher.com/lessons-learned-building-a-deployment-pipeline-with-docker-docker-compose-and-rancher-part-1/)*
*[Part 2: Moving to Compose
blueprints](https://rancher.com/lessons-learned-building-a-continuous-deployment-pipeline-with-docker-docker-compose-and-rancher-part-2/)*
*[Part 3: Adding Rancher for
Orchestration](https://rancher.com/lessons-learned-building-a-deployment-pipeline-with-docker-docker-compose-and-rancher-part-3/)[Part
4: Completing the Cycle with Service
Discovery](https://rancher.com/lessons-learned-building-a-deployment-pipeline-with-docker-docker-compose-and-rancher-part-4/)*
This post is the first in a series in which we’d like to share the story
of how we implemented a container deployment workflow using Docker,
Docker-Compose and Rancher. Instead of just giving you the polished
retrospective, though, we want to walk you through the evolution of the
pipeline from the beginning, highlighting the pain points and decisions
that were made along the way. Thankfully, there are many great resources
to help you set up a continuous integration and deployment workflow with
Docker. This is not one of them! A simple deployment workflow is
relatively easy to set up. But our own experience has been that building
a deployment system is complicated mostly because the easy parts must be
done alongside the legacy environment, with many dependencies, and while
changing your dev team and ops organization to support the new
processes. Hopefully, our experience of building our pipeline the hard
way will help you with the hard parts of building yours. In this first
post, we’ll go back to the beginning and look at the initial workflow we
developed using just Docker. In future posts, we’ll progress through the
introduction of Docker-compose and eventually Rancher into our workflow.
To set the stage, the following events all took place at a
Software-as-a-Service provider where we worked on a long-term services
engagement. For the purpose of this post, we’ll call the company Acme
Business Company, Inc., or ABC. This project started while ABC was in
the early stages of migrating its mostly-Java micro-services stack from
on-premise bare metal servers to Docker deployments running in Amazon
Web Services (AWS). The goals of the project were not unique: lower lead
times on features and better reliability of deployed services. The plan
to get there was to make software deployment look something like this:
[![CD Part 1
software-deployment-workflow_edited](images/rancher_blog_CD-Part-1-software-deployment-workflow_edited-1024x192.jpg)](https://cdn.rancher.com/wp-content/uploads/2016/03/18024249/CD-Part-1-software-deployment-workflow_edited.jpg)
The process starts with the code being changed, committed, and pushed to
a git repository. This would notify our CI system to run unit tests,
and if successful, compile the code and store the result as an
artifact. If the previous step was successful, we trigger another job
to build a Docker image with the code artifact and push it to a private
Docker registry. Finally, we trigger a deployment of our new image to
an environment. The necessary ingredients are these:

- A source code repository. ABC already had its code in private
  GitHub repository.
- A continuous integration and deployment tool. ABC had a local
  installation of Jenkins already.
- A private registry. We deployed a Docker registry container, backed
  by S3.
- An environment with hosts running Docker. ABC had several target
  environments, with each target containing both a staging and
  production deployment.

When viewed this way, the process is deceptively simple. The reality
on the ground, though, is a bit more complicated. Like many other
companies, there was (and still is) an organizational divide between
development and operations. When code is ready for deployment, a ticket
is created with the details of the application and a target
environment. This ticket is assigned to operations and scheduled for
execution during the weekly deployment window. Already, the path to
continuous deployment and delivery is not exactly clear. In the
beginning, the deployment ticket might have looked something like this:

```
DEPLOY-111:
App: JavaService1, branch "release/1.0.1"
Environment: Production
```

The deployment process:

- The deploy engineer for the week goes to Jenkins and clicks “Build
  Now” for the relevant project, passing the branch name as a
  parameter. Out pops a tagged Docker image which is automatically
  pushed into the registry. The engineer selects a Docker host in the
  environment that is not currently active in the load balancer. The
  engineer logs in and pulls the new version from the registry

```
docker pull registry.abc.net/javaservice1:release-1.0.1
```

- Finds the existing container

```
docker ps
```

- Stops the existing container.

```
docker stop [container_id]
```

- Starts a new container with all of the necessary flags to launch the
  container correctly. This can be borrowed from the previous running
  container, the shell history on the host, or it may be documented
  elsewhere.

```
docker run -d -p 8080:8080 … registry.abc.net/javaservice1:release-1.0.1
```

- Pokes the service and does some manual testing to verify that it is
  working.

```
curl localhost:8080/api/v1/version
```

- During the production maintenance window, updates the load-balancer
  to point to the updated host.

- Once verified, the update is applied to all of the other hosts in
  the environment in case a failover is required.

Admittedly, this deployment process isn’t very impressive, but it’s a
great first step towards continuous deployment. There are plenty of
places to improve, but consider the benefits:

- The ops engineer has a recipe for deployment and every application
  deploys using the same steps. The parameters for the Docker run
  step have to be looked up for each service, but the general cadence
  is always the same: Docker pull, Docker stop, Docker run. This is
  super simple and makes it hard to forget a step.
- With a minimum of two hosts in the environment, we have manageable
  blue-green deployments. A production window is simply a cutover in
  the load-balancer configuration with an obvious and quick way to
  rollback. As the deployments become more dynamic, upgrades,
  rollbacks, and backend server discovery get increasingly difficult
  and require more coordination. Since deployments are manual, the
  costs of blue-green are minimal but provide major benefits over
  in-place upgrades.

Alright, on to the pain points:

- **Retyping the same commands**. Or, more accurately, hitting up and
  enter at your bash prompt repeatedly. This one is easy: automation
  to the rescue! There are lots of tools available to help you launch
  Docker containers. The most obvious solution for an ops engineer is
  to wrap the repetitive logic in a bash script so you have a single
  entry point. If you call yourself a devops engineer, instead, you
  might reach for Ansible, Puppet, Chef, or SaltStack. Writing the
  scripts or playbooks are easy, but there are a few questions to
  answer: where does the deployment logic live? And how do you keep
  track of the different parameters for each service? That brings us
  to our next point.
- Even an ops engineer with super-human abilities to avoid typos and
  reason clearly in the middle of the night after a long day at the
  office won’t know that the service is now listening on a different
  port and the Docker port parameter needs to be changed. The crux of
  the issue is that the details of how the application works are
  (hopefully) well-known to developers, and that information needs to
  be transferred to the operations team. Often times, the operations
  logic lives in a separate code repository or no repository at all.
  Keeping the relevant deployment logic in sync with the application
  can be difficult. For this reason, it’s a good practice to just
  commit your deployment logic into the code repo with your
  Dockerfile. If there are situations where this isn’t possible,
  there are ways to make it work (more on this later). The important
  thing is that the details are committed somewhere. Code is better
  than a deploy ticket, but a deploy ticket is still much better than
  in someone’s brain.
- **Visibility**. Troubleshooting a container requires logging into
  the host and running commands. In reality, this means logging into
  a number of hosts and running a combination of ‘docker ps’ and
  ‘docker logs --tail=100’. There are many good solutions for
  centralizing logs and, if you have the time, they are definitely
  worth setting up. What we found to generally be lacking, though,
  was the ability to see what containers were running on which hosts.
  This is a problem for developers, who want to know what versions are
  deployed and at what scale. And this is a major problem for
  operations, who need to hunt down containers for upgrades and
  troubleshooting.

Given this state of affairs, we started to implement changes to address
the pain points. The first advancement was to write a bash script
wrapping the common steps for a deployment. A simple wrapper might look
something like this:

```
!/bin/bash
APPLICATION=$1
VERSION=$2

docker pull "registry.abc.net/${APPLICATION}:${VERSION}"
docker rm -f $APPLICATION
docker run -d --name "${APPLICATION}" "registry.abc.net/${APPLICATION}:${VERSION}"
```

This works, but only for the simplest of containers: the kind that users
don’t need to connect to. In order to enable host port mapping and
volume mounts, we need to add application-specific logic. Here’s the
brute force solution that was implemented:

```
APPLICATION=$1
VERSION=$2

case "$APPLICATION" in
java-service-1)
  EXTRA_ARGS="-p 8080:8080";;
java-service-2)
  EXTRA_ARGS="-p 8888:8888 --privileged";;
*)
  EXTRA_ARGS="";;
esac

docker pull "registry.abc.net/${APPLICATION}:${VERSION}"
docker stop $APPLICATION
docker run -d --name "${APPLICATION}" $EXTRA_ARGS "registry.abc.net/${APPLICATION}:${VERSION}"
```

This script was installed on every Docker host to facilitate
deployments. The ops engineer would login and pass the necessary
parameters and the script would do the rest. Deployment time was
simplified because there was less for the engineer to do. The problem
of encoding the deployment logic didn’t go away, though. We moved it
back in time and turned it into a problem of committing changes to a
common script and distributing those changes to hosts. In general, this
is a great trade. Committing to a repo gives you great benefits like
code review, testing, change history, and repeatability. The less you
have to think about at crucial times, the better. Ideally, the relevant
deployment details for an application would live in the same source repo
as the application itself. There are many reasons why this may not be
the case, not the least of which being that developers may object to
having “ops” stuff in their java repo. This is especially true for
something like a deployment bash script, but also pertains to the
Dockerfile itself. This comes down to a cultural issue and is worth
working through, if at all possible. Although it’s certainly doable to
maintain separate repositories for your deployment code, you’ll have to
spend extra energy making sure that the two stay in sync. But, of
course, this is an article about doing it the hard way. At ABC, the
Dockerfiles started life in a dedicated repository with one folder per
project, and the deploy script lived in its own repo. [![cd
3](images/rancher_blog_cd-3.png)](images/rancher_blog_cd-3.png)
The Dockerfiles repository had a working copy checked out at a
well-known location on the Jenkins host (say,
‘/opt/abc/Dockerfiles’). In order to build the Docker image for an
application, Jenkins would first check for a Dockerfile in a local
folder ‘docker’. If not present, Jenkins would search the Dockerfiles
path, copying over the Dockerfile and accompanying scripts before
running the ‘docker build’. Since the Dockerfiles are always at
master, it’s possible to find yourself in a situation where the
Dockerfile is ahead of (or behind) the application configuration, but in
practice this mostly just works. Here’s an excerpt from the Jenkins
build logic:

```
if [ -f docker/Dockerfile ]; then
  docker_dir=Docker
elif [ -f /opt/abc/dockerfiles/$APPLICATION/Dockerfile ]; then
  docker_dir=/opt/abc/dockerfiles/$APPLICATION
else
  echo "No docker files. Can’t continue!"
  exit 1
if
docker build -t $APPLICATION:$VERSION $docker_dir
```

Over time, dockerfiles and supporting scripts were migrated into the
application source repositories. Since Jenkins was already looking in
the local repo first, no changes were required to the build pipeline.
After migrating the first service, the repo layout looked roughly like:
[![cd
4](images/rancher_blog_cd-4.png)](images/rancher_blog_cd-4.png)
One problem we ran into with having a separate repo was getting Jenkins
to trigger a rebuild of the application if either the application source
or packaging logic changed. Since the ‘dockerfiles’ repo contained
code for many projects, we didn’t want to trigger all repos when a
change occurred. The solution: a well-hidden option in the Jenkins [Git
plugin](https://wiki.jenkins-ci.org/display/JENKINS/Git+Plugin) called
[Included Regions](https://issues.jenkins-ci.org/browse/JENKINS-11749).
When configured, Jenkins isolates the build trigger to a change in a
specific sub-directory inside the repository. This allows us to keep all
Dockerfiles in a single repository and still be able to trigger specific
builds when a change is made (compared to building all images when a
change is made to a specific directory inside the repo). [![CD Part
1_2_jenkins-included-regions_edited](images/rancher_blog_CD-Part-1_2_jenkins-included-regions_edited-1-1024x759.jpg)](https://cdn.rancher.com/wp-content/uploads/2016/03/18063855/CD-Part-1_2_jenkins-included-regions_edited-1.jpg)
Another aspect of the initial workflow was that the deploy engineer
had to force a build of the application image before deployment. This
resulted in extra delays, especially if there was a problem with the
build and the developer needed to be engaged. To reduce this delay, and
pave the way to more continuous deployment, we started building Docker
images on every commit to a well-known branch. This required that every
image have a unique version identifier, which was not always the case if
we relied solely on the official application version string. We ended
up using a combination of official version string, commit count, and
commit sha:

```
commit_count=$(git rev-list --count HEAD)
commit_short=$(git rev-parse --short HEAD)
version_string="${version}-${commit_count}-${commit_short}"
```

This resulted in a version string that looks like ‘1.0.1-22-7e56158’.
Before we end our discussion of the Docker file phase of our pipeline,
there are a few parameters that are worth mentioning. Before we
operated a large number of containers in production we had little use
for these, but they have proven helpful in maintaining the uptime of our
Docker cluster.

- [**Restart
  Policy**](https://docs.docker.com/engine/reference/run/#restart-policies-restart)
  - A restart policy allows you to specify, per-container, what
    action to take when a container exits. Although this can be used to
    recover from an application panic or keep the container retrying
    while dependencies come online, the big win for Ops is automatic
    recovery after a Docker daemon or host restart. In the long run,
    you’ll want to implement a proper scheduler that can restart failed
    containers on new hosts. Until that day comes, save yourself some
    work and set a restart policy. At this stage in ABC, we defaulted to
    ‘--restart always’, which will cause the container to restart
    indefinitely. Simply having a restart policy will make planned (and
    unplanned) host restarts much less painful.
- \*\*[Resource
  Constraints](https://docs.docker.com/engine/reference/run/#runtime-constraints-on-resources) \*\* -
  With runtime resource constraints, you can set the maximum amount of
  memory or CPU that a container can consume. It won’t save you from
  general over-subscription of a host, but it can keep a lid on memory
  leaks and runaway containers. We started out by applying a generous
  memory limit (e.g. ‘--memory=“8g“‘) to containers that were
  known to have issues with memory growth. Although having a hard
  limit means the application will eventually hit an Out-of-Memory
  situation and panic, the host and other containers keep right on
  humming.

Combining restart policies and resource limits gives you greater cluster
stability while minimizing the impact of the failure and improving time
to recovery. In practice, this type of safeguard gives you the time to
work with the developer on the root cause, instead of being tied up
fighting a growing fire. To summarize, we started with a rudimentary
build pipeline that created tagged Docker images from our source repo.
We went from deploying containers using the Docker CLI to deploying them
using scripts and parameters defined in code. We also looked at how we
organized our deployment code, and highlighted a few Docker parameters
to help Ops keep the services up and running. At this point, we still
had a gap between our build pipelines and deployment steps. The
deployment engineer were bridging that gap by logging into a server to
run the deployment script. Although an improvement from where we
started, there was still room for a more automated approach. All of the
deployment logic was centralized in a single script, which made testing
locally much more difficult when developers need to install the script
and muddle through its complexity. At this point, handling any
environment specific information by way of environment variables
was also contained in our deployment script. Tracking down which
environmental variables were set for a service and adding new ones
was tedious and error-prone. In the [next
post](https://rancher.com/lessons-learned-building-a-continuous-deployment-pipeline-with-docker-docker-compose-and-rancher-part-2/),
we take a look at how we addressed these pain points by deconstructing
the common wrapper script, bringing the deployment logic closer to the
application using Docker Compose.[Go to Part
2>>](https://rancher.com/lessons-learned-building-a-continuous-deployment-pipeline-with-docker-docker-compose-and-rancher-part-2/) 
Please also download your free copy of ”[Continuous Integration and
Deployment with Docker and
Rancher](https://info.rancher.com/cicd-with-docker-ebook)” a detailed
eBook that walks through leveraging containers throughout your CI/CD
process.

Build a CI/CD Pipeline with Kubernetes and RancherRecorded Online Meetup of best practices and tools for building pipelines with containers and kubernetes.[Watch the training](https://rancher.com/events/2018/2018-08-07-onlinemeetup-building-a-cicd-pipeline-with-k8s/)
