---
title: "Cloud Modernization Best Practices"
date: 2022-08-08T14:28:00
slug: "cloud-modernization-best-practices"
author: "SUSE"
image: "images/Cloud-Native-Tansformations_1.png"
products: ["Kubernetes (generic)"]
tags: ["cloud"]
content_type: "opinion"
draft: false
migration:
  wp_id: 93532
  original_url: "https://www.suse.com/c/rancher_blog/cloud-modernization-best-practices/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

Cloud services have revolutionized the technical industry, and services and tools of all kinds have been created to help organizations migrate to the cloud and become more scalable in the process. This migration is often referred to as cloud modernization.

To successfully implement cloud modernization, you must adapt your existing processes for future feature releases. This could mean adjusting your continuous integration, continuous delivery (CI/CD) pipeline and its technical implementations, updating or redesigning your release approval process (*eg* from manual approvals to automated approvals), or making other changes to your software development lifecycle.

In this article, you’ll learn some best practices and tips for successfully modernizing your cloud deployments.

## **Best practices for cloud modernization**

The following are a few best practices that you should consider when modernizing your cloud deployments.

### **Split your app into microservices where possible**

Most existing applications deployed on-premises were developed and deployed with a [monolithic architecture](https://en.wikipedia.org/wiki/Monolithic_application) in mind. In this context, monolithic architecture means that the application is single-tiered and has no modularity. This makes it hard to bring new versions into a production environment because any change in the code can influence every part of the application. Often, this leads to a lot of additional and, at times, manual testing.

Monolithic applications often do not [scale horizontally](https://medium.com/swlh/scaling-monolithic-applications-3c69193f942a) and can cause various problems, including complex development, tight coupling, [slow application starts](https://articles.microservices.com/monolithic-vs-microservices-architecture-5c4848858f59#:~:text=Drawbacks%20of%20Monolithic%20Architecture,entire%20application%20on%20each%20update.) due to application size, and reduced reliability.

To address the challenges that a monolithic architecture presents, you should consider [splitting your monolith](/blog/moving-your-monolith-best-practices-and-focus-areas/) into microservices. This means that your application is split into different, loosely coupled services that each serve a [single purpose](https://medium.com/@kmdkhadeer/microservices-best-practices-5fe3e28394b3).

All of these services are independent solutions, but they are meant to work together to contribute to a larger system at scale. This increases reliability as one failing service does not take down the whole application with it. Also, you now get the freedom to scale each component of your application without affecting other components. On the development side, since each component is independent, you can split the development of your app among your team and work on multiple components parallelly to ensure faster delivery.

For example, the [Lyft engineering team managed to quickly grow](https://eng.lyft.com/scaling-productivity-on-microservices-at-lyft-part-1-a2f5d9a77813?gi=39c1ac3a1526) from a handful of different services to hundreds of services while keeping their developer productivity up. As part of this process, they included automated acceptance testing as part of their pipeline to production.

### **Isolate apps away from the underlying infrastructure**

Engineers built scripts or pieces of code agnostic to the infrastructure they were deployed on in many older applications and workloads. This means they wrote scripts that referenced specific folders or required predefined libraries to be available in the environment in which the scripts were executed. Often, this was due to required configurations on the hardware infrastructure or the operating system or due to dependency on certain packages that were required by the application.

Most cloud providers refer to this as a [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/). In this model, the cloud provider or service provider takes responsibility for the parts of the services being used, and the service user takes responsibility for protecting and securing the data for any services or infrastructure they use. The interaction between the services or applications deployed on the infrastructure is well-defined through APIs or integration points. This means that the more you move away from managing and relying on the underlying infrastructure, the easier it becomes for you to replace it later. For instance, if required, you only need to adjust the APIs or integration points that connect your application to the underlying infrastructure.

To isolate your apps, you can [containerize](https://www.suse.com/suse-defines/definition/containerization/) them, which bakes your application into a repeatable and reproducible container. To further separate your apps from the underlying infrastructure, you can move toward [serverless-first development](https://www.zdnet.com/article/a-serverless-journey-begins-with-several-first-steps-actually/), which includes a serverless architecture. You will be required to re-architect your existing applications to be able to execute on [AWS Lambda](https://aws.amazon.com/lambda/) or [Azure Functions](https://azure.microsoft.com/en-us/services/functions) or adopt other serverless technologies or services.

While going serverless is recommended in some cases, such as simple CRUD operations or applications with high scaling demands, it’s not a requirement for successful cloud modernization.

### **Pay attention to your app security**

As you begin to incorporate cloud modernization, you’ll need to ensure that any deliverables you ship to your clients are secure and follow a [shift-left process](https://www.aquasec.com/cloud-native-academy/devsecops/shift-left-devops). This process lets you quickly provide feedback to your developers by incorporating security checks and guardrails early in your development lifecycle (*eg* running static code analysis directly after a commit to a feature branch). And to keep things secure at all times during the development cycle, it’s best to set up continuous runtime checks for your workloads. This will ensure that you actively catch future issues in your infrastructure and workloads.

Quickly delivering features, functionality, or bug fixes to customers gives you and your organization more responsibility in ensuring automated verifications in each stage of the software development lifecycle (SDLC). This means that in each stage of the delivery chain, you will need to ensure that the delivered application and customer experience are secure; otherwise, you could expose your organization to data breaches that can cause [reputational risk](https://blog.hubspot.com/service/reputational-risk).

Making your deliverables secure includes ensuring that any personally identifiable information is encrypted in transit and at rest. However, it also requires that you ensure your application does not have open security risks. This can be achieved by running static code analysis tools like [SonarQube](https://www.sonarqube.org/) or [Checkmarks](https://info.checkmarx.com/checkmarx-connect#).

In this blog post, you can read more about the importance of application security in your cloud modernization journey.

### **Use infrastructure as code and configuration as code**

[Infrastructure as code (IaC)](https://en.wikipedia.org/wiki/Infrastructure_as_code) is an important part of your cloud modernization journey. For instance, if you want to be able to provision infrastructure (*ie* required hardware, network and databases) in a repeatable way, using IaC will empower you to apply existing software development practices (such as pull requests and code reviews) to change the infrastructure. Using IaC also helps you to have immutable infrastructure that prevents accidentally introducing risk while making changes to existing infrastructure.

Configuration drift is a prominent issue with making ad hoc changes to an infrastructure. If you make any manual changes to your infrastructure and forget to update the configuration, you might end up with an infrastructure that doesn’t match its own configuration. Using IaC enforces that you make changes to the infrastructure only by updating the configuration code, which helps maintain consistency and a reliable record of changes.

All the major cloud providers have their own definition language for IaC, such as [AWS CloudFormation](https://aws.amazon.com/cloudformation/), [Google Cloud Platform (GCP)](https://cloud.google.com/blog/products/devops-sre/want-repeatable-scale-adopt-infrastructure-as-code-on-gcp) and [Microsoft Azure](https://docs.microsoft.com/en-us/devops/deliver/what-is-infrastructure-as-code).

Ensuring that you can deploy and redeploy your application or workload in a repeatable manner will empower your teams further because you can deploy the infrastructure in additional regions or target markets without changing your application. If you don’t want to use any of the major cloud providers’ offerings to avoid [vendor lock-in](https://en.wikipedia.org/wiki/Vendor_lock-in), other IaC alternatives include [Terraform](https://www.terraform.io/) and [Pulumi](https://www.pulumi.com/why-pulumi). These tools offer capabilities to deploy infrastructure into different cloud providers from a single codebase.

Another way of writing IaC is the [AWS Cloud Development Kit (CDK)](https://aws.amazon.com/cdk/), which has [unique capabilities](https://www.lockhead.info/index.php/2022/04/06/why-cdk-changes-the-everything-for-building-devops-teams-that-own-something-end-to-end/) that make it a good choice for writing IaC while driving cultural change within your organization. For instance, AWS CDK lets you write automated unit tests for your IaC. From a cultural perspective, this allows developers to write IaC in their preferred programming language. This means that developers can be part of a DevOps team without needing to learn a new language. AWS CDK can also be used to quickly deploy and develop infrastructure on AWS, [cdk8s](https://cdk8s.io/) for Kubernetes, and [Cloud Development Kit for Terraform (CDKTF)](https://www.terraform.io/cdktf).

After adapting to IaC, it’s also recommended to deploy all your [configurations as code (CAC)](https://www.cloudbees.com/blog/configuration-as-code-everything-need-know). When you use CoC, you can put the same guardrails (*ie* pull requests) around configuration changes required for any code change in a production environment.

### **Pay attention to resource usage**

It’s common for new entrants to the cloud to miss out on tracking their resource consumption while they’re in the process of migrating to the cloud. Some organizations start with [too much (~20 percent)](https://www.rapyder.com/blogs/top-cloud-mistakes-that-will-cost-dearly/#:~:text=IT%20teams%20have%20always%20believed%20in%20provisioning%20for%20around%2020%25%20additional%20infrastructure%20capacity%20on%2Dpremise.%C2%A0) of additional resources, while some forget to set up restricted access to avoid overuse. This is why tracking the resource usage of your new cloud infrastructure from day one is very important.

There are a couple of things you can do about this. The first and a very high-level solution is to set budget alerts so that you’re notified when your resources start to cost more than they are supposed to in a fixed time period. The next step is to go a level down and set up cost consolidation of each resource being used in the cloud. This will help you understand which resource is responsible for the overuse of your budget.

The final and very effective solution is to track and audit the usage of all resources in your cloud. This will give you a direct answer as to why a certain resource overshot its expected budget and might even point you towards the root cause and probable solutions for the issue.

## **Culture and process recommendations for cloud modernization**

How cloud modernization impacts your organization's culture and processes often goes unnoticed. If you really want to implement cloud modernization, you need to change every engineer in your organization's mindset drastically.

### **Modernize SDLC processes**

Oftentimes, organizations with a more traditional, non-cloud delivery model follow a checklist-based approach for their [SDLC](https://codilime.com/blog/the-stages-of-the-sdlc/). During your cloud modernization journey, existing SDLC processes will need to be enhanced to be able to cope with the faster delivery of new application versions to the production environment. Verifications that are manual today will need to be automated to ensure faster response times. In addition, client feedback needs to flow faster through the organization to be quickly incorporated into software deliverables. Different tools, such as SecureStack and SUSE Manager, can help automate and improve efficiency in your SDLC, as they take away the burden of manually managing rules and policies.

### **Drive cultural change toward blameless conversations**

As your cloud journey continues to evolve and you need to deliver new features faster or quickly fix bugs as they arise, this [higher change frequency](https://humanitec.com/blog/deployment-frequency-key-metric-in-devops) and higher usage of applications will lead to more incidents and cause disruptions. To avoid attrition and arguments within the DevOps team, it’s important to create a culture of [blameless communication](https://medium.com/the-pinch/enterprise-devops-sre-blameless-postmortems-and-blameless-culture-c96056d2d63c). Blameless conversations are the foundation of a healthy DevOps culture.

One way you can do this is by running [blameless post-mortems](https://www.atlassian.com/incident-management/postmortem/blameless). A blameless post-mortem is usually set up after a negative experience within an organization. In the post-mortem, which is usually run as a meeting, everyone explains his or her view on what happened in a non-accusing, objective way. If you facilitate a blameless post-mortem, you need to emphasize that there is no intention of blaming or attacking anyone during the discussion.

### **Track key performance metrics**

Google’s annual [State of DevOps](https://services.google.com/fh/files/misc/state-of-devops-2019.pdf) report uses four key metrics to measure DevOps performance: deploy frequency, lead time for changes, time to restore service, and change fail rate. While this article doesn’t focus specifically on DevOps, tracking these four metrics is also beneficial for your cloud modernization journey because it allows you to compare yourself with other industry leaders. Any improvement of key performance indicators (KPIs) will motivate your teams and ensure you [reach your goals](https://www.linkedin.com/pulse/legacy-software-modernization-article-3-using-key-ridene-ph-d-/).

One of the key things you can measure is the [duration of your modernization project](https://appdevelopermagazine.com/the-four-metrics-of-success-when-planning-a-legacy-modernization-project/). The project's duration will directly impact the project's cost, which is another important metric to pay attention to in your cloud modernization journey.

Ultimately, different companies will prioritize different KPIs depending on their goals. The most important thing is to pick metrics that are meaningful to you. For instance, a software-as-a-service (SaaS) business hosting a rapidly growing consumer website will need to track the time it takes to deliver a new feature (from commit to production). However, this metric isn’t meant for a traditional bank that only updates its software once a year.

You should review your chosen metrics regularly. Are they still in line with your current goals? If not, it’s time to adapt.

## **Conclusion**

Migrating your company to the cloud requires changing the entirety of your applications or workloads. But it doesn’t stop there. In order to effectively implement cloud modernization, you need to adjust your existing operations, software delivery process, and organizational culture.

In this roundup, you learned about some best practices that can help you in your cloud modernization journey. By isolating your applications from the underlying infrastructure, you gain flexibility and the ability to shift your workloads easily between different cloud providers. You also learned how implementing a modern SDLC process can help your organization protect your customer's data and avoid reputational loss by security breaches.

[SUSE](https://www.suse.com/) supports enterprises of all sizes on their cloud modernization journey through their [Premium Technical Advisory Services](https://www.suse.com/services/premium-technical-advisory/). If you’re looking to restructure your existing solutions and accelerate your business, [SUSE’s cloud native transformation](https://www.suse.com/solutions/cloud-native-transformation/) approach can help you avoid common pitfalls and accelerate your business transformation.

Learn more in the [SUSE & Rancher Community](http://community.suse.com). We offer free classes on Kubernetes, Rancher, and more to support you on your cloud native learning path.
