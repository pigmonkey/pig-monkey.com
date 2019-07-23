Title: Music Organization with Beets
Date: 2019-07-22
Tags: toolchain, linux, shell, annex

I organize my music with [Beets](http://beets.io/).

Beets [imports](https://beets.readthedocs.io/en/stable/reference/cli.html#import) music into my library, warns me if I'm [missing](https://beets.readthedocs.io/en/stable/plugins/missing.html) tracks, identifies tracks based on their [accoustic fingerprint](https://beets.readthedocs.io/en/stable/plugins/chroma.html), [scrubs](https://beets.readthedocs.io/en/stable/plugins/scrub.html) extraneous metadata, fetches and stores [album art](https://beets.readthedocs.io/en/stable/plugins/fetchart.html), cleans [genres](https://beets.readthedocs.io/en/stable/plugins/lastgenre.html), fetches [lyrics](https://beets.readthedocs.io/en/stable/plugins/lyrics.html), and -- most importantly -- [fetches metadata](https://beets.readthedocs.io/en/stable/plugins/mbsync.html) from [MusicBrainz](https://musicbrainz.org/). After some basic [configuration](https://github.com/pigmonkey/dotfiles/blob/master/config/beets/config.yaml), all of this happens automatically when I import new files into my library.

After the files have been imported, beets makes it easy to query my library based on any of the clean, consistent, high quality, crowd-sourced metadata.

    $ beet stats genre:ambient
    Tracks: 649
    Total time: 2.7 days
    Approximate total size: 22.4 GiB
    Artists: 76
    Albums: 53
    Album artists: 34

    $ beet ls -a 'added:2019-07-01..'
    Deathcount in Silicon Valley - Acheron
    Dlareme - Compass
    The Higher Intelligence Agency & Biosphere - Polar Sequences
    JK/47 - Tokyo Empires
    Matt Morton - Apollo 11 Soundtrack

    $ beet ls -ap albumartist:joplin
    /home/pigmonkey/library/audio/music/Janis Joplin/Full Tilt Boogie
    /home/pigmonkey/library/audio/music/Janis Joplin/I Got Dem Ol' Kozmic Blues Again Mama!

As regular readers will have surmised, the files themselves are stored in [git-annex](https://git-annex.branchable.com/).
