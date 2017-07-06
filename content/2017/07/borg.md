Title: Borg Assimilation
Date: 2017-07-05
tags: backups, crypto, linux

For years the core of my backup strategy has been [rsnapshot](http://rsnapshot.org/) via [cryptshot](https://github.com/pigmonkey/cryptshot) to various external drives for local backups, and [Tarsnap](https://www.tarsnap.com/) for remote backups.

Tarsnap, however, can be slow. It tends to take somewhere between 15 to 20 minutes to create my dozen or so archives, even if little has changed since the last run. My impression is that this is simply due to the number of archives I have stored and the number of files I ask it to archive. Once it has decided what to do, the time spent transferring data is negligible. I run Tarsnap hourly. Twenty minutes out of every hour seems like a lot of time spent Tarsnapping.

I've  eyed [Borg](https://github.com/borgbackup/borg) for a while (and before that, [Attic](https://attic-backup.org/)), but avoided using it due to the rapid development of its earlier days. While activity is nice, too many changes too close together do not create a reassuring image of a backup project. Borg seems to have stabilized now and has a large enough user base that I feel comfortable with it. About a month ago, I began using it to backup my laptop to [rsync.net](http://www.rsync.net/products/attic.html).

Initially I played with [borgmatic](https://torsion.org/borgmatic/) to perform and maintain the backups. Unfortunately it seems to have issues with signal handling, which caused me to end up with annoying lock files left over from interrupted backups. Borg itself has [good documentation](https://borgbackup.readthedocs.io/en/stable/) and is [easy to use](https://borgbackup.readthedocs.io/en/stable/usage.html), and I think it is useful to build familiarity with the program itself instead of only interacting with it through something else. So I did away with borgmatic and wrote a small bash script to handle my use case.

[Creating the backups](https://borgbackup.readthedocs.io/en/stable/usage.html#borg-create) is simple enough. Borg disables compression by default, but after a little experimentation I found that LZ4 seemed to be a decent compromise between compression and performance.

[Pruning backups](https://borgbackup.readthedocs.io/en/stable/usage.html#borg-prune) is equally easy. I knew I wanted to match roughly what I had with Tarsnap: hourly backups for a day or so, daily backups for a week or so, then a month or two of weekly backups, and finally a year or so of monthly backups.

My only hesitation was in how to maintain the health of the backups. Borg provides the convenient [borg check](https://borgbackup.readthedocs.io/en/stable/usage.html#borg-check) command, which is able to verify the consistency of both a repository and the archives themselves. Unsurprisingly, this is a slow process. I didn't want to run it with my hourly backups. Daily, or perhaps even weekly, seemed more reasonable, but I did want to make sure that both checks were completed successfully with some frequency. Luckily this is just the problem that I wrote [backitup](https://github.com/pigmonkey/backitup) to solve.

Because the consistency checks take a while and consume some resources, I thought it would also be a good idea to avoid performing them when I'm running on battery. Giving backitup the ability to detect if the machine is on battery or AC power was [a simple hack](https://github.com/pigmonkey/backitup/commit/0cd4d3a45df02a5f592617f8a4ad3811a02c9a38). The script now features the `-a` switch to specify that the program should only be executed when on AC power.

My completed Borg wrapper is thus:

    #!/bin/sh
    export BORG_PASSPHRASE='supers3cr3t'
    export BORG_REPO='borg-rsync:borg/nous'
    export BORG_REMOTE_PATH='borg1'

    # Create backups
    echo "Creating backups..."
    borg create --verbose --stats --compression=lz4             \
        --exclude ~/projects/foo/bar/baz                        \
        --exclude ~/projects/xyz/bigfatbinaries                 \
        ::'{hostname}-{user}-{utcnow:%Y-%m-%dT%H:%M:%S}'        \
        ~/documents                                             \
        ~/projects                                              \
        ~/mail                                                  \
        # ...etc

    # Prune backups
    echo "Pruning backups..."
    borg prune --verbose --list --prefix '{hostname}-{user}-'    \
        --keep-within=2d                                         \
        --keep-daily=14                                          \
        --keep-weekly=8                                          \
        --keep-monthly=12                                        \

    # Check backups
    echo "Checking repository..."
    backitup -a                                             \
        -p 172800                                           \
        -l ~/.borg_check-repo.lastrun                       \
        -b "borg check --verbose --repository-only"         \
    echo "Checking archives..."
    backitup -a                                             \
        -p 259200                                           \
        -l ~/.borg_check-arch.lastrun                       \
        -b "borg check --verbose --archives-only --last 24" \
    
This is executed by a [systemd service](https://github.com/pigmonkey/dotfiles/blob/master/config/systemd/user/borg.service).

    [Unit]
    Description=Borg Backup

    [Service]
    Type=oneshot
    ExecStart=/home/pigmonkey/bin/borgwrapper.sh

    [Install]
    WantedBy=multi-user.target
    
The service is called hourly by a [systemd timer](https://github.com/pigmonkey/dotfiles/blob/master/config/systemd/user/borg.timer).

    [Unit]
    Description=Borg Backup Timer

    [Timer]
    Unit=borg.service
    OnCalendar=hourly
    Persistent=True

    [Install]
    WantedBy=timers.target
    
I don't enable the timer directly, but add it to `/usr/local/etc/trusted_units` so that [nmtrust](https://github.com/pigmonkey/nmtrust) activates it when I'm connected to trusted networks.

    $ echo "borg.timer,user:pigmonkey" >> /usr/local/etc/trusted_units
    
I've been running this for about a month now and have been pleased with the results. It averages about 30 seconds to create the backups every hour, and another 30 seconds or so to prune the old ones. As with Tarsnap, deduplication is great.

    ------------------------------------------------------------------------------
                           Original size      Compressed size    Deduplicated size
    This archive:               19.87 GB             18.41 GB             10.21 MB
    All archives:              836.02 GB            773.35 GB             19.32 GB
                           Unique chunks         Total chunks
    Chunk index:                  371527             14704634
    ------------------------------------------------------------------------------

The most recent repository consistency check took about 30 minutes, but only runs every 172800 seconds, or once every other day. The most recent archive consistency check took about 40 minutes, but only runs every 259200 seconds, or once per 3 days. I'm not sure that those schedules are the best option for the consistency checks. I may tweak their frequencies, but because I know they will only be executed when I am on a trusted network and AC power, I'm less concerned about the length of time.

With Borg running hourly, I've reduced Tarsnap to run only once per day. Time will tell if Borg will slow as the number of stored archives increase, but for now running Borg hourly and Tarsnap daily seems like a great setup. Tarsnap and Borg both target the same files (with a few exceptions). Tarsnap runs in the AWS us-east-1 region. I've always kept my rsync.net account in their Zurich datacenter. This provides the kind of redundancy that lets me rest easy.

Contrary to what you might expect given the [number of blog posts on the subject](/tag/backups/), I actually spend close to no time worrying about data loss in my day to day life, thanks to stuff like this. An ounce of prevention, and all that. (Maybe a few kilograms of prevention in my case.)
