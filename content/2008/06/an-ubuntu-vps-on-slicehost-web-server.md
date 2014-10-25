Title: An Ubuntu VPS on Slicehost: Web Server
Date: 2008-06-10
Modified: 2012-12-22
Tags: vps, linux, howto, slicehost, nginx, ubuntu, php
Slug: an-ubuntu-vps-on-slicehost-web-server

<em>As <a href="http://pig-monkey.com/2008/06/09/a-move-to-slicehost/">mentioned previously</a>, I've recently moved this domain over to <a href="http://www.slicehost.com/">Slicehost</a>. What follows is Part Two of a guide, compiled from my notes, to setting up an Ubuntu Hardy VPS. See also <a href="http://pig-monkey.com/2008/06/10/an-ubuntu-vps-on-slicehost-basic-setup">Part One</a>, <a href="http://pig-monkey.com/2008/06/10/an-ubuntu-vps-on-slicehost-mail">Part Three</a>, <a href="http://pig-monkey.com/2008/06/10/an-ubuntu-vps-on-slicehost-wordpress">Part Four</a>.</em>

Now we've got a properly configured, but idle, box. Let's do something with it.

<a href="http://nginx.net/">Nginx</a> is a small, lightweight web server that's all the rage on some small corners of the Net. <a href="http://www.apache.org/">Apache</a> is extremely overkill for a small personal web server like this and, since we're limited to 256MB of RAM on this VPS, it quickly becomes a resource hog. <a href="http://www.lighttpd.net/">Lighttpd</a> is another small, lightweight web server, but I'm a fan of Nginx. Try it out.

<!--more-->

First, we need to install the web server. Nginx is now in Ubuntu's repositories:

    #!bash
    $ sudo aptitude install nginx

That's all it takes in Hardy, but if you really want a guide for it, <a href="http://articles.slicehost.com/2008/5/13/ubuntu-hardy-installing-nginx-via-aptitude">Slicehost has you covered</a>.

Slicehost has a few more useful guides to Nginx, including introductions to the config layout and how to get started with vhosts:

<ul>
<li><a href="http://articles.slicehost.com/2008/5/15/ubuntu-hardy-nginx-configuration">Nginx configuration</a></li>
<li><a href="http://articles.slicehost.com/2008/5/16/ubuntu-hardy-nginx-virtual-hosts">Nginx Virtual Hosts</a></li>
<li><a href="http://articles.slicehost.com/2008/5/16/ubuntu-hardy-nginx-virtual-host-settings">Nginx virtual host settings</a></li>
</ul>

Next up, we'll need to install MySQL and PHP, and get them working with Nginx.

Slicehost has a guide for <a href="http://articles.slicehost.com/2007/11/23/ubuntu-gutsy-mysql-and-ror">installing MySQL and Ruby on Rails</a>, which also includes suggestions on optimizing MySQL. I follow the MySQL part of the guide, stopping at "Ruby on Rails install".

Now MySQL is working, lets install PHP:

    #!bash
    $ sudo aptitude install php5-common php5-cgi php5-mysql php5-cli

To get PHP as FastCGI working with Nginx, we first have to spawn the fcgi process. There are a few different ways to do that. Personally, I use the <code>spawn-fcgi</code> app from <a href="http://www.lighttpd.net/">lighttpd</a>. To use it, we'll compile and make lighttpd, but <strong>not</strong> install it. We're only after one binary.

Lighttpd has a few extra requirements, so let's install those:

    #!bash
    $ sudo aptitude install libpcre3-dev libbz2-dev 

Now, download the source and compile lighttpd. Then copy the <code>spawn-fcgi</code> binary to <code>/usr/bin/</code>:

    #!bash
    $ wget http://www.lighttpd.net/download/lighttpd-1.4.19.tar.gz
    $ tar xvzf lighttpd-1.4.19.tar.gz
    $ cd lighttpd-1.4.19
    $ ./configure
    $ make
    $ sudo cp src/spawn-fcgi /usr/bin/spawn-fcgi

Then, create a script to launch spawn-fci (I call it <code>/usr/bin/php5-fastcgi</code>):

    #!/bin/sh
    /usr/bin/spawn-fcgi -a 127.0.0.1 -p 9000 -u www-data -C 2 -f /usr/bin/php5-cgi

The script tells spawn-fcgi to launch a fastcgi process, listening on 127.0.01:9000, owned by the web user, with only 2 child processes. You may want more child processes, but I've found 2 to be optimal.

Give the script permissions:

    #!bash
    $ sudo chmod +x /usr/bin/php5-fastcgi

I then link the script filename to a version-neutral, err, version:

    #!bash
    $ sudo ln -s /usr/bin/php5-fastcgi /usr/bin/php-fastcgi

Now we need an init script to start the process at boot. I use <a href="http://www.howtoforge.com/nginx_php5_fast_cgi_xcache_ubuntu7.04">this one from HowToForge</a>, named <code>/etc/init.d/fastcgi</code>:

    #!/bin/bash
    PHP_SCRIPT=/usr/bin/php-fastcgi
    RETVAL=0
    case "$1" in
        start)
            echo "Starting fastcgi"
            $PHP_SCRIPT
            RETVAL=$?
        ;;
	stop)
            echo "Stopping fastcgi"
            killall -9 php5-cgi
            RETVAL=$?
        ;;
	restart)
            echo "Restarting fastcgi"
            killall -9 php5-cgi
            $PHP_SCRIPT
            RETVAL=$?
        ;;
        *)
            echo "Usage: php-fastcgi {start|stop|restart}"
            exit 1
        ;;
    esac      
    exit $RETVAL

Give it permissions:

    #!bash
    $ sudo chmod 755 /etc/init.d/fastcgi

Start it:

    #!bash
    $ sudo /etc/init.d/fastcgi start

Have it start at boot:

    #!bash
    $ sudo update-rc.d fastcgi defaults

Alright, now that PHP is running how we want it to, let's tell Nginx to talk to it. To do that, add the following to your vhost server block in `/etc/nginx/sites-available/mydomain.com`, making sure to change the `SCRIPT_FILENAME` variable to match your directory structure:

    location ~ \.php$ {
        fastcgi_pass   127.0.0.1:9000;
        fastcgi_index  index.php;
        fastcgi_param  SCRIPT_FILENAME  /home/user/public_html/mydomain.com/public$fastcgi_script_name;
        include        /etc/nginx/fastcgi.conf;
    }

Now let's create that `/etc/nginx/fastcgi.conf` file that's being included above. As per the <a href="http://wiki.codemongers.com/NginxFcgiExample">Nginx wiki article</a>, mine looks like this:

    fastcgi_param  GATEWAY_INTERFACE  CGI/1.1;
    fastcgi_param  SERVER_SOFTWARE    nginx;
    fastcgi_param  QUERY_STRING       $query_string;
    fastcgi_param  REQUEST_METHOD     $request_method;
    fastcgi_param  CONTENT_TYPE       $content_type;
    fastcgi_param  CONTENT_LENGTH     $content_length;
    fastcgi_param  REQUEST_URI        $request_uri;
    fastcgi_param  DOCUMENT_URI       $document_uri;
    fastcgi_param  DOCUMENT_ROOT      $document_root;
    fastcgi_param  SERVER_PROTOCOL    $server_protocol;
    fastcgi_param  REMOTE_ADDR        $remote_addr;
    fastcgi_param  REMOTE_PORT        $remote_port;
    fastcgi_param  SERVER_ADDR        $server_addr;
    fastcgi_param  SERVER_PORT        $server_port;
    fastcgi_param  SERVER_NAME        $server_name;

Then restart Nginx:

    #!bash
    $ sudo /etc/init.d/nginx restart

Let's create a file named `test.php` in your domain's public root to see if everything is working. Inside, do something like printing <a href="http://us2.php.net/phpinfo">phpinfo</a>.

Go to http://mydomain.com/test.php. See it? Good. If you get "no input file specified" or somesuch, you broke something.

If you create an index.php, and delete any index.html or index.htm you might have, you'll notice Nginx throws a 403 Forbidden error. To fix that, find the line in your vhost config (`/etc/nginx/sites-available/mydomain.com`) under the `location /` block that reads `index index.html;` and change it to `index index.php index.html;`. Then restart Nginx.

If you want SSL with your Nginx, Slicehost has <a href="http://articles.slicehost.com/2007/12/19/ubuntu-gutsy-self-signed-ssl-certificates-and-nginx">a guide for generating the certificate</a> and <a href="http://articles.slicehost.com/2007/12/19/ubuntu-gutsy-nginx-ssl-and-vhosts">another guide for installing it</a>.

You'll want to install OpenSSL first:

    #!bash
    $ sudo aptitude install openssl

There is one bug in the second guide. In the first server module listening on port 443, which forwards www.domain1.com to domain1.com, the rewrite rule specifies the http protocol. So, in effect, what that rule does is forward you from a secure domain to unsecure: https://www.domain1.com to http://domain1.com. We want it to forward to a secure domain. Simply change the rewrite rule like thus:

    rewrite ^/(.*) https://domain1.com permanent;

Next up: <a href="http://pig-monkey.com/2008/06/10/an-ubuntu-vps-on-slicehost-mail">install a mail server</a>. (Previously, we did a <a href="http://pig-monkey.com/2008/06/10/an-ubuntu-vps-on-slicehost-basic-setup">basic setup</a>.)
