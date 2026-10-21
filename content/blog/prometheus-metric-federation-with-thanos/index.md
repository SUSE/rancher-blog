---
title: "Prometheus Metric Federation with Thanos"
date: 2020-07-14T09:56:00
slug: "prometheus-metric-federation-with-thanos"
authors: ["Gaurav Mehta"]
image: "images/rancher_blog_prometheus-thanos-featured.png"
products: ["Rancher Manager"]
tags: ["observability", "multi-cluster"]
content_type: "tutorial"
draft: false
migration:
  wp_id: 86293
  original_url: "https://www.suse.com/c/rancher_blog/prometheus-metric-federation-with-thanos/"
  disposition: migrate_refresh
  commercial: false
  outdated_reason: "Rancher 2.x built-in monitoring pre-2.5"
  redirect_target: ""
---

Read our free white paper: How to Build a Kubernetes Strategy[Download Now](https://more.suse.com/fy21-global-web-landing-page-how-to-build-enterprise-kubernetes-strategy)

Prometheus is a CNCF graduated project for monitoring and alerting. It is one of the most widely used monitoring and alerting tools in the Kubernetes ecosystem. Rancher users can leverage Prometheus quickly by using the built-in monitoring [stack.](https://rancher.com/docs/rancher/v2.x/en/cluster-admin/tools/monitoring/)

Prometheus stores its metrics as a time series database on the local [disk.](https://prometheus.io/docs/prometheus/latest/storage/) Prometheus local storage is limited by the size of the disk and amount of metrics it can retain.

Prometheus, however, allows integrations with remote systems for writing and reading metrics using the \_remote*write* and \_remote*read* directives. Prometheus also supports a wide number of remote endpoints and storage [integrations.](https://prometheus.io/docs/operating/integrations/#remote-endpoints-and-storage)

In this blog, we will explore a quick and easy way to set up Rancher monitoring remote endpoint integration with Thanos receive. [Thanos](https://thanos.io/) is an open source, highly available Prometheus setup with long-term metric capabilities. You can use this solution to federate metrics across all of your Prometheus instances, and allow central Grafana dashboarding to run off Thanos.

*Important Note:* As part of metric federation, the project/cluster metrics will be leaving the Rancher management plane boundaries. It is essential for cluster administrators to ensure appropriate access control mechanisms are in place to restrict access to this metric store.

## Installing Thanos

For this blog, we can set up Thanos on a Kubernetes cluster quickly using [kube-thanos](https://github.com/thanos-io/kube-thanos).

We will need the following Thanos components:

- Thanos store gateway
- Thanos receiver
- Thanos querier
- Object storage

The solution will look something like this:

```
                 +
Tenant's Premise | Provider Premise
                 |
                 |            +------------------------+
                 |            |                        |
                 |  +-------->+     Object Storage     |
                 |  |         |                        |
                 |  |         +-----------+------------+
                 |  |                     ^
                 |  | S3 API              | S3 API
                 |  |                     |
                 |  |         +-----------+------------+
                 |  |         |                        |       Store API
                 |  |         |  Thanos Store Gateway  +<-----------------------+
                 |  |         |                        |                        |
                 |  |         +------------------------+                        |
                 |  |                                                           |
                 |  +---------------------+                                     |
                 |                        |                                     |
+--------------+ |            +-----------+------------+              +---------+--------+
|              | | Remote     |                        |  Store API   |                  |
|  Prometheus  +------------->+     Thanos Receiver    +<-------------+  Thanos Querier  |
|              | | Write      |                        |              |                  |
+--------------+ |            +------------------------+              +---------+--------+
                 |                                                              ^
                 |                                                              |
+--------------+ |                                                              |
|              | |                PromQL                                        |
|    User      +----------------------------------------------------------------+
|              | |
+--------------+ |
                 +
```

[*Source: Thanos receive proposal*](https://github.com/thanos-io/thanos/blob/master/docs/proposals/201812_thanos-remote-receive.md)

Thanos supports several object storage [configurations](https://thanos.io/storage.md/#configuration).

We will use [MinIO](https://min.io) as our object storage. You need to define the object storage in a secret named thanos-objectStorage, which needs to be in the namespace of your Thanos deployment.

The `thanos-config.yaml` looks like this:

```
type: s3
config:
  bucket: thanos
  endpoint: ${minio-endpoint}
  access_key: ${minio-access-key}
  secret_key: ${minio-secret-key}
  insecure: true
```

You can create the secret as follows:
`kubectl create secret generic thanos-objectstorage --from-file=thanos.yaml="$PATH_TO_CONFIG"/thanos-config.yaml`

## Configuring Rancher Monitoring

The Prometheus version packaged with the Rancher monitoring operator already supports `remote_read` and `remote_write` integrations.

The extra settings for the Thanos receive endpoint can be passed via the advanced options as follows:

![Image 01](images/rancher_blog_image-01.jpg)

We need to specify a unique name as required by the Prometheus `remote_write` specification.

```
# The name will be used in metrics and logging in place of a generated value to help users distinguish between
# remote write configs.
[ name: <string> ]
```

Once you’ve deployed monitoring, you should be able to see your metrics using the Thanos querier.

![Image 02](images/rancher_blog_image-02.jpg)

The stored metrics will also be available in the object storage.

![Image 03](images/rancher_blog_image-03.jpg)

Since all cluster metrics will be available in this Thanos install, the owner for the workloads needs to ensure that access to workload and metrics is secured appropriately.

## Conclusion

Using the remote write and read capabilities within Rancher monitoring (Prometheus) and the Thanos receiver, you can achieve long-term metric storage and a global view of your multiple cluster metrics in a few easy steps.

Read our free white paper: How to Build a Kubernetes Strategy[Download Now](https://more.suse.com/fy21-global-web-landing-page-how-to-build-enterprise-kubernetes-strategy)
