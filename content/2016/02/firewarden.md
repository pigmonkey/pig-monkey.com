Title: Firewarden
Date: 2016-02-05
Tags: linux, privacy

I've [previously mentioned](http://pig-monkey.com/2015/08/firejail/) the [Firejail](https://firejail.wordpress.com/) sandbox program. It's an incredibly useful tool. I use it to jail pretty much [all the things](https://github.com/pigmonkey/spark/search?q=firejail). Over the past six months, I've found that one of my primary use cases for Firejail is to create private, temporary sandboxes which can be destroyed upon closure. I wrote [Firewarden](https://github.com/pigmonkey/firewarden), a simple wrapper script around Firejail, to reduce the keystrokes needed for this type of use.

## Disposable Browsers

Prepend any program with `firewarden` and it will launch the program inside a private Firejail sandbox. I use Firewarden to launch disposable [Chromium](https://www.chromium.org/) instances dozens of times per day. When the program passed to Firewarden is `chromium` or `google-chrome`, Firewarden will add the appropriate [options](http://peter.sh/experiments/chromium-command-line-switches/) to the browser to prevent the first run greeting, disable the default browser check, and prevent the [WebRTC IP leak](https://www.privacytools.io/webrtc.html). The following two commands are equivalent:

    $ firejail --private chromium --no-first-run --no-default-browser-check --enforce-webrtc-ip-permission-check
    $ firewarden chromium

Firewarden also provides a few options to request a more restricted Firejail sandbox. For instance, you may want to open a URL in Chromium, but also use an isolated network namespace and create a new `/dev` directory (which has the effect of disabling access to webcams, speakers and microphones). The following two commands are equivalent:

    $ firejail --private --net=enp0s25 --netfilter --private-dev chromium --no-first-run --no-default-browser-check --enforce-webrtc-ip-permission-check https://example.org
    $ firewarden -d -i chromium https://example.org

In this example, Firewarden used [NetworkManager](https://wiki.gnome.org/Projects/NetworkManager) to discover that `enp0s25` was the first connected device, so it used that for the network namespace.


## Local Files

Firewarden isn't just useful for browsers. It can be used with any program, but my other major use case is safely viewing local files. File types like PDF and JPG can include malicious code and are a primary vector for malware. I use [zathura](https://pwmt.org/projects/zathura/) as my PDF reader, which is a simple and lightweight viewer that doesn't include anywhere near the number of potential vulnerabilities as something like Adobe Acrobat, but I still think it prudent to take extra precautions when viewing PDF files downloaded from the internet.

If Firewarden thinks the final argument is a local file, it will create a new directory in `/tmp`, copy the file into it, and launch the program in a sandbox using the new temporary directory as the user home directory<sup class="footnote-ref" id="fnref:private-home"><a rel="footnote" href="#fn:private-home" title="see footnote">1</a></sup>. Firewarden will also default to creating a new `/dev` directory when viewing local files, as well as disabling network access (thus preventing a malicious file from phoning home). When the program has closed, Firewarden removes the temporary directory and its contents

    $ firewarden zathura notatrap.pdf

The above command is the equivalent of:

    $ export now=`date --iso-8601=s`
    $ mkdir -p /tmp/$USER/firewarden/$now
    $ cp notatrap.pdf /tmp/$USER/firewarden/$now/
    $ firejail --net=none --private-dev --private=/tmp/$USER/firewarden/$now zathura notatrap.pdf
    $ rm -r /tmp/$USER/firewarden/$now

I use this functionality numerous times throughout the day. I also include Firewarden in [my mailcap](https://github.com/pigmonkey/dotfiles/blob/master/mutt/mailcap), which goes a long way to reducing the dangers of email attachments.

Firewarden doesn't add any new functionality to Firejail, but it does make it easier to take advantage of some of the great features that Firejail provides. [Check it out](https://github.com/pigmonkey/firewarden) if you're interested in reducing the keystrokes required to Jail All The Things&trade;.


<div id="footnotes">
    <h2>Notes</h2>
    <ol>
        <li id="fn:private-home"><a rev="footnote" href="#fnref:private-home" class="footnote-return" title="return to article">&crarr;</a> This is similar to using Firejail's old <code>--private-home</code> option, which was <a href="https://l3net.wordpress.com/2016/02/04/firejail-0-9-38-release-announcement/">removed in 0.9.38</a>. However, that option was limited to files in the user's home directory. It couldn't be easily used with a file from a USB drive mounted at <code>/media/usb</code>, for instance.</li>
    </ol>
</div>
