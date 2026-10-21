---
title: "Citrix and Rancher Integration: Cloud-Native Stack on Kubernetes"
date: 2020-02-19T09:45:00
slug: "citrix-and-rancher-integration-cloud-native-stack-on-kubernetes"
author: "Rancher Admin"
image: "images/rancher_blog_Citrix-Partner-01.png"
products: ["Rancher Manager"]
tags: ["networking"]
content_type: "company-news"
draft: true
migration:
  wp_id: 85977
  original_url: "https://www.suse.com/c/rancher_blog/citrix-and-rancher-integration-cloud-native-stack-on-kubernetes/"
  disposition: move_to_suse
  commercial: true
  outdated_reason: "Partner integration from 2020 (Citrix)"
  redirect_target: "suse.com (new URL pending)"
---

Kubernetes and containers are changing how applications are built, deployed and managed. Rancher makes application deployment simple and easily portable regardless of location or infrastructure.

At Citrix, we operate on the same core principle. We provide application delivery and load balancing solutions for a high-quality user experience, to any device, across any network, for your web, traditional and cloud-native applications regardless of where they are hosted.

Citrix is excited about our collaboration with Rancher Labs to deliver our cloud-native stack on their complete [Kubernetes management platform](https://rancher.com/products/rancher/). Citrix Cloud Native Stack integrates with Rancher as pre-built and reusable application stack templates. These templates stitch together all components of the Citrix Cloud Native Stack ([Citrix Ingress Controller](https://developer-docs.citrix.com/projects/citrix-k8s-ingress-controller/en/latest/), [Citrix Node Controller](https://github.com/citrix/citrix-k8s-node-controller), [Citrix Observability Exporter](https://github.com/citrix/citrix-observability-exporter), [IPAM](https://developer-docs.citrix.com/projects/citrix-k8s-ingress-controller/en/latest/crds/vip/)). You can modify and deploy these templates into running application stacks via the Rancher admin console.

Citrix Cloud Native Stack is now available in the Rancher app catalog. Check out [Github](https://github.com/rancher/charts) for more details.

The benefits of running the Citrix Stack in Rancher include:

1. **Production-grade Ingress solutions** for cloud native environments with the best performance/scale in the industry.
2. Your **choice of the best proxy architecture** for your requirements (see the blog series on [how to evaluate proxy architectures for your application delivery](https://thenewstack.io/part-1-the-best-way-to-select-a-proxy-architecture-for-microservices-application-delivery/)).
3. **Different Citrix ADC form factors** (Appliance, Virtual Machine(s), Cloud Instance(s), Containers) that are built on a single code base, enabling a consistent approach to tooling to manage all the Citrix devices.
4. **Stakeholder requirements.** Citrix understands the needs of the different application stakeholders (Developers, DevOps, DevSecOps, SREs and Platform team) and caters to their requirements.
5. **Rich Observability Stack** with deep integration into open source tools like [Prometheus](https://prometheus.io/), [Grafana](https://grafana.com/), [Zipkin](https://zipkin.io/)/Jaegar, [Kibana](hhttps://www.elastic.co/products/kibana) and many more.
6. **API Gateway functionality** provided by Citrix to handle concurrent API calls, including traffic management, authorization and access control, and monitoring.

We will cover the benefits of Citrix and Rancher in detail in future blogs, so stay tuned. Also, look out for an upcoming Citrix and Rancher workshop that highlights how the solutions complement each other.

## More Resources

Get a fundamental understanding of how Rancher works with Kubernetes. This detailed guide explains the details of Rancher’s features and functionality. [Read the Rancher Architecture whitepaper.](https://more.suse.com/fy21-global-web-landing-page-rancher2-technical-architecture)
