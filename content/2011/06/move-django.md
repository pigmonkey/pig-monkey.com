Title: A Move to Django
Date: 2011-06-11
Modified: 2012-12-22
Tags: admin, python, code, django
Slug: move-django

You may not notice much, but this blog has been completely rewritten.

I started developing in [Django](http://djangoproject.com) last winter and quickly became smitten with both the Django framework and the [Python](http://python.org). Most of the coding I've done this year has been in Python. Naturally, I had thoughts of moving this website from [Wordpress](http://wordpress.org) over to a Django-based blog.

For a while I did nothing about it. Then I had another project come up that required some basic blog functionality be added to a Django-based site. A blog is -- or, at least, can be -- a fairly simple affair, but before writing my own I decided to look around and see what else was out there. There's a number of Django-based blogs floating around ([Kevin Fricovsky has a list](http://blog.montylounge.com/2010/02/10/eleven-django-blog-engines-you-should-know/)), but few of them jumped out at me. Most were not actively developed and depended on too many stale packages for my taste, or they just had a feature set that I didn't like.

Out of all of them, two presented themselves as possibilities: [Mingus](https://github.com/montylounge/django-mingus) (written by the previously mentioned Kevin) and Nathan Borror's [django-basic-apps](https://github.com/nathanborror/django-basic-apps). Mingus tries to be a full-featured blogging application and was much too complex for the simple project I was then working on. But the blog application in django-basic-apps (a fork of which provides Mingus with its core blog functionality) looked like it would fit the bill. As the name implies, it is meant to be a very basic blog. I dived in to the code I discovered that, with a few modifications, it would do what I needed.

So I finished that project. But now having messed with blogging in Django I was more motivated to get started on rewriting my own site. I took another look at Mingus. Although it was too complex for the previous project, the features it provides are very similar to the features I wanted for this website. I looked at and thought about Mingus for a time, repeatedly turning it down and then coming back to it. The question centered around the project's staleness more than anything else. Currently, Mingus is built for Django 1.1. That's an old version. As of this writing, the current version is 1.3. Many improvements have been made in Django since 1.1 and I was not too keen to forgo them and run an old piece of code. Mingus is under active development, and will be updated for Django 1.3, but it's a hobby-project, so the work is understandably slow.

In the end, I decided that the best thing to do was go my own route, but take some pointers and inspiration from Mingus. I would make my own fork of django-basic-apps, using that blog as the basis, and build a system on top of that. I created [my fork](https://github.com/pigmonkey/django-vellum) last month and have been steadily plodding away on it in my free time. Over the course of the development I created [a few](https://github.com/pigmonkey/django-wmd) [simple](https://github.com/pigmonkey/django-badgr) [applications](https://github.com/pigmonkey/django-twat) to complement the core blog, and [contributed code](https://github.com/bartTC/django-markup/commit/13654d7159a7c8b82f1fc3e5bd222441448b3f47) to another project.

It's not quite done -- there's still a few things I want to improve -- but it's good enough to launch. (If you notice any kinks, let me know.) I'm quite pleased with it.

This is a notable occasion. I've been using Wordpress since before it was Wordpress, but it is time to move on. (Wordpress is a fork of an old piece of code called [b2/cafelog](http://cafelog.com/). My database tables have been rocking the `b2` prefix since 2002.)

As you've no doubt noticed, the look of the site hasn't changed much. I tweaked a few things here and there, but for the most part just recreated the same template as what I had written for Wordpress. I am planning on a redesign eventually. For now, I wanted to spend my time developing the actual blog rather than screwing with CSS.

So, there you have it. [Everything is open source](https://github.com/pigmonkey/django-vellum). Download it, fork it, hack it (and don't forget to send your code changes back my way). Let me know what you think. Build your own blog with it! (There's even a [script to import data from Wordpress](https://github.com/pigmonkey/django-vellum/blob/master/vellum/management/commands/wordpress_import.py).) I think it's pretty sweet. The only thing lacking is documentation, and that's my next goal.


Disqus
---------

The biggest change for the user is probably the comments, which are now powered by [Disqus](http://disqus.com/). Consider it a trial. I've seen Disqus popping up on a number of sites the past year or so. At first it annoyed me, mostly because I use [NoScript](http://noscript.net/) and did not want to enable JavaScript for another domain just to comment on a site. But after I got over that I found that Disqus wasn't too bad. As a user I found it to be on par with the standard comment systems provided by Wordpress, Blogger, and the like. The extra features don't appeal to me. But as an administrator, Disqus appeals to me more because it means that I no longer have to manage comments myself! And as a developer, I'm attracted to [some of the things](http://blog.disqus.com/post/3879996850/scaling-disqus-at-pycon-2011) that Disqus has done (they're a Python shop, and run on top of Django) and their [open source contributions](https://github.com/disqus).

So I'm giving it a shot. Disqus will happily export comments, so if I (or you) decide that I don't like it, it will be easy to move to another system.


Markdown
--------------

One final note: I like [Markdown](http://daringfireball.net/projects/markdown/). That might be an understatement.

I first starting using Markdown on [GitHub](https://github.com), which I signed up for about the same time I started with Django and Python. After learning the [syntax](http://daringfireball.net/projects/markdown/syntax) and playing with it for a few weeks, I discovered that I had a very hard time writing prose in anything else. In fact, the desire to write blog posts in Markdown was probably the biggest factor that influenced me to get off my butt and move away from Wordpress.

So, I incorporated Markdown into the blog. But rather than just making the blog Markdown-only, I took a hint from Mingus and included [django-markup](https://github.com/bartTC/django-markup), which supports rendering in many [lightweight markup languages](https://secure.wikimedia.org/wikipedia/en/wiki/Lightweight_markup_language).

Because I'm still new to Markdown and occasionally cannot remember the correct syntax, I wanted to include some version of WMD. WMD is a [What You See Is What You Mean](https://secure.wikimedia.org/wikipedia/en/wiki/WYSIWYM) editor for Markdown, a sort of alternative to [WYSIWYG](https://secure.wikimedia.org/wikipedia/en/wiki/WYSIWYG) editors like TinyMCE. (It is my believe that WYSIWYG editors are one of the worst things to happen to the Internet.) All WMD consists of is a JavaScript library. The original was written by a guy named John Fraser, who was abducted by aliens some time in 2008. Since his disappearance from the interwebs, WMD has been forked countless times. I looked around at a few found a version that I was happy with (which happens to be a fork of a fork of a fork of a fork), and rolled it into [a reusable app](https://github.com/pigmonkey/django-wmd). While I was at it, I made some visual changes to the editing area for the post body. The result is an attractive post editing area that is simple to use and produces clean code. I think it is much better than what is offered by Wordpress.
