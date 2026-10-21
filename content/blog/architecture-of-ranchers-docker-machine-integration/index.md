---
title: "Architecture of Rancher's Docker-machine Integration"
date: 2015-03-31T09:01:00
slug: "architecture-of-ranchers-docker-machine-integration"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: ["cloud"]
content_type: "explainer"
draft: true
migration:
  wp_id: 85804
  original_url: "https://www.suse.com/c/rancher_blog/architecture-of-ranchers-docker-machine-integration/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher 1.x docker-machine integration"
  redirect_target: "rancher.com/blog (hub)"
---

As you may have seen, Rancher [recently
announced](https://rancher.com/rancher-adds-support-for-docker-machine-provisioning/)
our integration
with [docker-machine](https://github.com/docker/machine). This
integration will allow users to spin up Rancher compute nodes across
multiple cloud providers right from the Rancher UI. In our initial
release, we supported Digital Ocean. Amazon EC2 is soon to follow and
we’ll continue to add more cloud providers as interest dictates. We
believe this feature will really help the Zero-to-Docker \_(and
Zero-to-Rancher)\_ experience. But the feature itself is not the focus
of this post. In this post, I want to detail the software architerture
employed to achieve this integration. First, it’s important to
understand that everyhting in Rancher is an API resource with a process
lifecycle. Containers, images, networks, and accounts are all API
resources with their own process lifecycles. When you deploy a machine
in the Rancher UI, you’re creating a machine resource. It has three
life cycle processes: 1. Create 2. Bootstrap 3. Delete The create
process is kicked off when the user creates a machine in the UI. When
the create process completes, it auotmatically kicks off the bootstrap
process. Delete (perhaps obviously) occurs when the user chooses to
delete or destroy the host. Our integration with machine is achieved
through a microservice that hooks into Rancher machine lifecycle events
and execs out to the docker-machine binary accordingly. You can check
out the source code for this service here:
h[ttps://github.com/rancherio/go-machine-service](//github.com/rancherio/go-machine-service).
Logically, the interaction looks like this:
[![machine](images/rancher_blog_machine.png)](images/rancher_blog_machine.png)
*...Sorry for the bad graphic. Anyway...* When you spin up Rancher
with `docker run rancher/server ...` with the default configuration, the
Rancher API, Rancher Process Server, DB, and Machine Microservice are
all processes living inside that container (and in fact, the API and
process server are the same process). The docker-machine binary is in
the container as well but only runs when it is called. You may at this
point be wondering about that event bus. In Rancher, ***we keep eventing
dead-simple*** and above all follow this principle:

> There is no such thing as reliable messaging.

So, that “event bus” consists of the microservice making a POST
request to the `/subsribe` API endpoint. The response is a stream of
newline-terminated json events, similar in concept to the [docker event
stream](http://www.craigjellick.com/working-with-docker-events/). The
process server is responsible for firing (and refiring) events until it
receives a reply event (another API POST) indicating the event was
handled. Further event handlers are blocked until the current event
handler replies successfully. The microservice is responsible for
handling the events, replying, and acting idempotently so that refires
can occur without ill-effect. So when the machine microservie receives a
create event, it translate the machine API resource’s prooperties into
a docker-machine cli command and execs out to it. Since the machine
creation process is long lived, the service monitors the standard out
and error of the call and sends corresponding status updates to the
Rancher server. These are then presented to the user in the UI. When
docker-machine reports that the machine was successfully created, the
microservice will reply to the original event it received from the
Rancher server. The successful end of the create event will cause the
process server to automatically kick off the bootstrap event, which
makes it way right back down to the machine microservice. When that
event is received, we’ll again exec out to docker-machine to get the
details needed to connect to the machine’s docker daemon. We do this by
executing the `docker-machine config` command and parsing the response.
With the connection parameters in hand, the service fires up a rancher
agent on the machine via `docker run ... rancher/agent ...`. This is the
exact same command that a user would run if they wanted to manaully join
a server to Rancher. When that container is up and running, it will
report into the Rancher server and start hooking into container
lifecycle events in much the same way that this service hooks into
machine lifecycle events. From there, it’s business as normal for the
Rancher server and the machine’s rancher-agent. That about does it for
the technical architecture of our docker-machine integration. There are
a lot more interesting but minor technical detail to share, but I
didn’t want to go too far off into the weeds in this post. I’ll write
up some follow up post sharing those details in the not-too-distant
future. Finally, shout out (and thanks) to [Evan
Haslett](https://github.com/ehazlett), [Ben
Firshman](https://github.com/bfirsh), and the rest of the docker-machine
team and community for the help along the way. We look forward to more
exciting work with the docker-machine, including getting RancherOS in
there. If you’d like to learn more about Rancher, please schedule a
demo and we’ll walk you through the latest features, and our
future roadmap. *Note: This post also appears
on Craig’s personal blog
[here](http://www.craigjellick.com/architercutre-of-rancher-docker-machine-integration/).
Feel free to check out that blog for more software engineering
insights.*
