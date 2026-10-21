---
title: "What is CI/CD?"
date: 2018-11-15T09:03:00
slug: "what-is-ci-cd"
author: "Rancher Admin"
image: "images/rancher_blog_1-6-to-2-0-terms-and-concepts.svg"
products: ["Kubernetes (generic)"]
tags: ["ci-cd"]
content_type: "explainer"
draft: false
migration:
  wp_id: 85831
  original_url: "https://www.suse.com/c/rancher_blog/what-is-ci-cd/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

Build a CI/CD Pipeline with Kubernetes and RancherRecorded Online Meetup of best practices and tools for building pipelines with containers and kubernetes.[Watch the training](https://rancher.com/events/2018/2018-08-07-onlinemeetup-building-a-cicd-pipeline-with-k8s/)

The demands of modern software development combined with complexities of deploying to varied infrastructure can make creating applications a tedious process. As applications grow in size and scope, and development teams become more distributed and diverse, the overall process required to produce and release software quickly and consistently becomes more difficult.

To address these issues, teams began exploring new strategies to automate their build, test, and release processes to help deploy new changes to production faster. This lead to the development of continuous integration and continuous delivery.

In this guide we will explain what CI/CD is and how it helps teams produce well-tested, reliable software at a faster pace. Before exploring CI/CD and its benefits in depth, we should discuss some prerequisite technologies and practices that these systems build off of.

## Automated Build Processes

In software development, the build process converts code that developers produce into useable pieces of software that can be executed. For compiled languages like Go or C, this stage involves running the source code through a compiler to produce a standalone binary file. For interpreted languages like Python or PHP, there is no compilation step, but the code may still need to be frozen at a specific point in time, bundled with dependencies, and packaged for easier distribution. These processes result in an artifact that is often called a “build” or “release”.

While developers can create builds manually, this has a number of disadvantages. The shift from active development to creating a build introduces a context switch, forcing individuals to halt more productive work and focusing on the build process. Furthermore, because each developer is producing artifacts on their own, inconsistencies are also likely to arise.

To address these concerns, many teams configure automated build pipelines. These systems monitor source code repositories and automatically kick off a preconfigured build process when changes are detected. This limits the amount of human involvement and ensures that a consistent process is followed on each build.

There are many build tools designed to help you automate these steps. For example, within the Java ecosystem, the following tools are popular:

- **Ant:** Apache’s Ant is an open source Java library. Created in 2000, Ant is the original build tool in the Java space and is still frequently used today.
- **Maven:** Apache’s Maven is a build automation tool written primarily with Java projects in mind. Unlike Apache Ant, Maven follows the philosophy of [convention over configuration](https://en.wikipedia.org/wiki/Convention_over_configuration), requiring configuration only for the aspects of the build process that deviate from reasonable defaults.
- **Gradle:** Reaching version 1.0 in 2012, Gradle tries to incorporate the strengths of both Ant and Maven by incorporating Maven’s modern features without losing the flexibility provided by Ant. Build instructions are written in a dynamic language called Groovy. Despite being a newer tool in this space, it’s seen widespread adoption.

## Version Control

Most modern software development requires frequent collaboration within a shared codebase. Version control systems (VCS) are employed to help maintain project history, allow work on discrete features in parallel, and resolve conflicting changes. The VCS allows projects to easily adopt changes and to roll back in case of problems. Developers can work on projects on their local machines and use the VCS to manage the different branches of development.

Every change recorded in a VCS is called a **commit**. Each commit catalogs the changes to the codebase and includes metadata like a description that can be helpful when reviewing the commit history or merging updates.

Fig. 1 Distributed Version Control

![Fig. 1: Diagram of distributed version control](images/rancher_blog_what-is-cicd-version-control.png)

While version control is a valuable tool to help manage many different changes within a single codebase, distributed development often introduces challenges. Developing in independent branches of the codebase without regularly merging into a shared integration branch can make it difficult to incorporate changes later on. To avoid this, developers started adopting a practice called **continuous integration**.

## Continuous Integration (CI)

Continuous Integration (CI) is a process that allows developers to integrate work into a shared branch often, enhancing collaborative development. Frequent integration helps dissolve silos, reducing the size of each commit to lower the chance of merge conflicts.

A robust ecosystem of tools have been developed to encourage CI practices. These systems integrate with VCS repositories to automatically run build scripts and test suites when new changes are detected. Integration tests ensure that different components function together as a group, allowing teams to catch compatibility bugs early. Continuous integration produces builds that are thoroughly tested and reliable.

Fig. 2 Continuous Integration process

![Fig. 2: Diagram of a continuous integration process](images/rancher_blog_what-is-cicd-ci-process.png)

## Continuous Delivery and Continuous Deployment (CD)

Continuous delivery and continuous deployment are two strategies that build off of the foundation that continuous integration provides. **Continuous delivery** extends the continuous integration process by deploying builds that pass the integration test suite to a pre-production environment. This makes it straightforward to evaluate each build in a production-like environment so that developers can easily validate bug fixes or test new features without additional work. Once deployed to the staging area, additional manual and automated testing is possible.

**Continuous deployment** takes this approach one step further. Once a build passes automated tests in a staging environment, a continuous deployment system can automatically deploy the build to production servers. In other words, every “green build” is live and available to customers for early feedback. This enables teams to release of new features and bug fixes instantly, backed by the guarantees provided by their testing processes.

Fig. 3 Roadmap for CI/CD Flow Diagram

![Fig. 3: Diagram of a typical CI/CD development flow](images/rancher_blog_what-is-cicd-flow-diagram.png)

## Advantages of CI and CD

Continuous integration, delivery, and deployment provide some clear improvements to the software development process. Some of the primary benefits are outlined below.

### Fast Feedback Loop

A fast feedback loop is essential to implementing a rapid development cycle. To receive timely feedback, it is essential that software reaches the end user quickly. When properly implemented, CI/CD provides a platform to achieve this goal by making it simple to update production deployments. By requiring each change to go through rigorous testing, CI helps reduce the risks associated with each build and consequently allows teams to release valuable features to customers quickly and easily.

### Increased Visibility

CI/CD is usually implemented as a pipeline of sequential steps, visible to the entire team. As a result, each team members can track the state of build in the system and identify the build responsible for any test failures. By providing insight into the current state of the codebase, it is easier to plan the best course of action. This level of transparency offers a clear answer the question, “did my commit break the build?”

### Simplified Troubleshooting

Since the goal of CI is to integrate and test every change made to the codebase, it is safer to make small commits and merge them into the shared code repository early. As a result, when a bug is found, it is easier to identify the change that introduced the problem. Afterwards, depending on the magnitude of the issue, the team can choose to either roll back the change or write and commit a fix, decreasing the overall time to resolution in production.

### Higher Quality Software

Automating the build and deployment processes not only shortens the development cycle. It also helps teams produce higher quality software. By ensuring that each change is well-tested and deployed to at least one pre-production environment, teams can push changes to production with confidence. This is possible only when there is good test coverage of all levels of the codebase, from unit tests to more complex system tests.

### Fewer Integration Issues

Because the automated test suite runs on the builds automatically produced with every commit, it is possible to catch and fix most integration issues early. This gives developers early insight into other work currently being done that might affect their code. It tests that code written by different contributors works together from the earliest possible moment instead of later when there may be additional side effects.

### More Time Focused on Development

CI/CD systems rely on automation to produce builds and move new changes through the pipeline. Because manual intervention is not required, building and testing no longer require dedicated time from the development team. Instead, developers can concentrate on making productive changes to the codebase, confident that the automated systems will notify them of any problems.

## Continuous Integration and Delivery Best Practices

Now that we’ve seen some of the benefits of using CI/CD, we can discuss some guidelines to help you implement these processes successfully.

### Take Responsibility for the CI/CD Pipeline

Developers are responsible for the commits they make until the changes are deployed to pre-production. This means that the developer must ensure that their code is integrated properly and can be deployed at all times. If a change is committed that breaks these requirements, it is that developer’s duty to commit a fix rapidly to avoid impacting other people’s work. Build failures should halt the pipeline and block commits not involved in fixing the failure, making it essential to address the build problems quickly.

### Ensure Consistent Deployments

The deployment process should not be manual. Instead, a pipeline should automate the deployment process to ensure consistency and repeatability. This reduces the chances of pushing broken builds to production and helps avoid one-off, untested configurations that are difficult to reproduce.

### Commit the Codebase to Version Control

It is important that every change is committed to version control. This helps the team audit all proposed changes and lets the team revert problematic commits easily. It can also help preserve the integrity of configuration, scripts, databases, and documentation. Without version control, it is easy to lose or mishandle configuration and code changes, especially when multiple people are contributing to the same codebase.

### Make Small, Incremental Changes

A crucial point to keep in mind is that the changes should be small. Waiting to introduce changes in larger batches delays feedback from testing and makes it more difficult to identify the root cause of problems.

### Good Test Coverage

Since intent of CI/CD is to reduce manual testing, there should be a good automated test coverage throughout the codebase to ensure that the software is functioning as intended. Additionally, it is important to regularly clean up redundant or out-of-date tests to avoid affecting the pipeline.

The ratio of different types of tests in the test suite should reflect the “testing pyramid” model. The majority of the tests should be unit tests since they ensure basic functionality and are quick to execute. A smaller number of integration tests should follow to guarantee that components can operate together successfully. Finally, a small number regression, UI, system, and end-to-end tests should be included towards the end of the testing cycle to ensure that the build meets all of the behavioral requirements of the project. Tools like [JaCoCo](https://www.eclemma.org/jacoco/) for Java projects can determine how much of the codebase is covered by the testing suite.

Fig. 4 Test Pyramid

![Fig. 4: Diagram of test pyramid](images/rancher_blog_what-is-cicd-test-pyramid.png)

## What’s Next?

There are many different continuous integration and delivery tools available. Some examples include [Jenkins](https://jenkins.io/), [Travis CI](https://travis-ci.org/), [GoCD](https://www.gocd.org/), [CircleCI](https://circleci.com/), [Gitlab CI](https://about.gitlab.com/product/continuous-integration/), [Codeship](https://codeship.com/), and [TeamCity](https://www.jetbrains.com/teamcity/).

In the next article in this series, we will dig deeper to understand the features that each of these tools provide and help you determine the best continuous integration tool for your team.

Build a CI/CD Pipeline with Kubernetes and RancherRecorded Online Meetup of best practices and tools for building pipelines with containers and kubernetes.[Watch the training](https://rancher.com/events/2018/2018-08-07-onlinemeetup-building-a-cicd-pipeline-with-k8s/)
