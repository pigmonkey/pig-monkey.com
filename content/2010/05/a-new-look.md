Title: A New Look
Date: 2010-05-07
Modified: 2012-09-15
Tags: admin, twitter, design, css, rss
Slug: a-new-look

It's been nearly two years since I last redesigned this site. Don't let me go that long again! The web is supposed to be a dynamic place, you know. Anyway, here's the new look.

It isn't drastically different from the old one. I'm still keeping it clean and simple, and the base colors are the same.

You might notice the rounded corners on some things. Yeah, that's right. Web 2.0, here I come! I think rounded corners are only acceptable if accomplished with simple CSS. CSS3 is slated to include the <code>border-radius</code> property to achieve rounded corners. The specifications are not yet finalized, but Mozilla browsers have implemented the property with <code>-moz-border-radius</code> and WebKit browsers with <code>-webkit-border-radius</code>. Those are the properties that I'm using. That means you'll get rounded corners in browsers like Firefox and Safari. Opera seems to work too. Internet Explorer, not so much. (Come on, IE has a hard enough time complying with <em>current</em> standards. You can't expect it to look to the future!)

If you notice any bugs or would like to suggest any changes, let me know. After all, the site is really for you, dear user.

<!--more-->

(I did briefly look at everything on a Windows box running IE8. It seemed to work -- other than the rounded corners, of course -- but if you notice any bugs in that particular browser, <a href="http://www.mozilla.com/en-US/firefox/switch.html">you know the drill</a>.)

Two of the things that really spurred this design are <a href="http://lab.arc90.com/experiments/readability/">Readability</a> and <a href="http://brettterpstra.com/share/readability2.html">Clippable</a>. For about a month now, I've been using these bookmarklets while reading longs articles online. They help a lot. But it's really a problem with the design of some sites that I feel the need to use them. I decided that I wanted to redesign my site with <a href="http://www.alistapart.com/topics/design/typography/">typography</a> in mind.

I'm also now integrating Twitter posts into the blog. We'll see how that goes. They're styled differently, so there is a visual distinction between a tweet and a normal post. The idea is that I'm now just using twitter as a back-end to create short posts. If I want to, I can switch to some other <a href="http://en.wikipedia.org/wiki/Microblogging">microblogging</a> service and you, the user, need never know the difference. (I could even just use Wordpress to create short posts! But that might get me kicked off the interwebs...)

Tweets integrated into the blog means tweets in the RSS feed, as well. That makes my <a href="http://pig-monkey.com/2009/10/01/rss-mash-up/">RSS mash-up</a> a bit irrelevant. If you currently subscribe to that, I'd recommend changing your subscription back to <a href="/feed/">the normal feed</a>. For those who don't want to change, I've removed the Twitter feed from the mash-up's input. That way you won't have to read each of my tweets twice. The mash-up feed will now only include the blog and Flickr stream.

<h2>Blueprint</h2>

This design is built upon the <a href="http://www.blueprintcss.org/">Blueprint</a> CSS framework. I've used it a handful of times before, but never properly. My method was always to link to the three Blueprint CSS files (<code>screen.css</code>, <code>print.css</code>, and <code>ie.css</code>) in the header and then toss in a link to my own stylesheet underneath them. I never used the <a href="http://github.com/joshuaclayton/blueprint-css/blob/master/lib/compress.rb">compressor</a>.

The idea behind the compressor is pretty simple. It allows you to maintain one central instance of Blueprint and use that to generate the CSS needed for each individual project. 

The <a href="http://jdclayton.com/blueprints_compress_a_walkthrough.html">author's walk through</a> outlines the general idea:

    	<ul>
    	<li>Keep a core Blueprint folder checked out with <a href="http://git-scm.com/">Git</a> on your computer</li>
    		<li>Create a settings.yml file within the Blueprint folder with all the specifics of each project using Blueprint</li>
    		<li>Use the command line to generate <span class="caps">CSS</span> for a project on command
    	<ul>
    	<li>Incorporating any site-specific attributes
    	<ul>
    	<li>Namespace on all Blueprint classes</li>
    		<li>Custom grid template rather than the standard 24 columns / 30px column width / 10px gutter width</li>
    	</ul>
    	</li>
    		<li>Compressing any custom <span class="caps">CSS</span> and appending to the end of the Blueprint stylesheets</li>
    		<li>Appending custom semantic selectors to the end of the Blueprint stylesheets</li>
    	</ul></li>
    	</ul>

When I first head about this, I though that the compression bit was all well and good, but I've never been really adamant about optimizing CSS for speed in the first place. I'm more concerned about compliance with standards and readability. Maintaining a central Blueprint instance didn't appeal to me much, either. What really stood out is the ability to have custom semantic selectors.

CSS frameworks are neat. I've used a handful. Like any other tool, they're not always appropriate. When they are, they have certain advantages and disadvantages. One of the main things that I dislike about them is that they encourage you to clutter your code with framework-specific junk. If you're using <a href="http://960.gs/">960.gs</a> you're going to have elements with classes like "container_x", "grid_x", "omega", and "suffix_x" all over the place. With <a href="http://developer.yahoo.com/yui/grids/">Grids</a> you'll have "yui-g", "yui-b", "yui-main", and the like. Readability of code is diminished and you'll probably end up suffering from a case of <a href="http://en.wikipedia.org/wiki/Span_and_div#Overuse">div-itis</a>. Not to mention, you can forget about a strict separation of markup and styling. Sure, you <em>could</em> copy the style definitions for the specific framework classes into the classes or IDs of your own elements, but how many folks actually take the time to do all that copying and pasting? I sure don't! The appeal in a CSS framework is to save time, not make the process of building a site longer. Plus, there's an appeal in having the framework-related styling separate from the normal site styling. Such a separation makes the framework easy to update.

This is where Blueprint's semantic classes comes in. It allows you to tell Blueprint to take one of your classes (or IDs) and apply to it the properties of one of Blueprint's classes. A-mazing.

As an example, the header of this page might look something like this if built on Blueprint without the compressor:
<pre>
<div id="top" class="span-24 last">
	<ul id="nav" class="span-18 prepend-1">
		<li><a href="#">Blog</a></li>
		<li><a href="#">Who</a></li>
		<li><a href="#">What</a></li>
		<li><a href="#">Connections</a></li>
	</ul>
	<form method="get" id="search" class="span-5 last" action="...">
        <input type="text" id="search-box" value="Search" name="s" />
    </form>
</div>

<h1 id="title" class="span-24 last">pig-monkey.com</h1>
<p id="description" class="span-23 prepend-1 last">Blah blah blah...</p>

<ul id="flickr" class="span-20 append-2 prepend-2 last">
	<li><img src="myawesomephoto.jpg" alt="My Awesome Photo" /></li>
	<li><img src="myawesomephoto2.jpg" alt="My Awesome Photo" /></li>
	<li><img src="myawesomephoto3.jpg" alt="My Awesome Photo" /></li>
	<li><img src="myawesomephoto4.jpg" alt="My Awesome Photo" /></li>
	<li><img src="myawesomephoto5.jpg" alt="My Awesome Photo" /></li>
</ul>
</pre>

Look at those framework-specific classes all over the place. Nasty. But in the Blueprint compressor settings file, I can define some semantic classes.
<pre>
"#top, h1#title" : "span-24 last"
"#top #nav" : "span-18 prepend-1"
"#top form#search" : "span-5 last"
"#description" : "span-23 prepend-1 last"
"#flickr" : "span-20 append-2 prepend-1 last"
</pre>

Now my markup looks like this:
<pre>
<div id="top">
	<ul id="nav">
		<li><a href="#">Blog</a></li>
		<li><a href="#">Who</a></li>
		<li><a href="#">What</a></li>
		<li><a href="#">Connections</a></li>
	</ul>
	<form method="get" id="search" action="...">
        <input type="text" id="search-box" value="Search" name="s" />
    </form>
</div>

<h1 id="title">pig-monkey.com</h1>
<p id="description">Blah blah blah...</p>

<ul id="flickr">
	<li><img src="myawesomephoto.jpg" alt="My Awesome Photo" /></li>
	<li><img src="myawesomephoto2.jpg" alt="My Awesome Photo" /></li>
	<li><img src="myawesomephoto3.jpg" alt="My Awesome Photo" /></li>
	<li><img src="myawesomephoto4.jpg" alt="My Awesome Photo" /></li>
	<li><img src="myawesomephoto5.jpg" alt="My Awesome Photo" /></li>
</ul>
</pre>

Clean as a whistle! No useless <code>div</code>s, all elements semantically named, and not dependent on any framework.

As great as the compressor is, I do have a couple problems with it. When using the compressor, Blueprint intends that you only have 3 final (compressed) stylesheets: <code>screen.css</code>, <code>print.css</code>, and <code>ie.css</code>. Wordpress, of course, requires a <code>style.css</code> file to define the template. That's no problem. I just a create a <code>style.css</code> file that has the theme information in it and then toss in a <code>@import url('blueprint/screen.css')</code>. Then in the Wordpress header I can put a link to <code>style.css</code>, <code>print.css</code>, and <code>ie.css</code>. Everybody's happy.

Styling a website basically boils down to making a small change to the stylesheet and refreshing the page to see how that looks. Running the compressor after each change to combine the custom stylesheet with the <code>screen.css</code> file is not productive. So for the development process I tossed a <code>@import url('blueprint/custom.css')</code> into the main <code>style.css</code> file. That works fine.

Then I finish building the theme. I'm ready to compress the stylesheets, so I remove the call to the custom stylesheet in <code>style.css</code>. I tell the compressor where the custom stylesheet is and have it combine it with the <code>screen.css</code> file. I run the compressor, reload the site, and everything explodes.

Just when I thought I was done!

The problem is that in the stylesheet the compressor generates, it puts my custom styles above the semantic classes. Throughout the development process, I was calling the <code>screen.css</code> file (which includes the semantic classes) <em>before</em> the custom stylesheet. As you no doubt know, stylesheets <em>cascade</em>. You can't just switch up the order of elements without breaking stuff.

Oh well, I thought. At this point I was tired working on the site and didn't care enough to fight it. I just put the line to call the custom sheet back in <code>style.css</code> after Blueprint's <code>screen.css</code> file. I still feel like the whole semantic classes bit is enough of a reason to use the compressor, even if I'm not actually compressing my main stylesheet!
