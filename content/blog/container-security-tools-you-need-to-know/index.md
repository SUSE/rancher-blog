---
title: "Container Security Tools You Need to Know"
date: 2017-06-29T10:16:00
slug: "container-security-tools-you-need-to-know"
author: "Rancher Admin"
products: ["Docker/containers (generic)"]
tags: ["security"]
content_type: "explainer"
draft: true
migration:
  wp_id: 86594
  original_url: "https://www.suse.com/c/rancher_blog/container-security-tools-you-need-to-know/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "2017 Docker security tools list"
  redirect_target: "https://rancher.com/blog (hub)"
---

Cyber security is no longer a luxury. If you need a reminder of that,

just take a look at the seemingly endless number of stories appearing in

the news lately about things like malware and security breaches. If you

manage a Docker environment, and you want to help make sure your

organization or users are not mentioned in the news stories that

accompany the next big breach, you should know the tools available to

you for helping to secure the Docker stack, and put them to work. This

post identifies the Docker security tools available (both native ones

from Docker itself and third-party options) that can help to secure your

Docker containers.

### Docker Benchmark Security

![](images/rancher_blog_CICD-cover-150x150.jpg) Our newly-updated eBook walks

you through incorporating containers into your CI/CD pipeline. [Download the ebook](https://info.rancher.com/cicd-with-docker-ebook)

One of the first security tools for Docker that you should check out is

[Docker Benchmark for Security](https://github.com/docker/docker-bench-security). Docker

Benchmark for Security is a simple script that is designed to test your

Docker deployment to ensure that it adheres to established security best

practices. One of the things that makes Docker Benchmark for Security so

useful is that the development of the best practices was based on a

consensus of opinions from industry experts in a variety of different

job roles. Consultants, software developers, and security and compliance

experts all had a voice in establishing the best practices. You can find

a full description of the best practices and the rationale behind them

on the [Center for Internet Security](https://www.cisecurity.org/cis-benchmarks/).

### CoreOS Clair

[CoreOS Clair](https://github.com/coreos/clair) is a vulnerability

scanning engine that is designed for Docker containers. This API-based

scanning engine looks at each container layer, and searches for and then

reports on known vulnerabilities. CoreOS Clair has two primary use

cases. First, Clair is useful for checking images that you did not

create yourself. If, for example, you were to download an image from the

Internet, it would be difficult to know for sure whether or not that

image is safe for use. CoreOS Clair can help you make that

determination. A second use case for CoreOS Clair is that it can be used

to block and/or alert you to the use of insecure software.

### Docker Security Scanning

[Docker Security Scanning](https://github.com/kost/dockscan) is another

security vulnerability scanning tool for Docker. While it might be

tempting to dismiss this tool as just another scanning engine, there are

a couple of things about this tool that make it worth paying attention

to. First, [Docker Security](https://www.suse.com/c/six-essential-docker-security-best-practices-for-safe-containers/) isn’t limited to only scanning Docker

containers. The tool also checks for Docker installation security

issues. Furthermore, the tool is able to scan both local and remote

Docker installations. The other thing that makes Docker Security

Scanning worth a look is the fact that it is based around the use of

plugins. These plugins make Docker Security Scanning extensible, so that

functionality can be added as the tool matures. They are designed to be

easy to write, so an organization could conceivably create plugins for

its own purposes.

### Drydock

Drydock is designed to function similarly to Docker Benchmark for

Security, but is intended to be more flexible in its use. Like Docker

Benchmark, Drydock is a security auditing tool for Docker. The thing

that makes Drydock so unique is that it allows its users to create

custom audit profiles. These profiles can be used to fine-tune the

auditing process by eliminating audits that are known to cause a lot of

clutter within the resulting report (noise alerts). Drydock’s custom

audit profiles can also be used to deactivate audit tests that do not

pertain to your environment, or are known to produce false alarms.

Unlike some of the other tools that are available, Drydock makes it

surprisingly easy to create custom profiles. The tool includes a

built-in profile that contains all of the audit tests that will be

performed. You can prevent a check from running simply by commenting out

the check. You can download Drydock on

[GitHub.](https://github.com/zuBux/drydock)

### Twistlock

[Twistlock](https://www.twistlock.com/) is yet another security auditing

tool for Docker. One thing that makes Twistlock different from some

competing solutions is that it is a commercial application. There is a

free Developer Edition, and a licensed Enterprise Edition. Twistlock is

designed to scan each individual layer of the container stack, and is

able to use content fingerprinting techniques to identify the various

components, as well as known vulnerabilities that may be associated with

those components. The Enterprise Edition of Twistlock uses machine

learning to help to identify vulnerabilities. It also provides automated

policy creation and enforcement capabilities. The free Developer Edition

has a lot of similarities to the Enterprise Edition, but requires

policies to be created manually, and relies upon community support. The

Developer Edition is also limited to 10 repos and two hosts.

### Conclusion

As Docker has matured and moved into production, the importance of

properly securing Dockerized environments has increased. Fortunately, a

range of tools, including both free and commercial options, are

available for helping to harden your Docker stack with more (like

[Deepfence](http://deepfence.io/), [NeuVector](http://neuvector.com/),

and [Anchore](https://anchore.com/)) appearing all time. ***Brien Posey is a freelance technology author and 15-time Microsoft MVP. Prior to going freelance, Posey was a CIO for a national chain of hospitals and healthcare facilities. He also served as Lead Network Engineer for the United States Department of Defense at Fort Knox. In addition to Posey’s continued work in IT, Posey is in his third year of training as a commercial scientist-astronaut candidate.***
