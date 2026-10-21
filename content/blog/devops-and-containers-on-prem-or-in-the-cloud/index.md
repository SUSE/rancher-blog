---
title: "DevOps and Containers, On-Prem or in the Cloud"
date: 2017-03-14T11:28:00
slug: "devops-and-containers-on-prem-or-in-the-cloud"
author: "Rancher Admin"
products: ["Docker/containers (generic)"]
tags: ["cloud"]
content_type: "opinion"
draft: false
migration:
  wp_id: 87215
  original_url: "https://www.suse.com/c/rancher_blog/devops-and-containers-on-prem-or-in-the-cloud/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

![](images/rancher_blog_Cloud-or-On-Prem-2-300x170.jpg)The cloud vs.
on-premises debate is an old one. It goes back to the days when the
cloud was new and people were trying to decide whether to keep workloads
in on-premises datacenters or migrate to cloud hosts. But the Docker
revolution has introduced a new dimension to the debate. As more and
more organizations adopt containers, they are now asking themselves
whether the best place to host containers is on-premises or in the
cloud. As you might imagine, there’s no single answer that fits
everyone. In this post, we’ll consider the pros and cons of both cloud
and on-premises container deployment and consider which factors can make
one option or the other the right choice for your organization.

### DevOps, Containers, and the Cloud

First, though, let’s take a quick look at the basic relationship
between DevOps, containers, and the cloud. In many ways, the combination
of DevOps and containers can be seen as one way—if not the native
way—of doing IT in the cloud. After all, containers maximize
scalability and flexibility, which are key goals of the DevOps
movement—not to mention the primary reasons for many people in
migrating to the cloud. Things like virtualization and continuous
delivery seem to be perfectly suited to the cloud (or to a cloud-like
environment), and it is very possible that if DevOps had originated in
the Agile world, it would have developed quite naturally out of the
process of adapting IT practices to the cloud.

### DevOps and On-Premises

Does that mean, however, that containerization, DevOps, and continuous
delivery are somehow unsuited or even alien to on-premises deployment?
Not really. On-premises deployment itself has changed; it now has many
of the characteristics of the cloud, including a high degree of
virtualization, and relative independence from hardware constraints
through abstraction. Today’s on-premises systems generally fit the
definition of “private cloud,” and they lend themselves well to the
kind of automated development and operations cycle that lies at the
heart of DevOps. In fact, many of the major players in the
DevOps/container world, including AWS and Docker, provide strong support
for on-premises deployment, and sophisticated container management tools
such as Rancher are designed to work seamlessly across the
public/private cloud boundary. It is no exaggeration to say that
containers are now as native to the on-premises world as they are to the
cloud.

### Why On-premises?

Why would you want to deploy containers on-premises? **Local Resources**
Perhaps the most obvious reason is the need to directly access and use
hardware features, such as storage, or processor-specific operations.
If, for example, you are using an array of graphics chips for
matrix-intensive computation, you are likely to be tied to local
hardware. Containers, like virtual machines, always require some degree
of abstraction, but running containers on-premises reduces the number of
layers of abstraction between the application and underlying metal to a
minimum. You can go from the container to the underlying OS’s hardware
access more or less directly—something which is not practical with VMs
on bare metal, or with containers in the public cloud. **Local
Monitoring** In a similar vein, you may also need containers to monitor,
control, and manage local devices. This may be an important
consideration in an industrial setting, or a research facility, for
example. It is, of course, possible to perform monitoring and control
functions with more traditional types of software—The combination of
containerization and continuous delivery, however, allows you to quickly
update and adapt software in response to changes in manufacturing
processes or research procedures. **Local Control Over Security**
Security may also be a major consideration when it comes to deploying
containers on-premises. Since containers access resources from the
underlying OS, they have potential security vulnerabilities; in order to
make containers secure, it is necessary to take positive steps to add
security features to container systems. Most container-deployment
systems have built-in security features. On-premises deployment,
however, may be a useful strategy for adding extra layers of security.
In addition to the extra security that comes with controlling access to
physical facilities, an on-premises container deployment may be able to
make use of the built-in security features of the underlying hardware.
**Legacy Infrastructure and Cloud Migration** What if you’re not in a
position to abandon existing on-premises infrastructure? If a company
has a considerable amount of money invested in hardware, or is simply
not willing or able to migrate away from a large and complex set of
interconnected legacy applications all at once, staying on-premises for
the time being may be the most practical (or the most politically
prudent) short-to-medium-term choice. By introducing containers (and
DevOps practices) on-premises, you can lay out a relatively painless
path for gradual migration to the cloud. **Test Locally, Deploy in the
Cloud** You may also want to develop and test containerized applications
locally, then deploy in the cloud. On-premises development allows you to
closely monitor the interaction between your software and the deployment
platform, and observe its operation under controlled conditions. This
can make it easier to isolate unanticipated post-deployment problems by
comparing the application’s behavior in the cloud with its behavior in
a known, controlled environment. It also allows you to deploy and test
container-based software in an environment where you can be confident
that information about new features or capabilities will not be leaked
to your competitors.

### Public/Private Hybrid

Here’s another point to consider when you’re comparing cloud and
on-premises container deployment: public and private cloud deployment
are not fundamentally incompatible, and in many ways, there is really no
sharp line between them. This is, of course, true for traditional,
monolithic applications (which can, for example, also reside on private
servers while being accessible to remote users via a cloud-based
interface), but with containers, the public/private boundary can be made
even more fluid and indistinct when it is appropriate to do so. You can,
for example, deploy an application largely by means of containers in the
public cloud, with some functions running on on-premises containers.
This gives you granular control over things such as security or
local-device access, while at the same time allowing you to take
advantage of the flexibility, broad reach, and cost advantages of
public-cloud deployment.

### The Right Mix for Your Organization

Which type of deployment is better for your company? In general,
startups and small-to-medium-size companies without a strong need to tie
in closely to hardware find it easy to move into (or start in) the
cloud. Larger (i.e. enterprise-scale) companies and those with a need to
manage and control local hardware resources are more likely to prefer
on-premises infrastructure. In the case of enterprises, on-premises
container deployment may serve as a bridge to full public-cloud
deployment, or hybrid private/public deployment. The bottom line,
however, is that the answer to the public cloud vs. on-premises question
really depends on the specific needs of your business. No two
organizations are alike, and no two software deployments are alike, but
whatever your software/IT goals are, and however you plan to achieve
them, between on-premises and public-cloud deployment, there’s more
than enough flexibility to make that plan work.
