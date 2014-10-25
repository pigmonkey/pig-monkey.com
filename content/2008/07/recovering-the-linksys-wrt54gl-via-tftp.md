Title: Recovering the Linksys WRT54GL via TFTP
Date: 2008-07-18
Modified: 2012-09-15
Tags: linksys, firmware, dd-wrt, wireless, os x, router, tftp
Slug: recovering-the-linksys-wrt54gl-via-tftp

Last May, <a href="http://www.dd-wrt.com">DD-WRT</a> released the (long in development) v24 of their firmware. I had been running one of the release candidates for it on my Linksys WRT54GL, but decided today to upgrade to the stable release. I downloaded the appropriate file (<code>dd-wrt.v24_std_generic.bin</code>), followed the <a href="http://www.dd-wrt.com/wiki/index.php/Installation#Upload_The_Firmware">instructions for flashing through the web GUI</a>, and promptly bricked the router.

It wasn't totally destroyed. I could still ping the router, but couldn't access it in any other way. The power light would flash repeatedly, and no other lights came on. No amount of hard resets would fix it.

<!--more-->

According to <a href="http://www.dd-wrt.com/wiki/index.php/Recover_from_a_Bad_Flash#WRT54G.2FGL.2FGS">DD-WRT's wiki article on bad flashes</a>, the repetitive blinking of the power light means that the bootloader is defective, but that the problem might be solved using a TFTP recovery. The idea is that when the router first boots up, there's a brief moment where it will accept an upload. By pushing through firmware, you are able to temporarily boot the router.

On older Linksys routers, this only works with the official Linksys firmware, so I downloaded the latest version from <a href="http://www.linksys.com/servlet/Satellite?c=L_CASupport_C2&childpagename=US%2FLayout&cid=1166859841350&packedargs=sku%3DWRT54GL&pagename=Linksys%2FCommon%2FVisitorWrapper&lid=4135041350B01&displaypage=download">Linksys' support page for the WRT54GL</a>. Because the router will only accept the firmware at the very start of the boot process, I first unplugged the router, turning it off. To monitor the router during the process, I started a ping from my machine.
<pre>
$ ping 192.168.1.1
</pre>

Then, using the TFTP client that ships with OS X, I executed the upload
<pre>
$ echo "put FW_WRT54GL_4.30.12.3_US_EN_code.bin" | tftp -e 192.168.1.1
</pre>
and immediately plugged the router back in. In 10 seconds, TFTP reported that the file had been sent.

At this point, the router stopped responding to my pings for about 30 seconds. When it began replying again, I was able to access the default Linksys web GUI. The first thing I did in the GUI was to hit the "reset to factory defaults" button, which clears the NVRAM of my bad DD-WRT image and installs the fresh Linksys image. After that, I installed a new DD-WRT "mini" image (the WRT54GL requires you flash with "mini" before upgrading to "standard" when moving from the default firmware), by uploading <code>dd-wrt.v24_mini_generic.bin</code> via the upgrade page. This worked without a hitch.

In the DD-WRT web interface, I tried to flash the router with the standard firmware, but was greeted by a vague error message that told me only that the upgrade had failed. I went <a href="http://www.dd-wrt.com/wiki/index.php/What_is_DD-WRT%3F#File_Versions">back to the wiki to see what the differences were between mini and standard</a> and decided that it would be find to leave the router with mini. All I needed was for the router to act as a wireless repeater with a virtual interfaces. The mini firmware supports this, so I was able to <a href="http://pig-monkey.com/2007/12/02/escapades-in-the-art-of-wireless-piracy/">setup the router just as before</a>.
