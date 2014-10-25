Title: An Ubuntu VPS on Slicehost: Mail
Date: 2008-06-10
Modified: 2012-12-22
Tags: vps, postfix, linux, howto, slicehost, ubuntu, google apps
Slug: an-ubuntu-vps-on-slicehost-mail

<em>As <a href="http://pig-monkey.com/2008/06/09/a-move-to-slicehost/">mentioned previously</a>, I've recently moved this domain over to <a href="http://www.slicehost.com/">Slicehost</a>. What follows is Part Three of a guide, compiled from my notes, to setting up an Ubuntu Hardy VPS. See also <a href="http://pig-monkey.com/2008/06/10/an-ubuntu-vps-on-slicehost-basic-setup">Part One</a>, <a href="http://pig-monkey.com/2008/06/10/an-ubuntu-vps-on-slicehost-web-server">Part Two</a>, and <a href="http://pig-monkey.com/2008/06/10/an-ubuntu-vps-on-slicehost-wordpress">Part Four</a>.</em>

Last week I <a href="http://pig-monkey.com/2008/06/09/google-apps/">moved this domain's email to Google Apps</a>. Slicehost has <a href="http://articles.slicehost.com/2007/10/25/creating-mx-records-for-google-apps">a guide to creating MX records for Google Apps</a>. I have a couple other domains with Google Apps, along with a couple domains hosted locally with addresses that simply forward to my primary, Google hosted, email. I also need to send mail from the server. To accomplish all of this, I use <a href="http://www.postfix.org/">Postfix</a>.

<!--more-->

Installing Postfix is a simple matter. Telnet is used quite a bit for testing, so I install that too:

    #!bash
    $ sudo aptitude install postfix telnet mailutils

The Postfix setup will ask how it should be installed -- we want the "Internet Site" option -- and then ask you for your fully qualified domain name.

Done? Let's make sure Postfix is running:

    #!bash
    $ telnet localhost 25

If it's working Postfix should return:


    Trying 127.0.0.1...
    Connected to localhost.
    Escape character is '^]'.
    220 localhost ESMTP Postfix (Ubuntu)

Let's send a test message from root to the user account <code>user</code> (replace that with whatever your standard user is):

    ehlo localhost
    mail from: root@localhost
    rcpt to: user@localhost
    data
    Subject: Test
    Hi, is this thing on?
    .
    quit 

Now, check your email as `user` by running `mail`. See the message? Good.

Open `/etc/postfix/main.cf` to make sure that Postfix knows what domains it's receiving mail for. To do this, edit the `mydestination` variable to include all the proper domains. For me, the name of my server looks like server.mydomain.com. I want Postfix to accept mail for that domain, but not for mydomain.com (since that's being handled by Google Apps), so mine looks like:

    mydestination = server.mydomain.com, localhost.mydomain.com , localhost

Restart Postfix if you made any changes:

    #!bash
    $ sudo /etc/init.d/postfix restart

Right. Now let's send another test. Notice this time we're using full domain names, instead of localhost:

    #!bash
    $ telnet server.mydomain.com 25

    ehlo server.mydomain.com
    mail from: root@server.mydomain.com
    rcpt to: user@server.mydomain.com
    data
    Subject: domains!
    woot... I think this works.
    .
    quit

Working? Good.

Let's test from the outside. The first step is to open up the correct ports in the firewall. Assuming you have iptables configured in the way the <a href="http://articles.slicehost.com/2007/11/6/ubuntu-gutsy-setup-page-1">Slicehost article suggests</a>, open up your `/etc/iptables.test.rules` and add the following:

    # Allow mail server connections
    -A INPUT -p tcp -m state --state NEW --dport 25 -j ACCEPT 

Now let's apply the rules:

    #!bash
    $ sudo iptables-restore < /etc/iptables.test.rules

Make sure everything looks dandy:

    #!bash
    $ sudo iptables -L

If it meets your fancy, save the rules:

    #!bash
    $ sudo -i
    $ iptables-save > /etc/iptables.up.rules

And now, from your local computer, let's test it out.

    #!bash
    $ telnet server.mydomain.com 25

    ehlo server.mydomain.com
    mail from: root@server.mydomain.com
    rcpt to: user@server.mydomain.com
    data
    Subject: remote connection test
    Hello, you.
    .
    quit

Now check your mail on the mail server as before. Once again, everything should be working.

Now we need to setup a virtual domain. Remember, I don't want any virtual users. I only want aliases at a virtual domain to forward to my primary email address. That makes this relatively simple. (Be very, very happy. You should have seen this guide before, when I was still hosting virtual domains with virtual users!) Open up `/etc/postfix/main.cf` and add the following:

    virtual_alias_domains = myvirtualdomain.com
    virtual_alias_maps = hash:/etc/postfix/virtual

Create the `/etc/postfix/virtual` file referenced above and add the aliases:

    alias@myvirtualdomain.com       user@mydomain.com

Turn it into a database:

    #!bash
    $ cd /etc/postfix
    $ sudo postmap virtual

Restart Postfix:

    #!bash
    $ sudo /etc/init.d/postfix restart

Attempt to send an email to the new alias at the virtual domain:

    #!bash
    $ telnet server.mydomain.com 25
    ehlo server.mydomain.com
    mail from: root@server.mydomain.com
    rcpt to: alias@myvirtualdomain.com
    data
    Subject: virtual domain test
    I hope this works!
    .
    quit

The message should now be in your primary email inbox!

As long as we're setting up forwards, let's forward system account mail to somewhere where it'll actually get read. To do so, create a `~/.forward` file with the following contents:

    user@mydomain.com

Let's also create a `/root/.forward`, so that roots mail gets forwarded to my local account (where it is then forwarded to my primary email). Root's forward would simply read:

    user

Next up: <a href="http://pig-monkey.com/2008/06/10/an-ubuntu-vps-on-slicehost-wordpress">install Wordpress with rewrites</a>. (Previously, we did a <a href="http://pig-monkey.com/2008/06/10/an-ubuntu-vps-on-slicehost-basic-setup">basic setup</a> and <a href="http://pig-monkey.com/2008/06/10/an-ubuntu-vps-on-slicehost-web-server">installed a web server</a>.)
