Title: Optical Backups of Financial Archives
Date: 2019-06-29
Tags: backups, crypto, linux, annex

Every year I burn an optical archive of my financial documents, similar to how (and why) I [create optical backups of photos](/2013/05/optical-photo-backups/). I schedule this financial archive for the spring, after the previous year's taxes have been submitted and accepted. [Taskwarrior](https://taskwarrior.org/) solves the problem of remembering to complete the archive.

    $ task add project:finance due:2019-04-30 recur:yearly wait:due-4weeks "burn optical financial archive with parity"

The archive includes two [git-annex](https://git-annex.branchable.com/) repositories.

The first is my [ledger](https://www.ledger-cli.org/) repository. Ledger is the double-entry accounting system I began using in 2012 to record the movement of every penny that crosses one of my bank accounts (small cash transactions, less than about $20, are usually-but-not-always except from being recorded). In addition to the plain-text ledger files, this repository also holds PDF or JPG images of receipts.

The second repository holds my tax information. Each tax year gets a [ctmg](https://git.zx2c4.com/ctmg/about/) container which contains any documents used to complete my tax returns, the returns themselves, and any notifications of those returns being accepted.

The yearly optical archive that I create holds the entirety of these two repositories -- not just the information from the previous year -- so really each disc only needs to have a shelf life of 12 months. Keeping the older discs around just provides redundancy for prior years.


## Creating the Archive

The process of creating the archive is very similar to the process I outlined six years ago for the photo archives.

The two repositories, combined, are about 2GB (most of that is the directory of receipts from the ledger repository). I burn these to a 25GB BD-R disc, so file size is not a concern. I'll `tar` them, but skip any compression, which would just add extra complexity for no gain.

    $ mkdir ~/tmp/archive
    $ cd ~/library
    $ tar cvf ~/tmp/archive/ledger.tar ledger
    $ tar cvf ~/tmp/archive/tax.tar tax

The ledger archive will get signed and encrypted with my PGP key. The contents of the tax repository are already encrypted, so I'll skip encryption and just sign the archive. I like using detached signatures for this.

    $ cd ~/tmp/archive
    $ gpg -e -r peter@havenaut.net -o ledger.tar.gpg ledger.tar
    $ gpg -bo ledger.tar.gpg.sig ledger.tar.gpg
    $ gpg -bo tax.tar.sig tax.tar
    $ rm ledger.tar

Previously, when creating optical photo archives, I used [DVDisaster](https://web.archive.org/web/20160427222800/http://dvdisaster.net/en/index.html) to create the disc image with parity. DVDisaster no longer exists. The code can still be found, and the program still works, but nobody is developing it and it doesn't even an official web presence. This makes me uncomfortable for a tool that is part of my long-term archiving plans. As a result, I've moved back to using [Parchive](https://parchive.github.io/) for parity. Parchive also does not have much in the way of active development around it, but it [is still maintained](https://github.com/Parchive/par2cmdline/commits/master), has been around for a long period of time, is still used by a wide community, and will probably continue to exist as long as people share files on less-than-perfectly-reliable mediums.

As previously mentioned, I'm not worried about the storage space for these files, so I tell `par2create` to create PAR2 files with 30% redundancy. I suppose I could go even higher, but 30% seems like a good number. By default this process will be allowed to use 16MB of memory, which is cute, but RAM is cheap and I usually have enough to spare so I'll give it permission to use up to 8GB.

    $ par2create -r30 -m8000 recovery.par2 *

Next I'll use [hashdeep](http://md5deep.sourceforge.net/) to generate message digests for all the files in the archive.

    $ hashdeep * > hashes

At this point all the file processing is completed. I'll put a blank disc in my burner (a [Pioneer BDR-XD05B](https://pioneerelectronics.com/PUSA/Computer/Computer+Drives/BDR-XD05B)) and burn the directory using [growisofs](http://fy.chalmers.se/~appro/linux/DVD+RW/).

    $ growisofs -Z /dev/sr0 -V "Finances 2019" -r *


## Verification

The final step is to verify the disc. I have a few options on this front. These are the same steps I'd take years down the road if I actually needed to recover data from the archive.

I can use the previous hashes to find any files that do not match, which is a quick way to identify bit rot.

    $ hashdeep -x -k hashes *.{gpg,tar,sig,par2}

I can check the integrity of the PGP signatures.

    $ gpg --verify tax.tar.gpg{.sig,}
    $ gpg --verify tax.tar{.sig,}

I can use the PAR2 files to verify the original data files.

    $ par2 verify recovery.par2
