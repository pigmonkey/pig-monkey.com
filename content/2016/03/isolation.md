Title: Isolating Chrome Apps with Firejail
Date: 2016-03-29
Tags: linux, privacy

Despite its terse man page, Chromium provides [a large number of command-line options](http://peter.sh/experiments/chromium-command-line-switches/). One of these is `app-id`, which tells Chromium to directly launch a specific [Chrome App](https://chrome.google.com/webstore/category/apps). Combined with the isolation provided by [Firejail](https://firejail.wordpress.com/), this makes using Chrome Apps a much more enjoyable experience.

For instance, I use the [Signal Desktop app](https://whispersystems.org/blog/signal-desktop/). When I received the beta invite, I created a new directory to act as the home directory for the sandbox that would run the app.

    $ mkdir -p ~/.chromium-apps/signal

I then launched a sandboxed browser using that directory and installed the app.

    $ firejail --private=~/.chromium-apps/signal /usr/bin/chromium

After the app was installed, I added an alias to my zsh configuration to launch the app directly.

    alias signal="firejail --private=~/.chromium-apps/signal /usr/bin/chromium --app-id=bikioccmkafdpakkkcpdbppfkghcmihk"

To launch the application I can now simply run `signal`, just as if it was a normal desktop application. I don't have to worry about it accessing private information, or even care that it is actually running on Chromium underneath. I use this method daily for a number of different Chrome Apps, all in different isolated directories in `~/.chromium-apps`. As someone who is not a normal Chromium user, it makes the prospect of running a Chrome App much more attractive.
