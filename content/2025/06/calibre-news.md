Title: Calibre News
Date: 2025-06-27
Tags: osint, toolchain

I follow local news -- news from my city -- daily via RSS. For anything wider in scope, I find that weekly is the correct cadence. Anything more frequent is generally a waste of time and not conducive to living life. I get my non-local news via [Calibre News](https://manual.calibre-ebook.com/news.html).

Calibre ships with a large number of [recipes](https://github.com/kovidgoyal/calibre/tree/master/recipes), which are Python modules that tell it how to download content from websites. (One can create their own recipes, but I have not bothered to do so.) When a recipe is run, Calibre fetches all content and creates a nicely formatted EPUB. Often the recipe is able to bypass paywalls, making this the best way to freely read online news.

The news functionality has a scheduler which can be used to fetch content from selected recipes in an automated and periodic fashion. It can take some experimentation to figure out what schedule makes sense for which source, as there is not any sort of duplication controls. If the source only posts updates weekly, but you have Calibre scheduled to run the recipe daily, you will end up with 7 identical EPUBs at the end of the week.

Recipes can also be executed via the command line by passing a recipe name and output filename to `ebook-convert`. This allows you to setup your own scheduler using cron or systemd timers.

    $ ebook-convert "The Economist.recipe" .epub

Calibre includes configurable controls for how many issues of a news source you want to store. You can tell it to only keep up to 3 issues, or keep all issues up to 30 days old, for instance.

Once the EPUB is in the library, Calibre takes care of automatically pushing it to connected devices and deleting old files.

The author on these files is set to `calibre`, causing them to be stored within the library in a `calibre/` directory. My library is stored as a [git-annex](https://git-annex.branchable.com/), but unlike all the actual books in my library, I consider these downloads to be ephemeral. I do not want them tracked by git, or pushed to my special remotes. I achieve this by adding `calibre/` to my `.gitignore` file.

Each of the files is tagged with `news`, so I can easily exclude them from my book searches, or filter the library for only them.

The two recipes I keep scheduled are those for [The Economist](https://www.economist.com/) and [Foreign Affairs](https://www.foreignaffairs.com/). The Economist is scheduled for every Friday. Foreign Affairs is scheduled for every 60 days. What this means in practice is that I open Calibre every Friday morning and plug in my eReader. Within a few minutes Calibre will download my weekly news from The Economist, and Foreign Affairs every other month, and sync them to the device. I read those EPUBs over the next week.

Previously I also scheduled downloads for [The Diplomat](https://thediplomat.com/), but I found that The Economist's Asia coverage was adequate enough for my needs. I've also used Calibre to download [The Atlantic](https://www.theatlantic.com/) and [Harper's](https://harpers.org/), but these days I rarely find myself in the mood for long-form articles -- I'd rather spend that time reading a book. Foreign Affairs is the exception here, but it is a worthy one. Between [the one](https://mediabiasfactcheck.com/the-economist/) and [the other](https://mediabiasfactcheck.com/foreign-affairs/) I am mostly consuming facts, which I gather is not the case for many people.

Excepting the city news in my RSS reader, my news consumption outside of these EPUBs is almost zero. This has been working well for me. I judge my success by the number of memes I do not understand.
