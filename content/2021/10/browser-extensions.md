Title: Browser Extensions
Date: 2021-10-01
Tags: toolchain

I try to keep the number of browser extensions I use to a minimum. The following are what I find necessary in [Firefox](https://www.firefox.com).

## [ClearURLS](https://gitlab.com/KevinRoebert/ClearUrls)

ClearURLs removes extra cruft from URLs. I don't really a problem with things like UTM parameters. Such things seem reasonable to me. But, more broadly, digital advertising has proved itself hostile to my interests, so I choose to be hostile right back.

## [Cookie AutoDelete](https://github.com/Cookie-AutoDelete/Cookie-AutoDelete)

Cookie AutoDelete deletes cookies after a tab is closed or the domain changes. I whitelist cookies for some of the services I run, like my RSS reader, but every other cookie gets deleted 10 seconds after I leave the site. The extension can also manage other data stores, like IndexedDB and Local Storage.

## [Feed Preview](https://code.guido-berhoerster.org/addons/firefox-addons/feed-preview/)

Feed Preview adds an icon to the address bar when a page includes an RSS or Atom feed in its header. This used to be built in to Firefox, but for some inexplicable reason they removed it some years ago now. Removing the icon broke one of the core ways that I use a web browser. As the name suggests, the extension can also render a preview of the feed. I don't use it for that. I just want my icon back.

## [Firefox Multi-Account Containers](https://github.com/mozilla/multi-account-containers)

Firefox Multi-Account Containers is a Mozilla provided extension to create different containers and assign domains to them. In modern web browser parlance, a container means isolated storage. So a cookie in container A is not visible within container B, and vice versa.

## [Temporary Containers](https://github.com/stoically/temporary-containers)

Temporary Containers is the real workhorse of my containment strategy. It generates a new, temporary container for every domain. It automatically deletes the containers it generates 5 minutes after the last tab in that container is closed. This effectively isolates all domains from one another.

## [History Cleaner](https://github.com/Rayquaza01/HistoryCleaner)

History Cleaner deletes browser history that is older than 200 days. History is useful, but if I haven't visited a URL in more than 200 days, I probably no longer care about. Having all that cruft automatically cleaned out makes it easier to find what I'm looking for in the remaining history, and speeds up autocomplete in the address bar.

## [Redirector](https://github.com/einaregilsson/Redirector)

Redirector lets you create pattern-based URL redirects. I use it to redirect Reddit URLs to [Teddit](https://github.com/teddit-net/teddit), Twitter URLs to [Nitter](https://github.com/zedeus/nitter/), and Wikipedia mobile URLs to the normal Wikipedia site.

## [Stylus](https://github.com/openstyles/stylus)

Stylus allows custom CSS to be applied to websites. I use it to make websites less eye-burningly-bright. [Dark Reader](https://addons.mozilla.org/en-US/firefox/addon/darkreader/) is another solution to this problem, but I found it to be somewhat resource intensive. Stylus lets me darken websites with no performance penalty.

## [Tree Style Tab](https://github.com/piroor/treestyletab)

Tree Style Tab moves tabs from the default horizontal bar across the top of the browser chrome to a vertical sidebar, and allows the tabs to be placed into a nested tree-like hierarchy. In a recent-ish version of Firefox, Mozilla uglified the default horizontal tab bar. This was what finally pushed me into adopting tree style tabs. It took me a couple weeks to get used to it, but now I'm a convert. I wouldn't want to use a browser without it. Unfortunately, the extension does seem to have a performance penalty. Not so much during normal use, but it definitely increases the time required to launch the browser. To me, it is worth it.

## [uBlock Origin](https://github.com/gorhill/uBlock)

uBlock Origin blocks advertisements, malware, and other waste. This extension should need no introduction. The modern web is unusable without it. Until recently I used this in combination with [uMatrix](https://github.com/gorhill/uMatrix). I removed uMatrix when it was abandoned by the author, but was pleasantly surprised to find that current versions of uBlock by itself satisfies my needs in this department.

## [User-Agent Switcher](https://gitlab.com/ntninja/user-agent-switcher)

User-Agent Switcher allows the user-agent string to be changed. It seems odd that the user would need an extension to change the user-agent string in their user agent, but here we are. I mostly use this for testing things.

## [Vim Vixen](https://github.com/ueokande/vim-vixen)

Vim Vixen allows the browser to be controlled using vim-like keys. Back in those halcyon days before Mozilla broke their extension system, I switched between two extensions called Vimperator and Pentadactyl to accomplish this. Those were both complete extensions that were able to improve every interaction point with the browser. Vim Vixen is an inferior experience, but seems to be the best current solution. It's mostly alright.

## [Wallabagger](https://github.com/wallabag/wallabagger)

Wallabagger lets me save articles to my [Wallabag](https://wallabag.org/) instance with a single click.

## [Web Archives](https://github.com/dessant/web-archives)

Web Archives allows web pages to be looked up in various archives. I just use it for quick access to the [Internet Archive's Wayback Machine](http://web.archive.org/).
