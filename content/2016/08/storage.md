Title: Cold Storage
Date: 2016-08-26
tags: backups, linux, annex, crypto

This past spring I mentioned my [cold storage setup](/2016/03/backup/): a number of encrypted 2.5" drives in external enclosures, stored inside a [Pelican 1200](http://www.pelican.com/us/en/product/watertight-protector-hard-cases/small-case/standard/1200/) case, secured with [Abloy Protec2 321](https://securitysnobs.com/Abloy-Protec2-PL-321-Padlock.html) locks. Offline, secure, and infrequently accessed storage is an important component of any strategy for resilient data. The ease with which this can be managed with [git-annex](https://git-annex.branchable.com/) only increases [my infatuation with the software](/tag/annex/).

<a href="https://www.flickr.com/photos/pigmonkey/29168947362/in/dateposted/" title="Data Data Data Data Data"><img src="https://c3.staticflickr.com/9/8405/29168947362_2c7ecc9a97_c.jpg" width="800" height="450" alt="Data Data Data Data Data"></a>

I've been happy with the [Seagate ST2000LM003](https://www.amazon.com/gp/product/B00MPWYLHO/) drives for this application. Unfortunately the enclosures I first purchased did not work out so well. I had two die within a few weeks. They've been replaced with the [SIG JU-SA0Q12-S1](https://www.amazon.com/gp/product/B00YT6TOJO/). These claim to be compatible with drives up to 8TB (someday I'll be able to buy 8TB 2.5" drives) and support USB 3.1. They're also a bit thinner than the previous enclosures, so I can easily fit five in my box. The Seagate drives offer about 1.7 terabytes of usable space, giving this setup a total capacity of 8.5 terabytes.

Setting up git-annex to support this type of cold storage is fairly straightforward, but does necessitate some familiarity with how the program works. Personally, I prefer to do all my setup manually. I'm happy to let the [assistant](http://git-annex.branchable.com/assistant/) watch my repositories and manage them after the setup, and I'll occasionally fire up the [web app](https://git-annex.branchable.com/design/assistant/webapp/) to see what the assistant daemon is doing, but I like the control and understanding provided by a manual setup. The power and flexibility of git-annex is deceptive. Using it solely through the simplified interface of the web app greatly limits what can be accomplished with it.

## Encryption

Before even getting into git-annex, the drive should be encrypted with [LUKS](https://en.wikipedia.org/wiki/Linux_Unified_Key_Setup)/[dm-crypt](https://en.wikipedia.org/wiki/Dm-crypt). The need for this could be avoided by using something like [gcrypt](https://git-annex.branchable.com/special_remotes/gcrypt/), but LUKS/dm-crypt is an ingrained habit and part of my workflow for all external drives. Assuming the drive is `/dev/sdc`, pass `cryptsetup` some sane defaults:

    $ sudo cryptsetup --cipher aes-xts-plain64 --key-size 512 --hash sha512 luksFormat /dev/sdc

With the drive encrypted, it can then be opened and formatted. I'll give the drive a human-friendly label of `themisto`.

    $ sudo cryptsetup luksOpen /dev/sdc themisto_crypt
    $ sudo mkfs.ext4 -L themisto /dev/mapper/themisto_crypt

At this point the drive is ready. I close it and then mount it with [udiskie](https://github.com/coldfix/udiskie) to make sure everything is working. How the drive is mounted doesn't matter, but I like udiskie because it can [integrate with my password manager](https://github.com/pigmonkey/dotfiles/blob/master/config/udiskie/config.yml#L5) to get the drive passphrase.

    $ sudo cryptsetup luksClose /dev/mapper/themisto_crypt
    $ udiskie-mount -r /dev/sdc

## Git-Annex

With the encryption handled, the drive should now be mounted at `/media/themisto`. For the first few steps, we'll basically follow the [git-annex walkthrough](https://git-annex.branchable.com/walkthrough/). Let's assume that we are setting up this drive to be a repository of the annex `~/video`. The first step is to go to the drive, clone the repository, and initialize the annex. When initializing the annex I prepend the name of the remote with `satellite : `. My cold storage drives are all named after satellites, and doing this allows me to easily identify them when looking at a list of remotes.

    $ cd /media/themisto
    $ git clone ~/video
    $ cd video
    $ git annex init "satellite : themisto"

### Disk Reserve

Whenever dealing with a repository that is bigger (or may become bigger) than the drive it is being stored on, it is important to set a disk reserve. This tells git-annex to always keep some free space around. I generally like to set this to 1 GB, which is way larger than it needs to be.

    $ git config annex.diskreserve "1 gb"

### Adding Remotes

I'll then tell this new repository where the original repository is located. In this case I'll refer to the original using the name of my computer, `nous`.

    $ git remote add nous ~/video

If other remotes already exist, now is a good time to add them. These could be [special remotes](https://git-annex.branchable.com/special_remotes/) or normal ones. For this example, let's say that we have already completed this whole process for another cold storage drive called `sinope`, and that we have an [s3](https://git-annex.branchable.com/special_remotes/S3/) remote creatively named `s3`.

    $ git remote add sinope /media/sinope/video
    $ export AWS_ACCESS_KEY_ID="..."
    $ export AWS_SECRET_ACCESS_KEY="..."
    $ git annex enableremote s3

### Trust

[Trust](https://git-annex.branchable.com/trust/) is a critical component of how git-annex works. Any new annex will default to being semi-trusted, which means that when running operations within the annex on the main computer -- say, dropping a file -- git-annex will want to confirm that `themisto` has the files that it is supposed to have. In the case of `themisto` being a USB drive that is rarely connected, this is not very useful. I tell git-annex to trust my cold storage drives, which means that if git-annex has a record of a certain file being on the drive, it will be satisfied with that. This increases the risk for potential data-loss, but for this application I feel it is appropriate.

    $ git annex trust .

### Preferred Content

The final step that needs to be taken on the new repository is to tell it what files it should want. This is done using [preferred content](https://git-annex.branchable.com/preferred_content/). The [standard groups](https://git-annex.branchable.com/preferred_content/standard_groups/) that git-annex ships with cover most of the bases. Of interest for this application is the `archive` group, which wants all content except that which has already found its way to another archive. This is the behaviour I want, but I will duplicate it into a custom group called `satellite`. This keeps my cold storage drives as standalone things that do not influence any other remotes where I may want to use the default `archive`.

    $ git annex groupwanted satellite "(not copies=satellite:1) or approxlackingcopies=1"
    $ git annex group . satellite
    $ git annex wanted . groupwanted

For other repositories, I may want to store the data on multiple cold storage drives. In that case I would create a `redundantsatellite` group that wants all content which is not already present in two other members of the group.

    $ git annex groupwanted redundantsatellite "(not copies=redundantsatellite:2) or approxlackingcopies=1"
    $ git annex group . redundantsatellite
    $ git annex wanted . groupwanted

### Syncing

With everything setup, the new repository is ready to sync and to start to ingest content from the remotes it knows about!

    $ git annex sync --content

However, the original repository also needs to know about the new remote.

    $ cd ~/video
    $ git remote add themisto /media/themisto/video
    $ git annex sync

The same is the case for any other previously existing repository, such as `sinope`.
