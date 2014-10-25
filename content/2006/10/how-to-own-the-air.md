Title: How to Own the Air
Date: 2006-10-20
Modified: 2012-12-22
Tags: wireless, howto, crypto, linux
Slug: how-to-own-the-air

Before moving into my new place last month, I had planned on paying an ISP for internet access. But, complications arose with the company I had chosen, so I decided to cancel my order soon after it was placed. Instead, I planned to borrow internet access from my neighbors (hey, they're pumping signals into my air-space). Trouble was, everyone had encrypted their networks with <a href="http://en.wikipedia.org/wiki/Wired_Equivalent_Privacy">WEP</a>. No doubt this is a good thing, and a vast improvement from the last time I had scanned down here (about 8 months ago), but I wanted in. I was able to justify cracking in to myself by recognizing that my paranoia isn't limited just to the "others" out on the global interwebs -- no, I'd be just as paranoid about the owner of whomever's network I was breaking into watching my traffic. There was no question I'd make ample use of encryption, which, as a side benefit, meant that anything I did through his connection would be rather difficult to trace back. So, he was protected. As long as he wasn't paying for bandwidth by the KB, he'd not be much affected by my leeching. (I use the pronoun "he" because I know now that the owner of my primary network is, in fact, a he -- put a password on your routers, people!).

But there was another problem, in addition to WEP: during reconnaissance, I would rarely pick up any connected clients. Perhaps I was always trying at the wrong time of day. Or perhaps people pay for internet access and never use it. Regardless, it would have taken weeks of constant logging to gather enough IVs to crack the WEP key. So, the first step was to take the money I had saved by canceling my order with the ISP, and invest in a new wireless card that supported packet injection.

The <a href="http://www.proxim.com/products/cp/pc.html" >Proxim 8470-WD</a> (from <a href="http://www.aircrack-ng.org/doku.php?id=faq&DokuWiki=8fb30aa7da2a84fc23999e92b8e641ca#which_is_the_best_card_to_buy" >aircrack-ng's recommended list</a>) caught my eye, though it took a while before I could find it a decent price. To do my initial cracking, I popped in <a href="http://www.backtrack-linux.org/">Backtrack</a> and followed <a href="http://www.aircrack-ng.org/doku.php?id=newbie_guide&DokuWiki=8fb30aa7da2a84fc23999e92b8e641ca" >aircrack-ng's newbie guide</a>. (I had upgraded my trusty old Auditor cd to Backtrack just for this occasion. It's quite the nice distribution.) Within about 5 minutes, I had gained access to the first network. Goes to show how secure WEP is.

Though the Proxim card is plug and play in Ubuntu, the steps to crack WEP are a little different. Here's what I do (note that I do recommend using Backtrack, instead).

First, of course, one must install aircrack:

<pre>sudo apt-get install aircrack</pre>

You may change your mac address manually, or, if you aren't concerned with anonymity, don't change it all. I have a preference of using the <a href="http://www.alobbs.com/macchanger/" >macchanger</a> tool:

<pre>sudo apt-get install macchanger</pre>

Set your card's MAC address randomly. In this case, the network device is at <em>ath0</em>:

<pre>sudo ifconfig ath0 down
sudo macchanger -r ath0
sudo ifconfig ath0 up</pre>

Put your card into monitor mode:

<pre>sudo iwconfig ath0 mode monitor</pre>

Start scanning:

<pre>sudo airodump ath0 dump 0</pre>

In this case, <code>dump</code> is the file prefix for airodump's output and the <code>0</code> tells airodump to channel-hop. Now you want to pick your target network from the scan. It should have at least one client connected (displayed at the bottom of airodump's output), the more the merrier. (Hopefully that client is transmitting data, too.)

When you pick your target, kill the first instance of airodump and start it up again, this time specifying the channel of your target:

<pre>sudo airodump ath0 targetdump 9</pre>

The <code>targetdump</code> is the file prefix and <em>9</em> is the channel. Optionally you can add a <code>1</code> to the end of the command, which tells airodump to only capture <a href="http://en.wikipedia.org/wiki/Initialization_vector" >IV</a>s (which is what you're after). I normally don't bother.

When you've captured somewhere in the range of 250,000 - 500,000 data packets (shown by airodump in the "Packets" column of your target client), you can start cracking:

<pre>aircrack -b 00:12:34:45:78:A3 targetdump.cap</pre>

In this case, <code>-b</code> is the essid of your target network. Cracking could take minutes, hours, days, weeks, months, or years. I've never had to wait over 20 minutes.

But what if the client is being a party-pooper and not transmitting? That's where packet injection comes in. From aircrack's guide:

<blockquote>ARP works (simplified) by broadcasting a query for an IP and the device that has this IP sends back an answer. Because WEP does not protect against replay, you can sniff a packet, send it out again and again and it is still valid. So you just have to capture and replay an ARP-request targeted at the AP to create lots of traffic (and sniff IVs).</blockquote>

You'll want to keep airodump running, so that all the traffic you generate will be captured. In another terminal, start injecting:

<pre>sudo aireplay -3 -b 00:12:34:45:78:A3 -h A3:78:45:34:12:00 ath0</pre>

The <code>-3</code> tells airepay you want to replay ARP requests, <code>-b</code> is that target network, and <code>-h</code> is the client. In a little bit, aireplay should inform you that it has captured 1 (or more) ARP packets. Sit back and watch airodump count up the IVs.

If that pesky client still isn't cooperating, you can give it a little motivation. From aircrack:

<blockquote>Most operating systems clear the ARP cache on disconnection. If they want to send the next packet after reconnection (or just use DHCP), they have to send out ARP requests. So the idea is to disconnect a client and force it to reconnect to capture an ARP-request. A side-effect is that you can sniff the ESSID during reconnection too. This comes in handy if the ESSID of your target is hidden.

...the risk that someone recognizes this attack or at least attention is drawn to the stuff happening on the WLAN is higher than with other attacks.</blockquote>

Keep airodump and aireplay running, and in a new terminal give it a little kick in the butt:

<pre>sudo aireplay -0 5 -a 00:12:34:45:78:A3 -c A3:78:45:34:12:00 ath0</pre>

The first switch, <code>-0</code>, informs aireplay you want to force the client to be unauthenticated, <code>-a</code> is the target network, <code>-c</code> is the target client. When the client reconnects, you should start grabbing ARP requests.

After you have enough packets, crack the WEP key as before.

To manage and connect to my wireless networks, I've taken to using <a href="http://wifi-radar.systemimager.org/" >wifi-radar</a>. It scans for networks, allows you to specify which networks you prefer and, for each network, allows you to set preferences such as the WEP key, whether to use dynamic or static addresses, and the like. What I like best is the connection commands, which allows you to set commands you want executed before wifi-radar connects to the network, and after. In the before field, I have it randomly change my mac address:

<pre>ifconfig ath0 down && macchanger -r ath0 && ifconfig ath0 up</pre>

After it connects, I restart tor:

<pre>/etc/init.d/tor restart</pre>

(As another reference for you, <span class="removed_link">this site</span> keeps turning up as a guide to cracking WEP in Ubuntu.)
