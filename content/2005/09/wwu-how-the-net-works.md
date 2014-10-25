Title: WWU: How the net works
Date: 2005-09-28
Modified: 2012-09-15
Slug: wwu-how-the-net-works

I've been <a href="http://www.wwu.edu/" >here</a> for over a week now and I've yet to discuss the network. Surprising.

When you first plug into the network, the DHCP server (66.165.10.35) gives you a 10.242.*.* IP. This is for unregistered or quarantined computers (if someone is spreading a virus to all the poor Windows users, they'd be bumped to this network, which has no internet access and limited network access).

Opening up a web browser will take you the <span class="removed_link">registration page</span>, which basically just asks for your name and student number, throws that into a database with your MAC address, and gives you a 66.165.*.* IP, a registered address. (It should be mentioned that this is a public IP -- "a few ports are filtered" but I don't know which.) Windows users, though, have an extra step (so don't spoof your user agent when trying to register). They have to download the <span class="removed_link">ResTek Security Detector</span> (not based on <span class="removed_link">NetReg</span>), which checks to make sure you have all the latest Windows updates and an updated virus scanner (it doesn't actually scan your computer for viruses). If you lack either of these things, the proxy server (webproxy.restek.wwu.edu) will allow connections to certain addresses such as Microsoft, McAfee <a href="http://west.wwu.edu/atus/helpdesk/" >and the like</a> (I smell a security hole), so that you can get the latest updates on your 10.242.*.* computer. The school will also provide you with a free copy of McAfee Anti-virus, if you're lacking.

Students who wish to use dialup can dial extension 5255 from their modems and enter their Novell username (the scheme for the username -- which is the same as the name for the @cc.wwu.edu email the school gives out -- is in the form of lastnamefirstinitial. I think if you have a long last name it is only the first six letters of your last name. I don't know if first initial is included in that case) and password. This is the same username and password students use for their email, <a href="http://portal.cc.wwu.edu/mywestern/render.userLayoutRootNode.uP" >myWestern</a>, blackboard, lab computers, etc.
I assume students can access the dialup off-campus, but I don't know what the full phone number is. Most numbers here seem to be 360-788* or 360-650*. Somebody should do a scan.

Each student is allowed "as many IPs as you need", but only one per MAC address. Unused IPs are eventually unregistered. You are allowed to run an access point or router in your room, simply spoof your already registered MAC.

During your normal online browsing, you are encouraged to use the proxy server (running <a href="http://www.squid-cache.org/" >Squid</a>), which does no filtering, but caches data so that others can retrieve it quicker. This is done through an algorithm called Least Frequently Used with Dynamic Aging (LFUD), which "keeps popular objects in cache regardless of their size and thus optimizes byte hit rate (file size) at the expense of target hit rate" (more info <a href="http://www.hpl.hp.com/techreports/1999/HPL-1999-69.ps" >here</a>). The caching, of course, implies that they have the capability to log -- and do probably log quite a bit. But the sheer amount of traffic must make it impossible to log everything, or even start to filter through that which they do log. (They <a href="http://www.restek.wwu.edu/network/network-overview/proxy" >claim</a> that "the content accessed by individual users is not monitored.") Port scans and other questionable data probably go unnoticed. High bandwidth traffic -- such as me downloading 10gb at 1505.97kb/s -- might set off a few flags. <span class="removed_link">Public</span> and <a href="http://restek.wwu.edu/mystats" >private</a> statistics are available to view your daily, weekly, and monthly bandwidth consumption and bandwidth usage for the residence halls and the entire campus.

There's another range of addresses I haven't mentioned, which is the academic network. I believe they're 140.160.*.*. I think these addresses are also given out to those connecting via the wireless, but I've yet to try that out (it's either the 140 or 66.168.*.*). Apparently the main difference between the academic network and the normal 66.165.*.* is that the academic is more heavily monitored.

As far as bandwidth goes, there are no caps. Everybody has full access to the 28mbit pipe (this is lowered down to 3mbit during the summer), but bandwidth <a href="http://www.restek.wwu.edu/network/network-overview/bandwidth-prioritization/" >prioritization</a> does occur via <a href="http://www.bluecoat.com/">Packeteer</a>. This is the most interesting part of the network. Peer2peer traffic, instead of being outright banned, receives the lowest priority, making it a rare thing to see more than 4kb/s. This is understandable since p2p does take up a lot of bandwidth and the school wants to discourage students from committing copyright infringement, but it's also really annoying -- it makes it impossible to download the latest linux iso torrents and the like (yes, there are legitimate uses for p2p). Changing the port of your p2p server won't subvert the system, as Packeteer actually analyzes the traffic. Proxying the traffic through something like Tor may work, but that's really cruel to the Tor network and, as Tor is rather low latency itself, you won't see much improvement in speed. The easiest solution is to simply tunnel your p2p connection through ssh to an off-campus computer, but this obviously isn't very feasible for most students. I've yet to come with any other ways to get around the prioritization. Any ideas?

Another interesting note: there's a whole lot of <a href="http://www.famatech.com/" >RAdmin</a> traffic on the lan (port 4899).

Here's the output of a traceroute from the campus network to this site:
<blockquote> 1:  student-x-xx.na.reshall.wwu.edu (66.165.x.xx)
 1:  gw-2-1.na.reshall.wwu.edu (66.165.2.1)
 2:  bh-f-a.restek.wwu.edu (66.165.31.245)
 3:  core1-411.bellingham.fibercloud.net (216.57.208.173)
 4:  brdr1-gig100.bellingham.fibercloud.net (216.57.207.49)
 5:  12.124.173.17 (12.124.173.17)
 6:  gbr1-p60.st6wa.ip.att.net (12.123.44.114)
 7:  tbr1-p012501.st6wa.ip.att.net (12.122.12.157)
 8:  12.123.44.177 (12.123.44.177)
 9:  208.50.134.33 (208.50.134.33)
10:  so2-1-0-622M.ar1.LAX3.gblx.net (67.17.64.45)
11:  GE1-GX.dreamhost.com (67.17.162.162)
12:  basic-ogle.lilac.dreamhost.com (66.33.199.37)</blockquote>

Here's the output from an nslookup done on my public IP:
<blockquote>Server:         66.165.10.35
Address:        66.165.10.35#53

Non-authoritative answer:
65.2.165.66.in-addr.arpa        name = student-x-xx.na.reshall.wwu.edu.

Authoritative answers can be found from:
2.165.66.in-addr.arpa   nameserver = viking.wwu.edu.
2.165.66.in-addr.arpa   nameserver = kulshan.restek.wwu.edu.
2.165.66.in-addr.arpa   nameserver = henson.cc.wwu.edu.
henson.cc.wwu.edu       internet address = 140.160.240.12
viking.wwu.edu  internet address = 140.160.242.13
kulshan.restek.wwu.edu  internet address = 66.165.10.24</blockquote>

Here's the output of a whois (done from <a href="http://network-tools.com/">nwtools</a>) on my public IP:
<blockquote>This Registry database contains ONLY .EDU domains. 
The data in the EDUCAUSE Whois database is provided 
by EDUCAUSE for information purposes in order to 
assist in the process of obtaining information about 
or related to .edu domain registration records. 

The EDUCAUSE Whois database is authoritative for the 
.EDU domain.         

A Web interface for the .EDU EDUCAUSE Whois Server is 
available at: http://whois.educause.net 

By submitting a Whois query, you agree that this information 
will not be used to allow, enable, or otherwise support 
the transmission of unsolicited commercial advertising or 
solicitations via e-mail.

You may use "%" as a wildcard in your search. For further 
information regarding the use of this WHOIS server, please 
type: help 

--------------------------

Domain Name: WWU.EDU

Registrant:
   Western Washington University
   Computing Services
   P. O. Box 29480
   Bellingham, WA 98228-1480
   UNITED STATES

Contacts: 

   Administrative Contact:
   Robert Schneider
   Western Washington University
   Computing Services
   P. O. Box  29480
   Bellingham, WA 98228-1480
   UNITED STATES
   (360) 650-3502
   bobs@wwu.edu


   Technical Contact:
   J. Scott Williams
   Western Washington University
   Computing Services
   P.O. Box 29480
   Bellingham, WA 98228-1480
   UNITED STATES
   (360) 650-2868
   scott@wwu.edu


Name Servers: 
   VIKING.WWU.EDU		140.160.242.13
   HENSON.CC.WWU.EDU	140.160.240.12
   APPLE.UW.WA-K20.NET	

Domain record activated:    14-Apr-1987
Domain record last updated: 19-Aug-2002</blockquote>

(The 'x' that appear in my IP and hostname are censored, because I feel like it. The first 'x' in the IP corresponds to the first 'x' in the hostname and the 'xx' in the IP corresponds to the 'xx' in the hostname.)
