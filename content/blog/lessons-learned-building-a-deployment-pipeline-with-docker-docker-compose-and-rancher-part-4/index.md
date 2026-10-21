---
title: "Lessons Learned Building a Deployment Pipeline with Docker, Docker Compose and Rancher (Part 4)"
date: 2016-05-22T11:11:00
slug: "lessons-learned-building-a-deployment-pipeline-with-docker-docker-compose-and-rancher-part-4"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: ["networking"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 86790
  original_url: "https://www.suse.com/c/rancher_blog/lessons-learned-building-a-deployment-pipeline-with-docker-docker-compose-and-rancher-part-4/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Consul with Rancher 1.x"
  redirect_target: "rancher.com/blog (hub)"
---

![consul-logo-grad](images/rancher_blog_consul-logo-grad-300x225.png) In this post, we’ll discuss how we
implemented consul for service discovery with Rancher. *John
Patterson ([@cantrobot](https://twitter.com/cantrobot)*) and Chris
Lunsford run This End Out, an operations and infrastructure services
company. You can find them online at\*
[*https://www.thisendout.com*](https://thisendout.com/) \*and follow them
on twitter [@thisendout](https://twitter.com/thisendout). \*\* If you
haven’t already, please read the previous posts in this series: *[Part
1: Getting started with CI/CD and
Docker](https://rancher.com/lessons-learned-building-a-deployment-pipeline-with-docker-docker-compose-and-rancher-part-1/)*
[*Part 2: Moving to Compose
blueprints*](https://rancher.com/lessons-learned-building-a-continuous-deployment-pipeline-with-docker-docker-compose-and-rancher-part-2/)
*[Part 3: Adding Rancher for
Orchestration](https://rancher.com/lessons-learned-building-a-deployment-pipeline-with-docker-docker-compose-and-rancher-part-3/)*
In this final post of the series on building a deployment pipeline, we
will explore some of the challenges we faced when transitioning to
Rancher for cluster scheduling. In the [previous
article](https://rancher.com/lessons-learned-building-a-deployment-pipeline-with-docker-docker-compose-and-rancher-part-3/),
we removed the operator from the process of choosing where a container
would run by allowing Rancher to perform the scheduling. With this new
scheme, we must address how the rest of our environment knows where the
scheduler places these services and how they can be reached. We will
also talk about manipulating the scheduler with labels to adjust where
containers are placed and avoid port binding conflicts. Lastly, we will
optimize our upgrade process by taking advantage of Rancher’s rollback
capability. Before the introduction of Rancher, our environment was a
fairly static one. We always deployed containers to the same hosts, and
deploying to a different host meant that we would need to update a few
config files to reflect the new location. For example, if we were to add
one additional instance of the ‘java-service-1’ application, we would
also need to update the loadbalancer to point to the IP of the
additional instance. Now that we employ a scheduler, we lose
predictability of where our containers get deployed and need to make our
environment configuration dynamic, adapting to changes automatically. To
do this, we make use of service registration and discovery. A service
registry provides us a single source of truth about where our
applications are in the environment. Rather than hard-code service
locations, our applications can query the service registry through an
API and automatically reconfigure themselves when there is a change in
our environment. Rancher provides service discovery out of the box using
the Rancher DNS and metadata
services (there is a good write-up on the Rancher blog on service
discovery
[here](https://rancher.com/the-magical-moment-when-container-load-balancing-meets-service-discovery/)).
However, having a mix of Docker and non-Docker applications, we couldn’t
rely purely on Rancher to handle service discovery. We needed an
independent tool to track the locations of all our services, and
[consul](https://consul.io/) fit that bill. We won’t detail how to
setup Consul in your environment, however, we’ll briefly describe the
way we use Consul at ABC Inc. In each environment, we have a Consul
cluster deployed as containers. On each host in the environment, we
deploy a Consul agent, and if the host is running Docker, we also deploy
a [registrator](https://github.com/gliderlabs/registrator) container.
Registrator monitors the Docker events API for each daemon and
automatically updates Consul during lifecycle events. For example, after
a new container is deployed, registrator automatically registers the
service in Consul. When the container is removed, registrator
deregisters it. **Consul Service Listing** Having all of our services
registered in Consul, we can run
[consul-template](https://github.com/hashicorp/consul-template) in our
loadbalancer to dynamically populate a list of upstreams based on the
service data stored in Consul. For our NGINX loadbalancer, we can create
a template for populating the backends for the ‘java-service-1’
application:

```
# upstreams.conf
upstream java-service-1 {
{{range _, $element := service "java-service-1"}}
       server {{.Address}}:{{.Port}};
{{else}}
       server 127.0.0.1:65535; # force a 502{{end}} }
```

This template looks for a list of services registered in Consul as
‘java-service-1’. It will then loop through that list adding a service
line with the IP address and port of that particular application
instance. If there aren’t any ‘java-service-1’ applications
registered in Consul, we default to throwing a 502 to avoid an error in
NGINX. We can run consul-template in daemon mode, causing it to monitor
Consul for changes, re-render the template when a change occurs, and
then reload NGINX to apply the new configuration.

```
TEMPLATE_FILE=/etc/nginx/upstreams.conf.tmpl
RELOAD_CMD=/usr/sbin/nginx -s reload
consul-template -consul consul.stage.abc.net:8500 
       -template "${TEMPLATE_FILE}:${TEMPLATE_FILE//.tmpl/}:${RELOAD_CMD}"
```

With our loadbalancer setup to dynamically change as the rest of the
environment changes, we can fully rely on the Rancher scheduler to make
the complex decisions about where our services should run. However, our
‘java-service-1’ application binds TCP port 8080 on the Docker host
and if more than one of the application containers were to be scheduled
on the same host, it would result in a port binding conflict and
ultimately fail. To avoid this situation, we can manipulate the
scheduler by way of scheduling rules. Rancher gives us a way to
manipulate the scheduler by imposing conditionals using container labels
in our docker-compose.yml file. Conditionals can include affinity rules,
negation, and even “soft” enforcement (meaning avoid if possible). In
our case with the ‘java-service-1’ application, we know only one can
run on a host at a given time, so we can set an anti-affinity rule based
on the container name. This will cause the scheduler to look for a
Docker host that isn’t running a container with the name
‘java-service-1’. Our docker-compose.yml file then looks like the
following:

```
java-service-1:
   image: registry.abc.net/java-service-1:${VERSION}
   container_name: java-service-1
   ports:
         - 8080:8080
    labels:
         io.rancher.scheduler.affinity:container_label_ne: io.rancher.stack_service.name=java-service-1
```

Notice the introduction of the “labels” key. All scheduling rules are
added as labels. Labels can be added to Docker hosts and containers.
When we register our hosts in Rancher, we have the ability to associate
labels with them, which we can later key off of for scheduling
deployments. For example, if we had a set of Docker hosts that were
storage-optimized with SSD drives, we could add the host label
storage=ssd. **Rancher Host Labels** Containers needing to take
advantage of the optimized storage hosts can then add a label to force
the scheduler to only deploy them on hosts that match. We’ll update our
‘java-service-1’ application to only deploy on the storage optimized
hosts:

```
java-service-1:
    image: registry.abc.net/java-service-1:${VERSION}
    container_name: java-service-1
    ports:
         - 8080:8080
    labels:
         io.rancher.scheduler.affinity:container_label_ne: io.rancher.stack_service.name=java-service-1
         io.rancher.scheduler.affinity:host_label: storage=ssd
```

Using labels, we can finely tune where our applications are deployed,
allowing us to think in terms of desired capacity rather than individual
hosts running a specific container set. Labels also give you the ability
to switch to Rancher for all cluster scheduling even if you still have
applications that must be run on specific hosts. Lastly, we can optimize
our service upgrades by utilizing Rancher’s rollback capability. In our
deployment workflow, a service is deployed by calling rancher-compose
which instructs Rancher to perform an upgrade on that service stack. The
upgrade process roughly looks like the following:

1. Upgrade starts by pulling a new image for the service
2. One by one, existing containers are stopped and new containers are
   started
3. The upgrade is complete when the deployer logs into the UI and
   selects “Finish Upgrade”
4. The old, stopped service containers are removed

**Rancher Upgrade** This workflow is alright when there are very few
deployments taking place for a given service. However, when a service is
in the “upgraded” state (before the deployer selects “Finish
Upgrade“), any new upgrades to the same service will be blocked until
“Finish Upgrade” or “Rollback” is selected. The rancher-compose
utility gives us the option to programmatically select which action to
perform instead of requiring action on behalf of the deployer. For
example, if you have automated testing of your services, you can call
such tests after the rancher-compose upgrade returns. Depending on the
status of those tests, rancher-compose can be called again, this time
telling the stack to either “Finish Upgrade” or “Rollback.” A
primitive example with our deployment Jenkins job could look the
following:

```
# for the full job, see part 3 of this series
/usr/local/bin/rancher-compose --verbose 
    -f ${docker_dir}/docker-compose.yml 
    -r ${docker_dir}/rancher-compose.yml 
    up -d --upgrade
JAVA_SERVICE_1_URL=http://java-service-1.stage.abc.net:8080/api/v1/status
if curl -s ${JAVA_SERVICE_1_URL} | grep -q "OK"; then

# looks good, confirm or "finish" the upgrade
    /usr/local/bin/rancher-compose --verbose 
         -f ${docker_dir}/docker-compose.yml 
         -r ${docker_dir}/rancher-compose.yml 
         up --confirm-upgrade
else

     # looks like there's an error, rollback the containers
     # to the previously deployed version
     /usr/local/bin/rancher-compose --verbose 
        -f ${docker_dir}/docker-compose.yml 
        -r ${docker_dir}/rancher-compose.yml 
        up --rollback
fi
```

This logic will call our application endpoint to perform a simple status
check. If “OK” is in the output, then we finish the upgrade, otherwise
we need to rollback to the previously deployed version. If you do not
have automated testing, another option is to simple always finish or
“confirm” the upgrade.

```
# for the full job, see part 3 of this series
/usr/local/bin/rancher-compose --verbose 
    -f ${docker_dir}/docker-compose.yml 
    -r ${docker_dir}/rancher-compose.yml 
    up -d --upgrade --confirm-upgrade
```

If later down the road, you determine that a rollback is necessary, then
simply redeploy the previous version using the same deployment job. This
is not quite as friendly as the Rancher upgrade and rollback
capabilities, but it unblocks future upgrades by not leaving the stack
in the “Upgraded” state. When a service is rolled back in Rancher, the
containers are redeployed at the previous version. This can have
unintended consequences when deploying services with generic tags like
‘latest’ or ‘master’. For example, let’s assume the
‘java-service-1’ application was previously deployed with the tag
‘latest’. A change is made to the image, pushed to the registry and
the Docker tag ‘latest’ is updated to point to this new image. We
proceed with an upgrade, using the tag ‘latest’, and after testing it
is decided the application needs to be rolled back. Rolling the stack
with Rancher would still redeploy the newest image, because the tag
‘latest’ hasn’t been updated to point to the previous image. The
rollback may be successful in purely technical terms, but the intended
effect to deploy the last known working copy is missed entirely. We
avoid this at ABC Inc. by always using specific tags that correlate with
the version of the application. So instead of deploying our
‘java-service-1’ application using the tag ‘latest’, we can use the
version tag ‘1.0.1-22-7e56158’. This guarantees that rollbacks will
always point to the last working deployment of our application in an
environment. We hope sharing our experience t ABC Inc. has been helpful.
It was helpful for us to take a methodical journey to adopt Docker,
steadily improving our processes, and allowing our team to get
comfortable with the concepts. Making incremental changes towards a more
automated deployment workflow allows for the organization to realize
benefits in automation sooner and deployment teams to make more
pragmatic decisions about what they need in a pipeline. Our journey led
us to implementing Rancher, which proved to be one of the biggest wins
for visibility, automation, and even team collaboration. We hope that
sharing these lessons learned from our Docker-adoption process will help
you in your own process of adoption. We wish you luck on your journey!
*All four parts of the series are now live, you can find them here:
[Part 1: Getting started with CI/CD and
Docker](https://rancher.com/lessons-learned-building-a-deployment-pipeline-with-docker-docker-compose-and-rancher-part-1/)*
*[Part 2: Moving to Compose
blueprints](https://rancher.com/lessons-learned-building-a-continuous-deployment-pipeline-with-docker-docker-compose-and-rancher-part-2/)*
*[Part 3: Adding Rancher for
Orchestration](https://rancher.com/lessons-learned-building-a-deployment-pipeline-with-docker-docker-compose-and-rancher-part-3/)[Part
4: Completing the Cycle with Service
Discovery](https://rancher.com/lessons-learned-building-a-deployment-pipeline-with-docker-docker-compose-and-rancher-part-4/)*
Please also download your free copy of ”[Continuous Integration and
Deployment with Docker and
Rancher](https://info.rancher.com/cicd-with-docker-ebook)” a detailed
eBook that walks through leveraging containers throughout your CI/CD
process. *John Patterson
([@cantrobot](https://twitter.com/cantrobot)*) and Chris Lunsford run
This End Out, an operations and infrastructure services company. You can
find them online at\*
[*https://www.thisendout.com*](https://thisendout.com/) \*and follow them
on twitter [@thisendout](https://twitter.com/thisendout). \*\*
