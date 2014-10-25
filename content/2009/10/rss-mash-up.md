Title: RSS Mash-Up
Date: 2009-10-01
Modified: 2012-09-15
Tags: admin, twitter, rss
Slug: rss-mash-up

<p class="added">This mash-up feed still exists, but you probably don't want to use it. As of May 2010, Twitter feeds are now integrated into the blog and thus are included in <a href="http://pig-monkey.com/feed/">the normal feed</a>. The mash-up feed now only mashes the blog feed and Flickr photos</p>

When I first decided to add twitter posts to my site, I debated whether I would rather have them integrated into the actual blog posts or separated. Visually, I like to have the separation, but I always thought it would be neat to pull the twitter posts directly into Wordpress' database, and so have them integrated into my RSS feed. Otherwise, for those who wish to follow my twitter posts, but are not on twitter, they have to subscribe to two different feeds -- both my blog feed and twitter feed.

Today, I had the idea of keeping the actual separation of twitter and the blog, but simply creating a new RSS feed using some sort of RSS-mash-up-aggregator thingy. I thought <a href="http://feedburner.com/">Feedburner</a> could do something like that, but apparently not. After searching around for other options and not finding anything that really excited me, I decided to just use <a href="http://pipes.yahoo.com/pipes/">Yahoo Pipes</a>. After all, this is pretty much what it was made for.

<!--more-->

Combining feeds in Pipes is pretty simple, but after mashing them together, I discovered that twitter's RSS feed is kinda ugly. Luckily, editing feeds using regular expressions in Pipes is pretty simple, too. After polishing up the twitter feed a bit, I thought Why not toss my Flickr feed into this puppy? But occasionally I'll upload a large group of photos to Flickr at a single time, and I didn't want to totally bomb my new RSS feed. Plus, most of the time when I put photos on Flickr, I create an accompanying blog post, so I wasn't sure that adding the Flickr feed to the mash-up was even necessary. I figured that I'd toss in the Flickr feed for now, but compromise by having Pipes truncate it to the 6 most recent items.

<a href="http://pipes.yahoo.com/pipes/pipe.info?_id=27c9f21436b53398e2b48ec816612563">Now I have a pretty new feed.</a>

Then came the problem of what to do with it. I didn't want to just toss up a link somewhere. I preferred the idea of replacing my normal blog feed with this new super-feed. But I also didn't want to just edit the Wordpress template header. I new Feedburner had a plugin to integrate with Wordpress, so I thought about burning the new feed and then using the Feedburner plugin to pull it in, but that seemed a little excessive, particular since I don't care about any of the click-tracking or monetizing features of Feedburner. Then I found the <a href="http://wordpress.org/extend/plugins/wp-feedlocations/">Feed Locations</a> plugin, which does exactly what I wanted: allow me to specify the location of my feed in the Wordpress admin panel.

Now, if you ask Wordpress for this site's RSS feed, you get <a href="http://pipes.yahoo.com/pipes/pipe.run?_id=27c9f21436b53398e2b48ec816612563&_render=rss">the new feed</a>. If you're opposed to all this new fanciness and just want the plain old blog feed, it's still up at the <a href="http://pig-monkey.com/feed/">same location</a>, just not linked to from anywhere.

Let me know what you think about having the Flickr photos in the feed. If it's redundant, I'll take them out.
