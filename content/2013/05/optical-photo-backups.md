Title: Optical Backups of Photo Archives
Date: 2013-05-29
Modified: 2013-05-29
Tags: backups, crypto, linux
Slug: optical-photo-backups

I store my photos in [git-annex](http://git-annex.branchable.com/). A full copy of the annex exists on my laptop and on an external drive. Encrypted copies of all of my photos are stored on [Amazon S3](https://aws.amazon.com/s3/) (which I pay for) and [box.com](https://www.box.com/) (which provides 50GB for free) via git-annex [special remotes](http://git-annex.branchable.com/special_remotes/). The photos are backed-up to an external drive daily with the rest of my laptop hard drive via [backitup.sh](https://pig-monkey.com/2012/10/3/back-it-up/) and [cryptshot](http://pig-monkey.com/2012/09/24/cryptshot-automated-encrypted-backups-rsnapshot/). My entire laptop hard drive is also mirrored monthly to an external drive stored off-site.

(The majority of my photos are also [on Flickr](http://www.flickr.com/photos/pigmonkey/), but I don't consider that a backup or even reliable storage.)

All of this is what I consider to be the bare minimum for any redundant data storage. Photos have special value, above the value that I assign to most other data. This value only increases with age. As such they require an additional backup method, but due to the size of my collection I want to avoid backup methods that involve paying for more online storage, such as [Tarsnap](http://pig-monkey.com/2012/09/16/tarsnapper-managing-tarsnap-backups/).

I choose optical discs as the medium for my photo backups. This has the advantage of being read-only, which makes it more difficult for accidental deletions or corruption to propagate through the backup system. DVD-Rs have a capacity of 4.7 GBs and a cost of around $0.25 per disc. Their life expectancy varies, but 10-years seem to be a reasonable low estimate.


## Preparation

I keep all of my photos in year-based directories. At the beginning of every year, the previous year's directory is burned to a DVD.

Certain years contain few enough photos that the entire year can fit on a single DVD. More recent years have enough photos of a high enough resolution that they require multiple DVDs.


### Archive

My first step is to build a compressed archive of each year. I choose [tar](http://www.gnu.org/software/tar/) and [bzip2](http://en.wikipedia.org/wiki/Bzip2) compression for this because they're simple and reliable.

    #!bash
    $ cd ~/pictures
    $ tar cjhf ~/tmp/pictures/2012.tar.bz 2012

If the archive is larger than 3.7 GB, it needs to be split into multiple files. The resulting files will be burned to different discs. The capacity of a DVD is 4.7 GB, but I place the upper file limit at 3.7 GB so that the DVD has a minimum of 20% of its capacity available. This will be filled with parity information later on for redundancy.

    #!bash
    $ split -d -b 3700M 2012.tar.bz 2012.tar.bz.


### Encrypt

Leaving unencrypted data around is [bad form](http://www.youtube.com/watch?v=OwHrlM4oVSI). The archive (or each of the files resulting from splitting the large archive) is next encrypted and signed with [GnuPG](http://www.gnupg.org/).

    #!bash
    $ gpg -eo 2012.tar.bz.gpg 2012.tar.bz
    $ gpg -bo 2012.tar.bz.gpg.sig 2012.tar.bz.gpg


## Imaging

The encrypted archive and the detached signature of the encrypted archive are what will be burned to the disc. (Or, in the case of a large archive, the encrypted splits of the full archive and the associated signatures will be burned to one disc per split/signature combonation.) Rather than burning them directly, an image is created first.

    #!bash
    $ mkisofs -V "Photos: 2012 1/1" -r -o 2012.iso 2012.tar.bz.gpg 2012.tar.bz.gpg.sig

If the year has a split archive requiring multiple discs, I modify the sequence number in the volume label. For example, a year requiring 3 discs will have the label `Photos: 2012 1/3`.


### Parity

When I began this project I knew that I wanted some sort of parity information for each disc so that I could potentially recover data from slightly damaged media. My initial idea was to use [parchive](http://en.wikipedia.org/wiki/Parchive) via [par2cmdline](https://github.com/BlackIkeEagle/par2cmdline). Further research led me to [dvdisaster](http://dvdisaster.net/en/index.html) which, despite being a GUI-only program, seemed more appropriate for this use case.

Both dvdisaster and parchive use the same [Reed–Solomon error correction codes](http://en.wikipedia.org/wiki/Reed–Solomon_error_correction). Dvdidaster is aimed at optical media and has the ability to place the error correction data on the disc by [augmenting the disc image](http://dvdisaster.net/en/howtos30.html), as well as [storing the data separately](http://dvdisaster.net/en/howtos20.html). It can also [scan media for errors](http://dvdisaster.net/en/howtos10.html) and assist in judging when the media is in danger of becoming defective. This makes it an attractive option for long-term storage.

I use dvdisaster with the [RS02](http://dvdisaster.net/en/howtos32.html) error correction method, which augments the image before burning. Depending on the size of the original image, this will result in the disc having anywhere from 20% to 200% redundancy.


### Verify

After the image has been augmented, I mount it and verify the signature of the encrypted file on the disc against the local copy of the signature. I've never had the signatures not match, but performing this step makes me feel better.

    #!bash
    $ sudo mount -o loop 2012.iso /mnt/disc
    $ gpg --verify 2012.tar.bz.gpg.sig /mnt/disc/2012.tar.bz.gpg
    $ sudo umount /mnt/disc


### Burn

The final step is to burn the augmented image. I always burn discs at low speeds to diminish the chance of errors during the process.

    #!bash
    $ cdrecord -v speed=4 dev=/dev/sr0 2012.iso

Similar to the optical backups of my [password database](http://pig-monkey.com/2013/04/4/password-management-vim-gnupg/), I burn two copies of each disc. One copy is stored off-site. This provides a reasonably level of assurance against any loss of my photos.

