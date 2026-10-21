---
title: "Five Reasons to Use Base Container Images"
date: 2022-10-19T17:38:50
slug: "five-reasons-to-use-base-container-images"
author: "German M. Yebenes"
products: ["Other"]
tags: ["security", "developer-experience"]
content_type: "explainer"
draft: false
migration:
  wp_id: 95618
  original_url: "https://www.suse.com/c/rancher_blog/five-reasons-to-use-base-container-images/"
  disposition: migrate_refresh
  commercial: false
  outdated_reason: "SUSE BCI details from 2022"
  redirect_target: ""
---

Nowadays, the software development paradigm is based on containerizing applications to deploy on pods to let Kubernetes manage it.  Containerized applications can then allow Kubernetes to manage its deployment, replication, high availability, metrics and other capabilities so that the application can focus on doing what it was designed to do. This technology is used for projects and by customers all over the globe.

To start containerizing applications, you must use an image, usually a language-based one (Golang, Python, Rust, .NET, etc.) There are many image providers, from individual contributors submitting images to any registry to enterprise-level images by several vendors. Other OS-based images can help you during the development process.

I had an opportunity to engage in an interesting conversation with Software Engineers. We discussed one topic: **“W****hat are the major concerns with choosing the right container image for your needs?”**

In this article, I will articulate and address some of the concerns Software Engineers expressed to me. 

## Software engineering concerns

- Security: As a developer, I need to ensure I am not using a version affected by a CVE or any other vulnerability that could be exploited; how can I achieve this?

- Redistribution: As a developer, I need my application to deploy while being agnostic to the underlying host, architecture or orchestration technology.
- Repositories and tooling: Sometimes there are tools I need to use (git, compilers, libraries, etc.), but most of the images do not provide reliable repositories where I can get the tools and packages I need.
- Availability: Both open source contributors and enterprise software engineers create software for several platforms and architectures (ARM, x86\_64...). Depending on the needs, images should be adaptable not only for the architecture but also for the language specification. Is there a reliable registry to use as a single point of reference to get the latest images maintaining a tag-based history of the images?
- Supportability and lifecycle: An image not being supported is, in most cases, invalidated for enterprise-level software; there should be a vendor providing support for the base I am using to create or containerize applications, even more for ISVs/IHVs. Also, images must be proactive, providing updates, security fixes and performance during their lifecycles.

## The Base Container Image (BCI) approach to addressing these issues

SUSE released “Base Container Images” (BCI),  an enterprise-level container image focused on security, usability, agility and developer experience. BCI images are not only OS-based but also include language packs, busybox, base and minimal as well. This makes them ideal for any kind of development challenge, both community projects and productive applications.

BCI helps address these upcoming issues:

### Security

Nobody wants to build an application with a piece of software affected by Common Vulnerabilities and Exposures (CVE). As a developer, using a secure image ensures a reliable baseline to develop the applications. Let’s see some examples:

[Trivy](https://github.com/aquasecurity/trivy) is an image scanning software to check the vulnerabilities. 

```
➜  ~ trivy image registry.suse.com/bci/bci-base

2022-10-09T03:47:42.403+0200 INFO Need to update DB
2022-10-09T03:47:42.404+0200 INFO DB Repository: ghcr.io/aquasecurity/trivy-db
2022-10-09T03:47:42.404+0200 INFO Downloading DB...
34.35 MiB / 34.35 MiB [-------------------------------------------------------------------------------------------------------] 100.00% 23.13 MiB p/s 1.7s
2022-10-09T03:47:45.503+0200 INFO Vulnerability scanning is enabled
2022-10-09T03:47:45.503+0200 INFO Secret scanning is enabled
2022-10-09T03:47:45.503+0200 INFO If your scanning is slow, please try '--security-checks vuln' to disable secret scanning
2022-10-09T03:47:45.503+0200 INFO Please see also https://aquasecurity.github.io/trivy/v0.32/docs/secret/scanning/#recommendation for faster secret detection
2022-10-09T03:47:45.528+0200 INFO Detected OS: suse linux enterprise server
2022-10-09T03:47:45.528+0200 INFO Detecting SUSE vulnerabilities...
2022-10-09T03:47:45.528+0200 INFO Number of language-specific files: 0
registry.suse.com/bci/bci-base (suse linux enterprise server 15.4)
Total: 0 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 0, CRITICAL: 0)
```

***bci-base*** *scanning result*

The same results also happen for bci-micro, bci-minimal, buxybox and init. 

```
➜  ~ trivy image registry.suse.com/bci/bci-micro 

[…] 
2022-10-09T03:55:17.952+0200 INFO Detecting SUSE vulnerabilities... 
2022-10-09T03:55:17.953+0200 INFO Number of language-specific files: 0 
registry.suse.com/bci/bci-micro (SUSE Linux enterprise server 15.4) 

Total: 0 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 0, CRITICAL: 0) 
```

***bci-micro, bci-init, bci-buxybox*** *scanning results* 

These outputs can be achieved by maintaining the lifecycle of the images ensuring a reaction to every new vulnerability published in [CVE Mitre Database.](https://cve.mitre.org/)

### Redistribution

Applications, by design, must be redistributed even more if we talk about ISVs/IHVs software. There are two concerns here: 

- **EULA Agreements:**

According to BCI EULA, the only restriction to redistribute any application comes from third-party software or a subscription-bound resource; for instance, a package from a private repository or a hardware-specific vendor based on a license. No other restriction applies; any application developed with the image as it is provided will be redistributed. 

- **Software**:

BCI comes with a repository so you can add packages to the image as needed adding flexibility to customize the image while keeping the application redistributable, with no external dependencies added. 

### Repositories and tooling

The eternal discussion: what is the middle point between covering any need developers may have and trying to keep image footprints as small and simple as possible? 

Security is a major concern when it comes to enterprise-level images but also the developer experience. BCI faces this by providing tooling, compilers and other useful software through a repository available to every image. With *zypper* available, developers can add a layer on top of the image installing packages as required by their applications. 

There is no need to manually add repositories, look for the package, check and solve dependencies and rely on external software or package sources. 

These repositories are free to use, and SUSE maintains its packages. 

### Availability

According to the registry, BCI is provided and supported for different architectures: **aarch64, ppc64le, s390x and x86\_64.** This makes it easier to centralize the base images on BCI regardless of the type of application you are creating (Edge, IoT, sensors, devices, web, microservices....) 

BCI also provides language-based images with **Golang, Python, Rust, .NET, OpenJDK, NodeJS** and more for applications using a specific language.

### Supportability and lifecycle

SUSE designed BCI, and images are being supported commercially through a subscription for enterprise-level, ISV and IHVs. The supportability matrix covers the bases of BCI and language packs; you can check the status of the supportability on the [BCI registry.](https://registry.suse.com/)

BCI is also an open source project where you can see the actual state of the development, how they were built for the different architecture and everything related to the development stage.  

The images use Open Build Service (OBS) which is available for everyone, check it out! 

- [BCI Development project for SLE 15 SP4](https://build.opensuse.org/project/show/devel:BCI:SLE-15-SP4)
- [BCI Development project for SLE 15 SP3](https://build.opensuse.org/project/show/devel:BCI:SLE-15-SP3)

### Conclusion

Along with the portfolio of images out there, there are many possibilities to choose from. SUSE provides a secure-focused product while also focusing on the developer experience. 

BCI provides a flexible container image ecosystem, keeping the footprint as small as possible. Simultaneously, we provide a mechanism to extend images agilely so developers can focus on the application. 

Through subscriptions, ISVs and IHVs can leverage their applications providing SUSE enterprise-level support to the base images their applications are based on. 

Since BCI can be deployed and used in any type of host without breaking the supportability matrix, redistribution is no problem; anyone can access the images, build, and redistribute the application without further restrictions. 

Package repositories are there to provide flexibility to the developers without adding any kind of restrictions. The packages and their integration with the images are maintained by SUSE, an industry-leading vendor with reliability and confidence.

Get started by checking out these resources! 

[BCI Docs](https://documentation.suse.com/smart/linux/html/concept-bci-get-started/index.html) 

[Frequently Asked Questions](https://www.suse.com/products/base-container-images/FAQ/) 

[SUSE Container Images](https://registry.suse.com)
