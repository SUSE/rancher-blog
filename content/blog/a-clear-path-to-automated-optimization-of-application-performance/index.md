---
title: "A Clear Path to Automated Optimization of Application Performance"
date: 2020-07-16T09:45:00
slug: "a-clear-path-to-automated-optimization-of-application-performance"
author: "Rancher Admin"
image: "images/rancher_blog_automated-optimization-featured.png"
products: ["Kubernetes (generic)"]
tags: ["performance", "ai"]
content_type: "event"
draft: true
migration:
  wp_id: 85979
  original_url: "https://www.suse.com/c/rancher_blog/a-clear-path-to-automated-optimization-of-application-performance/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Past master class promo"
  redirect_target: "rancher.com/blog (hub)"
---

Register for the Kubernetes Master Class: A Clear Path to Automated Optimization of Kubernetes Performance[August 4, 2020 at 11am ET](https://info.rancher.com/kubernetes-master-class-aug4-2020)

Rancher has helped thousands of organizations manage their transitions to containerized applications and Kubernetes. With its innovative distribution and suite of services, Rancher has given IT and DevOps teams the roadmap they needed to drive Kubernetes success.
Given the complexity of Kubernetes and the shortage of engineers with Kubernetes-specific skills, Rancher’s offerings meet a critical and growing market need. The main driver of this growth is the growing momentum of cloud adoption among enterprises. The flexibility of cloud architectures and cloud-based apps deliver many benefits – and microservices, containerized apps and Kubernetes are a big part of that equation.

There is a wrinkle, however. It’s an impediment that many IT and DevOps teams hit as they shift more of their IT operations, workloads and apps to Kubernetes and the cloud. That speed bump is the difficulty many teams face in getting their applications to run just right in Kubernetes. That is, operating within their desired cost and performance parameters.

For teams early in their Kubernetes journeys, complexity troubles can do things like foil efforts to stand up their first few clusters or make applications crash. For teams that are further along the path, this complexity can undo their efforts to have many applications run well and cost-effectively. In all cases, complexity can keep many Kubernetes benefits frustratingly out of reach.

In this blog post, we’ll look at how team can tackle complexity problems in Kubernetes and automate application performance with machine learning and artificial intelligence.

## The Complexity Problem

IT and DevOps teams want and need their apps to hum, performance-wise, but do so efficiently. That means using just the cluster resources they require (CPU, memory, etc.) and not burning through lots of resources they don’t need.

Optimal use of cluster resources is a great goal. But thanks to the seemingly endless list of configuration choices and deployment options for Kubernetes, reaching that goal is often a tall order.
One way teams try to tackle the complexity is with frequent manual tuning. As with all things manual, that’s an inefficient, trial-and-error process that typically yields subpar results.
Another way to overcome the problem is with overprovisioning. Can’t tell exactly which cluster resource is causing an app to perform poorly or crash? Then overprovision key resources – and maybe some others for good measure – until things run properly. That works well until the cloud bill comes in and the CFO sees that cloud costs have gone through the roof.
These complexity-driven challenges are tough enough with small numbers of applications. Scaling up deployments by the hundreds or thousands of apps makes the problem exponentially worse. Without a better approach than manual intervention or overprovisioning, IT and DevOps teams will undoubtedly face major operational and financial problems down the road.

## Clearing the Complexity Hurdle with Machine Learning and AI

What organizations and teams need is a smart, effective, and automated way to optimize the performance of their applications running in Kubernetes.

The answer is machine learning-based artificial intelligence for IT operations (AIOps). This includes advanced machine learning techniques and automated learning, coupled with innovative engineering practices.

With machine learning ‘under the hood,’ solutions like [Red Sky Ops](https://www.carbonrelay.com/red-sky-ops/) from Carbon Relay can reduce the complexity of optimizing the performance of applications running in Kubernetes containers. The approach is to give the ‘experimentation’ with configuration settings over to machine intelligence. Leveraging the far faster, more methodical and more comprehensive capabilities delivered by compute power, the optimal configuration settings can be determined and delivered very rapidly – and they can be continuously tested, adapted and improved over time.
While other, commercially available AIOps solutions, including application resource management tools, can optimize applications based on costs, Carbon Relay’s is the only solution that can automatically optimize applications for both cost and pure performance.
To optimize an application to the best performance, you need to determine the values of its internal parameters. These parameters include resource allocation, such as pod CPU and memory, number of replicas and internal parameters such as JVM heap size and others.

For a typical application, the number of possible configurations could number in the millions. The correlations between these parameters and the application’s performance make it nearly impossible for a human to handle its complexity in its entirety. This complexity is a natural fit for machine learning models.

Using optimization techniques, engineers and DevOps teams can now run “experiments” in a development environment, proactively tuning their applications before ever shipping to production. These techniques combine machine learning algorithms with strong engineering capabilities to mimic production traffic and environment as closely as possible.

In addition, these machine learning techniques learn, adapt and evolve over time so that the optimization process becomes faster, more accurate and more efficient as your application evolves.
By putting these advanced technologies to work for them, teams can rest assured that the applications they have running in Kubernetes will deploy and run properly from the start, scale naturally and be intelligently and automatically optimized.

## A Closer Look at Automated Application Performance Optimization

To illustrate these capabilities, let’s walk through one example of how teams can ensure success and maximize the effectiveness of their Kubernetes initiatives.

This approach is based on the concept of *trials and experiments*. An experiment in this context is evaluates a single application or component to determine its optimal configuration. Each trial within an experiment tests a particular configuration of parameters.

To start, users first create an experiment definition, either from scratch or by using commercially available examples and templates. The experiment definition will include the metrics to be measured (to determine application performance) and the specific parameters to be tuned during each trial.

Next we’ll step through the running of an experiment using these simple steps:

1. Obtain the latest release of the technology.
2. Build an **experiment.yaml** file for the application being tested.
3. Initialize the appropriate controller in the cluster
4. Apply the manifests.
5. Observe, interpret and operationalize the results.

As the experiment progresses, the ML-powered AIOps platform will ‘learn’ the application and test configurations to zero in on the optimal results. Users to one of our open integrations can view the status of their experiments and pull their preferred configuration for deployment.

![Image 01](images/rancher_blog_image01.png)
Figure 1: Example of Experiment Results

Figure 1 shows the typical results of an experiment. In this case, we optimized a sample web app for both throughput and resource costs. Each dot represents a successfully deployed trial or a specific application configuration. The orange dots show the optimal configurations that trade off highest throughput and lowest cost. Failed trials (i.e., those configurations in which the application failed to deploy) are not shown and comprise less than 10 percent of all trials (compared to 50 percent failed trials with random exploration).

## Working with Experiment Results

The orange dots are the ones the machine learning algorithm deemed as “best”; these configurations cannot be beaten on both throughput and cost at the same time. Users can select their preferred configurations from these collections of trials, sometimes referred to as the Pareto front.

In addition, this map of trials illustrates just how far novice users can veer off track with suboptimal configurations. Sticking with default configurations isn’t an effective strategy because, with common open source components, the Helm chart default configurations are far from optimal on metrics such as cost, throughput, latency and more.

Exporting the optimal configuration and deploying is a simple process. With multiple experiments running under various load scenarios, users can collect a library of optimal deployment configurations that will adapt to different situations and scale their needs as necessary.

As the applications develop over time, it may be useful to run optimization experiments to ensure the evolved version remains optimal. The good news is that machine learning algorithms learn and retain information about each application’s performance and run future experiments in a fraction of the time required for the original experiment. Also, as this technology evolves, ML-based AIOps platforms will likely be able to automatically incorporate learnings from widespread open source components (such as [PostgreSQL](https://www.postgresql.org/), [Redis](https://redis.io/topics/introduction), [ELK](https://www.elastic.co/what-is/elk-stack), etc.) and speed up optimization for applications utilizing those tools.

![Image 02](images/rancher_blog_image02.png)
Example: Results of an Experiment

## Red Sky Ops and Rancher

Red Sky Ops is available in the Rancher Apps Catalog, so you can install it directly from the Rancher platform.

![Image 03](images/rancher_blog_image03.png)

## Conclusion

Whether you’re using the Rancher stack and services or some other distribution, and you and your team have the requisite skills, you can stand up your clusters and nodes and run your pods. But as your deployment scales, and the number of apps and workloads you have running on Kubernetes multiplies, both the complexity and its associated risks grow exponentially. Taming that complexity and mitigating those risks — and doing so efficiently with speed at scale – is a job that’s well beyond human capabilities. It’s a job for machines.
Machine learning–powered AIOps platforms and their experiment capabilities enable IT and DevOps teams to automate the optimization of their applications running on Kubernetes. Once teams turn that corner, they start experiencing faster and easier application deployments. They see the portability and scalability of their apps increase significantly — without any additional work required. And, they begin to drive big savings, especially in reduction of cloud costs.
Machine learning in IT and DevOps isn’t science fiction or a future thing; it’s here and happening now. Register for the upcoming Kubernetes Master Class to learn how you and your team can drive significant increases in performance and reliability with your Kubernetes apps, while closely controlling costs.

[Sign up](https://info.rancher.com/kubernetes-master-class-aug4-2020) for the **Master Class: A Clear Path to Automated Optimization of Kubernetes Performance**, August 4, 2020 at 11am ET.

Register for the Kubernetes Master Class: A Clear Path to Automated Optimization of Kubernetes Performance[August 4, 2020 at 11am ET](https://info.rancher.com/kubernetes-master-class-aug4-2020)
