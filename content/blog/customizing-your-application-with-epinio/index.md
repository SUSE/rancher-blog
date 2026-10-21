---
title: "Customizing your Application with Epinio"
date: 2022-05-26T15:48:04
slug: "customizing-your-application-with-epinio"
author: "Andrew Gracey"
image: "images/epinio.png"
products: ["Epinio"]
tags: ["developer-experience"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 91825
  original_url: "https://www.suse.com/c/rancher_blog/customizing-your-application-with-epinio/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Epinio discontinued"
  redirect_target: "rancher.com/blog (hub)"
---

One of the best things about Kubernetes is just how absurdly flexible it is.

You, as an admin, can shape what gets deployed into what is the best for your business. Whether this is a basic webapp with just a deployment, service and ingress; or if you need all sorts of features with sidecars and network policies wrapping the serverless service-mesh platform of the day. The power is there.

This has long been one of the weaknesses of the PaaS style approach since you tend to be locked into what the platform builder's opinions are at the time.

With some of the features in recent releases of Epinio, we've found a middle ground!

You can now give your developers both the ease of use, short learning curve and speed that they want while also getting the ability to shape what applications should look like in your environments!

This takes the shape of two features: custom Application Template(s), and a Service Marketplace. Let's dive into what these are and how to use them.

## Application Templates in Epinio

The way a deployment works with Epinio is that the developer pushes their code to the platform where it's cached in an object store, built using buildpacks, pushed to a registry, generates a values.yaml, then deployed using helm to the local cluster.

In past releases, all of this was configurable except the deployment itself. You could use your own object storage, buildpacks and registry but were locked into a basic application that was just a deployment, service and ingress.

We've introduced a new custom resource in Epinio that allows for a platform admin to set up a list of application templates that can be selected by the application developer for their application!

With this feature, you could offer a few different styles of applications to your developers to choose from while still keeping the developer's life easier as well as allowing for governance of what gets deployed. For example, you could have a secure chart, a chart with an open-telemetry sidecar, a chart that deploys Akri configurations, a chart that deploys to Knative or whatever you can dream of!

#### So how do I set up an application template in Epinio?

Good question, I'm glad you asked ![(big grin)](https://confluence.suse.com/s/-p2dvsd/8703/zb070w/_/images/icons/emoticons/biggrin.svg "(big grin)")

The first thing you need is a helm chart! (Feel free to copy from our default template found here: <https://github.com/epinio/helm-charts/blob/main/chart/application>)

Since Epinio generates the values.yaml during the push, your chart will be deployed with values that look similar to:

```
epinio:
  tlsIssuer: epinio-ca
  appName: placeholder
  replicaCount: 1
  stageID: 999
  imageURL: myregistry.local/apps/epinio-app
  username: user
  routes:
  - domain: epinio-app.local
    id: epinio-app.local
    path: /
  env:
  - name: env-name
    value: env-value
  configurations:
  - config-name
  start: null
```

Note: The ability for developers to pass in additional values is being added soon: <https://github.com/epinio/epinio/issues/1252>

Once you have all your customizations done, build it into a tgz file using `helm package` and host it somewhere accessible from the cluster (potentially in the cluster itself using Epinio?).

With the chart published, you can now expose it to your developers by adding this CRD to the namespace that Epinio is installed in ("epinio" if you followed the docs):

```
apiVersion: application.epinio.io/v1
kind: AppChart
metadata:
  name: my-custom-chart
  namespace: epinio
spec:
  description: Epinio chart with everything I need
  helmChart: https://example.com/file.tgz
  shortDescription: Custom Application Template with Epinio
```

With this done, the developer can view what templates can be used using:

```
epinio app chart list
```

Then when they push their code, they can pick the chart they want with:

```
epinio push --name myapp --app-chart my-custom-chart
```

## Service Marketplace in Epinio

The other huge piece of the puzzle is the service marketplace functionality. We went around in circles for a bit on what services to enable or which set of operators to support. Instead, we decided that Helm was a good way to give choice.

Similar to the Application Templates, the Service Marketplace offerings are controlled via CRDs in the epinio namespace so you can easily add your own.

By default, we include charts for Redis, Postgres, MySQL and RabbitMQ for use in developer environments.

To add a helm chart into the marketplace, create a new Epinio Service object that looks like:

```
apiVersion: application.epinio.io/v1
kind: Service
metadata:
  name: my-new-service
  namespace: epinio
spec:
  appVersion: 0.0.1
  chart: custom-service
  chartVersion: 0.0.1
  description: |
    This is a custom chart to demo services.
  helmRepo:
    name: custom-chart
    url: https://charts.bitnami.com/bitnami
  name: custom-chart
  shortDescription: A custom service 
  values: |-
    exampleValue: {}
```

Since we are using helm, you can put any Kubernetes object in the marketplace. This is super helpful as it means that we can seamlessly tie into other operator-based solutions (such as [Crossplane](https://crossplane.io/) or [KubeDB](https://kubedb.com/) but I'll leave that as an exercise for the reader).

We are working toward a 1.0.0 release that includes a better onboarding flow, improved security, bringing the UI to parity with the CLI and improving documentation of common workflows. You can track our progress in the milestone: <https://github.com/epinio/epinio/milestone/6>

## Give Epinio a try at <https://epinio.io/>
