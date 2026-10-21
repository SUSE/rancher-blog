---
title: "Integrate AWS Services into Rancher Workloads with TriggerMesh"
date: 2020-09-09T09:51:00
slug: "integrate-aws-services-into-rancher-workloads-with-triggermesh"
author: "Rancher Admin"
image: "images/rancher_blog_triggermesh-featured.png"
products: ["Rancher Manager"]
tags: ["cloud", "aws"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 86156
  original_url: "https://www.suse.com/c/rancher_blog/integrate-aws-services-into-rancher-workloads-with-triggermesh/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher catalog v1 era app"
  redirect_target: "rancher.com/blog (hub)"
---

Don’t miss the Computing on the Edge with Kubernetes conference on October 21. [Register Now](https://www.accelevents.com/e/edgeconference2020) Many businesses use cloud services on AWS and also run workloads on Kubernetes and Knative. Today, it’s difficult to integrate events from AWS to workloads on a Rancher cluster, preventing you from taking full advantage of your data and applications. To trigger a workload on Rancher when events happen in your AWS service, you need an event source that can consume AWS events and send them to your Rancher workload.

TriggerMesh Sources for Amazon Web Services (SAWS) are event sources for AWS services. Now available in the Rancher catalog, SAWS allows you to quickly and easily consume events from your AWS services and send them to your workloads running in your Rancher clusters.

SAWS currently provides event sources for the following Amazon Web Services:

- [CodeCommit](https://aws.amazon.com/codecommit/)
- [Cognito](https://aws.amazon.com/cognito/)
- [DynamoDB](https://aws.amazon.com/dynamodb/)
- [Kinesis](https://aws.amazon.com/kinesis/)
- [Simple Notifications Service (SNS)](https://aws.amazon.com/sns/)
- [Simple Queue Service (SQS)](https://aws.amazon.com/sqs/)

[TriggerMesh SAWS](https://github.com/triggermesh/aws-event-sources/) is open source software that you can use in any Kubernetes cluster with Knative installed. In this blog post, we’ll walk through installing SAWS in your Rancher cluster and demonstrate how to consume Amazon SQS events in your Knative workload.

## Getting Started

To get you started, we’ll walk you through installing SAWS in your Rancher cluster, followed by a quick demonstration of consuming Amazon SQS events in your Knative workload.

### SAWS Installation

1. TriggerMesh SAWS requires the [Knative serving component](https://knative.dev/docs/serving/). Follow the Knative documentation to [install the Knative serving component](https://knative.dev/docs/install/any-kubernetes-cluster/#installing-the-serving-component) in your Kubernetes cluster. Optionally, you may also install the [Knative eventing component](https://knative.dev/docs/eventing/) for the complete Knative experience. We used:

   ```
   kubectl --namespace kong get service kong-proxy
   ```

   We created a cluster from the GKE provider. A LoadBalancer service will be assigned an external IP, which is necessary to access the service over the internet.
2. With Knative serving installed, search for aws-event-sources from the Rancher applications catalog and install the latest available version from the helm3-library. You can install the chart at the Default namespace.

   ![Image 01](images/rancher_blog_image-01.jpg)

Remember to update the **Knative Domain** and **Knative URL Scheme** parameters during the chart installation. For example, in our demo cluster we used **Magic DNS (xip.io**) for configuring the DNS in the Knative serving installation step, so we specified 34.121.24.183.xip.io and http as the values of **Knative Domain** and **Knative URL Scheme**, respectively.

That’s it! Your cluster is now fully equipped with all the components to consume events from your AWS services.

### Demonstration

To demonstrate the TriggerMesh SAWS package functionality, we will set up an Amazon SQS queue and visualize the queue events in a service running on our cluster. You’ll need to have access to the SQS service on AWS to create the queue. A specific role is not required. However, make sure you have all the permissions on the queue: [see details here](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-overview-of-managing-access.html.).

#### Step 1: Create SQS Queue

![Image 02](images/rancher_blog_image-02.jpg)

Log in to the Amazon management console and create a queue.

#### Step 2: Create AWS Credentials Secret

Create a secret named awscreds containing your AWS credentials:

```
$ kubectl -n default create secret generic awscreds

--from-literal=aws_access_key_id=AKIAIOSFODNN7EXAMPLE

--from-literal=aws_secret_access_key=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
```

*Update the values of aws\_access\_key\_id and aws\_secret\_access\_key in the above command.*

#### Step 3: Create the AWSSQSSource Resource

Create the AWSSQSSource resource that will bring the events that occur on the SQS queue to the cluster using the following snippet. Remember to update the arn field in the snippet with that of your queue.

```
$ kubectl -n default create -f - << EOF

apiVersion: sources.triggermesh.io/v1alpha1

kind: AWSSQSSource

metadata:

name: my-queue

spec:

arn: arn:aws:sqs:us-east-1:043455440429:SAWSQueue

credentials:

  accessKeyID:

    valueFromSecret:

     name: awscreds

     key: aws_access_key_id

  secretAccessKey:

    valueFromSecret:

     name: awscreds

     key: aws_secret_access_key

sink:

 ref:

    apiVersion: v1

   kind: Service

   name: sockeye

EOF
```

Check the status of the resource using:

```
$ kubectl -n default get awssqssources.sources.triggermesh.io

NAME READY REASON SINK AGE

my-queue True http://sockeye.default.svc.cluster.local/ 3m19s
```

#### Step 4: Create Sockeye Service

[Sockeye](https://github.com/n3wscott/sockeye/) is a WebSocket-based CloudEvents viewer. Our `my-queue` resource created above is set up to send the cloud events to a service named sockeye as configured in the sink section. Create the sockeye service using the following snippet:

```
$ kubectl -n default create -f - << EOF

apiVersion: serving.knative.dev/v1

kind: Service

metadata:

name: sockeye

spec:

template:

 spec:

   containers:

    - image: docker.io/n3wscott/sockeye:v0.5.0@sha256:64c22fe8688a6bb2b44854a07b0a2e1ad021cd7ec52a377a6b135afed5e9f5d2

EOF
```

Next, get the URL of the sockeye service and load it in the web browser.

```
$ kubectl -n default get ksvc

NAME URL LATESTCREATED LATESTREADY READY REASON

sockeye http://sockeye.default.34.121.24.183.xip.io sockeye-fs6d6 sockeye-fs6d6 True
```

### Step 5: Send Messages to the Queue

We now have all the components set up. All we need to do is to send messages to the SQS queue.

![Image 03](images/rancher_blog_image-03.jpg)

The cloud events should appear in the sockeye events viewer.

![Image 04](images/rancher_blog_image-04.jpg)

## Conclusion

As you can see, using TriggerMesh Sources for AWS makes it easy to consume cloud events that occur in AWS services. Our example uses Sockeye for demonstration purposes: you can replace Sockeye with any of your Kubernetes workloads that would benefit from consuming and processing events from these popular AWS services.

The TriggerMesh SAWS package supports a number of AWS services. Refer to the [README](https://github.com/triggermesh/aws-event-sources/tree/master/cmd/) for each component to learn more. You can find sample configurations [here](https://github.com/triggermesh/aws-event-sources/tree/master/config/samples//).Don’t miss the Computing on the Edge with Kubernetes conference on October 21. [Register Now](https://www.accelevents.com/e/edgeconference2020)
