Title: Spark: Arch Linux Provisioning with Ansible
Date: 2015-12-13
Tags: linux

[Arch](https://www.archlinux.org/) has been my Linux distribution of choice for the past 5 years or so. It's a fairly simple and versatile distribution that leaves most choices up the user, and then gets out of your way. Although I think it makes for a better end experience, [the Arch Way](https://wiki.archlinux.org/index.php/Arch_Linux#Principles) does mean that it takes a bit more time to get a working desktop environment up and running.

At work I use [Ansible](http://www.ansible.com/) to automate the provisioning of [FreeBSD](https://www.freebsd.org/) servers. It makes life easier by not only automating the provisioning of machines, but also by serving as reference documentation for The One True Way&trade;. After a short time using Ansible to build servers, the idea of creating an Ansible playbook to provision my Arch desktop became attractive: I could pop a new drive into a machine, perform a basic Arch install, run the Ansible playbook and, in a very short period of time, have a fresh working environment -- all without needing to worry about recalling arcane system configuration or which obscure packages I want installed. I found a few projects out there that had this same goal, but none that did things in the way I wanted them done. So I built my own.

[Spark](https://github.com/pigmonkey/spark) is an Ansible playbook meant to provision a personal machine running Arch Linux. It is intended to run locally on a fresh Arch install (ie, taking the place of any [post-installation](https://wiki.archlinux.org/index.php/Installation_guide#Post-installation)), but due to Ansible's idempotent nature it may also be run on top of an already configured machine.

My machine is a Thinkpad, so Spark includes some tasks which are specific to laptops in general and others which only apply to Thinkpads. These tasks are tagged and isolated into their own roles, making it easy to use Spark to build desktops on other hardware. A community-contributed Macbook role exists to support Apple hardware. In fact, everything is tagged, and most of the user-specific stuff is accomplished with [variables](https://github.com/pigmonkey/spark/blob/master/group_vars/all). The idea being that if you agree with my basic assumptions about what a desktop environment should be, you can use Spark to build your machine without editing much outside of the variables and perhaps the playbook.

The roles gather tasks into logical groups, and the tasks themselves are fairly simple. A quick skim through the repository will provide an understanding of everything Spark will do a matter of minutes. Basically: a simple [i3](http://i3wm.org/) desktop environment, with GUI programs limited to web browsers and a few media and office applications (like [GIMP](http://www.gimp.org/) and [LibreOffice](https://www.libreoffice.org/)), everything else in the terminal, most network applications [jailed](http://pig-monkey.com/2015/08/firejail/) with [Firejail](https://l3net.wordpress.com/projects/firejail/), and all the annoying laptop tasks like lid closure events and battery management automated away. If you're familiar with my [dotfiles](https://github.com/pigmonkey/dotfiles), there won't be any surprises.

Included in Spark is a [file which describes how I install Arch](https://github.com/pigmonkey/spark/blob/master/INSTALL.md). It is extremely brief, but provides everything needed to perform a basic installation -- including full disk encryption *with* encrypted `/boot` -- which can then be filled out with Ansible. I literally copy/paste from the doc when installing Arch. It takes about 15 minutes to complete the installation. Running Ansible after that takes about an hour, but requires no interaction after entering a passphrase for the SSH key used to clone the dotfiles. Combined with [backups](http://pig-monkey.com/tag/backups/) of the data in my home dir, this allows me to go from zero to hero in less than a couple hours without needing to really think about it.

If you use Arch, fork the repository and try it out.