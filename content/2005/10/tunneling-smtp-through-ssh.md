Title: Tunneling SMTP through SSH
Date: 2005-10-11
Modified: 2012-10-12
Tags: crypto
Slug: tunneling-smtp-through-ssh

Since Dreamhost doesn't support any sort of secure SMTP, I've been tunneling it through ssh for the past month or so.

<blockquote>ssh -f -N -L 9999:mail.myserver.com:25 myserver.com -l user </blockquote>
<i>9999</i> is the local port, <i>mail.myserver.com</i> is the mail server, <i>25</i> is the remote port, <i>myserver.com</i> is where your shell is, <i>user</i> is your username on the server. Then, just tell Thunderbird (or whatever mail app you use) that your smtp server is localhost:9999

I have this run at bootup, so that all I have to do is type in my key when I boot up and all my mail is encrypted (Dreamhost does support IMAPS).

You could, of course, setup your ssh account to have no key, but this is a rather large sacrifice of security (as soon as the attacker acquires your private key, he has access to your ssh account)-- especially if your primary computer is a laptop, like mine.
