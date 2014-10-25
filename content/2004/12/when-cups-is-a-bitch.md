Title: When CUPS won't die...
Date: 2004-12-31
Modified: 2012-09-15
Slug: when-cups-is-a-bitch

I upgraded CUPS yesterday and apparently broke my printing. After some googling and searching on the Gentoo forums, I came up with the following:
1) Delete the printer from http://localhost:631/printers/
2) <i>killall cupsd</i> (perhaps using the PID and -9 switch if the bastard won't die)
3) <i>/etc/init.d/cupsd zap</i>
4) <i>/etc/init.d/cupsd start</i>
5) Add the printer back into the web panel

It works now.

(Note that you could probably fix the problem with a reboot, but that's just so Windows-like.)
