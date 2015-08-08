Title: Jailing the Browser
Date: 2015-08-08
Tags: linux, privacy

The web browser is one of our computers' primary means of interaction with the unwashed mashes. Combined with the unfortunately large attack surface of modern browsers, this makes a [sandbox](https://en.wikipedia.org/wiki/Sandbox_(computer_security)) which does not depend on the browser itself an attractive idea.

[Firejail](https://l3net.wordpress.com/projects/firejail/) is a simple, lightweight sandbox that uses [linux namespaces](https://lwn.net/Articles/531114/) to prevent programs from accessing things they do not need.

Firejail ships with default profiles for [Firefox](https://www.mozilla.org/en-US/firefox/new/) and [Chromium](https://www.chromium.org/Home). These profiles drop [capabilities](https://l3net.wordpress.com/2015/03/16/firejail-linux-capabilities-guide/), filter [syscalls](https://l3net.wordpress.com/2015/04/13/firejail-seccomp-guide/), and prevent access to common directories like `/sbin`, `~/.gnupg` and `~/.ssh`. This is a good start, but I see little reason to give the browser access to much of anything in my home directory.

The `--private` flag instructs Firejail to mount a new user home directory in a temporary filesystem. The directory is empty and all changes are discarded when the sandbox is closed -- think of it as a more effective [private browsing](https://support.mozilla.org/en-US/kb/private-browsing-use-firefox-without-history) or [incognito](https://dev.chromium.org/user-experience/incognito) mode that also resets your browser to factory defaults.

    $ firejail --private firefox

A more useful option for normal browsing is to specify a directory that Firejail should use as the user home. This allows you to keep a consistent browser profile and downloads directory, but still prevents the browser from accessing anything else in the normal user home.

    $ mkdir ~/firefox
    $ mv ~/.mozilla ~/firefox/
    $ firejail --private=firefox firefox

This is the method I default to for my browsing. I've created my own [Firejail profile for Firefox](https://github.com/pigmonkey/dotfiles/blob/master/config/firejail/firefox.profile) at `~/.config/firejail/firefix.profile` which implements this.

    include /etc/firejail/disable-mgmt.inc
    caps.drop all
    seccomp
    netfilter
    noroot

    # Use ~/firefox as user home
    private firefox

The only inconvenience I've discovered with this is that linking my [Vimperator](http://www.vimperator.org/vimperator/) configuration files into the directory from my [dotfiles repository](https://github.com/pigmonkey/dotfiles) creates a dangling link from the perspective of anything running within the jail. Since it cannot access my real home directory, it cannot see the link target in the `~/.dotfiles` directory. I have to copy the configuration files into `~/firefox` and then manually keep them in sync. I modify these files infrequently enough that for me this is worth the trade-off.

The temporary filesystem provided by `--private` is still useful when accessing websites that are especially sensitive (such as a financial institution) or especially shady. In my normal browser profiles, I have a number of extensions installed that block ads, disable scripts, etc. If these extensions completely break a website, and I don't want to take the time to figure out which of the dozens of things I'm blocking are required for the website to function, I'll just spin up a sandboxed browser with the `--private` flag, comfortable in the knowledge that whatever dirty scripts the site is running are limited in their ability to harm me.

I perform something like 90% of my web browsing in Firefox, but use Chromium for various tasks throughout the day. Both run in Firejail sandboxes, helping to keep me safe when surfing the information superhighway. Other programs, like torrent applications and PDF readers, also make good candidates for running within Firejail.
