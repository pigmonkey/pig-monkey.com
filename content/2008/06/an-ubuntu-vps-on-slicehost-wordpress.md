Title: An Ubuntu VPS on Slicehost: Wordpress
Date: 2008-06-10
Modified: 2012-12-22
Tags: vps, linux, howto, slicehost, nginx, wordpress, ubuntu, css
Slug: an-ubuntu-vps-on-slicehost-wordpress

<em>As <a href="http://pig-monkey.com/2008/06/09/a-move-to-slicehost/">mentioned previously</a>, I've recently moved this domain over to <a href="http://www.slicehost.com/">Slicehost</a>. What follows is Part Four of a guide, compiled from my notes, to setting up an Ubuntu Hardy VPS. See also <a href="http://pig-monkey.com/2008/06/10/an-ubuntu-vps-on-slicehost-basic-setup">Part One</a>, <a href="http://pig-monkey.com/2008/06/10/an-ubuntu-vps-on-slicehost-web-server">Part Two</a>, and <a href="http://pig-monkey.com/2008/06/10/an-ubuntu-vps-on-slicehost-mail">Part Three</a>.</em>

I prefer to install <a href="http://wordpress.org/">Wordpress</a> via Subversion, which makes updating easier. We'll have to install Subversion on the server first:

    #!bash
    $ sudo aptitude install subversion

<!--more-->

After that, <a href="http://codex.wordpress.org/Installing/Updating_WordPress_with_Subversion#New_Install_2">the Wordpress Codex has a guide to the rest of the install</a>.

Nothing further is needed, unless you want fancy rewrites. In that case, we'll have to make a change to your Nginx vhost config at `/etc/nginx/sites-available/mydomain.com`. Add the following to your server block under `location / {`:

    # wordpress fancy rewrites
    if (-f $request_filename) {
        break;
     }
     if (-d $request_filename) {
         break;
      }
      rewrite ^(.+)$ /index.php?q=$1 last;

While we're here, I usually tell Nginx to cache static files by adding the following right above the`location / {` block:

    # serve static files directly
    location ~* ^.+\.(jpg|jpeg|gif|png|ico|zip|tgz|gz|rar|bz2|doc|xls|exe|pdf|ppt|txt|tar|mid|midi|wav|bmp|rtf|css)$ {
        root  /home/user/public_html/mydomain.com/public;
        expires 7d;
        break;
    }

That'll go in the https server section, too. Now, enable rewrites in your Wordpress config. I use the following "custom" structure:

    /%year%/%monthnum%/%day%/%postname%/

Then, restart Nginx:

    #!bash
    $ sudo /etc/init.d/nginx restart

And there you have it! You know have a working, new web server and mail server.

(Previously, we did a <a href="http://pig-monkey.com/2008/06/10/an-ubuntu-vps-on-slicehost-basic-setup">basic setup</a>, <a href="http://pig-monkey.com/2008/06/10/an-ubuntu-vps-on-slicehost-web-server">installed a web server</a>, and <a href="http://pig-monkey.com/2008/06/10/an-ubuntu-vps-on-slicehost-mail">installed a mail server</a>.)
