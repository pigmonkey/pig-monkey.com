Title: Tarsnapper: Managing Tarsnap Backups
Date: 2012-09-16
Modified: 2012-12-22
Tags: python, backups, code, crypto, linux
Slug: tarsnapper-managing-tarsnap-backups

[Tarsnap](http://www.tarsnap.com/) bills itself as "online backups for the truly paranoid". I began using the service last January. It fast became my preferred way to backup to the cloud. It stores data on [Amazon S3](http://aws.amazon.com/s3/) and costs $0.30 per GB per month for storage and $0.30 per GB for bandwidth. Those prices are higher than just using Amazon S3 directly, but Tarsnap implements some impressive data de-duplication and compression that results in the service costing very little. For example, I currently have 67 different archives stored in Tarsnap from my laptop. They total 46GB in size. De-duplicated that comes out to 1.9GB. After compression, I only pay to store 1.4GB. Peanuts.

Of course, the primary requirement for any online backup service is encryption. [Tarsnap delivers](http://www.tarsnap.com/security.html). And, most importantly, the Tarsnap client is open-source, so the claims of encryption can actually be verified by the user. The majority of for-profit, online backup services out there fail on this critical point.

So Tarsnap is amazing and you should use it. The client follows the [Unix philosophy](https://en.wikipedia.org/wiki/Unix_philosophy): "do one thing and do it well". It's basically like [tar](https://www.gnu.org/software/tar/). It can create archives, read the contents of an archive, extract archives, and delete archives. For someone coming from an application like [Duplicity](http://duplicity.nongnu.org/), the disadvantage to the Tarsnap client is that it doesn't include any way to automatically manage backups. You can't tell Tarsnap how many copies of a backup you wish to keep, or how long backups should be allowed to age before deletion.

Thanks to the de-duplication and compression, there's not a great economic incentive to not keep old backups around. It likely won't cost you *that* much extra. But I like to keep things clean and minimal. If I haven't used an online backup in 4 weeks, I generally consider it stale and have no further use for it.

To manage my Tarsnap backups, I wrote a Python script called [Tarsnapper](https://github.com/pigmonkey/backups/blob/master/tarsnapper.py). The primary intent was to create a script that would automatically delete old archives. It does this by accepting a maximum age from the user. Whenever Tarsnapper runs, it gets a list of all Tarsnap archives. The timestamp is parsed out from the list and any archive that has a timestamp greater than the maximum allowed age is deleted. This is seamless, and means I never need to manually intervene to clean my archives.

Tarsnapper also provides some help for creating Tarsnap archives. It allows the user to define any number of named archives and the directories that those archives should contain. On my laptop I have four different directories that I backup with Tarsnap, three of them in one archive and the last in another archive. Tarsnapper knows about this, so whenever I want to backup to Tarsnap I just call a single command.

Tarsnapper also can automatically add a suffix to the end of each archive name. This makes it easier to know which archive is which when you are looking at a list. By default, the suffix is the current date and time.

Configuring Tarsnapper can be done either directly by changing the variables at the top of the script, or by creating a configuration file named `tarsnapper.conf` in your home directory. The config file on my laptop looks like this:

    #!bash
    [Settings]
    tarsnap: /usr/bin/tarsnap

    [Archives]
    nous-cloud: /home/pigmonkey/work /home/pigmonkey/documents /home/pigmonkey/vault/
    nous-config: /home/pigmonkey/.config

There is also support for command-line arguments to specify the location of the configuration file to use, to delete old archives and exit without creating new archives, and to execute only a single named-archive rather than all of those that you may have defined.

    $ tarsnapper.py --help
    usage: tarsnapper.py [-h] [-c CONFIG] [-a ARCHIVE] [-r]

    A Python script to manage Tarsnap archives.

    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            Specify the configuration file to use.
      -a ARCHIVE, --archive ARCHIVE
                            Specify a named archive to execute.
      -r, --remove          Remove archives old archives and exit.


It makes using a great service very simple. My backups can all be executed simply by a single call to Tarsnapper. Stale archives are deleted, saving me precious picodollars. I use this system on my laptop, as well as multiple servers. If you're interested in it, Tarsnapper can be [downloaded directly from GitHub](https://github.com/pigmonkey/backups/blob/master/tarsnapper.py). You can clone my entire [backups repository](https://github.com/pigmonkey/backups) if you're also interested in the other scripts I've written to manage different aspects of backing up data.

