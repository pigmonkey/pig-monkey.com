Title: I use FeedIron to repair neutered RSS feeds.
Date: 2019-12-17
Tags: micro, toolchain

[FeedIron](https://github.com/feediron/ttrss_plugin-feediron/) is a plugin for my feed reader, [Tiny Tiny RSS](https://tt-rss.org/). It takes broken, partial feeds and extracts the full article content, allowing me to read the article in my feed reader the way god intended. The plugin can be configured to extract content using [a number of filters](https://github.com/feediron/ttrss_plugin-feediron/#filters). I find that using [the xpath filter](https://github.com/feediron/ttrss_plugin-feediron/tree/master/filters/fi_mod_xpath) to specify an element on the page like `div[@class='entry-content']` corrects most neutered feeds.
