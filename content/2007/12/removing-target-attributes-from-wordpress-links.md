Title: Removing Target Attributes from Wordpress Links
Date: 2007-12-08
Modified: 2012-09-15
Slug: removing-target-attributes-from-wordpress-links

For years, I've always added the <code>target</code> attribute to links going off-site. And for a while less, I've wished that I hadn't -- I believe that where a link opens should be left up to the user -- but never had the motivation to stop or, more importantly, go back and edit all the old links.

Till now.

Instead of the Transitional doctype, I want to validate my pages with XHTML 1.0 Strict, in which the <code>target</code> attribute is deprecated. Google had the answer, in the form of <a href="http://lorelle.wordpress.com/2005/12/01/search-and-replace-in-wordpress-mysql-database/"> Lorelle's guide on search and replacing in WP databases</a>. It's quite simple, even for one with database-fu as weak as mine. Just login to your database via phpMyAdmin, hit the SQL button on the upper left and enter your query.

Lorelle's sample is:
<pre>UPDATE wp_posts SET post_content = REPLACE (
post_content,
'Item to replace here',
'Replacement text here');</pre>

I had to change my table, which is still named from my <a href="http://cafelog.com/">b2/cafelog</a> days, and so executed this:
<pre>UPDATE b2posts SET post_content = REPLACE (
post_content,
'target="_blank"',
'');</pre>

Shiny!
