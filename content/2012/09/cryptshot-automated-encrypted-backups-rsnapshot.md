Title: Cryptshot: Automated, Encrypted Backups with rsnapshot
Date: 2012-09-24
Modified: 2012-12-22
Tags: shell, backups, code, crypto, linux
Slug: cryptshot-automated-encrypted-backups-rsnapshot

Earlier this year I switched from [Duplicity](http://duplicity.nongnu.org/) to [rsnapshot](http://rsnapshot.org/) for my local backups. Duplicity uses a full + incremental backup schema: the first time a backup is executed, all files are copied to the backup medium. Successive backups copy only the deltas of changed objects. Over time this results in a chain of deltas that need to be replayed when restoring from a backup. If a single delta is somehow corrupted, the whole chain is broke. To minimize the chances of this happening, the common practice is to complete a new full backup every so often -- I usually do a full backup every 3 or 4 weeks. Completing a full backup takes time when you're backing up hundreds of gigabytes, even over USB 3.0. It also takes up disk space. I keep around two full backups when using Duplicity, which means I'm using a little over twice as much space on the backup medium as what I'm backing up.

The backup schema that rsnapshot uses is different. The first time it runs, it completes a full backup. Each time after that, it completes what could be considered a "full" backup, but unchanged files are not copied over. Instead, rsnapshot simply [hard links](http://en.wikipedia.org/wiki/Hard_link) to the previously copied file. If you modify very large files regularly, this model may be inefficient, but for me -- and I think for most users -- it's great. Backups are speedy, disk space usage on the backup medium isn't too much more than the data being backed up, and I have multiple full backups that I can restore from.

The great strength of Duplicity -- and the great weakness of rsnapshot -- is encryption. Duplicity uses [GnuPG](http://www.gnupg.org/) to encrypt backups, which makes it one of the few solutions appropriate for remote backups. In contrast, rsnapshot does no encryption. That makes it completely inappropriate for remote backups, but the shortcoming can be worked around when backing up locally.

My local backups are done to an external, USB hard drive. Encrypting the drive is simple with [LUKS](http://en.wikipedia.org/wiki/Linux_Unified_Key_Setup) and [dm-crypt](http://en.wikipedia.org/wiki/Dm-crypt). For example, to encrypt `/dev/sdb`:

    $ cryptsetup --cipher aes-xts-plain --key-size 512 --verify-passphrase luksFormat /dev/sdb

The device can then be opened, formatted, and mounted.

    $ cryptsetup luksOpen /dev/sdb backup_drive
    $ mkfs.ext4 -L backup /dev/mapper/backup_drive
    $ mount /dev/mapper/backup_drive /mnt/backup/

At this point, the drive will be encrypted with a passphrase. To make it easier to mount programatically, I also add a key file full of some random data generated from `/dev/urandom`.

    $ dd if=/dev/urandom of=/root/supersecretkey bs=1024 count=8
    $ chmod 0400 /root/supersecretkey
    $ cryptsetup luksAddKey /dev/sdb /root/supersecretkey

There are still a few considerations to address before backups to this encrypted drive can be completed automatically with no user interaction. Since the target is a USB drive and the source is a laptop, there's a good chance that the drive won't be plugged in when the scheduler kicks in the backup program. If it is plugged in, the drive needs to be decrypted before calling rsnapshot to do its thing. I wrote a wrapper script called [cryptshot](https://github.com/pigmonkey/cryptshot) to address these issues.

Cryptshot is configured with the [UUID](http://en.wikipedia.org/wiki/Universally_unique_identifier) of the target drive and the key file used to decrypt the drive. When it is executed, the first thing it does is look to see if the UUID exists. If it does, that means the drive is plugged in and accessible. The script then decrypts the drive with the specified key file and mounts it. Finally, rsnapshot is called to execute the backup as usual. Any argument passed to cryptshot is passed along to rsnapshot. What that means is that cryptshot becomes a drop-in replacement for encrypted, rsnapshot backups. Where I previously called `rsnapshot daily`, I now call `cryptshot daily`. Everything after that point just works, with no interaction needed from me.

If you're interested in cryptshot, you can [download it directly from GitHub](https://github.com/pigmonkey/cryptshot). The script could easily be modified to execute a backup program other than rsnapshot. You can clone my entire [backups repository](https://github.com/pigmonkey/backups) if you're also interested in the other scripts I've written to manage different aspects of backing up data.
