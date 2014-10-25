Title: Strategies for Working Offline
Date: 2012-10-20
Modified: 2012-12-22
Tags: linux
Slug: working-offline

Earlier this year I went through a period where I had only intermittent internet access. Constant, high-speed internet access is so common these days that I had forgotten what it was like to work on a computer that was offline more often than it was online. It provided an opportunity to reevaluate some aspects of how I work with data.

## E-Mail

For a period of a couple years I accessed my mail through the Gmail web interface exclusively. About a year ago, I moved back to using a local mail client. That turned out to be a lucky move for this experience. I found that I had three requirements for my mail:

1. I needed to be able to read mail when offline (all of it, attachments included),
2. compose mail when offline,
3. and queue messages up to be automatically sent out the next time the mail client found that it had internet access.

Those requirements are fairly basic. Most mail clients will handle them without issue. I've always preferred to connect to my mail server via IMAP rather than POP3. Most mail clients offer to cache messages retrieved over IMAP. They do this for performance reasons rather than to provide the ability to read mail offline, but the result is the same. For mail clients like [Mutt](http://www.mutt.org/) that don't have built-in caching, a tool like [OfflineImap](http://offlineimap.org/) is great.

## Wikipedia

Wikipedia is too valuable a resource to not have offline access to. There are [a number of options](https://en.wikipedia.org/wiki/Wikipedia:Database_download) for getting a local copy. I found [Kiwix](http://www.kiwix.org/index.php/Main_Page) to be a simple and effective solution. It downloads a compressed copy of the Wikipedia database and provides a web-browser-like interface to read it. The English Wikipedia is just shy of 10 gigabytes (other languages are of course available). That includes all articles, but no pictures, history or talk pages. Obviously this is something you want to download *before* you're depending on coffee shops and libraries for intermittent internet access. After Kiwix has downloaded the database, it needs to be indexed for proper searching. Indexing is a resource-intensive process that will take a long time, but it's worth it. When it's done, you'll have a not-insignificant chunk of our species' combined knowledge sitting on your hard-drive. (It's the next best thing to the [Guide](https://en.wikipedia.org/wiki/The_Hitchhiker%27s_Guide_to_the_Galaxy), really.)

## Arch Wiki

For folks like myself who run [Arch Linux](https://www.archlinux.org/), the [Arch Wiki](https://wiki.archlinux.org/) is an indispensable resource. For people who use other distributions, it's less important, but still holds value. I think it's the single best repository of Linux information out there.

For us Arch users, getting a local copy is simple. The [arch-wiki-docs](https://www.archlinux.org/packages/community/any/arch-wiki-docs/) package provides a flat HTML copy of the wiki. Even better is the [arch-wiki-lite](https://www.archlinux.org/packages/community/any/arch-wiki-lite/) package which provides a console interface for searching and viewing the wiki.

Users of other distributions could, at a minimum, extract the contents of the `arch-wiki-docs` package and grep through it.

## Tunneling

Open wireless networks are dirty places. I'm never comfortable using them without tunneling my traffic. An anonymizing proxy like [Tor](https://www.torproject.org/) is overkill for a situation like this. A full-fledged VPN is the best option, but I've found [sshuttle](https://github.com/apenwarr/sshuttle) to make an excellent poor-man's VPN. It builds a tunnel over SSH, while addressing some of the shortcomings of vanilla SSH port forwarding. All traffic is forced through the tunnel, including DNS queries. If you have a VPS, a shared hosting account, or simply a machine sitting at home, `sshuttle` makes it dead simple to protect your traffic when on unfamiliar networks.

## YouTube

YouTube is a great source of both education and entertainment. If you are only going to be online for a couple hours a week, you probably don't want to waste those few hours streaming videos. There's a number of browser plugins that allow you to download YouTube videos, but my favorite solution is a Python program called [youtube-dl](https://github.com/rg3/youtube-dl/). (It's unfortunately named, as it also supports downloading videos from [other sites](http://rg3.github.com/youtube-dl/documentation.html#d4) like Vimeo and blip.tv.) You pass it the URL of the YouTube video page and it grabs the highest-quality version available. It has a number of powerful options, but for me the killer feature is the ability to download whole playlists. Say you want to grab every episode of the great web-series [Sync](https://www.youtube.com/playlist?list=PL168F329FADED6741). Just pass the URL of the playlist to `youtube-dl`.

    $ youtube-dl -t https://www.youtube.com/playlist?list=PL168F329FADED6741

That's it. It goes out and grabs every video. (The `-t` flag tells it to use the video's title in the file name.) If you come back a few weeks later and think there might have been a couple new videos added to the playlist, you can just run the same command again but with the `-c` flag, which tells it to resume. It will see that it already downloaded part of the playlist and will only get videos that it doesn't yet have.

Even now that I'm back to having constant internet access, I still find myself using `youtube-dl` on a regular basis. If I find a video that I want to watch at a later time, I download it. That way I don't have to worry about buffering, or the video disappearing due to DMCA take-down requests.

## Backups

I keep [backitup.sh](http://pig-monkey.com/2012/10/3/back-it-up/) in my network profile so that my online backups attempt to execute whenever I get online. If you're only online once or twice a week, you probably have more important things to do than remembering to manually trigger your online backups. It's nice to have that automated.
