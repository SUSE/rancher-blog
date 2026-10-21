---
title: "Matador Deploy - Making Deployment on Rancher Fun"
date: 2016-07-26T11:12:00
slug: "matador-deploy-making-deployment-on-rancher-fun"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: ["ci-cd"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 86813
  original_url: "https://www.suse.com/c/rancher_blog/matador-deploy-making-deployment-on-rancher-fun/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher 1.x deploy tool, 2016"
  redirect_target: "rancher.com/blog (hub)"
---

*By Timon Sotiropoulos, software engineer at
[SEED](http://seeddigital.co/). SEED is a leading product development
company that builds design-driven web and mobile applications for
startup founders and enterprise innovators.* [![Seed
Logo](images/rancher_blog_Seed-Logo.png)](images/rancher_blog_Seed-Logo.png)Deployment
days can be quite confronting and scary for new developers. We realized
through onboarding some of our developers and introducing them to the
world of DevOps that the complexity and stress of deployment days could
take a toll on morale and productivity, with everyone always half
dreading a deployment on the upcoming calendar. After learning the no.1
rule of “never deploy on a Friday” the hard way, the team at SEED
decided there had to be a better way than the traditional “pull down
from Git repository and deploy to a server” method. **The Road to
Matador** This journey started with a trip down the lane of the hottest
containerisation framework in the business, the flying whale Docker. For
those have haven’t heard of it, Docker essentially allows you to create
a blueprint for your application inside its own contained virtual
machine image. What this means is that you can create a working version
of your app on any server that has Docker installed and be confident
that everything will work as expected. The next link in the chain we
discovered was [Rancher](https://rancher.com), an excellent tool for
automatically connecting and configuring Docker containers. Rancher
allows you to break your application up into multiple, separate
components the same way you would break up a program into different
classes, allowing single responsibility as well as the ability to scale
certain services up and down as required. This process and procedure
became second nature to us, but it was easy to mess things up. It was
easy to accidentally update the wrong Rancher environment and as we
planned on moving to a more continuous development lifecycle, the manual
updating of the Rancher environments had to stop. Our long term plan for
our continuous deployment process is to get to a point where a developer
can push their code to GitHub, build a copy of the Docker container, tag
it with that commit ID, and then push that code to their desired Rancher
environment. All the separate parts work independently, but we are
working towards integrating all of these tools into a fully-fledged
continuous deployment service. The first step is Matador Deploy. Matador
is a tool we have created to handle the creation and building of our
Docker containers and deploying them to the [Rancher
environments](https://rancher.com/rancher). The complication here is
that for each of our projects, we would have two or three separate
environments, one each for Production, Staging and Development. To do
this, we would have to duplicate all of our DevOps configurations and
scripts for each of our environments and then build the application
using a Makefile that set specific variables for each of the Rancher
Compose commands. However, we found that these Makefiles were simply
starting to duplicate themselves across all of our projects and we knew
there had to be a better way.

### So what does Matador do?

The first thing we wanted Matador to do was combine the similar parts of
our environments and Docker/Rancher configurations into one file, while
still also allowing us to have the environment-specific parts when
required, such as the environment variables that connected to our
production or staging database. This led to the creation of three files
that Matador requires to run: two generic templates that setup the
basics of the project, and one configuration file that holds all our
environment specific configuration:

- **docker-compose-template.yml**: The generic Docker Compose file for
  the application. This file contains all the configuration that
  builds the docker containers that together create your application
  stack, as well as the connections between them.
- **rancher-compose-template.yml:** The generic Rancher Compose file
  for the application. This file contains all the configuration that
  is specific to your Rancher environments, such as the scale for each
  of your docker containers or your SSL certificates that have been
  setup for the Rancher environment.
- **config.yml:** The config file is the one where you can define your
  environment specific configuration between your production, staging
  and development environments that have been set up on Rancher. Below
  is a short example of how this config file should be structured out:

```
image_base: seed/example-image
project_name: tester
global:
 web:
  environment:
   - TEST=forall
dev:
 web:
  environment:
   - NODE_ENV=dev
  labels:
   io.rancher.scheduler.affinity:host_label: client=ibackpacker,env=development
staging:
 web:
  environment:
   - NODE_ENV=staging
  labels:
   # io.rancher.scheduler.affinity:host_label: client=alessi,env=staging
   com.alessimutants.pods: version=0.1,branch=dev
prod:
 lb:
  labels:
   io.rancher.scheduler.local: 'false'
  web:
   image: seed/web
   environment:
    - NODE_ENV=prod
   labels:
    io.rancher.scheduler.local: 'false'
```

Everything defined in the config.yml file will be added to your
docker-compose-template depending on the environment variable that you
pass the application at run time. Matador will take the additional
config provided, then append or overwrite what is in the
docker-compose-template file and write out a new docker-compose file for
you automatically. The same is done with your rancher-compose-template;
although at this point in time there are no configuration options to
alter the template, this will be added in future releases. These output
files are then used as part of the Rancher Compose process to update
your environment on Rancher. They are also saved locally so that you can
review the configuration that Matador has created for you.

### So How Do I Use Matador?

We have put together some extremely detailed usage instructions on the
[GitHub repository](https://github.com/seedtech/matador-deploy), but the
general gist is pretty straight forward. You will need to download the
latest version of Matador Deploy from the [Python Package Index -
PyPI](https://pypi.python.org/pypi/matador-deploy), as well as [Rancher
Compose](https://github.com/rancher/rancher-compose), which can be
downloaded from their release page on GitHub. Once that is done, there
are a few required fields that you must supply to the configuration file
to make things work. These are the first two entries in the config.yml:

- project\_name: This field will be the name that your stack receives
  when it is deployed to Rancher. It will also be automatically
  namespaced with the environment that you pass to Matador when you
  deploy. Note, this is not the Rancher environment name, but rather
  the Rancher stack name.
- image\_base: This field is the most important because it provides
  the DockerHub registry that your application will attempt to load
  your docker images from. These also have a naming convention that is
  required for each of your respective environment images as follows:

seed/example-image:latest // Production Image seed/example-image:staging
// Staging Image seed/example-image:dev // Development Image

We do plan to include the building of your Docker images within Matador
itself in future releases, however for now you will need to add these
tags manually when pushing your images to DockerHub. Once your
config.yml, docker-compose-template.yml and rancher-compose-template.yml
have been configured, place them inside a folder called “templates” in
the root of your project directory. Finally, from the root of your
project directory call the following command:

```
$ matador-deploy –url http://rancher.url.co –key RANCHER_KEY –secret RANCHER_SECRET –env dev
```

The fields themselves are explained here:

--url: This refers to the rancher url that you are trying to upload
your rancher configuration to. --key: This is the API Key that needs to
be created specifically for the rancher environment that you are trying
to update. --secret: This is the Secret Key of Password that is
provided to you when you create a new API Key for your rancher
environment. --env: This is the environment that you wish to update. It
takes one of the following options are

The benefit of Matador in this instance is that it forces you to provide
the authentication information for your Rancher environment. One of the
issues with Rancher Compose is that it will search your local
environment in your shell for the Rancher environment keys, so if you
are pushing a lot of different stacks to Rancher (for example pushing to
Staging, then to Production), it can be easy to make a mistake and push
the wrong image to the wrong environment. If these fields aren’t
provided to Matador, the process will simply fail. There are also plans
to improve this even further by querying your Rancher server with your
API keys and having Matador actually tell you what environment it is
attempting to update - look for that too in a future release!

### Where To From Here?

We have a few ideas of things we want the application to be able to do
as we work our way into building a full continuous deployment tool. A
few basic examples would be: ● Adding Support for building docker images
and pushing them to Docker Hub ● Adding a tagging system that connects
your Docker Hub images to your currently loaded Image on your Rancher
environment ● Add a simplified rollback option, most likely using the
tagging system However, what we really want to know are the features
that you would find most useful. We have open sourced Matador because we
think that it could be really helpful in integrating all these excellent
services together in the future. So please give it a try, and if you
have any ideas either write an issue and we will have a look into it, or
just fork the repository and give it a go. We can’t wait to see what you
come up with.
