---
title: "How to Build and Run Your Own Container Images"
date: 2021-09-24T10:08:32
slug: "how-to-build-and-run-your-own-container-images"
author: "Rancher Admin"
products: ["Docker/containers (generic)"]
tags: ["developer-experience"]
content_type: "tutorial"
draft: false
migration:
  wp_id: 87326
  original_url: "https://www.suse.com/c/rancher_blog/how-to-build-and-run-your-own-container-images/"
  disposition: migrate
  commercial: false
  outdated_reason: ""
  redirect_target: ""
---

## Introduction

The rise of containerization has been a revolutionary development for many organizations. Being able to deploy applications of any kind on a standardized platform with robust tooling and low overhead is a clear advantage over many of the alternatives. Viewing container images as a packaging format also allows users to take advantage of pre-built images, shared and audited publicly, to reduce development time and rapidly deploy new software.

However useful shared public images are, most users will also require custom images that define how to run their own tools and services. Whether customizing readily available software, packaging and running internal tools, or creating images as a release medium for your own projects, creating images is a fundamental part of the container paradigm. In this guide, we’ll talk about how to create your own images and some of the considerations to keep in mind as you do.

## What Are Container Images?

Container images are static bundles of files that represent everything a container runtime, like [Docker](https://www.docker.com), needs to run a container. Images include the filesystem layout, all of the required applications and dependencies, and configuration.

Each image is built from either a parent image (an image used as the starting point for the new image) or from an empty pseudo-image called `scratch`. Most parent images typically provide a filesystem structure that resembles a minimal Linux system, package management tools, and the core functionality that you’d expect from a command line environment. Parent images are available for most popular Linux distributions, often in a variety of configurations. Images are also available preconfigured for different programming languages and ecosystems.

Container images are built by applying “layers” onto previous images. Each filesystem layer represents a point-in-time record of the filesystem state after certain actions. Images that have common ancestry share filesystem layers, allowing for reduced overhead and greater consistency between images.

## Creating a Container Image Interactively

There are a few different ways to create container images. One of the easiest to to get started with is to interactively create images. You can run a container image with an interactive shell, perform the actions needed to get the operating system into the desired state, and then save the result. This is a good way to test ideas and validate your processes.

To begin, start up a container using your chosen parent image. We need to pass in a few arguments to the `docker run` command to start the container with the correct configuration. Pass the `--interactive` or `-i` flag to indicate that the container’s `STDIN` should be opened. Additionally, we need to use the `--tty` or `-t` flag to allocate a psuedo-TTY to be able to run interactive commands. Lastly, we need to spawn an actual shell like `/bin/bash` so that we have an interface to interact with the container.

To demonstrate, we can start up an SLE15 container with a Bash shell session by typing:

```
docker run -it registry.suse.com/suse/sle15:latest /bin/bash
```

Docker will check for the latest SLE15 image locally and, if necessary, pull in any missing or stale image layers from Docker Hub. After all of the required layers are available, Docker will allocate a pseudo-TTY and start a Bash shell, dropping you into a new session within the container:

```
Unable to find image 'registry.suse.com/suse/sle15:latest' locally
latest: Pulling from suse/sle15
Digest: sha256:f9c401eccc260e71c8e0f2b13126e6ea8d5d20349ee2c70c7a0e2b287272b768
Status: Downloaded newer image for registry.suse.com/suse/sle15:latest
0f243d1adf40:/ #
```

From here, you can you can make changes to the file system to reflect the environment you need. As a simple example, we can add a message to a file:

```
echo 'hello there!' > /message
```

When you are finished with your changes, exit the session to back out of the container and return to your local shell:

```
exit
```

From here, we can take a look at our exited container by asking Docker to list all processes, including those that have completed:

```
docker ps --all
```

The output will list the recently terminated container.

```
CONTAINER ID   IMAGE                                COMMAND       CREATED              STATUS                       PORTS   NAMES
0f243d1adf40   registry.suse.com/suse/sle15:latest  "/bin/bash"   About a minute ago    Exited (0) 49 seconds ago           goofy_elgamal
```

If you do not provide a name for your container instance, Docker generates a random name for you. In this instance, our container has been named `goofy_elgamal`. We can use this or the container ID (`0f243d1adf40` here) to refer to this specific container instance.

If you are happy with your changes, you can save the image you created using the `docker commit` command. To do so, you need to provide the container name or the container ID from the last command as well as the name you want to use for the saved image. Here, we’ll name our image `hello_world` for simplicity:

```
docker commit goofy_elgamal hello_world
```

```
sha256:cae51db36851800ded5c72c6ee7ba6a68b62f97fe3c692918620465a28e19d49
```

If we check the list of available container images on our system, our new image will be among the results:

```
docker image ls
```

```
REPOSITORY                   TAG         IMAGE ID          CREATED           SIZE
hello_world                  latest      cae51db36851      39 seconds ago    121MB
registry.suse.com/suse/sle15 latest      4700c5afb975      45 hours ago      121MB
```

Now we can check whether our message is present within the image by running a container that displays the file we saved:

```
docker run hello_world cat /message
```

```
hello there!
```

Here, we passed the `cat /message` command to a new container spawned from our image to display the contents of the message file within the image.

If this is the action we want to execute automatically whenever the image is run, we can update the image with that command by modifying one of the container image’s attributes as we commit a new image. We’ll base this off of our most recent container (which we can get the ID of with `docker ps -lq`) and commit the new image as `hello_world:fixed`:

```
docker commit --change='CMD ["cat", "/message"]' $(docker ps -lq) hello_world:fixed
```

```
sha256:3a2cd24ddd785b2483e83e67be767bb36822722f6f745bad6c579c641d8bb8f9
```

Now, we can run containers from the new image without specifying a command to execute at runtime:

```
docker run hello_world:fixed
```

```
hello there!
```

This is a quick way to interactively create images to test out ideas, figure out dependencies, etc.

## Creating Images with a Dockerfile

While creating images interactively is sometimes more comfortable for beginners, it does have some serious disadvantages.

Images created interactively don’t provide a clean record of what actions were taken to create the image. This makes maintaining and updating the image very challenging over time. Since the process relies on logging in and completing a series of steps manually, it also is more error prone. Due to the way that container images are built up with a new layer for each additional action, it’s also easy to accidentally create unoptimized images with extra layers that are not needed. And finally, as we saw above with the `--change` flag, we often have to manipulate the final image using additional commands to access fairly basic Docker functionality.

### What are Dockerfiles?

In most real world situations, it’s preferable to create images from a `Dockerfile` instead. A `Dockerfile` is a plain text file that contains instructions that tell the Docker build engine how to create an image. The primary responsibilities of a `Dockerfile` include:

- Detailing the parent image or the initial state that the image should start from
- Providing metadata about the author and image properties
- Outlining the exact commands to run during the build process
- Specifying the runtime conditions for containers spawned from the image

Once a `Dockerfile` is defined, the `docker build` command can interpret it and combine it with a build context — a file path or URL representing a working directory — to create a new container image. This process enables simpler automation and leaves a good record of the actions taken to create the image.

The `Dockerfile` can be checked into source control and builds can be generated automatically by CI/CD processes as part of the development and release cycle. Furthermore, you have access to the full range of Docker image instructions at build time instead of having to specify changes after the image is built as we did when getting our interactive image to automatically run a command at start. Overall, this method of building images is self-documenting and offers more repeatability and flexibility than building images interactively.

### Reproducing the Interactive Image with a Docker File

To get an understanding of the general format of a `Dockerfile`, let’s show a very simple example by recreating our previous image.

Start by creating and moving into a directory that’ll serve as our build context:

```
mkdir ~/hello_world
cd ~/hello_world
```

As mentioned above, the build context is a path or URL on the host system that is accessible to Docker during the build process. This is useful for copying files to the container image, for example. It’s important to note that the entire build context is sent to the Docker daemon at build time, so if you choose a directory with a large number of unnecessary files and subdirectories, it can increase the build time and resource usage during the build process substantially for no purpose.

Inside our new, clean build context, use your favorite text editor to create and open a file called `Dockerfile` to define the container image:

```
nano Dockerfile
```

Inside, specify the parent image we want to use as our starting point using the `FROM` instruction. We’ll use the `sle15:latest` image, just as we did in the interactive image:

```
FROMregistry.suse.com/suse/sle15:latest
```

Next, we can create the `/message` file within the image using the `RUN` instruction:

```
FROM registry.suse.com/suse/sle15 RUN echo 'hello there!' > /message
```

Finally, we can specify the default action for containers spawned from this image by defining a `CMD`:

```
FROM registry.suse.com/suse/sle15:latest

RUN echo 'hello there!' > /message

CMD ["cat", "/message"]
```

Save and close the file when you are finished. Now, create a new image from the `Dockerfile` using the `docker build` command. We can set the tag for the image to `hello_world:first_dockerfile` by including the `-t` flag. Notice the dot at the end of the command, indicating that the current directory should be used as the build context for the new image:

```
docker build -t hello_world:first_dockerfile .
```

```
Sending build context to Docker daemon 2.048kB
Step 1/3 : FROM registry.suse.com/suse/sle15:latest
---> 4700c5afb975
Step 2/3 : RUN echo 'hello there!' > /message
---> Running in a07bfa65dcb1
Removing intermediate container a07bfa65dcb1
---> 7691663192b3
Step 3/3 : CMD ["cat","/message"]
---> Running in da122e223bfe
Removing intermediate container da122e223bfe
---> 8c2f63cb2103
Successfully built 8c2f63cb2103
Successfully tagged hello_world:first_dockerfile
```

Upon running the command, the Docker build process will set the context to the current directory and look for a `Dockerfile`. It will then interpret the instructions within to set up an environment and build the image according to the definition.

Once the image is built, we can create a container from it in much the same way as we did last time:

```
docker run hello_world:first_dockerfile
```

```
hello there!
```

The results are similar, but with greater repeatability, accountability, and control over the process.

### Taking Advantage of the Build Context

We can enhance our first `Dockerfile` to make it more flexible and, at the same time, demonstrate how the build context can influence the resulting image with a few minor modifications.

Instead of hard coding the message within the Dockerfile, we can place the message in a separate file located within our build context. This helps us separate data from the actual build process.

Inside of the directory with your `Dockerfile`, create a file called `message` with a new message inside. The easiest way to do this is to echo a string directly to a new filename:

```
echo 'message stored in build context' > message
```

Now, we have our message in a dedicated file instead of embedded within our `Dockerfile`. We need to adjust the build process to reflect this change though. Open the `Dockerfile` with your text editor to make the change:

```
nano Dockerfile
```

We need to change the second line, `RUN echo 'hello there!' > /message`, to refer to the external file we created. We can copy the file from the build context into the image using the `COPY` instruction. Since the following command looks for the message at `/message`, we’ll copy the file there:

```
FROM registry.suse.com/suse/sle15:latest

COPY message /message

CMD ["cat", "/message"]
```

The first argument to `COPY` refers to the file in the build context, while the second argument refers to the filesystem location within the actual image.

When you are finished build a new image using a different tag:

```
docker build -t hello_world:second_dockerfile .
```

```
Sending build context to Docker daemon 3.072kB
Step 1/3 : FROM registry.suse.com/suse/sle15:latest
---> 4700c5afb975
Step 2/3 : COPY message /message
---> 7b934fd5477b
Step 3/3 : CMD ["cat","/message"]
---> Running in fd0b1dcfc389
Removing intermediate container fd0b1dcfc389
---> 243dcef35719
Successfully built 243dcef35719
Successfully tagged hello_world:second_dockerfile
```

When you start a container based on the new image, you should see the message stored in the `message` file on your computer:

```
docker run hello_world:second_dockerfile
```

```
message stored in build context
```

> **Note**  
> The message printed by the container is static upon building. If you change the message with the file after building, you will need to rebuild the image to update the message being output.

## Dockerfile instructions

Now that you’ve gotten a bit of experience with some very simple `Dockerfile` instructions, it’s worthwhile to take a closer look at the most common operations available. We’ll take a look at the most common instructions, determine if they primarily affect the image build stage or the container runtime stage, and describe their general use.

We’ll start with a few operations typically found towards the beginning of the `Dockerfile`:

### FROM

The `FROM` instruction must be the first item in a `Dockerfile`. It specifies a parent image that your image will start from. You can specify any image found on [Docker Hub](https://hub.docker.com/), a different image registry, or any local image. You specify the image using the `<image_name>:<tag_name>` format.

For instance, to base your image off the official SLE15 image, you can specify the SUSE repository with the `latest` tag, like this:

```
FROM registry.suse.com/suse/sle15:latest
. . .
```

The `SUSE` images are maintained by the official SUSE team, so the repository is on SUSE registry. On the default docker registry to pull images from a repository that isn’t foundational, you typically have to specify the account namespace prior to the image name, separated by a slash.

For instance, to use an image called `test_image` with the tag `v1` from a `demouser` account, you would use the following syntax:

```
FROM demouser/test_image:v1
. . .
```

While the vast majority of images use the `FROM` instruction to specify a parent image, you can also use `FROM scratch` to indicate that your image should not have a parent image. The `scratch` image is a pseudo image that indicates that you want to start without a parent image. In this case, the images filesystem is completely blank and everything must be built from the ground up to create the image layers and filesystem. You most often see `FROM scratch` used in the official base images offered by Docker.

### LABEL

The `LABEL` instruction provides the ability to add key-value metadata to the image. This allows you to include arbitrary information about your image that might be useful for auditing or with automated processes. The `LABEL` instruction can be used many times within a single `Dockerfile`.

The basic syntax for adding a `LABEL` to your image is the following:

```
. . .
LABEL <key>=<value>
. . .
```

You can include multiple labels on the same line or you can add an additional `LABEL` instruction for subsequent items.

These two are effectively the same:

```
. . .
LABEL key1="value 1" key2="value 2"
. . .
```

```
. . .
LABEL key1="value 1"
LABLE key2="value 2"
. . .
```

Values that include spaces must be enclosed within quotes as demonstrated above.

### ADD

The `ADD` instruction is a way to copy file from the local filesystem, a remote URL, or a local compressed archive file to a location within the image filesystem. This allows you to add arbitrary files from local and remote sources into your image. The `ADD` instruction is very similar to the `COPY` instruction we will learn more about later.

The syntax of the basic `ADD` instruction looks like this:

```
. . .
ADD <source> <destination>
. . .
```

The source in this case can refer to:

- A local file or directory within the build context
- A remote URL

Sources can contain wildcard matching characters, which will be expanded when building to generate a list of valid files to copy. The source can also be a compressed or uncompressed tar archive on the local system. In this case, Docker will automatically extract the archive and copy the contents to the destination.

The destination can be an absolute or relative path. If a relative path is given, it is understood to be in relation to the `WORKDIR`, an instruction we’ll talk about later. If a destination ends with a trailing slash, it is interpreted as a directory. Otherwise, it is taken to be the name the file should be copied as in the image filesystem.

### COPY

The `COPY` instruction looks incredibly similar to the `ADD` instruction at first glance, and overlaps in purpose. The difference is that `COPY` only works with local files and provides no automatic archive extraction.

While these limitations may initially feel limiting, `COPY` is the recommended option for scenarios it can operate in due to its less ambiguous and easy-to-interpret behavior.

The `COPY` syntax mirrors that of `ADD`:

```
. . .
COPY <source> <destination>
. . .
```

The only difference being that the source here can only refer to local files or directories, which will be copied without extraction to the destination. Like `ADD`, sources can also use wildcard characters to match multiple files.

The `COPY` command can also take a `--from=` argument for use in multi-stage builds. This allows files to be copied from a previous image into the current image when the build process uses multiple images to produce the final image.

### ENV

The `ENV` instruction is used to set an environmental variable during the build and run stages of the image. This allows you to set variables that will influence the image during the build process or that will be available to processes when containers are actually running.

The `ENV` instruction can use either of the following syntaxes:

```
. . .
ENV <key> <value>
ENV <key>=<value>
. . .
```

The second form can contain multiple key-value pairings on the same line, separated by a space.

Once the environment variable is set, it is interpreted as it would be in any standard shell environment for the rest of the build process and in the containers spawned from the image.

### EXPOSE

The `EXPOSE` instruction communicates which ports the container’s services are listening on. This does not affect the way the container is built or run in any way but rather informs the container’s user which ports are being used. The user can then choose to publish the ports, exposing them to the network, if desired.

The `EXPOSE` instruction is basically a dedicated mechanism for communicating with the container user about your image’s network ports. The basic syntax can be any of the following:

```
. . .
EXPOSE <port>
EXPOSE <port>/tcp
EXPOSE <port>/udp
. . .
```

If no protocol is specified, as in the first format, TCP is assumed. To expose the same port for both protocols, a separate line for each is required.

### RUN

The `RUN` instruction is one of the most common instructions within any `Dockerfile`. The operation will execute the statements given to it within the image’s filesystem environment during the build process. This is the primary mechanism for making changes to build your image. It can run any commands available within the image’s filesystem.

The `RUN` instruction has two separate forms, the choice of which impacts its execution:

```
. . .
RUN <command>
RUN ["<executable", ..., "argn"]
. . .
```

The first format, providing a raw command and arguments after the `RUN` instruction, will execute the given command in a shell session. This is the simpler format that executes in much the same way as it would on the command line. Since the command is executed by a shell, normal shell processing of wildcards, environment variables, etc. take place during execution.

The second format, which provides an executable and a list of arguments within a JSON array is not executed in a shell environment. This means that any behavior that relies on shell interpretation will not function correctly unless you choose to use a shell as the initial executable. This style of execution can be more predictable and can help you avoid side effects in situations where you do not need to rely on shell processing.

### USER

The `USER` instruction controls what user, and optionally group, commands are executed as in the image environment. This can affect both the build and runtime process as every subsequent command that is run in the container environment (`RUN`, `CMD`, and `ENTRYPOINT`) will be executed by the provided user. The `USER` instruction can be used multiple times to switch users for certain commands.

By default, all instructions that manipulate the container file system are run as `root`. This makes configuration easy, but running containers as `root` can have severe security implications.

The syntax for the `USER` instruction is as follows:

```
USER <user_name_or_ID>:<group_name_or_ID>
```

The user and group components can either specify the name or the numerical ID within the image’s filesystem. Keep in mind that any user or group referenced must already exist on the image. You might need to execute commands using `RUN` prior to using `USER` to configure the identities you require.

The group element is optional and if it is left out, the colon can also be omitted. If the group is not specified, Docker will use the user’s primary group or the `root` group if that is undefined.

### VOLUME

The `VOLUME` instruction is responsible for creating mount points within the container image’s filesystem for mounting external volumes from the host or other locations. This is the primary filesystem-based method for sharing data between the host and container or between containers. The `VOLUME` instruction specifies the internal mount point, but does not map it to any specific location on the host. Instead, this mapping is specified at runtime.

The syntax of `VOLUME` instruction can either take a series of strings separated by spaces or a JSON array. For instance, these two will produce the same result:

```
VOLUME ["/data/vol1", "/data/vol2"]
VOLUME /data/vol1 /data/vol2
```

It is important to not think of the `VOLUME` instruction like the `mount` command in Linux. With the `VOLUME` instruction, all actions that will interact with the data within the volume must be performed prior to specifying the volume. Any data creation or copying performed after the `VOLUME` line will be discarded. Instead, you must perform your data actions on the mount point and then label it with `VOLUME` after you’ve performed the actions.

### WORKDIR

The `WORKDIR` instruction declares the directory context for instructions like `RUN`, `CMD`, `ENTRYPOINT`, `COPY`, and `ADD`. It specifies the location on the filesystem where these commands should executed. This has implications for any relative paths or commands that perform actions in relation to the current directory.

The `WORKDIR` instruction will automatically create the directory and any parent directories necessary. It can be used as many times as desired througout the `Dockerfile` to change the context as required for the build and runtime instructions.

To declare a `WORKDIR`, you can use the following syntax:

```
WORKDIR <filesystem_path>
```

Usually, it is best to provide an absolute path to remove ambiguity. If a relative path is given, it will be interpreted as relative to the previous `WORKDIR` value.

### CMD

The `CMD` instruction provides the default execution instructions for when a container is run from the image. While this can be overridden at runtime, this is the primary way to specify what should happen when a user executes `docker run` on your image. Since `CMD` helps specify the runtime command for the container, it can only be used once in a `Dockerfile`.

The `CMD` instruction can be used on its own or with conjunction with the `ENTRYPOINT` instruction we’ll discuss next. Because of this flexibility, the `CMD` instruction has a few different syntax variations that can affect how it is interpreted.

The first, called the “shell” form, simply lists out the commands and arguments as a string as they’d be given on the command line:

```
CMD ls -al /var/log | wc -l
```

This variant of the instruction is executed by passing the line directly to `/bin/sh -c`. This means that the string is interpreted and processed by the shell, which allows for piping, substitution, and any other shell magic that might alter the meaning of the command. This is a good format to use for simple commands that use the existing environment.

The second format is called the “exec” form. This is the recommended format for most use cases as it is predictable and avoids unintentional shell behavior that can change the execution of the command. The syntax of the exec form uses a JSON array with the executable as the first element and the parameters as each subsequent element:

```
CMD ["full/path/to/executable", "param1", "param2"]
```

Unlike the shell form, this form executes the first element directly and passes the remaining elements as arguments. This means no shell substitution or string manipulation is performed. This is clean way of ensuring that the commands provided are executed exactly as written.

The third format looks similar to the exec form and is used in conjunction with the `ENTRYPOINT` instruction (we cover this next). If an `ENTRYPOINT` is provided, the JSON array specified by `CMD` will be interpreted as *arguments* to the entry point command. This means that the `CMD` will contain only parameters with no executable:

```
ENTRYPOINT ["/path/to/entrypoint"]
CMD ["param1", "param2"]
```

This format allows users to easily override the specific arguments to the entry point command at runtime. This is useful if you want to provide a default executable and a default set of arguments, but allow the user to override just the arguments or override the entire command if desired. If your image should almost always run a certain command but might require different arguments at runtime, this is a good way of configuring that.

### ENTRYPOINT

The `ENTRYPOINT` instruction allows you to configure a container that can be run as an executable by default. The target of an `ENTRYPOINT` instruction is command and parameters that should be always run, unless overridden, when the container is started. This command allows you to operate the container as if you were operating the command or script specified by the instruction.

The `ENTRYPOINT` instruction has two syntaxes, similar to `CMD`.

The first syntax is a string that will be passed to `/bin/sh -c`. As before, this will cause the string to be interpreted by the shell, so string manipulation, substitution, etc. will take place. The format looks like this:

```
ENTRYPOINT ls -al
```

The second format is the recommended alternative. It uses a JSON array to specify the command and any parameters. These will be executed directly without using a shell. This means that no variable substitution or other shell behavior will take place. However, it has the advantage of being predictable and making it possible to coordinate with an associated `CMD` instruction.

### Using ENTRYPOINT and CMD Together

If your `Dockerfile` includes both a `ENTRYPOINT` and a `CMD` instruction, they both must use the exec form. When both instructions are present, the `ENTRYPOINT` will be interpreted as the command and required parameters. The `CMD` will be interpreted as the default, easily override-able parameters.

As a simple example, we can imaging a `Dockerfile` with the following instructions:

```
FROM registry.suse.com/sle15:latest
ENTRYPOINT ["ls", "-al"]
CMD ["/var/log"]
```

In this scenario, by default, when the resulting image is run, it will execute the command `ls -al /var/log`:

```
docker build -t entry_cmd_test .
docker run -it entry_cmd_test
```

```
total 16
drwxr-xr-x 4 root root 4096 Nov 28 12:57 .
drwxr-xr-x 10 root root 4096 Nov 28 12:57 ..
drwx------ 2 root root 4096 Nov 8 12:58 krb5
drwxr-x--- 2 root root 4096 Nov 28 12:57 zypp
```

We can easily change the directory being targeted by providing a parameter when we run that will override the one specified in `CMD`:

```
docker run -it entry_cmd_test /proc/sys
```

```
total 0
dr-xr-xr-x 1 root root 0 Nov 30 10:45 .
dr-xr-xr-x 579 root root 0 Nov 30 10:45 ..
dr-xr-xr-x 1 root root 0 Nov 30 10:45 abi
dr-xr-xr-x 1 root root 0 Nov 30 10:45 crypto
dr-xr-xr-x 1 root root 0 Nov 30 10:45 debug
dr-xr-xr-x 1 root root 0 Nov 30 10:45 dev
dr-xr-xr-x 1 root root 0 Nov 30 10:45 fs
dr-xr-xr-x 1 root root 0 Nov 30 10:45 kernel
dr-xr-xr-x 1 root root 0 Nov 30 10:45 net
dr-xr-xr-x 1 root root 0 Nov 30 10:45 user
dr-xr-xr-x 1 root root 0 Nov 30 10:45 vm
```

The `ENTRYPOINT` command and executable is still persistent even though we’ve overridden the parameters that were defined in `CMD`. This can provide some pretty interesting flexibility in how you construct your images.

## Controlling Image Layers and Caching

Each time you issue a `RUN` instruction, Docker executes the command and commits the results as an additional layer for your image. **Image layers** are extremely important to understand as you build images. Each additional layer adds additional size to your image. So being mindful of what instructions create layers can help you reduce image bloat.

The other important thing to understand about image layers is how it affects Docker’s build cache. Docker uses a build cache to reduce the time it spends rebuilding images. During a rebuild, if it determines that nothing has changed in a layer, it will use the cached layer and move on. If it determines that a change has happened, it will invalidate the cached layer and all subsequent layers and re-execute the instructions from that point on. Docker cannot perfectly determine when it’s best to invalidate its cache, so you must think about how your instructions affect the cache. By crafting your instructions carefully, you can manipulate the caching behavior to rely on the cache when it is safe and to bust the cache when you need to rebuild fresh.

A good example of this interplay between reducing image size and busting outdated layers is when installing software from a repository. With many Linux distributions including SUSE, Debian, Ubuntu, and Alpine Linux, installing software is conventionally broken down into a multi-part process. First, the local package indexes are updated by pulling down the latest information about the packages available from remote repositories. Afterwards, specific packages can be installed with the package manager using the local index to request the appropriate software from the remote repository.

An initial implementation of this process in a `Dockerfile` might look something like this:

```
. . .
RUN zypper refresh
RUN zypper install -y <package1>
. . .
```

This works well on our first run, but it does have some problems. When we craft translate these processes into `RUN` instructions, we want to reduce the resulting image layer size *and* make sure that the build process does not reuse an outdated image layer on rebuilds when a significant change has occurred.

Let’s walk through what happens if we add another package to the installation line and then rebuild the image:

```
. . .
RUN zypper refresh
RUN zypper install -y <package1> <package2>
. . .
```

In this case, Docker will begin evaluating the instructions to see where it can use image layers it already has cached to save time and resources. Since the `zypper refresh` line hasn’t changed, it assumes that the resulting layer is still acceptable and will not re-run that instruction. Next, it will skip down to the `zypper install` line. Since a new package has been added, it knows that it cannot use the previous layer for that instruction, so it reruns the command. However, since the `zypper refresh` was not executed this time, the package index available at that time may be outdated. One or both of the packages the system is requesting to download might no longer be available. In this case, Docker’s cached layer has prevented our rebuild from executing successfully.

If we have to add a new package to our install process, we need to make sure that the packaging command also reruns the package index update so that the build does not try to install using stale package information. We can achieve this by bundling the two packaging commands into a single `RUN` instruction. That way, if we change the installed package list, Docker re-run *both* the refresh and install commands together. Since the instruction that install the packages also updates the package index, we’ll always install with a fresh package list:

```
. . .
RUN zypper refresh && zypper install -y <package1> <package2>
. . .
```

While this ensures that we always use the latest index to install packages, we don’t need that index present on our completed image. Since the index files have served their purpose and are no longer necessary, we can string an additional command on the end of our `RUN` instruction to clean up the repositories. This will prevent these cached files from being committed into the image layer when the `RUN` instruction completes:

```
. . .
RUN zypper refresh && zypper install -y <package1> <package2> && zypper clean -aM
. . .
```

At this point, we’ve reduced this image layers to include all of the packages we need but none of the extra files that we aren’t using. The layer will automatically be rebuilt when we change the packages we need, but it will be reused in other cases, speeding up our builds.

## Conclusion

There is plenty more to learn about building your own images. With some reading and experimentation, it is usually possible to get a working `Dockerfile` that can build an image to your specifications. Once you’ve reached that goal, you can begin looking for opportunities to optimize your image to reduce the image size or build time. These are not usually of too much concern when you’re working on your own computer or deploying to a few machines, but they become incredibly important as you begin to use containers within CI/CD pipelines and automatic deployments.
