Title: Redundant File Storage
Date: 2016-08-19
tags: backups, linux, annex

As I've [mentioned previously](/tag/annex/), I store just about everything that matters in [git-annex](https://git-annex.branchable.com/) (the only exception is code, which is stored directly in regular git). One of git-annex's many killer features is [special remotes](https://git-annex.branchable.com/special_remotes/). They make tenable this whole "cloud storage" thing that we do now.

A special remote allows me to store my files with a large number of service providers. It makes this easy to do by abstracting away the particulars of the provider, allowing me to interact with all of them in the same way. It makes this safe to do by providing [encryption](https://git-annex.branchable.com/encryption/). These factors encourage redundancy, reducing my reliance on any one provider.

Recently I began playing with [rclone](http://rclone.org/). Rclone is a program that supports file syncing for a handful of cloud storage providers. That's semi-interesting by itself but, more significantly, there is [a git-annex special remote wrapper](https://github.com/DanielDent/git-annex-remote-rclone). That means any of the providers supported by rclone can be used as a special remote. I looked through all of rclone's supported providers and decided there were a few that I had no reason not to use.


## Hubic

[Hubic](https://hubic.com/en/) is a storage provider from [OVH](https://www.ovh.com/us/) with a data center in France. Their [pricing](https://hubic.com/en/offers/) is attractive. I'd happily pay €50 per year for 10TB of storage. Unfortunately they limit connections to 10 Mbit/s. In my experience they ended up being even slower than this. Slow enough that I don't want to give them money, but there's still no reason not to take advantage of their free 25 GB plan.

After signing up, I [setup a new remote in rclone](http://rclone.org/hubic/).

    $ rclone config
    n) New remote
    s) Set configuration password
    q) Quit config
    n/s/q> n
    name> hubic-annex
    Type of storage to configure.
    Choose a number from below, or type in your own value
     1 / Amazon Drive
       \ "amazon cloud drive"
     2 / Amazon S3 (also Dreamhost, Ceph)
       \ "s3"
     3 / Backblaze B2
       \ "b2"
     4 / Dropbox
       \ "dropbox"
     5 / Google Cloud Storage (this is not Google Drive)
       \ "google cloud storage"
     6 / Google Drive
       \ "drive"
     7 / Hubic
       \ "hubic"
     8 / Local Disk
       \ "local"
     9 / Microsoft OneDrive
       \ "onedrive"
    10 / Openstack Swift (Rackspace Cloud Files, Memset Memstore, OVH)
       \ "swift"
    11 / Yandex Disk
       \ "yandex"
    Storage> 7
    Hubic Client Id - leave blank normally.
    client_id> 
    Hubic Client Secret - leave blank normally.
    client_secret> 
    Remote config
    Use auto config?
     * Say Y if not sure
     * Say N if you are working on a remote or headless machine
    y) Yes
    n) No
    y/n> y
    If your browser doesn't open automatically go to the following link: http://127.0.0.1:53682/auth
    Log in and authorize rclone for access
    Waiting for code...
    Got code
    --------------------
    [remote]
    client_id = 
    client_secret = 
    token = {"access_token":"XXXXXX"}
    --------------------
    y) Yes this is OK
    e) Edit this remote
    d) Delete this remote
    y/e/d> y

With that setup, I went into my `~/documents` annex and added the remote.

    $ git annex initremote hubic type=external externaltype=rclone target=hubic-annex prefix=annex-documents chunk=50MiB encryption=shared rclone_layout=lower mac=HMACSHA512

I want git-annex to automatically send everything to Hubic, so I took advantage of [standard groups](https://git-annex.branchable.com/preferred_content/standard_groups/) and put the repository in the `backup` group.

    $ git annex wanted hubic standard
    $ git annex group hubic backup

Given Hubic's slow speed, I don't really want to download files from it unless I need to. This can be configured in git-annex by setting the cost of the remote. Local repositories default to 100 and remote repositories default to 200. I gave the Hubic remote a high cost so that it will only be used if no other remotes are available.

    $ git config remote.hubic.annex-cost 500

If you would like to try Hubic, I have a [referral code](https://hubic.com/home/new/?referral=FATDIA) which gives us both an extra 5GB for free.

## Backblaze B2

[B2](https://www.backblaze.com/b2/cloud-storage.html) is the cloud storage offering from backup company [Backblaze](https://www.backblaze.com/). I don't know anything about them, but at $0.005 per GB I like their [pricing](https://www.backblaze.com/b2/cloud-storage-providers.html). A quick search of reviews shows that the main complaint about the service is that they offer no geographic redundancy, which is entirely irrelevant to me since I build my own redundancy with my half-dozen or so remotes per repository.

Signing up with Backblaze took a bit longer. They wanted a phone number for 2-factor authentication, I wanted to give them a credit card so that I could use more than the 10GB they offer for free, and I had to generate an application key to use with rclone. After that, the [rclone setup](http://rclone.org/b2/) was simple.

    $ rclone config
    n) New remote
    s) Set configuration password
    q) Quit config
    n/s/q> n
    name> b2-annex
    Type of storage to configure.
    Choose a number from below, or type in your own value
     1 / Amazon Drive
       \ "amazon cloud drive"
     2 / Amazon S3 (also Dreamhost, Ceph)
       \ "s3"
     3 / Backblaze B2
       \ "b2"
     4 / Dropbox
       \ "dropbox"
     5 / Google Cloud Storage (this is not Google Drive)
       \ "google cloud storage"
     6 / Google Drive
       \ "drive"
     7 / Hubic
       \ "hubic"
     8 / Local Disk
       \ "local"
     9 / Microsoft OneDrive
       \ "onedrive"
    10 / Openstack Swift (Rackspace Cloud Files, Memset Memstore, OVH)
       \ "swift"
    11 / Yandex Disk
       \ "yandex"
    Storage> 3
    Account ID
    account> 123456789abc
    Application Key
    key> 0123456789abcdef0123456789abcdef0123456789
    Endpoint for the service - leave blank normally.
    endpoint> 
    Remote config
    --------------------
    [remote]
    account = 123456789abc
    key = 0123456789abcdef0123456789abcdef0123456789
    endpoint = 
    --------------------
    y) Yes this is OK
    e) Edit this remote
    d) Delete this remote
    y/e/d> y

With that, it was back to `~/documents` to initialize the remote and send it all the things

    $ git annex initremote b2 type=external externaltype=rclone target=b2-annex prefix=annex-documents chunk=50MiB encryption=shared rclone_layout=lower mac=HMACSHA512
    $ git annex wanted b2 standard
    $ git annex group b2 backup

While I did not measure the speed with B2, it feels as fast as my [S3](https://aws.amazon.com/s3/) or [rsync.net](http://www.rsync.net/products/git-annex-pricing.html) remotes, so I didn't bother setting the cost.

## Google Drive

While I do not regularly use Google services for personal things, I do have a Google account for Android stuff. Google Drive offers [15 GB of storage for free](https://support.google.com/drive/answer/2375123?hl=en) and [rclone supports it](http://rclone.org/drive/), so why not take advantage?

    $ rclone config
    n) New remote
    s) Set configuration password
    q) Quit config
    n/s/q> n
    name> gdrive-annex
    Type of storage to configure.
    Choose a number from below, or type in your own value
     1 / Amazon Drive
       \ "amazon cloud drive"
     2 / Amazon S3 (also Dreamhost, Ceph)
       \ "s3"
     3 / Backblaze B2
       \ "b2"
     4 / Dropbox
       \ "dropbox"
     5 / Google Cloud Storage (this is not Google Drive)
       \ "google cloud storage"
     6 / Google Drive
       \ "drive"
     7 / Hubic
       \ "hubic"
     8 / Local Disk
       \ "local"
     9 / Microsoft OneDrive
       \ "onedrive"
    10 / Openstack Swift (Rackspace Cloud Files, Memset Memstore, OVH)
       \ "swift"
    11 / Yandex Disk
       \ "yandex"
    Storage> 6
    Google Application Client Id - leave blank normally.
    client_id> 
    Google Application Client Secret - leave blank normally.
    client_secret> 
    Remote config
    Use auto config?
     * Say Y if not sure
     * Say N if you are working on a remote or headless machine or Y didn't work
    y) Yes
    n) No
    y/n> y
    If your browser doesn't open automatically go to the following link: http://127.0.0.1:53682/auth
    Log in and authorize rclone for access
    Waiting for code...
    Got code
    --------------------
    [remote]
    client_id = 
    client_secret = 
    token = {"AccessToken":"xxxx.x.xxxxx_xxxxxxxxxxx_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx","RefreshToken":"1/xxxxxxxxxxxxxxxx_xxxxxxxxxxxxxxxxxxxxxxxxxx","Expiry":"2014-03-16T13:57:58.955387075Z","Extra":null}
    --------------------
    y) Yes this is OK
    e) Edit this remote
    d) Delete this remote
    y/e/d> y

And again, to `~/documents`.

    $ git annex initremote gdrive type=external externaltype=rclone target=gdrive-annex prefix=annex-documents chunk=50MiB encryption=shared rclone_layout=lower mac=HMACSHA512
    $ git annex wanted gdrive standard
    $ git annex group gdrive backup

Rinse and repeat the process for other annexes. Revel in having simple, secure, and redundant storage.
