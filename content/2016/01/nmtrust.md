Title: Using Network Trust
Date: 2016-01-31
Tags: linux, privacy

Work continues on [Spark](https://github.com/pigmonkey/spark), my [Arch Linux provisioning system](http://pig-monkey.com/2015/12/spark/). As the project has progressed, it has created some useful tools that I've spun off into their own projects. One of those is [nmtrust](https://github.com/pigmonkey/nmtrust).

The idea is simple. As laptop users, we frequently connect our machines to a variety of networks. Some of those networks we trust, others we don't. I trust my home and work networks because I administer both of them. I don't trust networks at cafes, hotels or airports, but sometimes I still want to use them. There are certain services I want to run when connected to trusted networks: mail syncing, [file syncing](https://git-annex.branchable.com/), [online backups](https://www.tarsnap.com/), [instant messaging](https://www.bitlbee.org/) and the like. I don't want to run these on untrusted networks, either out of concern over the potential leak of private information or simply to keep my network footprint small.

The solution is equally simple. I use [NetworkManager](https://wiki.gnome.org/Projects/NetworkManager) to manage networks. NetworkManager creates a profile for every network connection. Every profile is assigned a UUID. I can decide which networks I want to trust, lookup their UUID with `nmcli conn`, and put those strings into a file somewhere. I keep them in `/usr/local/etc/trusted_networks`.

`nmtrust` is a small shell script which gets the UUIDs of all the active connections from NetworkManager and compares them to those in the trusted network file. It returns a different exit code depending on what it finds: `0` if all connections are trusted, `3` if one or more connections are untrusted, and `4` if there are no active connections.

This makes it extremely easy to write a script that executes `nmtrust` and takes certain action based on the exit code. For example, you may have a network backup script `netbackup.sh` that is executed every hour by cron. However, you only want the script to run when you are connected to a network that you trust.

    #!/bin/sh

    # Execute nmtrust
    nmtrust

    # Execute backups if the current connection(s) are trusted.
    if [ $? -eq 0 ]; then
        netbackup.sh
    fi

On machines running [systemd](https://wiki.freedesktop.org/www/Software/systemd/), most of the things that you want to start and stop based on the network are probably described by units. `ttoggle` is another small shell script which uses `nmtrust` to start and stop these units. The units that should only be run on trusted networks are placed into another file. I keep them in `/usr/local/etc/trusted_units`. `ttoggle` executes `nmtrust` and starts or stops everything in the trusted unit file based on the result.

For example, I have a timer `mailsync.timer` that periodically sends and receives my mail. I only want to run this on trusted networks, so I place it in the trusted unit file. If `ttoggle` is executed when I'm connected to a trusted network, it will start the timer. If it is run when I'm on an untrusted network or offline, it will stop the timer, ensuring my machine makes no connection to my IMAP or SMTP servers.

These scripts are easy to use, but they really should be automated so that nobody has to think about them. Fortunately, NetworkManager provides a dispatcher framework that we can hook into. When installed, [the dispatcher](https://github.com/pigmonkey/nmtrust/blob/master/dispatcher/10trust) will execute `ttoggle` whenever a connection is activated or deactivated.

The result of all of this is that trusted units are automatically started whenever all active network connections are trusted. Any other time, the trusted units are stopped. I can connect to shady public wifi without worrying about network services that may compromise my privacy running in the background. I can connect to my normal networks without needing to remember to start mail syncing, backups, etc.

All of this is baked in to Spark, but it's really just two short shell scripts and a NetworkManager dispatcher. It provides a flexible framework to help preserve privacy that is fairly easy to use. If you use NetworkManager, [try it out](https://github.com/pigmonkey/nmtrust).
