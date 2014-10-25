Title: Back It Up: A Solution for Laptop Backups
Date: 2012-10-03
Modified: 2012-12-22
Tags: shell, backups, code, linux
Slug: back-it-up

A laptop presents some problems for reliably backing up data. Unlike a server, the laptop may not always be turned on. When it is on, it may not be connected to the backup medium. If you're doing online backups, the laptop may be offline. If you're backing up to an external drive, the drive may not be plugged in. To address these issues I wrote a shell script called [backitup.sh](https://github.com/pigmonkey/backups/blob/master/backitup.sh).

## The Problem

Let's say you want to backup a laptop to an external USB drive once per day with [cryptshot](http://pig-monkey.com/2012/09/24/cryptshot-automated-encrypted-backups-rsnapshot/).

You could add a cron entry to call `cryptshot.sh` at a certain time every day. What if the laptop isn't turned on? What if the drive isn't connected? In either case the backup will not be completed. The machine will then wait a full 24 hours before even attempting the backup again. This could easily result in weeks passing without a successful backup.

If you're using [anacron](http://en.wikipedia.org/wiki/Anacron), or one of its derivatives, things get slightly better. Instead of specifying a time to call `cryptshot.sh`, you set the cron interval to `@daily`. If the machine is turned off at whatever time anacron is setup to execute `@daily` scripts, all of the commands will simply be executed the next time the machine boots. But that still doesn't solve the problem of the drive not being plugged in.

## The Solution

`backitup.sh` attempts to perform a backup if a certain amount of time has passed. It monitors for a report of successful completion of the backup. Once configured, you no longer call the backup program directly. Instead, you call `backitup.sh`. It then decides whether or not to actually execute the backup.

### How it works

The script is configured with the backup program that should be executed, the period for which you want to complete backups, and the location of a file that holds the timestamp of the last successful backup. It can be configured either by modifying the variables at the top of the script, or by passing in command-line arguments.

    $ backitup.sh -h
    Usage: backitup.sh [OPTION...]
    Note that any command line arguments overwrite variables defined in the source.

    Options:
        -p      the period for which backups should attempt to be executed
                (integer seconds or 'DAILY', 'WEEKLY' or 'MONTHLY')
        -b      the backup command to execute; note that this should be quoted if it contains a space
        -l      the location of the file that holds the timestamp of the last successful backup.
        -n      the command to be executed if the above file does not exist

When the script executes, it reads the timestamp contained in the last-run file. This is then compared to the user-specified period. If the difference between the timestamp and the current time is greater than the period, `backitup.sh` calls the backup program. If the difference between the stored timestamp and the current time is less than the requested period, the script simply exits without running the backup program.

After the backup program completes, the script looks at the returned [exit code](https://en.wikipedia.org/wiki/Exit_status). If the exit code is 0, the backup was completed successfully, and the timestamp in the last-run file is replaced with the current time. If the backup program returns a non-zero exit code, no changes are made to the last-run file. In this case, the result is that the next time `backitup.sh` is called it will once again attempt to execute the backup program.

The period can either be specified in seconds or with the strings `DAILY`, `WEEKLY` or `MONTHLY`. The behaviour of `DAILY` differs from `86400` (24-hours in seconds). With the latter configuration, the backup program will only attempt to execute once per 24-hour period. If `DAILY` is specified, the backup may be completed successfully at, for example, 23:30 one day and again at 00:15 the following day.

## Use

You still want to backup a laptop to an external USB drive once per day with cryptshot. Rather than calling `cryptshot.sh`, you call `backitup.sh`.

Tell the script that you wish to complete daily backups, and then use cron to call the script more frequently than the desired backup period. For my local backups, I call `backitup.sh` every hour.

    @hourly backitup.sh -l ~/.cryptshot-daily -b "cryptshot.sh daily"

The default period of `backitup.sh` is `DAILY`, so in this case I don't have to provide a period of my own. But I also do weekly and monthly backups, so I need two more entries to execute cryptshot with those periods.

    @hourly backitup.sh -l ~/.cryptshot-monthly -b "cryptshot.sh monthly" -p MONTHLY
    @hourly backitup.sh -l ~/.cryptshot-weekly -b "cryptshot.sh weekly" -p WEEKLY

All three of these entries are executed hourly, which means that at the top of every hour, my laptop attempts to back itself up. As long as the USB drive is plugged in during one of those hours, the backup will complete. If cryptshot is executed, but fails, another attempt will be made the next hour. Daily backups will only be successfully completed, at most, once per day; weekly backups, once per week; and monthly backups, once per month. This setup works well for me, but if you want a higher assurance that your daily backups will be completed every day you could change the cron interval to `*/5 * * * *`, which will result in cron executing `backitup.sh` every 5 minutes.

What if you want to perform daily online backups with [Tarsnapper](http://pig-monkey.com/2012/09/16/tarsnapper-managing-tarsnap-backups/)?

    @hourly backitup.sh -l ~/.tarsnapper-lastrun -b tarsnapper.py

At the top of every hour your laptop will attempt to run [Tarsnap](http://www.tarsnap.com/) via Tarsnapper. If the laptop is offline, it will try again the following hour. If Tarsnap begins but you go offline before it can complete, the backup will be resumed the following hour.

The script can of course be called with something other than cron. Put it in your `~/.profile` and have you backups attempt to execute every time you login. Add it to your network manager and have your online backups attempt to execute every time you get online. If you're using something like [udev](https://en.wikipedia.org/wiki/Udev), have your local backups attempt to execute every time your USB drive is plugged in.

## The Special Case

The final configuration option of `backitup.sh` represents a special case. If the script runs and it can't find the specified file, the default behaviour is to assume that this is the first time it has ever run: it creates the file and executes the backup. That is what most users will want, but this behaviour can be changed.

When I first wrote `backitup.sh` it was to help manage backups of my [Dropbox](https://www.dropbox.com/) folder. Dropbox doesn't provide support client-side encryption, which means users need to handle encryption themselves. The most common way to do this is to create an [encfs](http://www.arg0.net/encfs) file-system or two and place those within the Dropbox directory. That's the way I use Dropbox.

I wanted to backup all the data stored in Dropbox with Tarsnap. Unlike Dropbox, Tarsnap *does* do client-side encryption, so when I backup my Dropbox folder, I don't want to actually backup the encrypted contents of the folder -- I want to backup the decrypted contents. That allows me to take better advantage of Tarsnap's deduplication and it makes restoring backups much simpler. Rather than comparing [inodes](https://en.wikipedia.org/wiki/Inode) and restoring a file using an encrypted filename like `6,8xHZgiIGN0vbDTBGw6w3lf/1nvj1,SSuiYY0qoYh-of5YX8` I can just restore `documents/todo.txt`.

If my encfs filesystem mount point is `~/documents`, I can configure Tarsnapper to create an archive of that directory, but if for some reason the filesystem is not mounted when Tarsnapper is called, I would be making a backup of an empty directory. That's a waste of time. The solution is to tell `backitup.sh` to put the last-run file *inside* the encfs filesystem. If it can't find the file, that means that the filesystem isn't mounted. If that's the case, I tell it to call the script I use to automatically mount the encfs filesystem (which, the way I have it setup, requires no interaction from me).

    @hourly backitup.sh -l ~/documents/.lastrun -b tarsnapper.py -n ~/bin/encfs_automount.sh

## Problem Solved

`backitup.sh` solves all of my backup scheduling problems. I only call backup programs directly if I want to make an on-demand backup. All of my automated backups go through `backitup.sh`. If you're interested in the script, you can [download it directly from GitHub](https://github.com/pigmonkey/backups/blob/master/backitup.sh). You can clone my entire [backups repository](https://github.com/pigmonkey/backups) if you're also interested in the other scripts I’ve written to manage different aspects of backing up data.

[Hey yo but wait, back it up, hup, easy back it up](https://www.youtube.com/watch?v=F22yKJRZoZc&t=2m51s)
