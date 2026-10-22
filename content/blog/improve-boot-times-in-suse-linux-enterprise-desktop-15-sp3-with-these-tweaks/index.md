---
title: "Improve Boot Times in SUSE Linux Enterprise Desktop 15 SP3 with These Tweaks"
date: 2021-12-15T19:43:07
slug: "improve-boot-times-in-suse-linux-enterprise-desktop-15-sp3-with-these-tweaks"
author: "SUSE"
products: ["Other"]
tags: ["installation"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 93056
  original_url: "https://www.suse.com/c/rancher_blog/improve-boot-times-in-suse-linux-enterprise-desktop-15-sp3-with-these-tweaks/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "SLED 15 SP3 boot tweaks off topic"
  redirect_target: "suse.com"
---

So, you have a nice fresh install of SUSE Linux Enterprise Desktop but wonder about slow startup issues. Some may be transient, such as purging kernels, updating man pages, or the rpm database. Some may be BIOS related and some may just be your hardware, but in any case, still noticed at every boot.I'm a command-line junkie, but I will also delve into the awesome tool YaST to perform some tasks; however, there will be command-line actions needed!

In this blog, I hope to show you how to check your hardware setup, investigate systemd startup times, and network configuration tweaks for ipv4. Lastly, help you decide if these tweaks can be used for your end-use case.

## Analyzing the Initial Boot

Start by opening a terminal session; either use activities and search for **gnome-terminal** or press alt+F2 and run **gnome-terminal** from there.

Run the command **systemd-analyze** in the terminal to get a summary of the system boot time:

```
systemd-analyze

Startup finished in 4.732s (firmware) + 8.048s (loader) + 3.584s (kernel) + 3.170s (initrd) + 31.312s (userspace) = 50.847sgraphical.target reached after 31.293s in userspace
```

This system took 50 odd seconds from cold boot to the userspace (in my case, graphical target - GNOME on Wayland). I normally reboot to ensure anything transient is resolved (kernel purge, man DB update, etc) and re-run the **systemd-analyze** command.

```
systemd-analyze

Startup finished in 4.477s (firmware) + 7.963s (loader) + 3.554s (kernel) + 3.258s (initrd) + 31.249s (userspace) = 50.504s graphical.target reached after 31.232s in userspace
```

As seen in both outputs, the boot times from **systemd-analyze** are consistent, so let's have a closer look.

We should look at an additional summary of blame and critical-chain options for reference going forward.

I only check the top 10 to start with; if you want to see the full list, just skip the piping through **| head -n 10** part.

```
systemd-analyze blame | head -n 10

21.112s plymouth-quit-wait.service
 4.706s NetworkManager-wait-online.service
 2.592s lvm2-monitor.service
 1.753s dracut-initqueue.service
 1.418s postfix.service
 1.305s kdump-early.service
 1.130s firewalld.service
  955ms kdump.service
  939ms sshd.service
  933ms apparmor.service

systemd-analyze critical-chain

The time when unit became active or started is printed after the "@" character.
The time the unit took to start is printed after the "+" character.

graphical.target @31.293s
└─multi-user.target @31.293s
  └─getty.target @31.292s
    └─getty@tty1.service @31.291s
      └─plymouth-quit-wait.service @10.174s +21.112s
        └─systemd-user-sessions.service @10.158s +9ms
          └─remote-fs.target @10.156s
            └─iscsi.service @10.124s +31ms
              └─network-online.target @10.122s
                └─NetworkManager-wait-online.service @5.414s +4.706s
                  └─NetworkManager.service @5.357s +53ms
                    └─network-pre.target @5.354s
                      └─firewalld.service @4.222s +1.130s
                        └─polkit.service @4.030s +186ms
                          └─basic.target @4.004s
                            └─sockets.target @4.004s
                              └─pcscd.socket @4.004s
                                └─sysinit.target @4.001s
                                  └─apparmor.service @3.068s +933ms
                                    └─var.mount @3.048s +18ms
                                      └─local-fs-pre.target @3.026s
                                        └─lvm2-monitor.service @432ms +2.592s
                                          └─dm-event.socket @419ms
                                            └─-.mount
                                              └─system.slice
                                                └─-.slice
```

## Breaking Down the Boot Times

In the initial output on my system, there are times for *firmware*, *loader*, *kernel*, *initrd,* and *userspace*. Let's look at these:

### Firmware

My experience has shown that changing some of the BIOS boot settings can make a difference. All I can suggest is inspecting your system BIOS and disabling items not being used. To give an example, for this blog, I have Secure Boot disabled, TPM disabled, and network boot. I have removed the DVD drive that came with the system, and have an empty HDD caddy installed, so the BIOS option to boot from CDROM is disabled. Likewise, I disabled any POST Hotkey delay.

Since I installed it from USB and don't need this option anymore, let's reboot the system and disable the USB boot option in the BIOS to see if it's made a difference.

I have also set the login to the desktop as auto for this setup configuration. It will be rebooting, and the login screen adds additional time depending on your login method.

I rebooted after tweaking the BIOS settings and had an initial time of *4.732s* and *4.477s*, respectively. After disabling the USB Boot option, it was 4.819s, so no real improvement for me... .

### Loader (AKA Grub)

For the GRUB Boot Screen, we can improve by reducing the delay, which is set at eight seconds by default.

So we see an initial time of *8.048s* and *7.963s*, respectively, so let's fire up YaST Bootloader and make some changes. Now by default, the overall YaST GUI is not visible, so what I do is copy the desktop file to my user directory via:

```
cp /usr/share/applications/org.opensuse.YaST.desktop ~/.local/share/applications/
```

You can now search for YaST (and add to Favorites if needed), start YaST, highlight System and select Boot Loader in the right-hand panel:

![page4image31721712](https://media1-production-mightynetworks.imgix.net/asset/31940721/1638556984036.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max&impolicy=ResizeCrop&constraint=downsize&aspect=fit)

Now select the 'Boolader Options' tab. If the system is a single boot, uncheck the 'Probe Foreign OS' and reduce the Timeout seconds to 1.

![](https://media1-production-mightynetworks.imgix.net/asset/31942356/YaST_figure2.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max&impolicy=ResizeCrop&constraint=downsize&aspect=fit)

Press 'OK' and reboot the system to see the effect by running the**systemd-analyze** command:

```
Startup finished in 4.603s (firmware) + 1.651s (loader) + 3.581s (kernel) + 3.206s (initrd) + 31.275s (userspace) = 44.318sgraphical.target reached after 31.259s in userspace
```

The loader time is now down to *1.651s*, an approximate 6-second improvement. You can still select a boot option by pressing any key to stop the Grub counter if you wish to select an option.

You can also switch to just the text GRUB via unchecking the option from the Kernel Parameters tab *Graphical Console.*

![page5image31777104](https://media1-production-mightynetworks.imgix.net/asset/31940722/1638556984211.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max&impolicy=ResizeCrop&constraint=downsize&aspect=fit)

```
Startup finished in 4.453s (firmware) + 1.427s (loader) + 3.538s (kernel) + 3.188s (initrd) + 31.334s (userspace) = 43.941s graphical.target reached after 31.314s in userspace
```

### Kernel and Initrd

This part is very subjective depending on your needs; in my case, I cut out numerous modules that are not needed for my use case, but I think you will find that a number is not needed.

The first step is to open a terminal, switch to root user, and check mkinitrd output...

```
su -
Password:

mkinitrd
```

We are interested in this part of the output at the beginning:

```
dracut: dracut module 'dmraid' will not be installed, because command 'dmraid' could not be found!
dracut: dracut module 'nvmf' will not be installed, because command 'nvme' could not be found!
dracut: dracut module 'biosdevname' will not be installed, because command 'biosdevname' could not be found!
dracut: dracut module 'dmraid' will not be installed, because command 'dmraid' could not be found!
dracut: dracut module 'nvmf' will not be installed, because command 'nvme' could not be found!
```

We will use a dracut configuration file to modify these options, so fire up your favorite editor as your user and create a file called **01-yourhostname.conf -***my hostname is ernie so I called mine 01-ernie.conf.*

In this file we want the following:

```
hostonly="yes"
compress="cat"

omit_dracutmodules+=" dmraid nvmf biosdevname cdrom pollcdrom wacom selinux "

omit_drivers+=" wacom parport pcmcia cdrom serial pcspkr "
```

I have also omitted some others since I don't have hardware present on this laptop, serial wacom etc, likewise no selinux. Save the file and let's switch to the root user terminal session and copy to the required location:

```
cp /home/username/01-ernie.conf /etc/dracut.conf.d/

ls /etc/dracut.conf.d/
01-ernie.conf
```

Now, still as root users we need to rebuild initrd with the **mkinitrd** command:

```
mkinitrd

Creating initrd: /boot/initrd-5.3.18-59.27-default
dracut: Executing: /usr/bin/dracut --logfile /var/log/YaST2/mkinitrd.log --force /boot/initrd-5.3.18-59.27-default 5.3.18-59.27-default
dracut: dracut module 'dmraid' will not be installed, because it's in the list to be omitted!
dracut: dracut module 'nvmf' will not be installed, because it's in the list to be omitted!
dracut: dracut module 'biosdevname' will not be installed, because it's in the list to be omitted!
dracut: dracut module 'pollcdrom' will not be installed, because it's in the list to be omitted!
dracut: dracut module 'selinux' will not be installed, because it's in the list to be omitted!
Creating initrd: /boot/initrd-5.3.18-59.27-default
.....
dracut: *** Creating initramfs image file '/boot/initrd-5.3.18-59.27-default' done ***
ernie:~ #  exit
```

Reboot your system and again check the **systemd-analyze** output:

```
systemd-analyze
Startup finished in 4.598s (firmware) + 1.592s (loader) + 1.717s (kernel) + 3.141s (initrd) + 30.196s (userspace) = 41.245s
graphical.target reached after 30.180s in userspace
```

Another second or so saved, 1.717s (kernel) + 3.141s (initrd).

Now there are a couple more things I do. I remove plymouth and I don't use ipv6, so I also disable this. There is one thing you do need to do concerning the postfix configuration if only using ipv4.

This is so we can edit our 01-hostname.conf file and add plymouth and ipv6 to the list of modules to omit (omit\_dracutmodules).

Open a terminal and again switch to root user and copy the updated file over (tip once root user can use the up key to repeat the cp command):

```
su -
Password:
cp /home/username/01-ernie.conf /etc/dracut.conf.d/
```

Now, pause a moment as we will be running some additional commands for postfix and removal of plymouth (I use vi for this):

```
vi /etc/postfix/main.cf
```

{hit the / to search in vi and type in inet\_protocol and press i to insert} replace all with ipv4 press shift :wq to write and quit vi.

Fire up YaST -> System -> Network Settings and under the Global Options tab and under **IPv6 Protocol Settings**, uncheck the Enable IPv6 box, press ok, and say ok to the warning about a reboot required.

![page8image31838272](https://media1-production-mightynetworks.imgix.net/asset/31942708/1638560270825.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max&impolicy=ResizeCrop&constraint=downsize&aspect=fit)

This setting is in /etc/sysctl.d/70-yast.conf and changes net.ipv6.conf.all.disable\_ipv6 = 0 to 1.

Remove plymouth (plymouth and libply files):

```
zypper rm libply* ply*
Reading installed packages...
Resolving package dependencies...

The following 11 packages are going to be REMOVED:
  libply-boot-client5 libply-splash-core5 libply-splash-graphics5 libply5 plymouth plymouth-branding-SLE plymouth-dracut plymouth-plugin-label plymouth-plugin-label-ft plymouth-plugin-script
  plymouth-scripts

11 packages to remove.
After the operation, 827.0 KiB will be freed.
Continue? [y/n/v/...? shows all options] (y):y
.....
```

Add locks so they don't get reinstalled:

```
zypper al libply* ply*

Specified locks have been successfully added.

zypper ll

# | Name    | Type    | Repository | Comment
--+---------+---------+------------+--------
1 | libply* | package | (any)      |
2 | ply*    | package | (any)      |
```

Now let's rebuild initrd and reboot to see the check the changes:

```
Startup finished in 4.439s (firmware) + 1.440s (loader) + 1.648s (kernel) + 2.900s (initrd) + 10.317s (userspace) = 20.746s 
graphical.target reached after 10.304s in userspace
```

A .5-second speed up with the initrd, but notice the userspace time, a ten-second improvement!

Let's quickly review the current blame output:

```
systemd-analyze blame | head -n 10

4.671s NetworkManager-wait-online.service
1.649s dracut-initqueue.service
1.613s apparmor.service
1.430s postfix.service
1.291s kdump-early.service
1.152s firewalld.service
1.106s sshd.service
1.095s lvm2-monitor.service
 936ms kdump.service
 863ms display-manager.service
```

The original **21.112s plymouth-quit-wait.service** has gone.

One more thing is the NetworkManager waits for online service, so let's tweak that as well open a terminal session and switch to root user:

```
su -
Password:
vi /etc/sysconfig/network/config
```

We want to change the following entries:

1. WAIT\_FOR\_INTERFACES="1" from 30

2. NM\_ONLINE\_TIMEOUT="0"

```
systemd-analyze 
Startup finished in 4.422s (firmware) + 1.443s (loader) + 1.619s (kernel) + 2.940s (initrd) + 7.709s (userspace) = 18.136s 
graphical.target reached after 7.691s in userspace
```

```
systemd-analyze blame | head -n 10
2.531s display-manager.service
2.081s postfix.service
1.926s systemd-localed.service
1.921s sshd.service
1.797s kdump.service
1.742s apparmor.service
1.714s dracut-initqueue.service
1.223s kdump-early.service
1.173s lvm2-monitor.service
1.073s firewalld.service
```

The wait dropped to 13ms! **13ms NetworkManager-wait-online.service** has now reduced the time to 18 odd seconds from the original 50.

### Userspace

In another subjective section, we can analyze the *critical-chain* output:

```
systemd-analyze critical-chain 
The time when unit became active or started is printed after the "@" character.
The time the unit took to start is printed after the "+" character.

graphical.target @6.666s
└─display-manager.service @5.067s +1.598s
  └─time-sync.target @5.062s
    └─chronyd.service @4.832s +229ms
      └─network.target @4.826s
        └─NetworkManager.service @4.763s +62ms
          └─network-pre.target @4.761s
            └─firewalld.service @3.619s +1.141s
              └─polkit.service @3.463s +151ms
                └─basic.target @3.445s
                  └─sockets.target @3.445s
                    └─pcscd.socket @3.445s
                      └─sysinit.target @3.443s
                        └─apparmor.service @2.123s +1.319s
                          └─var.mount @2.075s +46ms
                            └─local-fs-pre.target @2.046s
                              └─lvm2-monitor.service @435ms +1.610s
                                └─dm-event.socket @421ms
                                  └─system.slice
                                    └─-.slice
```

I see the likes of pcscd, lvm2, and dm-event. I use neither a card reader nor lvm on my system, so I'm going to either remove the relevant packages or disable and mask the service. From the root user terminal session run:

```
zypper se -i pcsc
Loading repository data...
Reading installed packages...

S | Name         | Summary                   | Type
--+--------------+---------------------------+--------
i | libpcsclite1 | PC/SC Smart Card Library  | package
i | pcsc-lite    | PC/SC Smart Cards Library | package
```

Can we remove it?

```
zypper rm pcsc-lite libpcsclite1

The following 23 packages are going to be REMOVED:
NetworkManager-openconnect NetworkManager-openconnect-gnome NetworkManager-openconnect-lang apache-commons-logging flute java-11-openjdk java-11-openjdk-headless libbase libfonts libformula
liblayout libloader libpcsclite1 libreoffice-base librepository libserializer openconnect openconnect-lang pcsc-lite pentaho-libxml pentaho-reporting-flow-engine sac xml-commons-apis
```

Let's not, we can just disable and mask the service as follows:

```
systemctl status pcscd.socket pcscd.service
● pcscd.socket - PC/SC Smart Card Daemon Activation Socket
     Loaded: loaded (/usr/lib/systemd/system/pcscd.socket; enabled; vendor preset: enabled)
     Active: active (listening) since Thu 2021-11-04 07:27:44 CDT; 1h 1min ago
   Triggers: ● pcscd.service
     Listen: /run/pcscd/pcscd.comm (Stream)
     CGroup: /system.slice/pcscd.socket

Nov 04 07:27:44 ernie systemd[1]: Listening on PC/SC Smart Card Daemon Activation Socket.

● pcscd.service - PC/SC Smart Card Daemon
     Loaded: loaded (/usr/lib/systemd/system/pcscd.service; indirect; vendor preset: disabled)
     Active: inactive (dead)
TriggeredBy: ● pcscd.socket
       Docs: man:pcscd(8)

       Docs: man:pcscd(8)

systemctl stop pcscd.socket pcscd.service

systemctl disable pcscd.socket pcscd.service
Removed /etc/systemd/system/sockets.target.wants/pcscd.socket.

systemctl mask pcscd.socket pcscd.service
Created symlink /etc/systemd/system/pcscd.socket → /dev/null.
Created symlink /etc/systemd/system/pcscd.service → /dev/null.
```

Yet another reboot and inspect the critical-chain output:

```
systemd-analyze critical-chain

graphical.target @6.378s
└─display-manager.service @4.680s +1.697s
  └─time-sync.target @4.674s
    └─chronyd.service @4.564s +110ms
      └─network.target @4.557s
        └─NetworkManager.service @4.496s +59ms
          └─network-pre.target @4.494s
            └─firewalld.service @3.423s +1.070s
              └─polkit.service @3.259s +160ms
                └─basic.target @3.241s
                  └─sockets.target @3.241s
                    └─iscsid.socket @3.241s
                      └─sysinit.target @3.239s
                        └─apparmor.service @1.698s +1.541s
                          └─var.mount @1.618s +77ms
                            └─local-fs-pre.target @1.598s
                              └─lvm2-monitor.service @419ms +1.178s
                                └─dm-event.socket @407ms
                                  └─system.slice
                                    └─-.slice
```

Let's now look at removing lvm2:

```
zypper se -i lvm2

  | liblvm2cmd2_03     | LVM2 command line library    | package
  | lvm2               | Logical Volume Manager Tools | package

zypper rm lvm2  liblvm2cmd2_03

The following 2 packages are going to be REMOVED:
  liblvm2cmd2_03 lvm2

2 packages to remove.
After the operation, 5.7 MiB will be freed.
Continue? [y/n/v/...? shows all options] (y): 
(1/2) Removing lvm2-2.03.05-8.36.1.x86_64 ......................................................................................................................................................[done]
Additional rpm output:
Removed /etc/systemd/system/sysinit.target.wants/lvm2-monitor.service.
Removed /etc/systemd/system/sysinit.target.wants/lvm2-lvmpolld.socket.
rm: cannot remove '/var/lib/systemd/migrated/lvm2-lvmpolld': No such file or directory
rm: cannot remove '/var/lib/systemd/migrated/lvm2-lvmpolld': No such file or directory
rm: cannot remove '/var/lib/systemd/migrated/blk-availability': No such file or directory
rm: cannot remove '/var/lib/systemd/migrated/lvm2-monitor': No such file or directory

(2/2) Removing liblvm2cmd2_03-2.03.05-8.36.1.x86_64 ............................................................................................................................................[done]

zypper al liblvm2cmd2_03 lvm2

Specified locks have been successfully added.
```

All looking good, so reboot and check:

```
systemd-analyze critical-chain

graphical.target @6.234s
└─multi-user.target @6.234s
  └─cron.service @6.233s
    └─postfix.service @4.523s +1.708s
      └─time-sync.target @4.513s
        └─chronyd.service @4.279s +233ms
          └─network.target @4.273s
            └─NetworkManager.service @4.210s +62ms
              └─network-pre.target @4.208s
                └─firewalld.service @3.084s +1.122s
                  └─polkit.service @2.879s +200ms
                    └─basic.target @2.854s
                      └─sockets.target @2.854s
                        └─iscsid.socket @2.854s
                          └─sysinit.target @2.851s
                            └─systemd-backlight@backlight:amdgpu_bl0.service @3.282s +30ms
                              └─system-systemd\x2dbacklight.slice @3.280s
                                └─system.slice
                                  └─-.slice
```

I see there is an iscsi entry now; again I don't use this, so we can remove it:

```
zypper se -i iscsi
Loading repository data...
Reading installed packages...

S | Name                 | Summary                                   | Type
--+----------------------+-------------------------------------------+--------
i | iscsiuio             | Linux Broadcom NetXtremem II iscsi server | package
i | libopeniscsiusr0_2_0 | The iSCSI User-level Library              | package
i | open-iscsi           | Linux iSCSI Software Initiator            | package
i | yast2-iscsi-client   | YaST2 - iSCSI Client Configuration        | package

zypper rm iscsiuio libopeniscsiusr0_2_0  open-iscsi  yast2-iscsi-client

The following 4 packages are going to be REMOVED:
  iscsiuio libopeniscsiusr0_2_0 open-iscsi yast2-iscsi-client

4 packages to remove.
After the operation, 2.5 MiB will be freed.
Continue? [y/n/v/...? shows all options] (y):

zypper al iscsiuio libopeniscsiusr0_2_0  open-iscsi  yast2-iscsi-client
```

I also added **iscsi lvm mdraid dm dmraid** to omit modules and **iscsi\_if iscsi\_tcp** to **omit\_drivers** in my **01-ernie.conf** dracut conf file at this point as well.

Now, during boot, I also saw a warning appear with acpi backlight, but this system uses s**ystemd- backlight@backlight:amdgpu\_bl0.service** so can also look at disabling, note two services since have two GPUs....

```
journalctl -b | grep backlight

Nov 04 08:36:33 ernie systemd[1]: Created slice Slice /system/systemd-backlight.
Nov 04 08:36:33 ernie systemd[1]: Starting Load/Save Screen Backlight Brightness of backlight:amdgpu_bl0...
Nov 04 08:36:33 ernie systemd[1]: Starting Load/Save Screen Backlight Brightness of backlight:acpi_video0...
Nov 04 08:36:33 ernie systemd[1]: Starting Load/Save Screen Backlight Brightness of backlight:acpi_video1...
Nov 04 08:36:33 ernie systemd-backlight[1389]: Failed to get backlight or LED device 'backlight:acpi_video1': No such device
Nov 04 08:36:33 ernie systemd[1]: systemd-backlight@backlight:acpi_video1.service: Main process exited, code=exited, status=1/FAILURE
Nov 04 08:36:33 ernie systemd[1]: systemd-backlight@backlight:acpi_video1.service: Failed with result 'exit-code'.
Nov 04 08:36:33 ernie systemd[1]: Failed to start Load/Save Screen Backlight Brightness of backlight:acpi_video1.
Nov 04 08:36:33 ernie systemd-backlight[1384]: Failed to get backlight or LED device 'backlight:acpi_video0': No such device
Nov 04 08:36:33 ernie systemd[1]: Finished Load/Save Screen Backlight Brightness of backlight:amdgpu_bl0.
Nov 04 08:36:33 ernie systemd[1]: systemd-backlight@backlight:acpi_video0.service: Main process exited, code=exited, status=1/FAILURE
Nov 04 08:36:33 ernie systemd[1]: systemd-backlight@backlight:acpi_video0.service: Failed with result 'exit-code'.
Nov 04 08:36:33 ernie systemd[1]: Failed to start Load/Save Screen Backlight Brightness of backlight:acpi_video0.
```

We can use systemctl to check, disable and mask:

```
systemctl status systemd-backlight@backlight:acpi_video0.service
● systemd-backlight@backlight:acpi_video0.service - Load/Save Screen Backlight Brightness of backlight:acpi_video0
     Loaded: loaded (/usr/lib/systemd/system/systemd-backlight@.service; static)
     Active: failed (Result: exit-code) since Thu 2021-11-04 08:36:33 CDT; 15min ago
       Docs: man:systemd-backlight@.service(8)
   Main PID: 1384 (code=exited, status=1/FAILURE)

systemctl status systemd-backlight@backlight:acpi_video1.service
● systemd-backlight@backlight:acpi_video1.service - Load/Save Screen Backlight Brightness of backlight:acpi_video1
     Loaded: loaded (/usr/lib/systemd/system/systemd-backlight@.service; static)
     Active: failed (Result: exit-code) since Thu 2021-11-04 08:53:36 CDT; 38s ago
       Docs: man:systemd-backlight@.service(8)
    Process: 1355 ExecStart=/usr/lib/systemd/systemd-backlight load backlight:acpi_video1 (code=exited, status=1/FAILURE)
   Main PID: 1355 (code=exited, status=1/FAILURE)

Nov 04 08:53:36 ernie systemd[1]: Starting Load/Save Screen Backlight Brightness of backlight:acpi_video1...
Nov 04 08:53:36 ernie systemd-backlight[1355]: Failed to get backlight or LED device 'backlight:acpi_video1': No such device
Nov 04 08:53:36 ernie systemd[1]: systemd-backlight@backlight:acpi_video1.service: Main process exited, code=exited, status=1/FAILURE
Nov 04 08:53:36 ernie systemd[1]: systemd-backlight@backlight:acpi_video1.service: Failed with result 'exit-code'.
Nov 04 08:53:36 ernie systemd[1]: Failed to start Load/Save Screen Backlight Brightness of backlight:acpi_video1.
Nov 04 08:36:33 ernie systemd[1]: Starting Load/Save Screen Backlight Brightness of backlight:acpi_video0...
Nov 04 08:36:33 ernie systemd-backlight[1384]: Failed to get backlight or LED device 'backlight:acpi_video0': No such device
Nov 04 08:36:33 ernie systemd[1]: systemd-backlight@backlight:acpi_video0.service: Main process exited, code=exited, status=1/FAILURE
Nov 04 08:36:33 ernie systemd[1]: systemd-backlight@backlight:acpi_video0.service: Failed with result 'exit-code'.
Nov 04 08:36:33 ernie systemd[1]: Failed to start Load/Save Screen Backlight Brightness of backlight:acpi_video0.

systemctl stop systemd-backlight@backlight:acpi_video0.service

systemctl disable systemd-backlight@backlight:acpi_video0.service

systemctl mask systemd-backlight@backlight:acpi_video0.service
Created symlink /etc/systemd/system/systemd-backlight@backlight:acpi_video0.service → /dev/null.

systemctl stop systemd-backlight@backlight:acpi_video1.service

systemctl disable systemd-backlight@backlight:acpi_video1.service

systemctl mask systemd-backlight@backlight:acpi_video1.service
Created symlink /etc/systemd/system/systemd-backlight@backlight:acpi_video1.service → /dev/null.
```

After a reboot, the warnings have gone, from boot to the desktop in around 15 seconds.

## Summary

In closing, I hope you have successfully tweaked your system and have improved the boot speed.

I started with:

```
Startup finished in 4.477s (firmware) + 7.963s (loader) + 3.554s (kernel) + 3.258s (initrd) + 31.249s (userspace) = 50.504s
```

I finished with:

```
Startup finished in 2.390s (firmware) + 1.437s (loader) + 1.635s (kernel) + 3.044s (initrd) + 6.045s (userspace) = 14.553s
```

This was approximately a 36-second improvement, with around 25 of those seconds in userspace.

You may also be interested in YaST -> System -> Services Manager to peruse all the systemd services running and status as there may be others you wish to disable and/or mask.

![page17image31722752](https://media1-production-mightynetworks.imgix.net/asset/31942709/1638560271025.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max&impolicy=ResizeCrop&constraint=downsize&aspect=fit)

*Only for advanced users:* As a test, you can consider setting the option to zero and hide grub, but I would suggest the 1-second delay until you're sure after a few update cycles (especially kernel updates) that nothing unfavorable may occur. This reduced the loader time from 1.4 seconds to 370ms, and the overall warm boot time of 13.390s.

My cold boot time after all the tweaks is:

```
Startup finished in 3.048s (firmware) + 382ms (loader) + 1.632s (kernel) + 2.990s (initrd) + 6.048s (userspace) = 14.103s
```

If I also time the boot by pressing the power button on, it's around 20 seconds. Enjoy and remember to have fun!

### Laptop Hardware Summary

**HP Pavilion Notebook 15-aw057nr born 03/29/2017, BIOS F32A 04/25/2019**

**Boot**: UEFI (Secure boot and TPM disabled)

**CPU**: AMD A10-9600P RADEON R5, 10 COMPUTE CORES 4C+6G

**GPU 1**: [AMD/ATI] Wani [Radeon R5/R6/R7 Graphics]

**GPU 2**: [AMD/ATI] Topaz XT [Radeon R7 M260/M265/M340/M360/M440/M445/530/535/620/625 Mobile]

**RAM**: 12GB Samsung M471A1K43CB1-CRC @ 1866MT/s 

**HDD**: WDC WDS250G2B0A-00SM50 SATA 3.3, 6.0 Gb/s SSD

#### **Want to make sure you don't miss any of the action?**[**Join the SUSE & Rancher Community**](https://community.suse.com/sign_up?space_id=3669174&from=https%3A%2F%2Fcommunity.suse.com%2Ffeed%3Fautojoin%3D1%26autojoin_space_id%3D3669174)**to get updates on new content coming your way!**
