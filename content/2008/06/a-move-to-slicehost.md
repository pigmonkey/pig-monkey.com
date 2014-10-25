Title: A Move to Slicehost
Date: 2008-06-09
Modified: 2012-09-15
Tags: slicehost, vps
Slug: a-move-to-slicehost

Yesterday I moved this domain over to <a href="http://www.slicehost.com/">Slicehost</a>.

<a href="http://blog.gordaen.com/">Ian</a> first told me about Slicehost when we were both looking to move away from Dreamhost last November. Initially, we both intended to find another shared host, but that proved far too difficult -- it seems most hosting companies have something against shared hosting with decent limits and ssh access (that last part is the kicker).

I signed up with Slicehost at the end of last year and tinkered around with it for a month or so, experimenting with setting up the server in different ways. Eventually, I found an Ubuntu-Nginx-PHP-MySQL-Postfix-Dovecot setup that I enjoyed, and one which I was comfortable administering. In the beginning of the year, I moved a couple of my domains over to the Slice. It's been a great experience. I'm not sure why it took me 6 months to finally move this domain -- my primary one -- over. Running a VPS is deceivingly simple* and well worth the effort. If you're currently running on a shared host and have some basic competency in a UNIX environment, I'd recommend giving it a shot.

In a bit I'll post a series of guides, compiled from my notes, on how I setup the server.

* It's deceivingly simple if you're not running a full mail server with virtual users running around everywhere. That part was a pain. Hence, the <a href="http://pig-monkey.com/2008/06/09/google-apps/">move to Google</a>.
