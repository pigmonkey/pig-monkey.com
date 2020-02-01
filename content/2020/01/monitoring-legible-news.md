Title: Monitoring Legible News
Date: 2020-01-31
Tags: osint, toolchain, shell

I was sent a link to [Legible News](https://legiblenews.com/) last November by someone who had read my post on the now-defunct [Breaking News](/2016/07/breaking/). Legible News is a website that simply scrapes headlines from [Wikipedia's Current Events](https://en.wikipedia.org/w/index.php?title=Portal:Current_events) once per day and presents them in a legible format. This seems like a simple thing, but is [far beyond the capabilities of most news organizations today](https://zainamro.com/notes/unbearable-news).

Legible News provides no update notification mechanism. I addressed this by plugging it into [my urlwatch system](/2019/12/urlwatch/). Initially this presented two problems: the email notification included the HTML markup, which I didn't care about, and it included both the old and new content of every changed line -- effectively sending me the news from today and yesterday.

The first problem was easily solved by using the `html2text` filter provided by [urlwatch](https://github.com/thp/urlwatch). This strips out all markup, which is what I thought I wanted. I ran this for a bit before deciding that I did want the output to contain links. What I really wanted was some sort of `html2markdown` filter.

I also realized I did not just want to be sent new lines, but every line anytime there was a change. If the news yesterday included a section titled "Armed conflicts and attacks", and the news today included a section with the same title, I wanted that in my output despite it not having changed.

I solved both of these problems using the `diff_tool` argument of urlwatch. This allows the user to pass in a special tool to replace the default use of `diff` to generate the notification output. The tool will be called with two arguments: the filename of the previously downloaded version of the URL and the filename of the current version. I wrote a simple script called `html2markdown.sh` which ignores the first argument and simply passes the second argument to [Pandoc](https://pandoc.org) for formatting. 

    #!/bin/sh

    pandoc --from html \
    --to markdown_strict \
    --reference-links \
    --reference-location=block \
    $2

This script is used as the `diff_tool` in the urlwatch job definition.

    #!yaml

    kind: url
    name: Legible News
    url: https://legiblenews.com/
    diff_tool: /home/pigmonkey/bin/html2markdown.sh

The result is the latest version of Legible News, nicely converted to Markdown, delivered to my inbox every day. The output would be even better if Legible News used semantic markup -- specifically heading elements -- but it is perfectly serviceable as is.

After I built this I discovered that [somebody had created an RSS feed for Legible News](https://feed43.com/3068865104604836.xml) using a service called [Feed43](http://feed43.com/).
