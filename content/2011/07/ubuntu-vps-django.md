Title: An Ubuntu VPS for Django
Date: 2011-07-19
Modified: 2012-12-22
Tags: shell, postfix, vps, python, linux, howto, django, nginx, ubuntu
Slug: ubuntu-vps-django

Three years ago I wrote [a guide to building a VPS web server](http://pig-monkey.com/2008/06/10/an-ubuntu-vps-on-slicehost-basic-setup/) for serving sites in a PHP environment. That setup served me well for some time, but most of the sites I run now -- [including this one](http://pig-monkey.com/2011/06/11/move-django/) -- are now written in Python. Earlier this year I built another web server to reflect this. It's similar to before; I still use Ubuntu and I still like to serve pages with nginx. But PHP has been replaced with Python, and many of the packages used to build the environment have changed as a result. As with the last time, I decided to compile my notes into a guide, both for my own reference and in case anyone else would like to duplicate it. So far, the server has proven to be fast and efficient. It serves Python using uWSGI, uses a PostgreSQL database, and includes a simple mail server provided by Postfix. I think it's a good setup for serving simple Django-based websites.

Basic Setup
----------------

[As with last time](http://pig-monkey.com/2008/06/10/an-ubuntu-vps-on-slicehost-basic-setup), I recommend following [Slicehost's basic server setup article](http://articles.slicehost.com/2010/4/30/ubuntu-lucid-setup-part-1). It discusses user administration, SSH security, and firewalls. I no longer use Slicehost as my VPS provider, but I find that Slicehost's articles provide an excellent base regardless of the host.


###Packages

Packages should upgraded immediately to address any known security vulnerabilities.

    #!bash
    $ sudo apt-get update
    $ sudo apt-get upgrade

After the repositories have been updated, I install some essential packages.

    #!bash
    $ sudo apt-get install build-essential screen dnsutils

[Build-essential](http://packages.ubuntu.com/lucid/build-essential) includes necessary tools to compile programs. I am incapable of using a computer that does not have [screen](http://packages.ubuntu.com/lucid/screen) on it, so that gets installed too. The third package, [dnsutils](http://packages.ubuntu.com/lucid/dnsutils), is optional, but includes `dig` which is useful for troubleshooting DNS issues.


###DenyHosts

Slicehost's setup article recommends turning off password authentication in SSH, forcing users to login with keys only. I use keys whenever I can, but I appreciate the option of being able to login to my server from any computer, when I may or may not have my SSH key with me. So I leave password authentication enabled. This presents the possibility of brute-force attacks. Enter [DenyHosts](http://denyhosts.sourceforge.net/). DenyHosts, which I have [discussed previously](http://pig-monkey.com/2008/10/03/thoughts-on-ssh-security/) attempts to protect against SSH attacks by banning hosts after a certain number of failed login attempts. When password authentication is enabled, running DenyHosts is a smart move.

    #!bash
    $ sudo apt-get install denyhosts
    $ sudo vim /etc/denyhosts.conf


###Personalize the Environment

I use `update-alternatives` to set my default editor to [vim](http://www.vim.org).

    #!bash
    $ sudo update-alternatives --config editor

All of my personal configuration files are kept in a [github repository](https://github.com/pigmonkey/dotfiles). I'll check out that repository into `~/src` and install the files.

    #!bash
    $ mkdir ~/src
    $ cd ~/src
    $ sudo apt-get install git-core
    $ git clone git://github.com/pigmonkey/dotfiles.git
    $ ln -s ~/src/dotfiles/bash_profile ~/.bash_profile
    $ ln -s ~/src/dotfiles/bashrc ~/.bashrc
    $ ln -s ~/src/dotfiles/bash_aliases ~/.bash_aliases
    $ ln -s ~/src/dotfiles/bash_colors ~/.bash_colors
    $ ln -s ~/src/dotfiles/vimrc ~/.vimrc
    $ ln -s ~/src/dotfiles/vim ~/.vim
    $ ln -s ~/src/dotfiles/screenrc ~/.screenrc
    $ source ~/.bash_profile


###Time

The next step is to set the server's timezone and sync the clock with [NTP](http://www.ntp.org).

    #!bash
    $ sudo dpkg-reconfigure tzdata
    $ sudo apt-get install ntp


###Rootkits

There's no reason not to run both [chkrootkit](http://www.chkrootkit.org/) and [rkhunter](http://rkhunter.sourceforge.net) to check for rootkits and related vulnerabilities.


####chrkrootkit

Slicehost has [an excellent article for setting up and using chkrootkit](http://articles.slicehost.com/2010/3/24/scanning-for-rootkits-with-chkrootkit-updated).

Later on I'll be installing some Python development packages. One of them creates a directory called `/usr/lib/pymodules/python2.6/.path`, which sets off a warning in chkrootkit. Part of chkrootkit's desgin philosophy is to not include any whitelists: if chkrootkit finds something that it doesn't like, you're going to hear about it. I have cron run chkrootkit nightly and I want to receive any warnings, but I don't want to receive the same false positive every morning in my inbox.

The solution is to create a file that contains chkrootkit's warning. I call that file `whitelist` and store it in the same directory as chkrootkit. When chkrootkit is run, any output is redirected to a file. That file is compared to the whitelist using `diff` and the output *of that* -- if any -- is then read. At the end, the file containing chkrootkit's output is deleted so that the working directory is ready for the next run. The effect is that I only hear warnings from chkrootkit that I *have not explicit whitelisted*. All of this can be accomplished in a single crontab entry.

    #!bash
    0 3 * * * (cd /home/demo/src/chkrootkit-0.49; ./chkrootkit -q > message 2>&1; diff -w whitelist message; rm -f message)


####rkhunter

I'm sure it doesn't surprise you that I'm going to recommend reading Slicehost's [article on rkhunter](http://articles.slicehost.com/2010/3/24/scanning-for-rootkits-with-rkhunter-updated).

Unlike chkrootkit, rkhunter does allow for whitelists. On a clean Ubuntu 10.04 system, I find that I need to whitelist a few items in the config.

    #!bash
    $ sudo vim /etc/rkhunter.conf

    SCRIPTWHITELIST="/usr/sbin/adduser /usr/bin/ldd /bin/which"
    ALLOWHIDDENDIR="/dev/.udev /dev/.initramfs"
    APP_WHITELIST="openssl:0.9.8k gpg:1.4.10"

    $ sudo /usr/local/bin/rkhunter --propupd

The script that my cronjob runs is slightly different from the one demonstrated in the Slicehost article. Their script executes a few commands, groups the output together, and sends it to `mail` to email the system administrator. This results in daily emails, regardless of whether rkhunter finds any warnings or not. My script is simpler and does not result in so many messages.

    #!bash
    #!/bin/sh
    /usr/local/bin/rkhunter --versioncheck -q
    /usr/local/bin/rkhunter --update -q
    /usr/local/bin/rkhunter --cronjob --report-warnings-only

The version check and update commands both have the `-q` switch, which disables any output -- I don't care to know whether rkhunter updated itself or not. The final line actually executes the scan. Notice that there's no reference to `mail`. This script does not send any messages. The reason for that is that rkhunter itself provides the mail functionality. Inside of `/etc/rkhunter.conf` there is a `MAIL-ON-WARNING` variable. As long as the machine has an smtp server on it (which I'll get to later in this guide), simply filling in this variable will result in any warnings being emailed to the system administrator.


Web Server
----------------

With the basics complete, it's time to start serving something! In my [previous article](http://pig-monkey.com/2008/06/10/an-ubuntu-vps-on-slicehost-web-server/) I covered serving a PHP-based Wordpress site via FastCGI and nginx. This time around the stack will be different: [nginx](http://nginx.org/), [uWSGI](http://projects.unbit.it/uwsgi/), [Python](http://www.python.org/), and [Django](http://www.djangoproject.com/).

A few basic packages will help flesh out the server's Python development environment:

    #!bash
    $ sudo apt-get install python-psycopg2 python-setuptools python2.6-dev psmisc python-imaging locate python-dateutil libxml2-dev python-software-properties


###uWSGI

Installing [uWSGI](http://projects.unbit.it/uwsgi/) is a simple matter of compiling it and moving the resulting binary into one of your system's bin directories.

    #!bash
    $ cd ~/src/
    $ wget http://projects.unbit.it/downloads/uwsgi-0.9.8.tar.gz
    $ tar xvzf ~/uwsgi-0.9.8.tar.gz
    $ cd uwsgi-0.9.8/
    $ make -f Makefile.Py26
    $ sudo cp uwsgi /usr/local/sbin


###nginx

The [nginx](http://nginx.org/) package in Ubuntu's official repositories is always notoriously outdated. It used to be you had to compile the server from source, but there is now an [Ubuntu PPA](https://launchpad.net/ubuntu/+ppas) for the latest stable versions. [As described by the nginx wiki](http://wiki.nginx.org/Install#Ubuntu_PPA), all that is needed is to add the PPA to your `sources.list` and `apt-get` away!

    #!bash
    $ sudo add-apt-repository ppa:nginx/stable
    $ sudo apt-get update 
    $ sudo apt-get install nginx


###Python and Django

If you do Python development and haven't heard of [virtualenv](http://pypi.python.org/pypi/virtualenv), it is well worth reading up on. It allows the user to create an isolated, virtual Python environment for each project. This helps immensely when developing (or serving) multiple projects on a single machine. Needless to say, I consider it to be a required package.


####Install

I'll be installing virtualenv and [virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper) (a set of scripts to facilitate working with virtual environments). I also prefer [pip](http://pypi.python.org/pypi/pip) over `easy_install` for managing Python packages.

    #!bash
    $ sudo easy_install -U pip 
    $ sudo pip install virtualenv
    $ sudo pip install virtualenvwrapper


####Setup a virtual environment

Virtual environments can be stored wherever you fancy. For now, I keep them in a hidden folder in my home directory. For these examples, I'll setup an environment called `myproject`.

    #!bash
    $ mkdir ~/.virtualenvs
    $ cd ~/.virtualenvs
    $ virtualenv --no-site-packages --distribute myproject

Notice the `--no-site-packages` switch. That tells `virtualenv` to create this environment without any of the Python packages already installed, creating a completely fresh, clean environment. The `--distribute` switch causes the new virtual environment to be setup with [distribute](http://packages.python.org/distribute/), a replacement for the old and rather broken [setuptools](http://pypi.python.org/pypi/setuptools).

All that's needed to get `virtualenvwrapper` up and running is to add two lines to your `.bashrc` and re-source the file.

    #!bash
    $ vim ~/.bashrc
    
    export WORKON_HOME=$HOME/.virtualenvs
    source /usr/local/bin/virtualenvwrapper.sh
    
    $ . ~/.bashrc

We can now use commands like `workon` to ease the process of activating a certain environment.

I'll go ahead and install [yolk](http://pypi.python.org/pypi/yolk) in the environment to help manage packages.

    #!bash
    $ workon myproject
    $ pip install yolk
    $ yolk -l

The last command will cause `yolk` to list all packages installed in the environment. Try deactivating the environment and then running `yolk` again.

    #!bash
    $ deactivate
    $ yolk -l
    yolk: command not found

'yolk' wasn't found, because it was only installed within the virtual environment. Neat!


####Install Django

Finally, it's time to install Django! The process is simple enough.

    #!bash
    $ workon myproject
    $ pip install django

And that's it!

The [Python Imaging Library](http://www.pythonware.com/products/pil/) is likely to be needed for any Django project. I installed it in the beginning of this section, but because I used the `--no-site-packages` when creating my virtual environment, it is not available for use within the project. To fix that, I'll just link the package in. I also previously installed [psyopg2](http://initd.org/psycopg/), which Python will need to communicate with my PostgreSQL database, so I'll link that in as well. `psyopg2` depends on [mx](http://www.egenix.com/products/python/mxBase/), which was also previously installed but still must be made available in the environment.

    #!bash
    $ cdsitepackages
    $ ln -s /usr/lib/python2.6/dist-packages/PIL
    $ ln -s /usr/lib/python2.6/dist-packages/PIL.pth
    $ ln -s /usr/lib/python2.6/dist-packages/psycopg2
    $ ln -s /usr/lib/python2.6/dist-packages/mx

That wasn't too painful!


####Create a Django project

While I'm still in the virtual environment, I'll go ahead and create a new Django project. The project will have the same name as the environment: `myproject`. For this tutorial, I'll stick with the precedence set by the Slicehost tutorials and use `demo` as the name of both my user and group on the server.

I like to keep my sites in the `/srv/` directory. I structure them so that the code that runs the site, any public files, logs, and backups are all stored in separate sub-directories.

    #!bash
    $ cd /srv/
    $ sudo mkdir -p myproject.com/{code,public,logs,backup}
    $ sudo mkdir -p myproject.com/public/{media,static}
    $ sudo chown -R demo:demo myproject.com
    $ cd myproject.com
    $ sudo chown -R :www-data logs public
    $ sudo chmod -R g+w logs public
    $ cd code/
    $ django-admin.py startproject myproject

Notice that the `logs` and `public` directories were `chown`ed to the www-data group. That is the name of the user and group that nginx will run as. The web server will need permissions to write to those locations.


####Save Requirements

With the environment setup and all the necessary packages installed, now is a good time to tell pip to [freeze](http://www.pip-installer.org/en/latest/#freezing-requirements) all the packages and their versions. I keep this file in a `deploy` folder in my project.

    #!bash
    $ mkdir /srv/myproject.com/code/deploy
    $ pip freeze > /srv/myproject.com/code/deploy/requirements.txt

Now, if I needed to recreate the virtual environment somewhere else, I could just tell pip to install all the packages from that file.

    #!bash
    $ pip install -r /srv/myproject.com/code/deploy/requirements.txt


###Configure uWSGI

Now that I have something to serve, I'll configure uWSGI to serve it. The first step is to create a configuration file for the project. I call mine `wsgi.py` and store it in `/srv/myproject.com/code/myproject/`. It appends the current directory to the Python path, specifies the Django settings file for the project, and registers the WSGI handler.

    #!python
    import sys
    import os
    
    sys.path.append(os.path.abspath(os.path.dirname(__file__)))
    os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'
    
    import django.core.handlers.wsgi
    
    application = django.core.handlers.wsgi.WSGIHandler()

With that done, the next step is to decide how uWSGI should be run. I'm going to use Ubuntu's [upstart](http://upstart.ubuntu.com/) to supervise the service. I keep the upstart script in my project's `deploy/` directory.

    #!bash
    $ vim /srv/myproject.com/code/deploy/uwsgi.conf

    description "uWSGI server for My Project"
    
    start on runlevel [2345]
    stop on runlevel [!2345]
    
    respawn
    exec /usr/local/sbin/uwsgi \
    --home /home/demo/.virtualenvs/myproject/ \
    --socket /var/run/myproject.com.sock \
    --chmod-socket \
    --pythonpath /srv/myproject.com/code/ \
    --module myproject.wsgi \
    --process 2 \
    --harakiri 30 \
    --master \
    --logto /srv/myproject.com/logs/uwsgi.log

Sadly, upstart doesn't seem to recognize links. Rather than linking the config file into `/etc/init/`, I have to copy it.

    #!bash
    $ sudo cp /srv/myproject.com/code/deploy/uwsgi.conf /etc/init/uwsgi-myproject.conf


###Configure nginx

Nginx's configuration is pretty straight-forward. If you've never configured the server before, [Slicehost's articles](http://articles.slicehost.com/nginx) can set you down the right path. My own nginx config looks something like this:

    user www-data www-data;
    worker_processes 4;
    pid /var/run/nginx.pid;
    
    events {
            worker_connections 768;
            use epoll;
    }
    
    http {
    
        ##
        # Basic Settings
        ##
        
        sendfile on;
        tcp_nopush on;
        tcp_nodelay on;
        keepalive_timeout 30;
        types_hash_max_size 2048;
        # server_tokens off;
        
        # server_names_hash_bucket_size 64;
        # server_name_in_redirect off;
        
        include /etc/nginx/mime.types;
        default_type application/octet-stream;
        
        ##
        # Logging Settings
        ##
        
        access_log /var/log/nginx/access.log;
        error_log /var/log/nginx/error.log;
        
        ##
        # Gzip Settings
        ##
        
        gzip on;
        gzip_disable "msie6";
        gzip_types text/plain text/css application/json application/x-javascript text/xml application/xml application/xml+rss text/javascript;
        gzip_proxied any;
        gzip_comp_level 2;
        
        # gzip_vary on;
        # gzip_buffers 16 8k;
        # gzip_http_version 1.1;
        
        ##
        # Virtual Host Configs
        ##
        
        include /etc/nginx/conf.d/*.conf;
        include /etc/nginx/sites-enabled/*;
    }

I keep the virtual host config for my project inside the project's `code/deploy/` directory. A basic virtual host for a Django project would looks like this:

    server {
        listen 80;
        server_name www.myproject.com;
        rewrite ^/(.*) http://myproject.com/$1 permanent;
    }
    
    server {
        listen 80;
        server_name myproject.com;
        
        access_log /srv/myproject.com/logs/access.log;
        error_log /srv/myproject.com/logs/error.log;
        
        location /media {
            root /srv/myproject.com/public/;
        }

        location /static {
            root /srv/myproject.com/public/;
        }

        location / {
            uwsgi_pass unix:///var/run/myproject.com.sock;
            include uwsgi_params;
        }
    }

To install and enable the virtual host, I'll link the configuration file first to the nginx `sites-available` directory, and then link that link to the `sites-enabled` directory.

    #!bash
    $ sudo ln -s /srv/myproject.com/code/deploy/nginx.conf /etc/nginx/sites-available/myproject.com
    $ sudo ln -s /etc/nginx/sites-available/myproject.com /etc/nginx/sites-enabled/myproject.com


###SSL

If you need to encrypt communications, [Linode has a tutorial](http://library.linode.com/web-servers/nginx/configuration/ssl) on using both self-signed certificates and commercial certificates with nginx.


###Fire it Up

Nginx should be set to talk to uWSGI, which should be set to talk to the Django project. Time for a test run!

    #!bash
    $ sudo start uwsgi-myproject
    $ sudo /etc/init.d/nginx start


###memcached

Django has a very good built-in [cache framework](https://docs.djangoproject.com/en/dev/topics/cache/). I like to take advantage of it with a memory-based backend: namely, [memcached](http://memcached.org/). It's fast, efficient, and easy to setup.

All that's needed is to install memcached on the server, followed by the Python API [python-memcached](http://www.tummy.com/Community/software/python-memcached/). 

    #!bash
    $ sudo apt-get install memcached
    $ workon myproject
    $ pip install python-memcached

The default configuration file in Ubuntu lives at `/etc/memcached.conf`. I usually stick with the defaults, but sometimes end up changing the port that memchached runs on or the amount of memory it is allowed to use.


###logrotate

With the web server more-or-less complete, I like to setup logrotate to manage the logs in my project's directory. Once again, Slicehost has [an excellent introduction to logrotate](http://articles.slicehost.com/2010/6/30/understanding-logrotate-on-ubuntu-part-1) and [an example config for virtual hosts](http://articles.slicehost.com/2010/6/30/understanding-logrotate-on-ubuntu-part-2).

I maintain a configuration file for each of the domains being served by the machine. The file for a domain lives in -- you guessed it -- the associated project's `deploy/` folder. Each contains two entries: one for the nginx virtual host and one for the uWSGI instance. The reason for this is that each config block needs a `postrotate` section to restart the associated server after the logs have been rotated. I don't want nginx to be restarted everytime a uWSGI log is rotated, and I don't want uWSGI restarted everytime an nginx log is rotated.

    #!bash
    $ vim /srv/myproject.com/code/deploy/logrotate

    /srv/myproject.com/logs/access.log /srv/myproject.com/logs/error.log {
        rotate 14
        daily
        compress
        delaycompress
        sharedscripts
        postrotate
            [ ! -f /var/run/nginx.pid ] || kill -USR1 `cat /var/run/nginx.pid`
        endscript
    }
    
    /srv/myproject.com/logs/uwsgi.log {
        rotate 14
        daily
        compress
        delaycompress
        postrotate
           restart --quiet uwsgi-myproject
        endscript
    }

This file is linked in to the `/etc/logrotate.d/` directory. Logrotate will automatically include any file in that directory inside its configuration.

    #!bash
    $ sudo ln -s /srv/myproject.com/code/deploy/logrotate /etc/logrotate.d/myproject


Database Server
----------------------

A web server isn't much use without a database these days. I use [PostgreSQL](http://www.postgresql.org/).


###Install

    #!bash
    $ sudo apt-get install postgresql


###Configure

PostgreSQL has some unique terminology and ways of doing things. When I first set it up for the first time, having coming from a MySQL background, not everything was completely straightforward. As usual, [Slicehost has a number of articles](http://articles.slicehost.com/postgresql) that will provide a foundation.

In the `/etc/postgresql/8.4/main/postgresql.conf` file, I uncomment the following two lines:

    track_counts = on
    autovacuum = on

Then restart the database server.

    #!bash
    $ sudo /etc/init.d/postgresql-8.4 restart

After that I'll change the password for the postgres user and the postgres database role.

    #!bash
    $ sudo passwd postgres
    $ sudo -u postgres psql
    \password postgres
    \q

To allow local socket connections to the database using passwords, I open up `/etc/postgresql/8.4/main/pg_hba.conf` and find the following line:

    local   all         all                               ident

Which I then change to:

    local   all         all                               md5

After which another restart is in order.

    #!bash
    $ sudo /etc/init.d/postgresql-8.4 restart


###Create a database

The next step is to create a user (or role, in PostgreSQL's parlance) and database for the project. I use the same name for both.

    #!bash
    $ sudo -u postgres createuser -PE myproject
    $ sudo -u postgres createdb -O myproject myproject

After that, I should be able to connect.

    #!bash
    $ psql -U myproject


####Import the Database

If I'm restoring a previous database from a backup, now would be the time to import the backup.

    #!bash
    $ psql -U myproject < myproject.postgresql

And now Django should be able to connect!

The basic server is setup and secure. Django, uWSGI, nginx and PostgreSQL are all running and getting along swimmingly. At this point, many people would be done, but I also like to have a minimal mail server.


Mail Server
---------------

Most of my domains use [Google Apps](http://www.google.com/apps/), so I don't need a full-blown mail server. I do want programs and scripts to be able to send mail, and I prefer not to do so through an external SMTP server -- I'd rather just deal with having sendmail running on my own box. And I do have a few domains that do not use Google Apps. They have one or two aliases associated with them, so the server needs to receive messages for those domains and forward them off to an external address. If any of this sounds vaguely familiar, it's because it's the same thing I detailed [last time](http://pig-monkey.com/2008/06/10/an-ubuntu-vps-on-slicehost-mail/). My setup now is the same as then, so I won't repeat any of it here.

For a more detailed explanation of running [Postfix](http://www.postfix.org/), you can [read the Slicehost articles](http://articles.slicehost.com/email).


A Note on Git
------------------

I use [Git](http://git-scm.com/) to keep track of the code for all my projects. (If you're new to Git, you ought to skim the [Git Reference](http://gitref.org/) or [Everyday GIT With 20 Commands Or So](http://www.kernel.org/pub/software/scm/git/docs/everyday.html)). To manage websites, I create a repository of the directory with the code that runs the site (in this case, `/srv/myproject.com/code/`) and another empty, bare repository to work as a hub. With a `post-update` and `post-commit`, the end result is an excellent web workflow:

 -  A copy of the hub can be checked out on a local machine for development. Whenever a change is committed, a simple `git push` will push the code to the web server and automatically make it live.
 - Changes can be made on the server in the actual live website directory. (This is not a best practice, but I do it more often than I should probably admit.) Whenever a change is committed, it is automatically pushed to the hub, so that a simple `git pull` is all that's needed on the development machine to update its repository.

A more detailed explanation of this workflow is at [Joe Maller's blog](http://joemaller.com/990/a-web-focused-git-workflow/).

To start, I need to create a repository for the new project I created in this tutorial. And, since this is a new server, I need to give Git my name and email address to record with every commit.

    #!bash
    $ git config --global user.name "Pig Monkey"
    $ git config --global user.email "pm@pig-monkey.com"
    $ cd /srv/myproject.com/code/
    $ git init

Before adding the files, I create a `.gitignore` file in the repository root to tell Git to ignore compiled Python files.

    $ vim .gitignore
    
    *.pyc

Now I add all the files to the repository, confirm that it worked, and commit the files.

    #!bash
    $ git add .
    $ git status -s
    $ git commit -m "Initial commit of myproject.com"

I create the bare hub directory directly along side the projects `code/`.

    #!bash
    $ cd ../
    $ mkdir hub.git
    $ cd hub.git
    $ git --bare init

With the hub created, I need to add it as the remote for the main repository and push the master branch to it.

    #!bash
    $ cd ../code
    $ git remote add hub /srv/myproject.com/hub.git
    $ git remote show hub
    $ git push hub master

Now the hub needs a `post-update` script so that every time something is pushed to it, that change is automagically pulled into the live website directory.

    #!bash
    $ vim /srv/myproject.com/hub.git/hooks/post-update

    #!/bin/sh
    echo
    echo "**** Pulling changes into live"
    echo

    cd /srv/myproject.com/code || exit
    unset GIT_DIR
    git pull hub master
    
    exec git-update-server-info

    $ chmod +x /srv/myproject.com/hub.git/hooks/post-update

And the live website directory requires a `post-commit` script so that every time something is committed inside of it, that change is automagically pushed to the hub.

    #!bash
    $ vim /srv/myproject.com/code/.git/hooks/post-commit

    #!/bin/sh
    echo
    echo "**** pushing changes to Hub"
    echo
    
    git push hub
    
    $ chmod +x /srv/myproject.com/code/.git/hooks/post-commit

All that's left is to check out the hub onto the development machine -- my laptop, in this case!

    #!bash
    $ mkdir ~/work/myproject/
    $ cd ~/work/myproject/
    $ git clone ssh://myserver.com/srv/myproject.com/hub.git code

To test things out, we can add a file to the repository on the development machine.

    #!bash
    $ cd code/
    $ touch test
    $ git add test
    $ git commit -m "A test"
    $ git push

Now go back to the server, and the file should be there! To test things the other way around, I'll delete the file from the live repository.

    #!bash
    $ cd /srv/myproject.com/code/
    $ ls
    myproject test
    $ git rm test
    $ git commit -m "Removing the test file"

And once again to the development machine:

    #!bash
    $ git pull
    $ ls
    deploy  myproject

No more test! It's pretty dandy.

###Restoring

If I was building a new server and restoring a project from an old server, I would simply mirror the old hub and then clone that in the live directory.

    #!bash
    $ cd /srv/myproject.com/
    $ git clone --mirror ssh://myoldserver.com/srv/myproject.com/hub.git
    $ git clone hub.git code/


Resources
--------------

Prior to building this server, I was new to a lot of this -- particularly, uWSGI and virtualenv. The following tutorials helped me a good deal in putting together the perfect setup for my needs.

 - [A Primer on virtualenv](http://iamzed.com/2009/05/07/a-primer-on-virtualenv/) by Chris Scott
 - [A web-focused Git workflow](http://joemaller.com/990/a-web-focused-git-workflow/) by Joe Maller
 - [Deployment with uWSGI and nginx](http://blog.zacharyvoase.com/2010/03/05/django-uwsgi-nginx/) by Zachary Voase
 - [Django on uWSGI and Nginx](http://brandonkonkle.com/blog/2010/sep/14/django-uwsgi-and-nginx/) by Brandon Konkle
 - [Django, Nginx and uWSGI in production](http://www.jeremybowers.com/blog/post/5/django-nginx-and-uwsgi-production-serving-millions-page-views/) by Jeremy Bowers
 - [Notes on using pip and virtualenv with Django](http://www.saltycrane.com/blog/2009/05/notes-using-pip-and-virtualenv-django/) by Eliot
 - [Presentation: pip and virtualenv](http://mathematism.com/2009/07/30/presentation-pip-and-virtualenv/) by Rich Leland
 - [Provisioning a new Ubuntu server for Django](http://brandonkonkle.com/blog/2010/jun/25/provisioning-new-ubuntu-server-django/) by Brandon Konkle
 - [Running Django with Nginx and uWSGI](http://www.westphahl.net/blog/2010/4/8/running-django-nginx-and-uwsgi/) by Simon Westphahl
 - [virtualenvwrapper Command Reference](http://www.doughellmann.com/docs/virtualenvwrapper/command_ref.html)
 - [Working with virtualenv](http://www.arthurkoziel.com/2008/10/22/working-virtualenv/) by Arthur Koziel
