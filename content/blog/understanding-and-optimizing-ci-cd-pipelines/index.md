---
title: "Understanding and Optimizing CI/CD Pipelines"
date: 2023-08-07T16:52:45
slug: "understanding-and-optimizing-ci-cd-pipelines"
authors: ["Kovid Rathee"]
products: ["Kubernetes (generic)"]
tags: ["ci-cd"]
content_type: "explainer"
draft: false
migration:
  wp_id: 116202
  original_url: "https://www.suse.com/c/rancher_blog/understanding-and-optimizing-ci-cd-pipelines/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

Building, testing and deploying software is a time-consuming process that many organizations aim to minimize by automating repeatable work wherever possible. To do so, many organizations are utilizing a continuous integration, continuous delivery (CI/CD) philosophy in combination with cloud native tools like [Kubernetes](https://kubernetes.io/) to develop and deploy software at scale.

Traditionally, developing and deploying software has involved manual intervention to build the application source code, run it against a test suite and deploy it to the production environment. This process is inefficient, can increase human error, reduces developer productivity and leads to downtime.

Utilizing CI/CD pipelines with Kubernetes solves many of these issues by automating the management of the code and infrastructure. CI/CD pipelines automate the building, testing and deployment processes, while Kubernetes manages the virtual infrastructure. As a result, your users have a more reliable experience, and your organization's losses are minimized.

The problem is that there is a steep learning curve when it comes to Kubernetes and CI/CD pipelines; however, this article can help. Here, you'll learn about the underlying components of Kubernetes-based CI/CD pipelines and some best practices you can implement to help optimize them.

## CI/CD pipelines

Kubernetes CI/CD pipelines consist of several components. The most important ones are a version control system (VCS), a CI/CD tool, Kubernetes and containers running inside Kubernetes:

CI refers to the practice of automatically building an application from source code, testing the code against a defined set of use cases and checking the security vulnerability of the code. In comparison, CD refers to setting up an environment (Kubernetes, in this case), deploying the application to that environment, and testing the deployed application for any issues. In many instances, you may need to deploy an application to several environments, which is where a tool like [Rancher Fleet](https://fleet.rancher.io/) can help.

### Version control system

Version control systems (VCS) like [Git](https://www.atlassian.com/git/tutorials/what-is-git), [Subversion](https://subversion.apache.org/) and [Mercurial](https://www.mercurial-scm.org/) keep track of code changes made during application development in code repositories. They also help multiple developers collaborate on the same codebase easily. Code pushed to a repository can be configured to trigger the CI/CD pipeline. This allows developers to easily integrate CI/CD pipelines into their regular workflow.

Git is the [most popular VCS tool](https://www.bairesdev.com/blog/which-version-control-system-developers-use/). In this article, references to Git can apply to other VCS tools as well.

### CI/CD tool

As mentioned in the introduction, CI/CD allows you to automate your build, test and deploy cycle, and your CI/CD workflow will be based on your VCS and triggered based on its actions. For instance, if you're using Git, raising a pull request or merging one branch into another branch will trigger your CI/CD pipeline, and your code changes will go through sanity checks, functional tests and security checks.

Kubernetes is ideal for long-running applications that need to scale in and out, but it's also great for transient workloads triggered by CI/CD tools. Having version-control and automated workflows for development and deployment is great, but you still need infrastructure to run the CI/CD workflows.

### Containers

A container is built from a container image, a template with instructions on creating the container. The most popular containers used currently are created using [Docker](https://docs.docker.com/get-started/overview/) (to the extent that sometimes the terms *container* and *Docker container* are used synonymously). Kubernetes supports Docker containers as well as other [OCI-compliant](https://opencontainers.org/) containers, such as [Kata Containers](https://katacontainers.io/), [Firecracker](https://github.com/firecracker-microvm/firecracker) and [gVisor](https://gvisor.dev/).

### Kubernetes cluster

A Kubernetes cluster is a collection of infrastructure resources where you can deploy containers containing your applications or services. If your application fails, Kubernetes can automatically create new container instances to replace the lost ones and get your application running again, possibly without downtime. CI/CD pipelines can be integrated with Kubernetes clusters running your applications to trigger deploys automatically.

## Tips and best practices for improving CI/CD pipelines

Setting up a CI/CD pipeline and integrating it with Kubernetes is a good start, but don't stop there! To get the most out of your Kubernetes CI/CD pipelines, consider implementing the following best practices:

### Keep secrets secure

CI/CD pipelines often require sensitive information or *secrets* to connect and communicate between different parts of the infrastructure (including the VCS and Kubernetes). These secrets include authentication tokens, encryption keys and access credentials.

Secrets should always be encrypted and stored *outside* the container so that the rest of the application and infrastructure are not compromised if someone gets unauthorized access to the container. [Storing them in Git](/blog/managing-sensitive-data-in-kubernetes-with-sealed-secrets-and-external-secrets-operator-eso/) alongside your code is a popular approach since it easily integrates with CI/CD workflows.

### Validate your builds

It's important to validate CI/CD pipeline configurations, and the application builds automatically before proceeding to the testing stages, or in other words, the build should be testable before it reaches the testers.

[Build validation testing](https://www.educative.io/answers/what-is-build-validation-testing) is a type of [smoke testing](https://www.freecodecamp.org/news/smoke-testing/) that can be automated by enforcing policies on your CI/CD pipeline configurations. Validating your builds will save precious building resources and ensure they are utilized efficiently by providing successful and validated builds to the testing team.

### Implement blue-green deployment patterns

Despite all the validation and testing, some builds may experience issues when deployed to production. The [blue-green deployment pattern](https://glossary.cncf.io/blue-green-deployment/) can be leveraged to prevent downtime and minimize this risk.

In this pattern, you create a new environment (green) identical to the current production environment (blue). You then run the new application version on the newly created green environment and gradually move traffic from the blue environment to the green environment. Once you've verified that nothing is failing on the green environment, you can deprecate the blue environment (after keeping it around for some time in case you need to roll the changes back).

This can be implemented seamlessly in Kubernetes, where environments are just containers. You can [configure your CI/CD pipeline](https://docs.gitlab.com/ee/ci/environments/incremental_rollouts.html#blue-green-deployment) to deploy using the blue-green pattern and use load balancers to move traffic from the blue to the green environment.

### Secure your CI/CD pipeline

In any application, it's possible that vulnerable code is included in its containers. Security vulnerabilities can also come in through the container images that your containers are built with. If a base image on top of which your container image is built contains vulnerable code, these vulnerabilities will end up in your container. In addition, vulnerabilities and threats can be introduced through the containers' interactions with the underlying operating system and from vulnerable containers over the network. This creates a complex situation where manually tracking vulnerabilities can become overwhelming.

Moreover, you want to be able to verify builds and check for vulnerabilities in the development and testing stages by executing runtime behavior assessments and image scans. From delivery to production, you might need an additional level of security with CIS benchmark tests, security auditing and detailed monitoring against threats and violations of any kind. In the same way that code cleanup, compiling, testing and packaging are essential steps in any pipeline, it's equally important that you integrate security scanning tools such as [NeuVector](https://github.com/jenkinsci/neuvector-vulnerability-scanner-plugin), which offers [dedicated plugins for CI/CD pipelines](https://github.com/jenkinsci/neuvector-vulnerability-scanner-plugin).

### Automate your tests

Automated testing is one of the most significant benefits of a CI/CD pipeline. [Multiple types of tests](https://www.atlassian.com/continuous-delivery/software-testing/types-of-software-testing) should be run every time a new build of your application is validated in the pipeline. Unit tests can check if there are any errors in smaller units of the application. Integration tests can check for issues when multiple parts of your application interact with each other.

In addition, you can benefit from adding performance tests to your test suite, especially if speed and load tolerance are key requirements for your application. Apart from these, you should also test the application by setting up a few end-to-end tests for essential use cases.

Testing can help improve your productivity and efficiency by shortening the feedback cycle and flagging errors early. Container-based testing tools like [Jenkins X](https://jenkins-x.io/) can be used inside your Kubernetes CI/CD pipelines to simplify your testing setup.

### Favor GitOps workflows

CI is responsible for testing and merging your code, while CD manages the infrastructure and powers the delivery of code to production. Like secrets, you should consider storing configurations for the CI/CD pipeline alongside the application code in your code repository. This provides all the benefits of a Git-based programming workflow such as version control, pull requests, and code review, in addition to added convenience, collaboration, and productivity. [GitOps](/blog/leveraging-gitops-to-automate-the-delivery-of-code-and-infrastructure/) is a framework that takes your programming workflows and couples them with infrastructure management in an automated fashion. This means you'll be able to manage infrastructure configurations in the same way you currently manage your code. A Git repository becomes the single source of truth for your infrastructure. To adopt GitOps as a preferred approach, you need to select the appropriate tools that support this methodology. For instance, if you're implementing continuous delivery for a large-scale Kubernetes-based application, you can use tools like [Fleet](https://fleet.rancher.io/), an open-source container management and deployment engine that works in conjunction with [Rancher](https://www.rancher.com/), an open-source Kubernetes management application. Because [Fleet is integrated into Rancher](https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/deploy-apps-across-clusters/fleet) by default, you just need to select the **Continuous Delivery** option, which will take you directly to Fleet.

## Conclusion

In this article, you learned about the most important components of a CI/CD pipeline, their role in the pipeline and how they're connected. You also learned some best practices to help optimize your CI/CD pipelines.

You can explore CI/CD pipelines with Kubernetes further using [Rancher](https://ranchermanager.docs.rancher.com/), which was created by [SUSE](https://www.suse.com/), the world's leading open source Kubernetes management platform. You can [get started](https://ranchermanager.docs.rancher.com/getting-started/overview) using the official documentation, [set up pipelines](https://www.youtube.com/watch?v=kagSBoInW6g) using Rancher Fleet and explore more tutorials on the [Rancher Labs YouTube channel](https://www.youtube.com/@Rancher).
