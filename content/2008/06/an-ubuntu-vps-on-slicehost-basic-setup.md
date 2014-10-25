Title: An Ubuntu VPS on Slicehost: Basic Setup
Date: 2008-06-10
Modified: 2012-12-22
Tags: shell, vps, linux, howto, slicehost, ubuntu
Slug: an-ubuntu-vps-on-slicehost-basic-setup

<em>As <a href="http://pig-monkey.com/2008/06/09/a-move-to-slicehost/">mentioned previously</a>, I've recently moved this domain over to <a href="http://www.slicehost.com/">Slicehost</a>. What follows is Part One of a guide, compiled from my notes, to setting up an Ubuntu Hardy VPS. See also <a href="http://pig-monkey.com/2008/06/10/an-ubuntu-vps-on-slicehost-web-server">Part Two</a>, <a href="http://pig-monkey.com/2008/06/10/an-ubuntu-vps-on-slicehost-mail">Part Three</a>, and <a href="http://pig-monkey.com/2008/06/10/an-ubuntu-vps-on-slicehost-wordpress">Part Four</a>.</em>

Slicehost has an <a href="http://articles.slicehost.com/">excellent article repository</a>, containing guides on a number of subjects. After building a fresh Slice, you should first follow <a href="http://articles.slicehost.com/2008/4/25/ubuntu-hardy-setup-page-1">Part 1</a> and <a href="http://articles.slicehost.com/2008/4/25/ubuntu-hardy-setup-page-2">Part 2</a> of Slicehost's basic setup articles.

I use slightly different coloring in my bash prompt, so, rather than what Slicehost suggests in their article, I add the following to `~/.bashrc`:

<!--more-->

    #!bash
    export PS1='\[\033[0;32m\]\u@\[\033[0;35m\]\h\[\033[0;33m\] \w\[\033[00m\]: '

This is a good time to protect SSH by installing <a href="http://denyhosts.sourceforge.net/">DenyHosts</a>, which I discuss <a href="http://pig-monkey.com/2008/10/03/thoughts-on-ssh-security/">here</a>:

    #!bash
    $ sudo aptitude install denyhosts

Ubuntu's default text editor is nano, which I abhor. Real men use vim. Ubuntu comes with a slimmed down version of vim, but you'll probably want the full version:

    #!bash
    $ sudo aptitude install vim


To change the global default editor variable, execute the following and select the editor of your choice:

    #!bash
    $ sudo update-alternatives --config editor

This is also a perfect time to install <a href="http://www.gnu.org/software/screen/">GNU Screen</a>.

    #!bash
    $ sudo aptitude install screen

If you're not familiar with Screen, <a href="http://www.redhatmagazine.com/2007/09/27/a-guide-to-gnu-screen/">Red Hat Magazine has a nice little introduction</a>

My .screenrc looks like this:

    #!bash
    # Print a pretty line at the bottom of the screen
    hardstatus alwayslastline
    hardstatus string '%{= kG}[ %{G}%H %{g}][%= %{=kw}%?%-Lw%?%{r}(%{W}%n*%f%t%?(%u)%?%{r})%{w}%?%+Lw%?%?%= %{g}][%{Y}%Y-%m-%d %{W}%c %{g}]'
    
    # Nobody likes startup messages
    startup_message off
    
    # Turn visual bell on and set the message to display for only a fraction of a second
    vbell on
    vbellwait .3
    
    # Set default shell title to blank
    shelltitle ''
    
    # Gimme my scrollback!
    defscrollback 5000
    
    # Change command character to backtick
    escape `` 
    
    # Stop programs (like vim) from leaving their contents
    # in the window after they exit
    altscreen on
    
    # Default screens
    screen -t shell 0 

I prefer to have my bash profile setup to connect me to Screen as soon as I login. If there are no running sessions, it will create one. If there is a current session, it will disconnect the session from wherever it is connected and connect it to my login. When I disconnect from screen, it automatically logs me out. To achieve this, I add the following to `~/.bashrc`:

    #!bash
    # If possible, reattach to an existing session and detach that session
    # elsewhere. If not possible, create a new session.
    if [ -z "$STY" ]; then
        exec screen -dR
    fi

I would also recommend following Slicehost's guide to <a href="http://articles.slicehost.com/2007/9/10/scanning-for-rootkits-with-chkrootkit">installing chkrootkit</a> and <a href="http://articles.slicehost.com/2007/9/10/scanning-for-rootkits-with-rkhunter">rkhunter</a>.

One more thing: let's set the timezone of the server to whatever is local to you (Slicehost's Ubuntu image defaults to UTC). To do that, run:

    #!bash
    $ sudo dpkg-reconfigure tzdata

Next up: <a href="http://pig-monkey.com/2008/06/10/an-ubuntu-vps-on-slicehost-web-server">install a web server</a>.
