Title: Thoughts on SSH Security
Date: 2008-10-03
Modified: 2012-12-22
Tags: vps, linux, howto, slicehost, ssh, ubuntu
Slug: thoughts-on-ssh-security

<a href="http://www.openssh.com/">OpenSSH</a> has a history of security. Only rarely are holes found in the actual program. It's much more likely that a system will be compromised through poor configuration of the SSH daemon. Ideally, an SSH config would allow only protocol 2 connections, allow only specified users to connect (and certainly not root), disable X11 forwarding, disable password authentication (forcing ssh keys instead), and allowing connections only from specified IPs. These config options would look like this:

    Protocol 2
    PermitRootLogin no
    AllowUsers demo
    X11Forwarding no
    PasswordAuthentication no

Allowing connections from only specified IP addresses would be accomplished by adding something like the following to `/etc/hosts.deny`:

    sshd: ALL # Deny all by default
    sshd: 192.168.1.0/255.255.255.0 # Allow this subnet
    sshd: 4.2.2.1 # Allow this IP

(You could also accomplish this with iptables, but I think editing the above file is simpler.)

But the last two options -- disabling password auth and allowing only certain IP addresses -- limits mobility. I constantly login to my <a href="http://pig-monkey.com/2008/06/09/a-move-to-slicehost/">slice</a> from multiple IPs, and I also need to login during travel when I may or may not have my key on me.

The main thing these two options protect against is a brute force attack. By allowing password logins from any IP, we give the attacker the ability to exploit the weakest part of SSH. This is where <a href="http://denyhosts.sourceforge.net/">DenyHosts</a> comes in.

DenyHosts is a python script which attempts to recognize and block brute force attacks. It has many attractive <a href="http://denyhosts.sourceforge.net/features.html">features</a> and is included in the default Ubuntu repositories.

    #!bash
    $ sudo aptitude install denyhosts

The config file is located at `/etc/denyhosts.conf`. It is very simply and readable. I recommend reading through it, but most of the default options are acceptable. If any changes are made, the daemon must be restarted:

    #!bash
    $ sudo /etc/init.d/denyhosts restart

Default Ports
-----------------

Many people also advocating changing SSH's default port to something other than 22 (more specifically, something over 1024, which won't be scanned by default by <a href="http://nmap.org/">nmap</a>). The argument in support of this is that many automated attack scripts look for SSH only on port 22. By changing the port, you save yourself the headache of dealing with script kiddies. Opponents to changing the port would argue that the annoyance of having to specify the port number whenever using `ssh` or `scp` outweighs the minute security benefits. It's a heated argument. I lean toward leaving SSH on the default port.
