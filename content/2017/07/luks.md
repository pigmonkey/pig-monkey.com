Title: LUKS Header Backup
Date: 2017-07-16
tags: backups, crypto, linux

I'd neglected backup [LUKS](https://en.wikipedia.org/wiki/Linux_Unified_Key_Setup) headers until [Gwern's data loss postmortem](https://www.gwern.net/Notes#november-2016-data-loss-postmortem) last year. After reading his post I dumped the headers of the drives I had accessible, but I never got around to performing the task on my less frequently accessed drives. Last month I had trouble mounting one of those drives. It turned out I was simply using the wrong passphrase, but the experience prompted me to make sure I had completed the header backup procedure for all drives.

I dump the header to memory using [the procedure from the Arch wiki](https://wiki.archlinux.org/index.php/Dm-crypt/Device_encryption#Backup_using_cryptsetup). This is probably unnecessary, but only takes a few extra steps. The header is stored in my password store, which is obsessively backed up.

    $ sudo mkdir /mnt/tmp
    $ sudo mount ramfs /mnt/tmp -t ramfs
    $ sudo cryptsetup luksHeaderBackup /dev/sdc --header-backup-file /mnt/tmp/dump
    $ sudo chown pigmonkey:pigmonkey /mnt/tmp/dump
    $ pass insert -m crypt/luksheader/themisto < /mnt/tmp/dump
    $ sudo umount /mnt/tmp
    $ sudo rmdir /mnt/tmp
