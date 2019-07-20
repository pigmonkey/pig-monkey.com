Title: An Offline Lexicon
Date: 2019-07-19
Tags: toolchain, linux, shell

[dictd](https://sourceforge.net/projects/dict/) is a dictionary database server and client. It can be used to lookup word definitions over a network. I don't use it for that. I use the program to provide an offline dictionary. Depending on a network connection, web browser and third-party websites just to define a word strikes me as dumb.

To make this go, dictionary files must be installed. I use the [GNU Collaborative International Dictionary of English](http://gcide.gnu.org.ua/) (GCIDE), [WordNet](https://wordnet.princeton.edu/), and the [Moby Thesaurus](https://www.gutenberg.org/ebooks/3202). The GCIDE is derived from [Noah Webster's famous American dictionary](http://jsomers.net/blog/dictionary). WordNet is a more modern (one might say "dry") resource. The Moby Thesaurus is a public domain thesaurus originally built by [Grady Ward](https://en.wikipedia.org/wiki/Grady_Ward). Between these three sources I can have a pretty good grasp on the English language. No network connectivity required.

I use a shell alias to always pipe the definitions through `less`.

    def () {
        dict $1 | less
    }
