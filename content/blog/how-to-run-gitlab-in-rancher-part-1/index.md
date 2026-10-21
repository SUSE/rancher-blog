---
title: "How to Run GitLab in Rancher - Part 1"
date: 2017-06-15T10:18:00
slug: "how-to-run-gitlab-in-rancher-part-1"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: ["ci-cd"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 86689
  original_url: "https://www.suse.com/c/rancher_blog/how-to-run-gitlab-in-rancher-part-1/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher 1.x catalog and stacks"
  redirect_target: "https://rancher.com/blog (hub)"
---

Build a CI/CD Pipeline with Kubernetes and RancherRecorded Online Meetup of best practices and tools for building pipelines with containers and kubernetes.[Watch the training](https://rancher.com/events/2018/2018-08-07-onlinemeetup-building-a-cicd-pipeline-with-k8s/)

*Note: This post is the first in a two-part series on using GitLab and
Rancher together for continuous integration and deployment, and [part
two](https://rancher.com/run-gitlab-rancher-2/) is now up. We’ve also
made the [entire walkthrough available for
download](https://info.rancher.com/run-gitlab-in-rancher).*

### ![GitLab and Rancher](images/rancher_blog_GitLab-and-Rancher-e1497567295680-300x232.jpg)Introduction

GitLab is, at its core, a tool for centrally managing Git repositories.
As one might expect form a platform that provides this service, GitLab
provides a robust authentication and authorization mechanism, groups,
issue tracking, wiki, and snippets, along with public, internal, and
private repositories. GitLab goes further by including a powerful
continuous integration (CI) engine and a Docker container registry,
allowing you to go from development to release inside of the same
utility. It continues by adding two more powerful open source software
utilities: Prometheus for monitoring, and Mattermost for team
communication. The platform has a solid API and integrates with existing
third-party systems like JIRA, Bugzilla, Pivotal, Slack, HipChat,
Bamboo, and more. All of this begs the question: why use GitLab instead
of using SaaS services directly? The answer lies in personal taste. For
most people, paying SaaS providers for the services that they provide is
an excellent solution. You can focus on building your application and
let them worry about maintaining the tools. What if you already have
infrastructure with spare capacity? What if you just want private
repositories without paying for that privilege? What if you did the math
and determined that you can save money by hosting it yourself? What if
you just want to own your own data? Bringing services in-house opens you
up to the risk of spending more time managing them and getting them to
talk to each other, which is why GitLab truly shines as an option. With
one click and a few minutes of configuration, you can be up and running
with a complete solution.

### Deploying GitLab

The Rancher Catalog contains an entry for GitLab CE that will install
the latest version. It assumes that you have a host where you want to
directly open 80 and 443 for HTTP/HTTPS and where you’ll open a port to
map to 22 inside of the container. The catalog item sets the environment
variable `GITLAB_OMNIBUS_CONFIG` with the values you provide. GitLab
then incorporates these values into its configuration when it launches.
For a very basic GitLab deployment the catalog item is sufficient, but
I’d like to show you how to do a bit more... For this tutorial, we’re
going to deploy GitLab CE, but we’re not going to open any ports. Host
ports are expensive, so we’ll use a load balancer for this later. We’ll
configure HTTPS and the Docker Registry and wire it up for use with
Rancher.

1. Create a new stack called gitlab
2. Add a service to the stack called gitlab
   - Image: gitlab/gitlab-ce:latest
   - Volumes:
     - gitlab-etc:/etc/gitlab
     - gitlab-opt:/var/opt/gitlab
     - gitlab-log:/var/log/gitlab
   - Networking
     - Set a specific host name: git
   - Health Check
     - HTTP: Port 80
     - Path: GET /HTTP/1.0
3. Add a sidekick to the service called postfix
   - Image: tozd/postfix
   - Environment:
     - MY\_NETWORKS:10.42.0.0/16, 127.0.0.0/8
     - ROOT\_ALIAS: you@yourdomain.com
   - Volumes:
     - postfix-log:/var/log/postfix
     - postfix-spool:/var/spool/postfix
   - Health Check:
     - TCP: Port 25

Before you launch, you have a couple of options for configuring GitLab:

1. Add all GitLab variables to GITLAB\_OMNIBUS\_CONFIG
2. Set all variables later

For the first time through, I recommend, option 2. The
default \*gitlab.rb \*file that GitLab provides is well documented, and if
you haven’t worked with GitLab before, you will learn a lot about its
capabilities from going through that file. Go ahead and click Launch.
Rancher will fetch the images and bring them up for you.

### Set Up SSL Offloading

While Rancher is fetching the images, let’s add a load balancer with
HTTPS. To do this, we’ll first create a LetsEncrypt container, then add
it to a load balancer and wait for the certificate to register. Once
that completes, we’ll add the configuration for GitLab to the load
balancer. In this example, I’m going to use the domain “example.com”
with the hostnames of “git” for GitLab, and “registry” for the
Docker registry. Make sure you’ve added the corresponding records to
your DNS zone file and pointed them to the host where the balancer will
be running before continuing to the next step.

#### Deploying LetsEncrypt:

1. From the Rancher community catalog, choose the LetsEncrypt service.
   Accept the TOS in the first dropdown, then set the following options
   for HTTP validation:
   - Your Email Address: [you@yourdomain.com](mailto:you@yourdomain.com)
   - Certificate Name: gitlab
   - Domain Names: git.example.com,registry.example.com
   - Domain Validation Method: HTTP
2. Click *Launch* to launch the container. You now have 120 seconds to
   complete the next step.

#### Deploying the Load Balancer

1. In the gitlab stack, click the dropdown next to Add Service and
   choose Add Load Balancer. Give it a name and add the following
   services selectors. Alternatively, if you already have an
   environment-wide load balancer, edit it to add the services below.
   - Public / HTTP
   - Port: 80
   - Path: /.well-known/acme-challenge
   - Target: letsencrypt
   - Port: 80
2. Click *Edit* to save your changes.

Monitor the logs for the LetsEncrypt container and in two minutes you’ll
see it report that it has registered the certificates for the two
domains. If you see errors reporting status 403 or 503, check your load
balancer configuration and make sure that it’s set up correctly. The
LetsEncrypt container will restart and continue to try and register the
certificates. Once the registration is successful, you’ll find the
certificates in the Rancher UI under the Infrastructure tab. We’re
ready to add SSL support to GitLab via the load balancer:

1. Edit the load balancer
2. Add the following Service Rules:
   - Public / HTTP
     - Host: git.example.com
     - Port: 80
     - Target: gitlab
     - Port: 80
   - Public / HTTPS
     - Host: git.example.com
     - Port: 443
     - Target: gitlab
     - Port: 80
   - Public / HTTPS
     - Host: registry.example.com
     - Port: 443
     - Target: gitlab
     - Port: 80
   - Public / TCP
     - Port: 2222
     - Target: gitlab
     - Port: 22
3. Click *Edit* to save your changes.

### Configure GitLab

GitLab’s configuration is saved in */etc/gitlab/gitlab.rb* within the
container. When we launched the service, we created a Docker volume to
store this data persistently. Within Rancher, find your Gitlab container
and log into it with Execute Shell. Change to */etc/gitlab* and edit
*gitlab.rb*. There are many variables within *gitlab.rb* that you can
use to adjust how Gitlab behaves. Each section includes a link to
Gitlab’s documentation that describes what that service does and what
each variable adjusts. For this tutorial, find and change or uncomment
the following variables:

```
external_url ‘https://git.example.com’
gitlab_rails['gitlab_ssh_host'] = 'git.example.com’
gitlab_rails['gitlab_email_enabled'] = true
gitlab_rails['gitlab_email_from'] = 'git@example.com'
gitlab_rails['gitlab_email_display_name'] = 'Gitlab'
gitlab_rails['gitlab_email_reply_to'] = 'noreply@example.com'
gitlab_rails['gravatar_plain_url'] = 'https://secure.gravatar.com/avatar/%{hash}?s=%{size}&d=identicon'
gitlab_rails['gravatar_ssl_url'] = 'https://secure.gravatar.com/avatar/%{hash}?s=%{size}&d=identicon'
gitlab_rails['gitlab_shell_ssh_port'] = 2222
gitlab_rails['smtp_enable'] = true
gitlab_rails['smtp_address'] = 'postfix'
gitlab_rails['smtp_port'] = 25
gitlab_rails['smtp_domain'] = 'yourdomain.com'
gitlab_rails['smtp_authentication'] = false
gitlab_rails['smtp_enable_starttls_auto'] = false
gitlab_rails['manage_backup_path'] = true
gitlab_rails['backup_path'] = '/var/opt/gitlab/backups'
gitlab_rails['backup_archive_permissions'] = 0644
gitlab_rails['backup_pg_schema'] = 'public'
gitlab_rails['backup_keep_time'] = 604800
registry_external_url 'https://registry.example.com’
gitlab_rails['registry_enabled'] = true
gitlab_rails['registry_host'] = 'registry.example.com'
gitlab_rails['registry_api_url'] = 'http://localhost:5000'
gitlab_rails['registry_key_path'] = '/var/opt/gitlab/gitlab-rails/certificate.key'
gitlab_rails['registry_path'] = '/var/opt/gitlab/gitlab-rails/shared/registry'
gitlab_rails['registry_issuer'] = 'omnibus-gitlab-issuer'
registry['enable'] = true
registry['token_realm'] = 'https://git.example.com'
nginx['listen_port'] = 80
nginx['listen_https'] = false
nginx['proxy_set_headers'] = {
 'Host' => '$http_host_with_default',
 'X-Real-IP' => '$remote_addr',
 'X-Forwarded-For' => '$proxy_add_x_forwarded_for',
 'X-Forwarded-Proto' => 'https',
 'X-Forwarded-Ssl' => 'on',
 'Upgrade' => '$http_upgrade',
 'Connection' => '$connection_upgrade'
}
registry_nginx['enable'] = true
registry_nginx['listen_port'] = 80
registry_nginx['listen_https'] = false
registry_nginx['proxy_set_headers'] = {
 'Host' => '$http_host',
 'X-Real-IP' => '$remote_addr',
 'X-Forwarded-For' => '$proxy_add_x_forwarded_for',
 'X-Forwarded-Proto' => 'https',
 'X-Forwarded-Ssl' => 'on'
}
registry_nginx['custom_gitlab_server_config'] = 'proxy_cache_convert_head off;'
```

With these variables changed, you’ll have accomplished the following:

1. Set the hostname for your git URLs
2. Configured GitLab to bounce HTTP to HTTPS
3. Enabled HTTPS gravatar URLs for both HTTP and HTTPs (necessary to
   avoid mixed-content errors)
4. Set the reported SSH port to 2222
5. Activated emails from GitLab
6. Enabled email delivery through the Postfix sidekick
7. Activated the nightly backups with a one-week retention period
8. Enabled the Container Registry
9. Activated the configuration and required headers for GitLab to
   understand that it’s behind an SSL load balancer

Save this file, and reconfigure GitLab by typing *gitlab-ctl
reconfigure* and pressing Enter. GitLab will rebuild its configuration
files and restart services that need to be restarted.

### Logging In

You’re ready to go! Point your browser at <https://git.example.com> and
you’ll be greeted with a screen that asks you to set a password. This is
for the default user, named *root*, and once you’ve set the password,
you’ll be asked to log in again. Congratulations! You have a running
GitLab instance! There are still some changes that we need to make
inside of GitLab to secure it, so keep reading.

### Locking it Down

I recommend that you make all the following changes:

#### Change the Root Username

Logging into anything as *root* is bad, and that username is a known
target. You’re logged in as the only user right now, and the first thing
you should do is change your username.

1. Click the wrench icon in the top right, next to the search bar
2. Select *Administrator* in the bottom of the middle column
3. Select the *Edit* button in the top right
4. Change your name, username, and email address
5. Scroll down and click *Save Changes*

The Administrator account’s old email address was *admin@example.com*,
and changing this information just tried to send an email to that
account to inform it of the change. I’m sure the people who own
example.com are *thrilled* with the amount of email they get.

1. Back in Rancher, find your *postfix* container and *Execute Shell*
2. Type *mailq* and press Enter. You should see a deferred message
   stuck in the queue. Note its ID
3. Type *postsuper –d <id>* and press Enter. This will delete that
   message from the queue.

#### Disable Public Sign-up

This next change will keep the Internet from taking over your new Gitlab
instance and using it for their nefarious ends.

1. Click the wrench icon again to return to the Admin dashboard
2. Click the dropdown next to the gear icon in the top right and choose
   *Settings*
3. You can adjust any of these to suit your needs, but the one you want
   to disable is the default of *Sign-up enabled* under *Sign-up
   Restrictions*.

#### Check your ports

In this example we’re using ports 80, 443, and 2222. No other ports on
the host are necessary for Gitlab, but 2222 is not a common port. Make
sure that you have this open in your firewall. At this point you have an
awesome GitLab installation. You can immediately start using it for your
projects. Go crazy! There’s so much to do inside of GitLab.

### Add your SSH Key

Although you can work with Gitlab over HTTPS, doing so over SSH is more
common. Before you can do this, you need to add your SSH public key to
Gitlab so that it knows who you are. If you don’t have an SSH key you
can make one (on Linux or Mac) with:

```
ssh-keygen -b 2048
```

Always use a passphrase for security – your key might have permission
to log in as a privileged user, and if your laptop is ever compromised,
you don’t want to give an attacker that level of access. (If you prefer
not to use a passphrase or deal with ssh agents, see the excellent
Kryptonite project at [krypt.co](https://krypt.co). Save this with the defaults
(or choose a new key name), and then in GitLab:

- Click the dropdown next to your avatar in the top right corner and
  select Settings followed by SSH Keys
- Paste your public key (the contents of the file that ends in .pub)
  into the box on the page that open

Next week, we’ll publish part 2 of this series, where we’ll cover
how to use GitLab CI Multi-Runner to build containers, and configuring
a project to use GitLab’s container registry. We’ll also cover
building containers via GitLab CI and deploying to Rancher. [**To part 2
>>**](https://rancher.com/run-gitlab-rancher-2/)

Build a CI/CD Pipeline with Kubernetes and RancherRecorded Online Meetup of best practices and tools for building pipelines with containers and kubernetes.[Watch the training](https://rancher.com/events/2018/2018-08-07-onlinemeetup-building-a-cicd-pipeline-with-k8s/)
