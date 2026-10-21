---
title: "Lessons learned building a deployment pipeline with Docker, Docker-Compose and Rancher (Part 3)"
date: 2016-05-11T11:11:00
slug: "lessons-learned-building-a-deployment-pipeline-with-docker-docker-compose-and-rancher-part-3"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: ["ci-cd"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 86788
  original_url: "https://www.suse.com/c/rancher_blog/lessons-learned-building-a-deployment-pipeline-with-docker-docker-compose-and-rancher-part-3/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher 1.x orchestration, 2016"
  redirect_target: "rancher.com/blog (hub)"
---

*[![compose](images/rancher_blog_compose.png)](images/rancher_blog_compose.png)John
Patterson ([@cantrobot](https://twitter.com/cantrobot)) and Chris
Lunsford run This End Out, an operations and infrastructure services
company. You can find them online at*
[*www.thisendout.com*](https://thisendout.com/) *and on
Twitter [@thisendout](https://twitter.com/thisendout).* *Update: All
four parts of the series are now live: [Part 1: Getting started with
CI/CD and
Docker](https://rancher.com/lessons-learned-building-a-deployment-pipeline-with-docker-docker-compose-and-rancher-part-1/)*
*[Part 2: Moving to Compose
blueprints](https://rancher.com/lessons-learned-building-a-continuous-deployment-pipeline-with-docker-docker-compose-and-rancher-part-2/)*
*[Part 3: Adding Rancher for
Orchestration](https://rancher.com/lessons-learned-building-a-deployment-pipeline-with-docker-docker-compose-and-rancher-part-3/)[Part
4: Completing the Cycle with Service
Discovery](https://rancher.com/lessons-learned-building-a-deployment-pipeline-with-docker-docker-compose-and-rancher-part-4/)*
In this installment of our series, we’ll explore how we came to
Rancher, detailing how it solved some issues around deploying and
managing containers. If you recall from [part
2](https://rancher.com/lessons-learned-building-a-continuous-deployment-pipeline-with-docker-docker-compose-and-rancher-part-2/)
of our series, we migrated our application deployments to Docker Compose
and established deployment jobs for our applications. This provided the
ability for developers easily to make changes to their application
deployment logic and enabled operations to see when an application was
deployed. However, there are some outstanding issues with this setup.

## Challenges We Faced with Docker-Compose

First, operations have to schedule all services manually. The deployer
has to decide which host to deploy an application to, which means the
deployer must keep track of the available resources on every host. Also,
if a host or container fails, the operator is responsible for
re-deploying the application. In practice, this means that hosts are
often unbalanced, and services experience longer downtime after failure.
Second, it’s difficult to get information about the state of your
services. As an example, consider a common question asked by operators,
project managers, and developers alike: “Which version of application x
is deployed in staging?” With manual scheduling, finding the answer
often involved directly messaging a favorite ops engineer and having
them log into a server to run a docker ps. This is where Rancher
provided a huge benefit: information about deployed services was easily
accessible by everyone without requiring an ad-hoc request to
operations. Before landing on Rancher, we tried other solutions that
provided interfaces into a Docker host or cluster. One of the biggest
burdens that many other solutions did not address was multi-environment
management. Having 8 environments running various workloads, we needed a
unified way to manage the cluster without having to visit 8 different
services. Also, we wanted to give developers free reign to modify the
development environments, knowing we could rebuild it at a moment’s
notice. However, for production, we wanted to provide them with limited
read-only access. A central management plan for all environments using a
role-based access control (RBAC) model thus became desirable. We started
looking at Rancher mainly due to how easy it was to setup.

## Rancher Met the Challenge

**Within the span of half a day, Rancher was up and running using AWS
ELB, Elasticache, RDS and our existing Docker hosts. Having the ability
to easily configure authentication was also a big plus.** We won’t go
into the details of the deployment of Rancher itself, as docs are
describing how to do this.
Instead, we’ll pick up right after initial setup and explain our
migration from the existing setup (as described in parts
[one](https://rancher.com/lessons-learned-building-a-deployment-pipeline-with-docker-docker-compose-and-rancher-part-1/)
and
[two](https://rancher.com/lessons-learned-building-a-continuous-deployment-pipeline-with-docker-docker-compose-and-rancher-part-2/)
of this series). Let’s start by creating our environments, and to keep
it simple, we’ll setup development (dev), staging (stage), and
production (prod). Each environment has existing Docker hosts running on
top of Ubuntu and configured by an in-house Ansible playbook that
installed Docker, our monitoring agent, and made a few
organization-specific changes. Rancher allows you to add existing hosts
to each environment by running a single command to register the Docker
host to the internal Rancher server. **Adding a Rancher Host**
Typically, adding hosts requires a few clicks in the web UI and running
an environment specific, generated command on each end system, however,
using the Rancher API, we are able to automate this step using Ansible.
For the curious, the relevant section of our playbook is below (mostly
adapted from the [logic in Hussein Galas’
repo](https://github.com/galal-hussein/Rancher-Agent-Ansible/blob/master/tasks/main.yml)):
[[name: install dependencies for uri
module]][
[ apt: name=python-httplib2 update\_cache=yes]
] [[[name: check if the
rancher-agent is running] [ command: docker ps
--filter ‘name=rancher-agent’] [ register:
containers]]]
[[[name: get registration command from rancher]
[ uri:] [ method:
GET] [ user: “{{ RANCHER\_API\_KEY
}}“] [ password: “{{ RANCHER\_SECRET\_KEY
}}“] [ force\_basic\_auth:
yes] [ status\_code:
200] [ url:
“https://rancher.abc.net/v1/projects/{{ RANCHER\_PROJECT\_ID
}}/registrationtokens“] [ return\_content:
yes] [ validate\_certs:
yes] [ register:
rancher\_token\_url] [ when:
“‘rancher-agent’ not in
containers.stdout“]]]
[[[name: register the host machine with
rancher] [ shell: >]
[ docker run -d --privileged] [ -v
/var/run/docker.sock:/var/run/docker.sock] [
{{ rancher\_token\_url.json[‘data’][0][‘image’]
}}] [ {{
rancher\_token\_url.json[‘data’][0][‘command’].split() |
last}}] [ when: “‘rancher-agent’ not in
containers.stdout“]]]
With our environments created and hosts registered, let’s take a look at
how to integrate our deployment workflow with Rancher. On each Docker
host, there are some containers already running, deployed by Ansible via
a Jenkins job. Out of the box, Rancher provides the ability to:

- Manage existing containers (ex. start, stop, edit, view logs, launch
  an interactive shell)
- Access information about running and stopped containers (ex. image,
  entry point, command, port mappings, environment variables)
- View resource utilization on a host and container level (ex. CPU,
  memory, disk, network)

**Standalone Containers** Immediately, having done nothing but register
our hosts, we now have visibility into the state of all our containers
in each environment. The best part is we can share this information with
our other teams by giving them limited permissions in each environment.
Having this visibility eliminates the need for operators to log into the
Docker hosts to manually interrogate, and we reduce the number of
requests for environmental information by providing limited access to
the various teams. For example, granting the development team read-only
access to our environments has helped build a bridge between them and
the operations team. Both teams now feel more empowered and connected to
the state of the environment. Troubleshooting has become a joint
venture, instead of a one way, synchronous information flow, which has
reduced the overall time spent resolving issues that crop up. With our
existing Docker hosts added, and after having read a great [series on
Jenkins and
Rancher](https://rancher.com/docker-based-build-pipelines-part-1-continuous-integration-and-testing/),
we decided the next area to improve was our existing deployment
pipelines, modifying them to use rancher compose instead of
Ansible calling Docker Compose. Before we dive in, however, there are a
couple of things to know about Rancher stacks, scheduling, Docker
Compose, and rancher compose. **Stacks and Services**: Rancher makes a
distinction between standalone containers (those deployed outside of
Rancher or in a one-off capacity through the Rancher UI) and [stacks and
services](https://docs.rancher.com/rancher/concepts/#stacks). Simply put,
stacks are groups of services, and services are all the containers
required that make up an application (more on this later). Standalone
containers are manually scheduled. **Scheduling**: The previous
deployment techniques required the operator to make decisions about
which hosts a container should run on. In the case of the deployment
script, it was which host the operator ran the script on. In the case of
the Ansible playbook, it was the host(s), or groups passed to the
Jenkins job. Either way, it required the operator to make decisions,
typically based off of very little information, that could be
detrimental to the deployment (what if the host is maxed on CPU
utilization?). Clustering solutions such as Docker Swarm, Kubernetes,
Mesos, and Rancher all implement schedulers to solve this problem.
Schedulers interrogate information about a group of hosts which are
candidates for being targetted for an action. The scheduler will
gradually reduce the list based off of default or custom requirements,
like CPU utilization and (anti)affinity rules (ex. do not deploy two of
the some container on the same host). As an operator performing a
deployment, this makes my life much easier since the scheduler can do
these calculations much faster and more accurately than I can
(especially during late night deployment windows). Out of the box,
Rancher provides a scheduler when deploying services via stacks.
**Docker Compose**: Rancher uses Docker Compose to create stacks and
define services. Since we already converted our services to use Docker
Compose files, we can easily create stacks in Rancher. Stacks can be
created from the UI, manually, or via the CLI through the rancher
compose utility. **Rancher Compose**: Rancher compose is a utility that
allows us to manage our stacks and services per environment in Rancher
via the CLI. It also allows additional access to Rancher utilities by
way of a rancher-compose.yml file. This is purely a supplemental file,
and is not a replacement to docker-compose.yml. In a rancher-compose.yml
file you can define, for example:

- An upgrade strategy per service
- Health checks per service
- Desired scale per service

These are all very useful features in Rancher that aren’t available
through Docker Compose or the Docker daemon. For a full list of features
offered by Rancher Compose, you can browse the documentation. We can easily
migrate our services to deploy as Rancher stacks by updating the
existing deployment job to use Rancher Compose instead of Ansible. We,
then are able to remove the DESTINATION parameter, but we kept VERSION
to use when interpolating our docker-compose.yml. Below is a snippet of
the shell logic we use in our Jenkins deployment: [[export
RANCHER\_URL=http://rancher.abc.net/]][
[export RANCHER\_ACCESS\_KEY=...] [export
RANCHER\_SECRET\_KEY=...] [
] [if [ -f docker/docker-compose.yml ];
then] [
docker\_dir=docker] [elif [ -f
/opt/abc/dockerfiles/java-service-1/docker-compose.yml ];
then] [
docker\_dir=/opt/abc/dockerfiles/java-service-1]
[else] [ echo “No docker-compose.yml found.
Can’t continue!“] [ exit
1] [fi] [
] [if ! [ -f
${docker\_dir}/rancher-compose.yml ]; then]
[ echo “No rancher-compose.yml found. Can’t
continue!“] [ exit
1] [fi] [
] [/usr/local/bin/rancher-compose --verbose
] [ -f ${docker\_dir}/docker-compose.yml
] [ -r ${docker\_dir}/rancher-compose.yml
] [ up -d
--upgrade]]
Stepping through the snippet, we see that:

1. We define how to access our Rancher server via environment variables
2. Locate the docker-compose.yml file otherwise exit the job with an
   error
3. Locate the rancher-compose.yml file otherwise exit the job with an
   error
4. Run rancher-compose, telling it to not block and output logs with -d
   and to upgrade a service if it already exists (--upgrade)

You can see that, for the most part, the logic has stayed the same; the
biggest difference being the use of rancher-compose instead of the
Ansible deployment playbook and the addition of a rancher-compose.yml
file for each of our services. For our java-service-1 application, the
docker-compose and rancher-compose files now look like:
[[docker-compose.yml java-service-1: image:
registry.abc.net/java-service-1:${VERSION} container\_name:
java-service-1 expose: - 8080 ports: - 8080:8080 rancher-compose.yml
java-service-1: scale:
3]]
With our deployment jobs created, let’s review our deployment workflow.

1. A developer makes a change to code and pushes that change to git
2. Jenkins begins unit testing the code and notifies a downstream job
   on success
3. The downstream job builds and pushes a docker image with the new
   code artifact to our private Docker registry
4. A deployment ticket is created with the application and version
   number to be deployed to an environment

[[DEPLOY-111:]][
[ App: JavaService1, branch “release/1.0.1“]
[ Environment:
Production]]

1. The deployment engineer runs the deployment Jenkins job for the
   application, providing the version number as a parameter
2. Rancher compose runs, either creating or upgrading the stack, on the
   environment and, after the desired scale has been reached, concludes
   the job
3. The deployment engineer and developer verify the service manually
4. The deployment engineer confirms the upgrade in the Rancher UI

## Key Takeaways

**With Rancher managing our service deployments, we benefit from
built-in scheduling, scaling, healing, upgrades, and rollbacks, for very
little effort on our part.** Also, the migration from an Ansible
deployment to Rancher was minimal, only requiring the addition of a
rancher-compose.yml. However, having Rancher handle the scheduling of
our containers means it becomes harder for us to keep track of where our
applications are running. For example, since we no longer make the
decision of where the java-service-1 application runs, a load balancer
for that application cannot have a static IP for the backend. We need to
give our applications a way to discover each other. Lastly, in our
java-service-1 application, we are exposing and explicitly binding port
8080 to the docker host running our container. If another service
binding that same port were to be scheduled on the same host, it would
fail to start. A person making scheduling decisions can easily work
around this. However, we need to inform our scheduler to avoid this
scenario. In the [last part of our
series](https://rancher.com/lessons-learned-building-a-deployment-pipeline-with-docker-docker-compose-and-rancher-part-4/),
we will explore the ways we mitigated these new pain points through the
use of affinity rules, host labels, service discovery, and smarter
upgrades and rollbacks. [Go to Part
4>>](https://rancher.com/lessons-learned-building-a-deployment-pipeline-with-docker-docker-compose-and-rancher-part-4/)
In the meantime, please download a free copy of “[Continuous Integration
and Deployment with Docker and
Rancher](https://info.rancher.com/cicd-with-docker-ebook)” a detailed
eBook that walks through leveraging containers throughout your CI/CD
process.
