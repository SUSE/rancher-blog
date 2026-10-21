---
title: "Terraforming Rancher Deployments on Digital Ocean"
date: 2017-11-06T11:30:00
slug: "terraforming-rancher-deployments-on-digital-ocean"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: ["cloud", "installation"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 87293
  original_url: "https://www.suse.com/c/rancher_blog/terraforming-rancher-deployments-on-digital-ocean/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher 1.x Terraform on DigitalOcean"
  redirect_target: "docs.rancher.com"
---

Having a cool deployment system is pretty neat, but one thing every
engineer learns one way or another is that manual processes aren’t
processes, they’re chores. If you have to do something more than once,
you should automate it if you can. Of course, if the task of automating
the process takes longer than the total projected time you’ll spend
executing the process, you shouldn’t automate it.

[![XKCD 1205 - Is
It Worth the Time?](https://i.imgur.com/VA2B455.png)](https://xkcd.com/1205/) XKCD 1205 - Is It Worth the
Time?

With Rancher, the server can automate many traditionally manual tasks,
saving you a lot of time in the long run. If you’re running Rancher in
different environments or even testing it out with different domains or
instance sizes, however, you’ll want to automate even the setup and
teardown of your Rancher server.

In a prior blog post, I walked through how to [build a personal
cloud](https://rancher.com/building-personal-cloud-rancher-digitalocean/)
on Digital Ocean with Rancher. In this article, I’m going to outline
the advantages of automating a Rancher installation and how to Terraform
a Rancher server on Digital Ocean. Although it is possible to create
more complicated configurations using Terraform, this tutorial will
follow the basic steps for bootstrapping a docker host on Digital Ocean
using Terraform. We will be deploying a single docker container—in
this case, Rancher—using one simple line of provisioning. In essence,
this tutorial is more generally about Terraforming droplets and basic
network configuration in Digital Ocean.

## Advantages of Automating Rancher

The Rancher server is one of the simpler deployment tools to configure;
it consists of a simple Docker container that bootstraps all the
required services and interfaces for managing a cluster with Rancher.
Because Rancher runs inside a Docker container, it can be platform
agnostic. A standard installation of Rancher doesn’t require any
parameters passed to Docker other than a port map, so the local network
interface can talk to the Rancher container. This essentially means that
all of the Rancher server configuration occurs in the Rancher web
interface, not in the command line. Rancher is ready to go out of the
box, so the primary tasks that require automation in a Rancher workflow
are spinning up a droplet on Digital Ocean, getting Docker configured,
connecting our domain, configuring security credentials, and starting
the Rancher docker container. Of course, we also want to be able to undo
all these tasks by stopping the instance, removing A-records, and
purging security credentials. Thankfully, an incredible automation tool
already exists for the automation of infrastructure, and I’m speaking
of course of [Terraform](https://www.terraform.io/) by HashiCorp. As a
developer who loves side projects, when experimenting with new
technologies and tools I like to do it on a budget. I was
primarily drawn to Terraform because it enabled me to tear down my
infrastructure with a single command when I was finished using it. This
allowed me to minimize the impact that my experimentation had on my
wallet. Often, in corporate settings, the compute budget of a team can
be quite less than the desired budget, so cost-cutting measures must be
taken to keep the cloud bills low and the managers happy. Using a
terraform scripted infrastructure for Rancher allows us to spin up our
Rancher environment in under 5 minutes, while teardown takes 30 seconds
and can be run whenever we’re finished the current Rancher session.
Terraform also permits us to make changes to configurations
using `plans`. With `plans`, we are able to resize, rename, and rebuild
our infrastructure in seconds. This can be useful when testing out
different domain configurations, cluster sizes (in case we need more
resources on our Rancher server), and Rancher versions. A final anecdote
I’ll share is from my experience as a deployment engineer. When
launching a new service in a corporate setting, I had to manage five
different deployment environments: dev, QA, test, beta, and prod.
Typically, these versions will all be one version offset from another
and isolated in their own networks running on their own hardware.
Learning a tool like Terraform helped me create a simple script that can
spin up an application using the same exact process in each environment.
By tweaking a few variables in my `terraform.tfvars` file, however, I
can easily reconfigure an installation to run a specific version of the
application and make domains and networking settings point to the
environment-specific networks. Although the installation I’ll be
showing you is simple, the skills learned by understanding why each line
in a Terraform script is there will help you to craft Terraform scripts
that fit your unique deployment environments and situations.

## Terraforming a Rancher Server

Terraform offers a wide range of `Providers`, which are used to create,
manage, and modify infrastructure. Providers can access clouds, network
configurations, git repositories, and more. In this article, we’re
going to be using the Digital
Ocean [provider](https://www.terraform.io/docs/providers/do/index.html) for
Terraform. The Digital Ocean provider gives us access to a variety of
services: domains, droplets, firewalls, floating IP addresses, load
balancers, SSH keys, volumes, and more. For the purposes of running a
Rancher server, we want to configure domains, droplets, SSH keys, and
floating IPs for our Digital Ocean account. As I’ve said before, one of
most persuasive features of Digital Ocean is it’s incredible API based
droplet initialization. In under 30 seconds, we can spin up almost any
droplet Digital Ocean has to offer. This process includes the
installation of our SSH keys—as soon as the droplet is up and running,
we can SSH into it and provision it. Terraform exploits these awesome
features, letting us spin up a droplet, then successively SSH into the
droplet and execute our provisioning commands. Because Digital Ocean
droplets spin up so quickly, the whole process can take under a minute.
Terraform’s powerful library of providers gives us the ability to
explain in plain English what we want our infrastructure to look like,
and it can handle all the API requests, response checking and
formatting, and droplet state detection. In order to get started
Terraforming on Digital Ocean, we want to generate a Digital Ocean API
key with both read and write permissions. We can do
this [here](https://cloud.digitalocean.com/settings/api/tokens) by
clicking on `Generate New Token` and ticking the `Write` field. When
writing terraform files, it is important to keep your credentials out of
the equation and in an environment file. The separation of credentials
from configuration allows us to copy and paste this configuration
wherever we need it, and specify different credentials for different
installations. Terraform supports custom environment files
called `terraform.tfvars`. In your current working directory, create a
new file called `terraform.tfvars` and set the value of `do_token` to
your Digital Ocean API token as follows: `do_token = "<my_token>"`. The
main configuration of our `plan` must live in a file
named `terraform.tf` in our local directory, so let’s generate that
file and tell it to import our key from the `terraform.tfvars` file as
follows:

```
# terraform.tf
# Set the variable value in *.tfvars file
variable "do_token" {                     # Your DigitalOcean API Token
  type        = "string"
}
```

Next, let’s add our SSH key to our Digital Ocean account. We’re going
to want to use a variable in the `terraform.tfvars` file to specify the
path to the key as this may change in different installations. We’ll
add both the private and public keys as variables because we’ll need to
use the private key to provision our instance in further steps.

```
# terraform.tfvars
do_token = "<my_token>"
local_ssh_key_path="<path_to_private_key>"
local_ssh_key_path_public="<path_to_public_key>"
```

After adding the ssh key paths as variables, we want to initialize those
variables in the Terraform plan.

```
# terraform.tf
...
variable "local_ssh_key_path" {           # The path on your local machine to the SSH private key (defaults to "~/.ssh/id_rsa")
  type        = "string"
  default     = "~/.ssh/id_rsa"
}
variable "local_ssh_key_path_public" {    # The path on your local machine to the SSH public key (defaults to "~/.ssh/id_rsa.pub")
  type        = "string"
  default     = "~/.ssh/id_rsa.pub"
}
```

Here, we can set some default values so, in the case where we don’t
want to specify key paths, they’ll default to the standard location for
ssh keys in Unix based systems. Now that we’ve configured our SSH keys,
we need to add the public key to Digital Ocean. This is also a simple
process using Terraform; just configure the Digital Ocean provider and
tell it to add an SSH key.

```
# terraform.tf
...
# Configure the Digital Ocean Provider
provider "digitalocean" {
  token = "${var.do_token}"
}

# Create a new DO SSH key
resource "digitalocean_ssh_key" "terraform_local" {
  name       = "Terraform Local Key"
  public_key = "${file("${var.local_ssh_key_path_public}")}"
}
```

If we ran the plan now, we’d see a new SSH key in the Digital Ocean
security panel named `Terraform Local Key`, which would match the public
key specified by our terraform variable. However, we want to get a few
more actions added before we run the Terraform script. We want to spin
up a droplet to run our Rancher server, so let’s tell Terraform what we
want our droplet to look like.

```
# terraform.tf
...
resource "digitalocean_droplet" "rancher-controller" {
  image       = "coreos-stable"
  name        = "rancher.demo"
  region      = "nyc3"
  size        = "4gb"
  ssh_keys    = ["${digitalocean_ssh_key.terraform_local.id}"]
  private_networking = true
}
```

First, we name the resource `rancher-controller`. Terraform allows you
to use resources as both constructors and objects, so after this stage
of our plan executes, we will be able to call `rancher-controller` and
ask for attributes like `ipv4_address`, which don’t exist until after
Digital Ocean processes our request. We’re going to need this IP
address in order to SSH into the machine for the provisioning step. Then
we specify our image as `coreos-stable` because it comes packed with
Docker and allows us to launch the Rancher server with minimal overhead
and additional steps. The region can be specified to whichever you
prefer, though typically you’ll want to specify the same region for
your worker nodes to keep latency low. We also specify
the `ssh_keys` variable as the attribute of our previously
defined `terraform_local` object. The `id` property is generated when we
execute the `digitalocean_ssh_key` resource and contains a ssh public
key ID Next, we want to add a provisioning step to
the `rancher-controller` item which will start the docker container that
serves the Rancher server. This requires what in Terraform language is
known as a `provisioner`. Because this process can be completed with a
simple command execution, we can use the default remote execution
provisioner. To add the provisioning step to the terraform plan, we add
a new field in the `rancher-controller` object.

```
# terraform.tf
...
resource "digitalocean_droplet" "rancher-controller" {
  image       = "coreos-stable"
  name        = "rancher.demo"
  region      = "nyc3"
  size        = "4gb"
  ssh_keys    = ["${digitalocean_ssh_key.terraform_local.id}"]
  private_networking = true

  provisioner "remote-exec" {
    connection {
      type        = "ssh"
      private_key = "${file("${var.local_ssh_key_path}")}"
      user        = "core"
    }

    inline = [
      "sudo docker run -d --restart=unless-stopped -p 80:8080 rancher/server",
    ]
  }
}
```

In this step, we’ve added a new provisioner of the `remote-exec` class
as well as specified connection variables for how we want to connect to
the server (`ssh` as user `core` with the private
key `var.local_ssh_key_path` as is defined in `terraform.tfvars`). Then,
we tell the provisioner to perform an inline command, though you can
follow this with a series of commands in an array, our array has a
single item. We’re asking docker to fetch the `rancher/server` image
from Docker Hub and run the container, mapping port 8080 on the
container to port 80 on our host, as the rancher server should be the
only application running on port 80 on our host. The final step in our
Terraform configuration is to make our host accessible through a Digital
Ocean hosted domain. If you don’t want to connect a domain to your
Rancher server, you can simply use the IP address returned by Terraform
after running the plan as it is, and access Rancher that way. If you
choose to use a domain, you can better secure your Rancher server with
GitHub authentication or other domain-based authentication methods.
Let’s define a new variable at the top of the `terraform.tf` file and
include it in the `terraform.tfvars` file.

```
# terraform.tf
variable "do_domain" {                    # The domain you have hooked up to Digital Ocean's Networking panel
  type        = "string"
}
...
```

```
# terraform.tfvars
...
do_domain = "<digital_ocean_hosted_domain>"
```

We can now access this domain name by referencing `vars.do_domain` in
our Terraform plan. Digital Ocean supports the use of floating IP
addresses on their platform, which can be directed to different droplets
using internal networking. The best way to configure domain routes is to
set up a floating IP, point the desired subdomain at the floating IP,
and then point the floating IP at the desired droplet. This way, we can
modify the floating IP whenever the droplet is rebuilt without having to
change the A records on the domain. Also, if we decide to use a Digital
Ocean load balancer in the future, we can point the floating IP at the
load balancer and not worry about changing domain records when droplets
spin up and down. To add a floating IP address and domain record to our
plan, we must add these lines to the `terraform.tf` file:

```
# terraform.tf
...
resource "digitalocean_floating_ip" "rancher-controller" {
  droplet_id = "${digitalocean_droplet.rancher-controller.id}"
  region     = "${digitalocean_droplet.rancher-controller.region}"
}

# Create a new record
resource "digitalocean_record" "rancher-controller" {
  name        = "rancher"
  type        = "A"
  domain      = "${var.do_domain}"
  ttl         = "60"
  value       = "${digitalocean_floating_ip.rancher-controller.ip_address}"
}
```

The first half of this configuration grabs the droplet ID from
the `rancher-controller` droplet that we just spun up. We also define a
region for the IP that matches our droplet. The floating IP resource
will interface with the droplet resource to learn its internal IP
address and route the two together. It then exposes its own IP address
so that our domain record can dynamically set the value of the A record
to the floating IP. The second half of the configuration creates a new A
record on our domain with the name `rancher` creating a
subdomain `rancher.<digital_ocean_hosted_domain>`. We set the
time-to-live to 60 seconds, so when we tear down the instance and
rebuild it, the new IP address is quickly resolved. The value field is
populated with the floating IP from earlier. Now that we’ve taken all
these steps to configure the Rancher server, our `terraform.tf` file
should look as follows:

```
# terraform.tf
variable "do_token" {                     # Your DigitalOcean API Token
  type        = "string"
}
variable "do_domain" {                    # The domain you have hooked up to Digital Ocean's Networking panel
  type        = "string"
}
variable "local_ssh_key_path" {           # The path on your local machine to the SSH private key (defaults to "~/.ssh/id_rsa")
  type        = "string"
  default     = "~/.ssh/id_rsa"
}
variable "local_ssh_key_path_public" {    # The path on your local machine to the SSH public key (defaults to "~/.ssh/id_rsa.pub")
  type        = "string"
  default     = "~/.ssh/id_rsa.pub"
}

# Configure the DigitalOcean Provider
provider "digitalocean" {
  token = "${var.do_token}"
}

# Create a new DO SSH key
resource "digitalocean_ssh_key" "terraform_local" {
  name       = "Terraform Local Key"
  public_key = "${file("${var.local_ssh_key_path_public}")}"
}

resource "digitalocean_droplet" "rancher-controller" {
  image       = "coreos-stable"
  name        = "rancher.${var.do_domain}"
  region      = "nyc3"
  size        = "4gb"
  ssh_keys    = ["${digitalocean_ssh_key.terraform_local.id}"]
  private_networking = true

  provisioner "remote-exec" {
    connection {
      type        = "ssh"
      private_key = "${file("${var.local_ssh_key_path}")}"
      user        = "core"
    }

    inline = [
      "sudo docker run -d --restart=unless-stopped -p 80:8080 rancher/server",
    ]
  }
}

resource "digitalocean_floating_ip" "rancher-controller" {
  droplet_id = "${digitalocean_droplet.rancher-controller.id}"
  region     = "${digitalocean_droplet.rancher-controller.region}"
}

# Create a new record
resource "digitalocean_record" "rancher-controller" {
  name        = "rancher"
  type        = "A"
  domain      = "${var.do_domain}"
  ttl         = "60"
  value       = "${digitalocean_floating_ip.rancher-controller.ip_address}"
}
```

The `terraform.tfvars` file should have the following variables exposed:

```
# terraform.tfvars
do_token = "<token>"
do_domain = "<domain>"
local_ssh_key_path="<ssh_key_path>"
local_ssh_key_path_public="<ssh_pub_path>"
```

Once we’ve populated the variables and confirmed our files look right,
we can install terraform and execute our plan. We can head over to
Terraform’s [download
page](https://www.terraform.io/downloads.html) and grab the package
appropriate for our system. Once the installation is finished, we’ll
open a terminal window and `cd` into the directory with
our `terraform.tf` and `terraform.tfvars` files. To plan our Terraform
build, run the following: `$ terraform plan` We should see this line in
our response, noting that we’re creating 4 new resources on Digital
Ocean: `Plan: 4 to add, 0 to change, 0 to destroy.` After planning, we
can apply the plan by running the following: `$ terraform apply` After a
minute or so, we’ll see the script complete and, by navigating
to `rancher.<do_domain>`, we should see the Rancher server up and
running! Please browse around the
Rancher [blog](https://rancher.com/blog) to see all the cool things you
can build with a Rancher server!

## Conclusion and Further Steps

As a quick recap, let’s review why we set out to Terraform our Rancher
server in the first place. Rancher is easy to configure and deploy.
There’s not really any frustration involved in spinning up a Rancher
server and getting started. The friction in deploying Rancher, then,
comes from the configuration of infrastructure; networking, machines,
and images. Terraform has given us the power to automate the
straightforward but time-consuming task of spinning up droplets on
Digital Ocean, configuring floating IP addresses and domains, and
provisioning a Rancher server. These aren’t tasks that are difficult on
their own, but when managing many deployments of Rancher or when testing
in different environments, quick and painless solutions like Terraform
can prevent simple tasks from becoming a burden and reduce the
possibility for simple mistakes to break systems. With that in mind,
let’s talk about a few more complex ways we can deploy Rancher using
Terraform. In a fully automated production process, we wouldn’t be
using the simple SSH provisioner as the primary configuration tool for
our new droplet. We’d have a Chef server up and running and use
the [Chef](https://www.terraform.io/docs/provisioners/chef.html) provisioner
for Terraform to ensure the filesystem and properties of our droplet are
exactly as they should be for our installation. The Chef scripts would
proceed to launch the Rancher server. If you have an interest in this
process and how one would go about setting it up, let me know! I’d love
to go into more detail about using Chef recipes to configure and deploy
Rancher servers, but I don’t quite have the space for it in this
article. If High Availibility is what we’re looking for, Digital Ocean
isn’t really the best choice for cloud infrastructure. Picking Amazon
AWS or Google Cloud Platform would be more sensible as Rancher uses
MySQL to mediate between HA hosts in a Rancher cluster and those clouds
provide home baked scalable and properly Highly Available MySQL
solutions (Amazon RDS and Google Cloud SQL, respectively). If you’re
interested in running HA Rancher and happen to be using one of those
clouds, check out the [Amazon
AWS](https://www.terraform.io/docs/providers/aws/index.html) and [Google
Cloud
Platform](https://www.terraform.io/docs/providers/google/index.html) infrastructure
providers for Terraform. You’d also benefit by reading up on the
documentation for [Multi-Node Rancher
Deployments](https://rancher.com/docs/rancher/v1.0/en/installing-rancher/installing-server/multi-nodes/).
If you’d be interested in a tutorial utilizing Terraform to run Highly
Available Rancher servers on Amazon AWS or Google Cloud Platform, please
let me know! I’d love to go into detail and break down the best
solutions for HA Rancher in cloud-hosted environments. If you’re just
interested in our simple deployment from this article, the following
section gives a few tips and tricks for making your Rancher Terraform
script your own.

### Changing or Cleaning Up your Rancher Installation

When the fun is finished, or we need to make a change to our
configuration, these two commands will let you apply changes, or destroy
your installation. When changing your configuration, if you make any
modifications to the droplet settings, it will wipe and rebuild the
droplet. **YOU WILL LOSE ALL CONFIGURATION AND DATA ON THE RANCHER
SERVER IF YOU REAPPLY A PLAN WITH MODIFIED DROPLET SETTINGS.**
`$ terraform plan && terraform apply` The above command will re-plan and
apply any changes made to
the `terraform.tf` and `terraform.tfvars` files, which may consist of
tearing the droplet down and rebuilding it. To fully tear down our
infrastructure stack, we can run one simple command.
`$ terraform destroy` We’ll be asked to enter `yes` to confirm the
destruction of resources, but once we do, Terraform will go ahead and
tear down the droplet, domain, floating IP, and SSH keys that were added
to our Digital Ocean account.

### Upgrading Rancher with Terraform

If you want to upgrade your Rancher server that has been deployed via
Terraform and you plan on retaining your data, follow the process
outlined [here](https://rancher.com/docs/rancher/v1.6/en/upgrading/#single-container) to
SSH into your droplet and run the commands specified. In a production
environment, it’d be best to use Chef as the provisioner for your
Terraform plan and push changes to your droplets via Chef to upgrade the
Rancher version. If you don’t care about retaining the data when
upgrading, you can modify the line from the `terraform.tf` file from the
provisioning block as follows.
`"sudo docker run -d --restart=unless-stopped -p 80:8080 rancher/server:<desired_version_tag>"`
Wow, that was quite the process, but now we can build and tear down
Rancher server hosts at will in under a minute! Moving these files to
other environments and tweaking the variables to fit different
installations allow us to create an incredibly simple and repeatable
deployment process. With the tools and skills learned from this article,
we can take on more challenging tasks, like running Rancher in a highly
available manner, without the burden of manually spinning up machines,
installing docker, booting up the Rancher container, and configuring our
networks. I hope you’ve enjoyed this approach to automating Rancher
deployments on Digital Ocean! Stay tuned to see some more
Rancher-related content and feel free to give us feedback on our [user
Slack](https://slack.rancher.io/) or [forums](https://forums.rancher.com/).

![Student at the University of Chicago](images/rancher_blog_Eric-150x150.png) *Eric Volpert
is a student at the University of Chicago and works as an evangelist,
growth hacker, and writer for our Rancher Labs. He enjoys any
engineering challenge. He’s spent the last three summers as an internal
tools engineer at Bloomberg and a year building DNS services for the
Secure Domain Foundation with CrowdStrike. Eric enjoys many forms of
music ranging from EDM to High Baroque, playing MOBAs and other
action-packed games on his PC, and late-night hacking sessions, duct
taping APIs together so he can make coffee with a voice command.*
