---
title: "How to Manage Harvester 0.3.0 with Rancher 2.6.1 Running in a VM within Harvester"
date: 2021-10-20T15:50:10
slug: "how-to-manage-harvester-0-3-0-with-rancher-2-6-1-running-in-a-vm-within-harvester"
author: "SUSE"
products: ["Harvester"]
tags: ["virtualization"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 93395
  original_url: "https://www.suse.com/c/rancher_blog/how-to-manage-harvester-0-3-0-with-rancher-2-6-1-running-in-a-vm-within-harvester/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Harvester 0.3.0 and Rancher 2.6.1 specific"
  redirect_target: "/harvester"
---

What I liked about the release of Harvester 0.2.0 was the ease of enabling the embedded Rancher server, which allowed you to create Kubernetes clusters in the same Harvester cluster.

With the release of Harvester 0.3.0, this option was removed in favor of installing Rancher 2.6.1 separately and then importing your Harvester cluster into Rancher, where you could manage it. A Harvester node driver is provided with Rancher 2.6.1 to allow you to create Kubernetes clusters in the same Harvester 0.3.0 cluster.

I replicated my Harvester 0.2.0 plus the Rancher server experience using Harvester 0.3.0 and Rancher 2.6.1.

There's no upgrade path from Harvester 0.2.0 to 0.3.0, so the first step was reinstalling my Intel NUC with Harvester 0.3.0 following the docs at: <https://docs.harvesterhci.io/v0.3/install/iso-install/>.

Given that my previous Harvester 0.2.0 install included Rancher, I figured I'd install Rancher in a VM running on my newly installed Harvester 0.3.0 node - but which OS would I use? With Rancher being deployed using a single Docker container, I was looking for a small, [lightweight OS for the edge](https://www.suse.com/products/micro/) that included Docker. From past experience, I knew that openSUSE Leap had slimmed down images of its distribution available at <https://get.opensuse.org/leap/> - click the alternative downloads link immediately under the initial downloads. Known as Just enough OS (JeOS), these are available for both Leap and Tumbleweed (their rolling release). I opted for Leap, so I created an image using the URL for the OpenStack Cloud image (trust me - the KVM and XEN image hangs on boot).

![](https://media1-production-mightynetworks.imgix.net/asset/30164176/Screenshot_from_2021-10-20_16-48-14_edited.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max&impolicy=ResizeCrop&constraint=downsize&aspect=fit)

Knowing that I wanted to be able to access Rancher on the same network my Harvester node was attached to, I also enabled  Advanced | Settings | vlan (VLAN) and created a network using VLAN ID 1 (Advanced | Networks).

The next step is to install Rancher in a VM. While I could do this manually, I prefer automation and wanted to do something I could reliably repeat (something I did a lot while getting this working) and perhaps adapt when installing future versions. When creating a virtual machine, I was intrigued by the user data and network data sections in the advanced options tab, referenced in the docs at <https://docs.harvesterhci.io/v0.3/vm/create-vm/>, along with some basic examples. I knew from past experience that cloud-init could be used to initialize cloud instances, and with the openSUSE OpenStack Cloud images using cloud-init, I wondered if this could be used here. According to the examples in the cloud-init docs at <https://cloudinit.readthedocs.io/en/latest/topics/examples.html>, it can!

When creating the Rancher VM, I gave it 1 CPU with a 4-core NUC and Harvester 0.3.0 not supporting over-provisioning (it's a bug - phew!) - I had to be frugal! Through trial and error, I also found that the minimum memory required for Rancher to work is 3 GB. I chose my openSUSE Leap 15.3 JeOS OpenStack Cloud image on the volumes tab, and on the networks tab, I chose my custom (VLAN 1) network.

The real work is done on the advanced options tab. I already knew JeOS didn't include Docker, so that would need to be installed before I could launch the Docker container for Rancher. I also knew the keyboard wasn't set up for me in the UK, so I wanted to fix that too. Plus, I'd like a message to indicate it was ready to use. I came up with the following User Data:

```
password: changeme
packages:
  - docker
runcmd:
  - localectl set-keymap uk
  - systemctl enable --now docker
  - docker run --name=rancher -d --restart=unless-stopped -p 80:80 -p 443:443 --privileged rancher/rancher:v2.6.1
  - until curl -sk https://127.0.0.1 -o /dev/null; do sleep 30s; done
final_message: Rancher is ready!
```

Let me go through the above lines:

- Line 1 sets the password of the default **opensuse** user - you will be prompted to change this the first time you log in as this user, so don't set it to anything secret!
- Lines 2 & 3 install the docker package.
- Line 4 says we'll run some commands once it's booted the first time.
- Line 5 sets the UK keyboard.
- Line 6 enables and starts the Docker service.
- Line 7 pulls and runs the Docker container for Rancher 2.6.1 - this is the same line as the Harvester docs, except I've added "--name=rancher" to make it easier when you need to find the Bootstrap Password later.

  **NOTE:** When you create the VM, this line will be split into two lines with an additional preceding line with ">-" - it will look a bit different, but it's nothing to worry about!
- Line 8 is a loop checking for the Rancher server to become available - I test localhost, so it works regardless of the assigned IP address.
- Line 9 prints out a message saying it's finished (which happens after the previous loop completes).

An extra couple of lines will be automatically added when you click the create button but don't click it yet as we're not done!

This still left a problem with which IP address I use to access Rancher? With devices being assigned random IP addresses via DHCP, how do I control which address is used? Fortunately, the Network Data sections allow us to set a static address (and not have to mess with config files or run custom scripting within the VM):

```
network:
  version: 1
  config:
    - type: physical
      name: eth0
      subnets:
        - type: static
          address: 192.168.144.190/24
          gateway: 192.168.144.254
    - type: nameserver
      address:
        - 192.168.144.254
      search:
        - example.com
```

I won't go through all the lines above but will call out those you need to change for your own network:

- Line 8 sets the IP address to use with the CIDR netmask (/24 means 255.255.255.0).
- Line 9 sets the default gateway.
- Line 12 sets the default DNS nameserver.
- Line 14 sets the default DNS search domain.

See <https://cloudinit.readthedocs.io/en/latest/topics/network-config-format-v1.html#> for information on the other lines.

![](https://media1-production-mightynetworks.imgix.net/asset/30164166/Screenshot_from_2021-10-15_19-12-55_edited.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max&impolicy=ResizeCrop&constraint=downsize&aspect=fit)

Unless you unticked the start virtual machine on creation, your VM should start booting once you click the Create button. If you open the Web Console in VNC, you'll be able to keep an eye on the progress of your VM. When you see the message **Rancher is ready,**you can try accessing Rancher in a web browser at the IP address you specified above. Depending on the web browser you're using and its configuration, you may see warning messages about the self-signed certificate Rancher is using.

The first time you log in to Rancher, you will be prompted for the random bootstrap password which was generated. To get this, you can SSH as the **opensuse** user to your Rancher VM, then run:

```
sudo docker logs rancher 2>&1 | grep "Bootstrap Password:"
```

![](https://media1-production-mightynetworks.imgix.net/asset/30163503/Screenshot_from_2021-10-20_18-54-28.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max&impolicy=ResizeCrop&constraint=downsize&aspect=fit)

Copy the password and paste it into the password field of the Rancher login screen, then click the login with Local User button.

![](https://media1-production-mightynetworks.imgix.net/asset/30163562/Screenshot_from_2021-10-20_18-55-21.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max&impolicy=ResizeCrop&constraint=downsize&aspect=fit)

You're then prompted to set a password for the default admin user. Unless you can remember random strings or use a password manager, I'd set a specific password. You also need to agree to the terms and conditions for using Rancher!

Finally, you're logged into Rancher, but we're not entirely done yet as we need to add our Harvester cluster. To do this, click on the hamburger menu and then the Virtualization Management tab. Don't panic if you see a failed whale error - just try reloading.

![](https://media1-production-mightynetworks.imgix.net/asset/30164540/Screenshot_from_2021-10-20_19-00-30.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max&impolicy=ResizeCrop&constraint=downsize&aspect=fit)

Clicking the Import Existing button will give you some registration commands to run on one of your Harvester node(s).

![](https://media1-production-mightynetworks.imgix.net/asset/30164718/Screenshot_from_2021-10-20_19-00-57.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max&impolicy=ResizeCrop&constraint=downsize&aspect=fit)

To do this, SSH to your Harvester node as the **rancher** user and then run the first kubectl command prefixed with **sudo**. Unless you've changed your Harvester installation, you'll also need to run the curl command, again prefixing the kubectl command with **sudo**. The webpage should refresh, showing your Harvester cluster's management page. If you click the Harvester Cluster link or tab, your Harvester cluster should be listed. Clicking on your cluster name should show something familiar!

Finally, we need to activate the Harvester node driver by clicking the hamburger menu and then the Cluster Management tab. Click Drivers, then Node Drivers, find Harvester in the list, and click Activate.

Now we have Harvester 0.3.0 integrated with Rancher 2.6.1, running similarly to Harvester 0.2.0, although sacrificing 1 CPU (which will be less of an issue once the CPU over-provisioning bug is fixed) and 3GB RAM.

Admittedly, running Rancher within a VM in the same Harvester you're managing through Rancher doesn't seem like the best plan, and you wouldn't do it in production, but for the home lab, it's fine. Just remember not to chop off the branch you're standing on!
