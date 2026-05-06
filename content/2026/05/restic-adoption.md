Title: Restic Adoption
Date: 2026-05-06
tags: backups, linux

After mulling it over for many cycles, I finally decided to migrate my online backups to [Restic](https://restic.net/). As is my wont, I have published my solution as [Restash](https://github.com/pigmonkey/restash/) so that members of the Pig Monkey Data Backups Fan Club can be like me.

The [`restash` script](https://github.com/pigmonkey/restash/blob/master/restash) will look pretty familiar to anyone who has been using my old [Borg wrapper script](/2017/07/borg/). It is mostly the same basic structure, with Borg logic replaced with Restic logic, and two other significant differences.

Previously I ran the Borg wrapper hourly via a systemd timer, and used [backitup](https://github.com/pigmonkey/backitup) to run the verification checks (and [compacting](/2024/07/borg-compact/)) less frequently. Now the script has subcommands, and I use different systemd units to call the different functions on different schedules -- backups more frequently, verification and pruning less frequently.

Previously I achieved redundancy by using Borg to backup hourly to my [rsync.net](https://www.rsync.net/products/borg.html) account, while [Tarsnap](https://www.tarsnap.com/) ran daily backups of a smaller subset of the same data. Now I'm using Restic to backup hourly to my [rsync.net](https://www.rsync.net/products/restic.html) account, and also using Restic to backup the same data daily to a [Backblaze B2](https://www.backblaze.com/cloud-storage) bucket. I've been an rsync.net customer since 2014 and I think highly of their service, but the B2 bucket is cheap insurance that helps me [sleep](/2018/11/sleep/) better.

In [the example config](https://github.com/pigmonkey/restash/blob/master/restash.conf.example) you will see that the `SFTP_HOST` is simply `restic`. That refers to an entry in my `~/.ssh/config`, which looks something like this:

    Host restic
        Hostname abc123.rsync.net
        User abc123
        IdentityFile ~/.ssh/passphraseless-key
        IdentitiesOnly yes
        BatchMode yes
        ServerAliveInterval 60
        ServerAliveCountMax 3

The only other significant change from the old Borg wrapper script is that I broke out some of the config options, backup targets, and excludes to separate files to make it easier for you, my adoring public, to reuse the tool.

As hinted at in the README, I still use [nmtrust](https://github.com/pigmonkey/nmtrust) to only execute backups on trusted networks. Don't be a data litterer.
