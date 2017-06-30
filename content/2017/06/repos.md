Title: Automated Repository Tracking
Date: 2017-06-29
tags: linux, backups

I have confidence in my backup strategies for my own data, but until recently I had not considered backing up other people's data.

Recently, the author of a repository that I tracked on GitHub deleted his account and disappeared from the information super highway. I had a local copy of the repository, but I had not pulled it for a month. A number of recent changes were lost to me. This inspired me to setup the system I now use to automatically update local copies of any code repositories that are useful or interesting to me.

I clone the repositories into `~/library/src` and use [myrepos](https://myrepos.branchable.com/) to interact with them. I use myrepos for work and personal repositories as well, so to keep this stuff segregated I setup a separate config file and a [shell alias](https://github.com/pigmonkey/dotfiles/blob/master/aliases#L63) to refer to it.

    alias lmr='mr --config $HOME/library/src/myrepos.conf --directory=$HOME/library/src'
    
Now when I want to add a new repository, I clone it normally and register it with myrepos.

    $ cd ~/library/src
    $ git clone https://github.com/warner/magic-wormhole
    $ cd magic-wormhole && lmr register

The `~/library/src/myrepos.conf` file has a default section which states that no repository should be updated more than once every 24 hours.

    [DEFAULT]
    skip = [ "$1" = update ] && ! hours_since "$1" 24

Now I can ask myrepos to update all of my tracked repositories. If it sees that it has already updated a repository within 24 hours, myrepos will skip the repository.

    $ lmr update
    
To automate this I create a [systemd service](https://github.com/pigmonkey/dotfiles/blob/master/config/systemd/user/library-repos.service).

    [Unit]
    Description=Update library repositories

    [Service]
    Type=oneshot
    ExecStart=/usr/bin/mr --config %h/library/src/myrepos.conf -j5 update

    [Install]
    WantedBy=multi-user.target
    
And a [systemd timer to run the service every hour](https://github.com/pigmonkey/dotfiles/blob/master/config/systemd/user/library-repos.timer).

    [Unit]
    Description=Update library repositories timer

    [Timer]
    Unit=library-repos.service
    OnCalendar=hourly
    Persistent=True

    [Install]
    WantedBy=timers.target
    
I don't enable this timer directly, but instead add it to my `trusted_units` file so that [nmtrust](https://github.com/pigmonkey/nmtrust) will enable it only when I am on a trusted network.

    $ echo "library-repos.timer,user:pigmonkey" >> /usr/local/etc/trusted_units
    
If I'm curious to see what has been recently active, I can `ls -ltr ~/library/src`. I find this more useful than [GitHub stars](https://help.github.com/articles/about-stars/) or similar bookmarking.

I currently track 120 repositories. This is only 3.3 GB, which means I can incorporate it into my normal backup strategies without being concerned about the extra space.

The internet can be fickle, but it will be difficult for me to loose a repository again.
