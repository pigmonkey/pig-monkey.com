Title: Git Annex Recovery
Date: 2025-01-26
tags: backups, linux, annex

Occasionally I'll come across some sort of corruption on one of my [cold storage drives](/2016/08/storage/). This can typically repaired in-place via [git-annex-repair](https://git-annex.branchable.com/git-annex-repair/), but I usually take it as a sign that the hard drive itself is beginning to fail. I prefer to replace the drive. At the end of the process, I want the new drive to be mounted at the same location as the old one was, and I want the repository on the new drive to have the same UUID as the old one. This way the migration is invisible to all other copies of the repository.

To do this, I first prepare the new drive using whatever sort of LUKS encryption and formatting I want, and then mount it at the same location as wherever the old drive was normally mounted to. Call this path `$good`. The old drive I'll mount to some other location. Call this path `$bad`.

Next I create a new clone of the repository on the new drive. Most recently I did this for my video repo, which lives at `~/library/video`.

    $ git clone ~/library/video $good/video

The `.git/config` file from the old drive will have the UUID of the annex and other configuration options, as well as any knowledge about other remotes. I copy that into the new repo.

    $ cp $bad/video/.git/config $good/video/.git/config

The actual file contents are stored in the `.git/annex/objects/` directory. I copy those over to the new drive.

    $ mkdir $good/video/.git/annex
    $ rsync -avhP --no-compress --info=progress2 $bad/video/.git/annex/objects $good/video/.git/annex/

Next I initialize the new annex. It will recognize the old config and existing objects that were copied over.

    $ cd $good/video
    $ git annex init

At this point I could be done. But if I suspect that there was corruption in one of the files in the `.git/annex/objects` directory that I copied over, I will next tell the annex to run a check on all its files. I'll usually start this with `--incremental` in case I want to kill it before it completes and resume it later. I'll provide some integer to `--jobs` depending on how many cores I want to devote to hashing and what I think is appropriate for the disk read and transfer speeds.

    $ git annex fsck --incremental --jobs=N

If any of the files did fail, I'll make sure one of the other remotes is available and then tell the new annex to get whatever it wants.

    $ git annex get --auto

Finally, I would want to get rid of any of those corrupt objects that are now just wasting space.

    $ git annex unused
    $ git annex dropunused all
