---
title: "Kubernetes Cloud Deployments with Terraform"
date: 2022-03-28T19:50:20
slug: "kubernetes-cloud-deployments-with-terraform"
author: "Matthew Casperson"
image: "images/shutterstock_175600700.jpg"
products: ["Kubernetes (generic)"]
tags: ["cloud", "gitops"]
content_type: "tutorial"
draft: false
migration:
  wp_id: 90537
  original_url: "https://www.suse.com/c/rancher_blog/kubernetes-cloud-deployments-with-terraform/"
  disposition: migrate_refresh
  commercial: false
  outdated_reason: "Terraform provider versions"
  redirect_target: ""
---

Kubernetes is a rich ecosystem, and the native YAML or JSON manifest files remain a popular way to deploy applications. YAML’s support for multi-document files makes it often possible to describe complex applications with a single file. The Kubernetes CLI also allows for many individual YAML or JSON files to be applied at once by referencing their parent directory, reducing most Kubernetes deployments to a single kubectl call.  

However, anyone who frequently deploys applications to Kubernetes will discover the limitations of static files. 

The most obvious limitation is that images and their tags are hard coded as part of a pod, deployment, stateful set or daemon set resource. Updating the image tag in a Kubernetes resource file as a CI/CD pipeline that generates new images requires custom scripting, as there is no native solution. 

Helm offers a solution thanks to its ability to generate YAML from template files. But Helm doesn't solve another common scenario where Kubernetes deployments depend on external platforms. Databases are a common example, as hosted platforms like AWS RDS or Azure SQL Database offer features that would be difficult to replicate in your own Kubernetes cluster.  

Fortunately, Terraform provides a convenient solution to all these scenarios. Terraform exposes a common declarative template syntax for all supported platforms, maintains state between deployments, and includes integrated variable support allowing frequently updated values (like image tags) to be passed at deployment time. Terraform also supports a wide range of platforms, including Kubernetes and cloud providers, so your deployments can be described and deployed with a single tool to multiple platforms. 

This post will teach you how to deploy WordPress to Kubernetes with an RDS database using Terraform. 

## **Prerequisites**

To follow along with this post, you'll need to have Terraform installed. The [Terraform website](https://learn.hashicorp.com/tutorials/terraform/install-cli) has instructions for installing the Terraform CLI in major operating systems. 

You'll also deploy an RDS database in AWS. To grant Terraform access to your AWS infrastructure, you'll need to configure the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) or define the [AWS environment variables](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html). 

Terraform will then install WordPress to an existing Kubernetes cluster. [K3s](https://k3s.io/) is a good choice for anyone looking to test Kubernetes deployments, as it creates a cluster on your local PC with a single command. 

The code shown in this post is available from [GitHub](https://github.com/mcasperson/TerraformK8sWordpress). 

## **Defining the Terraform providers**

To start, create a file called `providers.tf`. This will house the provider configuration. 

[Providers](https://www.terraform.io/language/providers) are like plugins that allow Terraform to manage external resources. Both AWS and Kubernetes have providers created by Hashicorp. The providers are defined in the *required\_providers* block, which allows Terraform to download the providers if they are not already available on your system: 

```
terraform { 

  required_providers { 

    aws = { 

      source  = "hashicorp/aws" 

    } 

    kubernetes = { 

      source  = "hashicorp/kubernetes" 

    } 

  } 
```

 

## **Configuring state**

Terraform persists the state of any resources it creates between executions in a [backend](https://www.terraform.io/language/settings/backends). By default, the state will be saved locally, but since you are working with AWS, it is convenient to save the state in a shared S3 bucket. This way, if Terraform is executed as part of a CI/CD workflow, the build server can access the shared state files. 

The following configuration defines the bucket and region where the Terraform state will be saved. You'll need to choose your own bucket, as S3 buckets require universally unique names, and so the name I've chosen here won't be available: 

```
  backend "s3" { 

    bucket = "mattc-tf-bucket" 

    key    = "wordpress" 

    region = "us-west-2" 

  } 

} 
```

 

## **Configuring the providers**

Then the providers are configured. Here you set the default region for AWS and configure the Kubernetes provider to access the cluster defined in the local *config* file: 

```
provider "aws" { 

  region = "us-west-2" 

} 

 

provider "kubernetes" { 

  # Set this value to "/etc/rancher/k3s/k3s.yaml" if using K3s 

  config_path    = "~/.kube/config" 

} 
```

 

There are many different ways to access a Kubernetes cluster, and the Kubernetes provider has [many different authentication options](https://registry.terraform.io/providers/hashicorp/kubernetes/latest/docs#authentication). You may want to use some of these alternative configuration options to connect to your cluster. 

 

## **Creating a VPC**

Your [RDS](https://aws.amazon.com/rds/) database requires a [VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html). The VPC is created with a [module](https://registry.terraform.io/modules/terraform-aws-modules/vpc/aws/latest) that abstracts away many of the finer points of AWS networking. All you need to do is give the VPC a name, define the VPC [CIDR](https://www.keycdn.com/support/what-is-cidr) block, enable DNS support (RDS requires this), set the subnet availability zones and define the subnet CIDR blocks. 

Add the following code to a file called *vpc.tf* to create a VPC to host the RDS database: 

```
module "vpc" { 

  source = "terraform-aws-modules/vpc/aws" 

 

  name = "my-vpc" 

  cidr = "10.0.0.0/16" 

 

  enable_dns_hostnames = true 

  enable_dns_support   = true 

 

  azs             = ["us-west-2a", "us-west-2b"] 

  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24"] 

} 
```

 

## **Create the database security group**

You'll need to define a [security group](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) to grant access to the RDS database. Security groups are like firewalls that permit or deny network traffic. You'll create a new security group with the [security group module](https://registry.terraform.io/modules/terraform-aws-modules/security-group/aws/latest).  

For this example, you'll grant public access to port 3306, the default MySQL port. Add the following code to the *sg.tf* file: 

```
module "mysql_sg" { 

  source = "terraform-aws-modules/security-group/aws" 

 

  name        = "mysql-service" 

  description = "Allows access to MySQL" 

  vpc_id      = module.vpc.vpc_id 

 

  ingress_with_cidr_blocks = [ 

    { 

      from_port   = 3306 

      to_port     = 3306 

      protocol    = "tcp" 

      description = "MySQL" 

      cidr_blocks = "0.0.0.0/0" 

    } 

  ] 

} 
```

##

## **Create the RDS instance**

With the VPC and security group configured, you can now create a MySQL RDS instance. This is done with the [RDS module](https://registry.terraform.io/modules/terraform-aws-modules/rds/aws/latest). 

Save the following to the file *rds.tf* to create a small MySQL RDS instance with public access in the VPC and with the security group created in the previous sections: 

```
module "db" { 

  source  = "terraform-aws-modules/rds/aws" 

 

  identifier = "wordpress" 

 

  publicly_accessible = true 

 

  engine            = "mysql" 

  engine_version    = "5.7.25" 

  instance_class    = "db.t3.small" 

  allocated_storage = 5 

 

  db_name  = "wordpress" 

  username = "user" 

  port     = "3306" 

 

  iam_database_authentication_enabled = true 

 

  vpc_security_group_ids = [module.mysql_sg.security_group_id] 

 

  maintenance_window = "Mon:00:00-Mon:03:00" 

  backup_window      = "03:00-06:00" 

 

  # DB subnet group 

  create_db_subnet_group = true 

  subnet_ids             = [module.vpc.public_subnets[0], module.vpc.public_subnets[1]] 

 

  # DB parameter group 

  family = "mysql5.7" 

 

  # DB option group 

  major_engine_version = "5.7" 

} 
```

##

## **Deploy WordPress to Kubernetes**

You now have all the AWS resources required to support a WordPress installation. WordPress itself will be hosted as a Kubernetes deployment and exposed by a Kubernetes service. 

The AWS resources in the previous sections were created via Terraform modules, which usually group together many related resources deployed with each other to create common infrastructure stacks. 

There is no need to use modules to deploy the Kubernetes resources, though. Kubernetes has already abstracted away much of the underlying infrastructure behind resources like pods and deployments. The Terraform provider exposes Kubernetes resources almost as you would find them in a YAML file. 

Terraform HCL files are far more flexible than the plain YAML used by Kubernetes. In the template below, you can see that the image being deployed is defined as *wordpress:${var.wordpress\_tag}*, where *wordpress\_tag* is a Terraform variable. You will also notice several environment variables defined with the values returned by creating the AWS RDS instance. For example, the database hostname is set as *module.db.db\_instance\_address*, which is the RDS instance address returned by the *db* module. 

Create the following template in a file called *wordpress.tf*:

```
resource "kubernetes_deployment" "wordpress" { 

  metadata { 

    name      = "wordpress" 

    namespace = "default" 

  } 

  spec { 

    replicas = 1 

    selector { 

      match_labels = { 

        app = "wordpress" 

      } 

    } 

    template { 

      metadata { 

        labels = { 

          app = "wordpress" 

        } 

      } 

      spec { 

        container { 

          image = "wordpress:${var.wordpress_tag}" 

          name  = "wordpress" 

          port { 

            container_port = 80 

          } 

          env { 

            name = "WORDPRESS_DB_HOST" 

            value = module.db.db_instance_address 

          } 

          env { 

            name = "WORDPRESS_DB_PASSWORD" 

            value = module.db.db_instance_password 

          } 

          env { 

            name = "WORDPRESS_DB_USER" 

            value = module.db.db_instance_username 

          } 

        } 

      } 

    } 

  } 

} 

 

resource "kubernetes_service" "wordpress" { 

  metadata { 

    name      = "wordpress" 

    namespace = "default" 

  } 

  spec { 

    selector = { 

      app = kubernetes_deployment.wordpress.spec.0.template.0.metadata.0.labels.app 

    } 

    type = "ClusterIP" 

    port { 

      port        = 80 

      target_port = 80 

    } 

  } 

} 
```

 

## **Defining variables**

The final step is to expose the variables used by the Terraform deployment. As noted in the previous section, the WordPress image tag deployed by Terraform is defined in the variable *wordpress\_tag*. 

Save the following template to a file called *vars.tf*: 

```
variable "wordpress_tag" { 

  type = string 

  default = "4.8-apache" 

} 
```

 

## **Deploying the resources**

Ensure you have a valid Kubernetes configuration file saved at *~/.kube/config* and have configured the AWS CLI (see the prerequisites section for more information). Then instruct Terraform to download the providers by running the command: 

```
terraform init 
```

 

To deploy the resources without any additional prompts, run the command: 

```
terraform apply --auto-approve 
```

 

At this point, Terraform will proceed to deploy the AWS and Kubernetes resources, giving you a complete infrastructure stack with two simple commands. 

To define the [wordpress image tag](https://hub.docker.com/_/wordpress?tab=tags) used by the deployment, set the *wordpress\_tag* variable with the *-var* argument: 

```
terraform apply --auto-approve -var "wordpress_tag=5.9.0-apache" 
```

 

## **Conclusion**

The ability to deploy multiple resources across many platforms is a powerful feature of Terraform. It allows DevOps teams to use the best solution for the job rather than limit themselves to the features of any single platform. In addition, Terraform's support for variables allows commonly updated fields, like image tags, to be defined at deployment time. 

In this post, you learned how to use Terraform to deploy WordPress to Kubernetes backed by an AWS RDS database, taking advantage of variables to define the WordPress version at deployment time.

### **Let’s continue the conversation!**[**Join the SUSE & Rancher Community**](https://community.suse.com/)**where you can further your Kubernetes knowledge and share your experience.**
