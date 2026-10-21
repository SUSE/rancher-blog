---
title: "How to Run GitLab in Rancher - Part 2"
date: 2017-06-22T11:18:00
slug: "how-to-run-gitlab-in-rancher-part-2"
author: "Rancher Admin"
products: ["Rancher 1.x"]
tags: ["ci-cd"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 87002
  original_url: "https://www.suse.com/c/rancher_blog/how-to-run-gitlab-in-rancher-part-2/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Rancher 1.x GitLab runner setup"
  redirect_target: "https://rancher.com/blog (hub)"
---

Build a CI/CD Pipeline with Kubernetes and RancherRecorded Online Meetup of best practices and tools for building pipelines with containers and kubernetes.[Watch the training](https://rancher.com/events/2018/2018-08-07-onlinemeetup-building-a-cicd-pipeline-with-k8s/)

![GitLab and
Rancher](images/rancher_blog_GitLab-and-Rancher-e1497567295680-300x232.jpg)\*This is part two
of our series on using GitLab and Rancher together to build a CI/CD
pipeline, and follows [**part**
**one**](https://rancher.com/how-to-run-gitlab-in-rancher-1/) from last
week, which covered deploying, configuring, and securing GitLab in
Rancher. We’ve also made **[the entire walkthrough available for
download](https://info.rancher.com/run-gitlab-in-rancher).** \*

### Using GitLab CI Multi-Runner to Build Containers

GitLab CI is a powerful tool for continuous integration and continuous
delivery. To use it with Rancher, we’ll deploy a runner that will
execute jobs.

#### Launching the Runner

There are several ways that runners can be deployed, but since we’ll be
targeting building containers from our repositories, we’ll run a Docker
container that has direct access to */var/run/docker.sock* to build
images that are siblings to itself.

1. In Rancher, add a service to your Gitlab stack
2. Set it up with the following configuration:

- Name: runner01
- Image: gitlab/gitlab-runner
- Console: None
- Volumes:
  - /var/run/docker.sock:/var/run/docker.sock
  - runner01-etc:/etc/gitlab-runner

When the container launches, it will create a default configuration in
*/etc/gitlab-runner*, to which we’ve connected a volume. The next step
is to register the runner with your Gitlab instance. The options that
I’m setting below are correct for a basic runner that will build any
job. You can also limit runners to specific repositories or use other
images. Read the documentation from Gitlab to learn what options are
best for your environment.

#### Configuring the Runner

1. Execute a shell into the container
2. Run *gitlab-ci-multi-runner register* to begin the registration
   process
3. Answer the questions that it asks according to the following example
   (answers are in bold):

root@4bd974b1c799:/# gitlab-ci-multi-runner register Running in
system-mode.

Please enter the gitlab-ci coordinator URL (e.g. https://gitlab.com/):
**https://git.example.com** Please enter the gitlab-ci token for this
runner: **DGQ-J7n0tR33LXB3z\_** Please enter the gitlab-ci description
for this runner: [4bd974b1c799]: **runner01** Please enter the
gitlab-ci tags for this runner (comma separated): **<press enter>**
Whether to lock Runner to current project [true/false]: [false]:
**<press enter>** Registering runner... succeeded runner=DGQ-J7dD
Please enter the executor: docker, parallels, ssh, docker-ssh+machine,
kubernetes, docker-ssh, shell, virtualbox, docker+machine: **docker**
Please enter the default Docker image (e.g. ruby:2.1): **docker:stable**
Runner registered successfully.

Feel free to start it, but if it’s running already the config should be
automatically reloaded. The main items to note are:

- Enter the URL for your Gitlab instance
- Enter the runner token (found in Admin/Runners)
- Give your runner a recognizable name
- Choose runner type of docker
- Choose the docker:stable container image

After the initial registration completes, we need to edit
/etc/gitlab-runner/config.toml and make a change:

- volumes = [“/var/run/docker.sock:/var/run/docker.sock“,
  “/cache”]

This will mount */var/run/docker.sock* inside the container so that
containers that it builds will be stored in the images store of the host
itself. This is a far better solution than Docker in Docker. Changes to
*config.toml* are picked up automatically by the runner, so you don’t
need to restart. You can see and interact with your runner in Gitlab
under *Admin/Runners.*

### Configuring a Project to Use GitLab’s Container Registry

GitLab’s Container Registry is tied directly to repositories, so you
won’t be able to push containers to arbitrary locations. If you have a
repository called *demo-php* in group *docker*, the path to the image
will be *registry.example.com/docker/demo-php* with tags defined
according to how you tell GitLab CI to build the containers. For the
rest of this example I’ll use the repository whose content you can find
at *https://github.com/oskapt/rancher-gitlab-demo*. To set this up in
your GitLab environment do the following:

1. 1. Create a project in GitLab. In this tutorial, I’ll call it
   *example/demo* (the group is *example* and the project is
   *demo*)
   1. Clone and modify the *rancher-gitlab-demo* repo:

```
$ git clone https://github.com/oskapt/rancher-gitlab-demo.git demo
$ cd demo
$ git remote set-url origin ssh://git@git.example.com:2222/example/demo.git
$ git push -u origin master
```

The file looks like this:

```
variables:
  REGISTRY_HOST: registry.example.com
  TEST_IMAGE: $REGISTRY_HOST/$CI_PROJECT_PATH:$CI_BUILD_REF_NAME
  RELEASE_IMAGE: $REGISTRY_HOST/$CI_PROJECT_PATH:latest

stages:
  - build
  - release

before_script:
  - docker info
  - docker login -u gitlab-ci-token -p $CI_BUILD_TOKEN $REGISTRY_HOST

build:
  stage: build
  script:
    - docker build --pull -t $TEST_IMAGE .
    - docker push $TEST_IMAGE

release:
  stage: release
  script:
    - docker pull $TEST_IMAGE
    - docker tag $TEST_IMAGE $RELEASE_IMAGE
    - docker push $RELEASE_IMAGE
  only:
    - master

push_to_docker_hub:
  # in order for this to work you will need to set
  # `HUB_USERNAME` and `HUB_PASSWORD` as CI variables
  # in the Gitlab project
  stage: release
  variables:
    DOCKER_IMAGE: $HUB_USERNAME/$CI_PROJECT_NAME:latest
  script:
    - docker login -u $HUB_USERNAME -p $HUB_PASSWORD
    - docker tag $RELEASE_IMAGE $DOCKER_IMAGE
    - docker push $DOCKER_IMAGE
  only:
    - master
  when: manual
```

I’ve designed this CI file to be used in multiple basic Docker projects
without any modification. After you set items in the variables section
to your liking, the rest of the file will adapt to any project. There
are two stages - *build* and *release*. GitLab has its own token that
allows it to log into its own registry, which it does in the
*before\_script* section. It then executes the script commands in the
*build* section, which will build your container and tag it with the
format designated in the `TEST_IMAGE` variable. The result will be a
container tagged with the branch name, like this for our *develop*
branch:

```
registry.example.com/example/demo:develop
```

It then pushes this into the registry. If you push to the *master*
branch, it does all of this and then continues with the *release* stage
to tag the image with *latest* before pushing it. The result is a
container tagged both *master* and *latest*, and since latest is the
default tag name, you can pull it without specifying the tag at all.
Finally, a manual option available for the *master* branch is to push
the container to Docker Hub. For this to work, you have to first set
`HUB_USERNAME` and `HUB_PASSWORD` in the Gitlab project under *Settings
| CI/CD Pipelines | Secret Variables*. Gitlab CI will re-tag the
*master* image with the value of *DOCKER\_IMAGE* and then push it out to
Docker Hub. Because we’ve specified *manual* for *when*, GitLab will not
do this automatically. You’ll have to manually execute this stage from
GitLab.

### Building the Container via GitLab CI

Commit these changes and push them to your Gitlab project in the
*develop* branch. If everything has been set up correctly, you’ll be
able to see the pipeline start under the *Pipelines* tab in the project.
You can select the *Status* icon to view a detailed progress log for the
stages. If there are any issues, GitLab CI will report that the pipeline
failed, and you can view the log to see why. When you fix the issues and
push a new commit, it will start a new pipeline. If the error was
transient (unable to connect to Docker Hub, for example), you can run
that stage of the pipeline again. If you ever want to just run a
pipeline from the existing code, you can do so by clicking *Run
Pipeline* and choosing the branch you want to build. When everything is
finished, your pipeline will say *Passed* and you’ll see your container
under the *Registry* tab in your GitLab project.

### Create a Deployment User

Before you can use the registry, you’ll need to add it to Rancher.
Rather than use your administrator account, I recommend that you create
a *deploy* user with Reporter permissions on any project you want to
deploy (or any group containing multiple projects).

1. Click the wrench in the top right corner to enter the admin area
2. Click the *New User* button in the bottom of the middle column
3. Create a user named *deploy*
4. Under *Access* indicate that the user is *External*. This will give
   it restricted access within Gitlab.
5. Click *Create User*, which will take you to a summary screen.

GitLab defaults to sending a login email to the user, so we need to edit
the user to set a password.

1. From the summary screen, click *Edit* in the top right
2. Set a password for the user and click *Save Changes*
3. Navigate to your project in Gitlab and click *Settings* and then
   *Members*
4. Type *deploy* in the search bar and choose the *deploy* user
5. Give the user *Reporter* permissions
6. Click *Add to project* to save your changes.

The *deploy* user now has permission to access containers from your
project’s container registry.

### Deploy the Container to Rancher

All this setup has brought us to this point - pulling containers from
your own private registry and deploying them in Rancher. The last thing
we need to do is add the registry and then make a new stack and service.

1. In Rancher, click *Infrastructure* and choose *Registries*
2. Click *Add Registry*
3. Choose *Custom*
4. Enter your registry URL (e.g. *example.com*)
5. Enter your deployment user’s username and password
6. Click *Create*

With the registry added to Rancher, you’re ready to create services from
those images.

1. Create a stack called *demo*
2. Add a service and name it anything you like. Set the image to use
   the *develop* tag of your new container image.
   - example.com/example/demo:develop
3. Click *Create*

Congratulations! You’ve just deployed the development version of your
project from your private container registry!

### Where to Go From Here

This has been a long journey, but with all of the heavy lifting done,
you can get back to work using the tools we’ve installed. Some things to
do from here:

- Set up groups for your other projects. Use logical collections, like
  *docker* or *websites* for the projects that will be contained
  within.
- Import other projects into Gitlab
- Set up Gitlab CI to build the containers
- Change to the *master* branch and merge *develop* to bring in
  *.gitlab-ci.yml* and then push that to Gitlab. Update Rancher to
  pull the *latest* image tag.
- Add *HUB\_USERNAME* and \*HUB\_\*PASSWORD to the project, and then
  manually push your image to Docker Hub

Have fun!

Build a CI/CD Pipeline with Kubernetes and RancherRecorded Online Meetup of best practices and tools for building pipelines with containers and kubernetes.[Watch the training](https://rancher.com/events/2018/2018-08-07-onlinemeetup-building-a-cicd-pipeline-with-k8s/)
