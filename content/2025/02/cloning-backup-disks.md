Title: Cloning Backup Drives
Date: 2025-02-05
tags: backups, linux

Continuing with the theme of [replacing drives](/2025/01/git-annex-recovery/), recently I decided to preemptively replace one of the external drives that I backup to via [rsnapshot](https://rsnapshot.org/) -- or, more specifically, via [cryptshot](https://github.com/pigmonkey/cryptshot). The drive was functioning nominally, but its date of manufacture was 2014. That's way too long to trust spinning rust.

rsnapshot implements deduplication via hard links. Were I to just `rsync` the contents of the old drive to the new drive without any special consideration for the links, it would dereference the links, copying them over as separate files. This would cause the size of the backups to balloon past the capacity of the drive. Rsync provides the `--hard-links` flag to address this, but I've heard some stories about this failing to act as expected when the source directory has a large number of hard links (for some unknown definition of "large"). I've been [rsnapshotting since 2012](/2012/09/cryptshot-automated-encrypted-backups-rsnapshot/) (after a pause sometime [after 2006](/2006/02/rsnapshot/), apparently) and feel safe assuming that my rsnapshot repository does have a "large" number of hard links.

I also do not really care about syncing. The destination is completely empty. There's no file comparison that needs to happen. I don't need to the ability to pause partway through the transfer and resume later. Rsync is my default solution for pushing files around, but in this case it is not really needed. I only want to mirror the contents of the old drive onto the new drive, exactly as they exist on the old drive. So I avoided the problem all together and just copied the partition via `dd`.

Both drives are encrypted with LUKS, so first I decrypt them. Importantly, I do not mount either decrypted partition. I don't want to risk any modifications being made to either while the copy is ongoing.

    $ sudo cryptsetup luksOpen /dev/sda old
    $ sudo cryptsetup luksOpen /dev/sdb new

Then I copy the old partition to the new one.

    $ sudo dd if=/dev/mapper/old of=/dev/mapper/new bs=32M status=progress

My new drive is the same size as my old drive, so after `dd` finished I was done. If the sizes differed I would need to use `resize2fs` to resize the partition on the new drive.

If I was replacing the old drive not just because it was old and I was ageist, but because I thought it may be corrupted, I would probably do this with [GNU ddrescue](https://www.gnu.org/software/ddrescue/ddrescue.html) rather than plain old `dd`. (Though, realistically, if that was the case I'd probably just copy the contents of my other rsnapshot target drive to the new drive, and replace the corrupt drive with that. Multiple backup mediums make life easier.)
