---
title: "Your Guide to Container Security"
date: 2017-03-29T10:16:00
slug: "your-guide-to-container-security"
author: "Rancher Admin"
products: ["Docker/containers (generic)"]
tags: ["security"]
content_type: "explainer"
draft: false
migration:
  wp_id: 86580
  original_url: "https://www.suse.com/c/rancher_blog/your-guide-to-container-security/"
  disposition: migrate_refresh
  commercial: false
  outdated_reason: "Clair and Docker scanning era tools"
  redirect_target: ""
---

Your storage system should be locked down with all security and access

control tools available to you as well. That is true whether the storage

serves containers or any other type of application environment. How do

you secure containers? That may sound like a simple question, but it

actually has a six- or seven-part answer. That’s because securing

containers doesn’t involve just deploying one tool or paying careful

attention to one area where vulnerabilities can exist. Because a

containerized software stack involves so many different components, you

need to secure many different layers. The tools designed to help you

harden one part of your environment won’t protect other segments.

Commercial security tools do exist, and are designed to provide

relatively comprehensive security or container environments. They are

good tools, and they can certainly be useful parts of a container

security strategy, but they have their limitations. To be truly secure,

you need to analyze each of the layers in your stack, and be sure that

they are covered adequately by the security tools or processes you put

in place. This post helps you plan a complete container security

strategy by outlining all of the layers you need to secure, and

explaining the primary considerations to keep in mind when securing each

one.

### Understanding the Layers

When planning your approach to container security, you should begin by

identifying all of the different layers of the software stack that you

have to secure. Those layers include:

**Your image registry.** This is the part of your stack that hosts your

images. Security vulnerabilities here could allow attackers to add

malicious images to your environment, or steal private data. **The orchestrator.** Your orchestrator is the brains of your container

cluster. If it’s not secured, an attacker could use it to disrupt

service, or possibly intercept private information. **Your hosting infrastructure.** The operating system or cloud environment that hosts

your container environment needs to be secure—otherwise, it can become

the front door for an attack against your environment. **Storage systems.** To protect the sensitive data hosted on your container

cluster, you need to keep the storage system you use free of

vulnerabilities. **The container daemon.** If the Docker daemon is

compromised, attackers can shut down containers or gain unauthorized

access to the ones you’re running. **Application code inside your containers.** Last but not least, you need to make sure the code that

runs inside your containers is free of vulnerabilities that could allow

attackers to disrupt or control your application when it is running.

### Securing the Stack

There are two main considerations to bear in mind when securing your

image registry. First, you need to make sure to lock down access

control. Your approach to doing this will vary depending on which

registry you use. Some registries offer finer-tuned access control

features than others, but all of the mainstream registries provide some

security controls. (For an overview of different registry options,

including a comparison of the security features built into them, check

out [Container Registries You May Have Missed](https://rancher.com/container-registries-might-missed/)) The

second challenge is detecting security vulnerabilities inside container

images themselves. For this task, two tools are available: Clair from

CoreOS and Docker Security Scanning from Docker. Both of these image

scanners will check an image for known malware signatures. They’re

designed mainly to be integrated into CoreOS’s and Docker’s registries,

but they can also work in standalones mode by manually scanning an

image.

### Orchestrator

Securing your orchestrator requires more work than simply turning on

some access control features or running a scanner. Orchestrators are

complex tools, and their inner workings vary from one orchestrator to

another. Explaining all of the details of configuring an orchestrator

for maximum security is beyond the scope of this article. In general,

however, key principles to follow include:

- Making sure you install your orchestrator from an official source.

  Be wary of third-party package repositories.
- Keep your orchestrator up-to-date.
- When configuring your orchestrator and the cluster it manages, limit

  public-facing network connections to the minimum necessary to run

  your application.
- Configure your orchestrator for automatic failover and high

  availability in order to mitigate the impact of potential DDoS or

  similar attacks.

If you use Kubernetes, you may also find [this article on security best practices](http://blog.kubernetes.io/2016/08/security-best-practices-kubernetes-deployment.html)

to be helpful. A similar guide for Mesos is available

[here](https://devops.com/mesos-security-awareness-considerations/).

### Hosting Infrastructure

The infrastructure you use to host your container environment could be

on-premises, in the cloud, or in some cases, a mix of both. Whatever it

looks like, you should be sure to secure the infrastructure as much as

possible. If you manage your host servers yourself, make sure they are

locked down with kernel hardening tools like SELinux or AppArmor. For

cloud-based deployments, take advantage of access control features (such

as IAM roles on AWS) to configure access to your environment. Security

auditing and monitoring tools will help to keep your infrastructure

secure, too.

### Storage

When it comes to containers and storage, however, one important point to

keep in mind is that, in many cases, many containers might share access

to the same storage directories. This happens if you map directories

inside containers to a shared location on the host. Under these

conditions, it’s especially important to make sure that any container

with access to a shared storage location is secure. You should also

limit storage access to read-only in cases where a container does not

need write permissions. And it’s always a good idea to have rollback

features built into your storage system so that you can undo changes to

data if necessary.

### Container Daemon

Running SELinux or AppArmor on the container host can help to defend the

Docker daemon against attack, but that is only one security challenge to

keep in mind when it comes to the daemon. You should also make sure that

daemon socket connections are [securely authenticated and encrypted](https://docs.docker.com/engine/security/https/). Of course,

it’s also essential to keep your Docker installation up-to-date to avoid

security vulnerabilities in the daemon.

### Application Code

You should secure the code running inside your containers just as you

would secure any type of application code—by obtaining the code from a

trusted source and auditing it with security tools designed to catch

vulnerabilities. Clair and Docker Security Scanning can help with the

latter, but they are not designed to be all-purpose static application

security testing solutions. For that reason, you may benefit from

deploying a tool like Veracode or OWASP to scan your code for

vulnerabilities.

### Conclusion

Keeping a container environment secure is a big task because there are

so many moving parts. The details of your security strategy will vary

depending on exactly which types of registries, orchestrators, hosting

infrastructure and so on that you choose to include in your stack. But

whatever your environment looks like, the key to keeping it secure is to

remember that there is no one-stop shopping. You have to keep all of the

different layers in mind, and develop a security plan that addresses

each one. *Chris Riley (@HoardingInfo) is a technologist who has spent 12 years helping organizations transition from traditional development practices to a modern set of culture, processes and tooling. In addition to being a research analyst, he is an O’Reilly author, regular speaker, and subject matter expert in the areas of DevOps strategy and culture. Chris believes the biggest challenges faced in the tech market are not tools, but rather people and planning.*
