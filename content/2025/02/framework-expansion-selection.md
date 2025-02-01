Title: Framework Expansion Selection
Date: 2025-02-01
Tags: hardware

When I ordered [my Framework 13](/2025/01/beginning-framework/) I chose their recommended selection of expansion cards: 2 USB-C cards, a USB-A card, and an HDMI card.

After I began using the laptop I realized that the HDMI expansion card provided no utility. At my desk both at home and at work I run everything -- power, peripherals, Ethernet, and display -- through a single USB-C cable. The only time I'd need HDMI on the laptop itself is if I was plugging into a TV in a hotel room or a projector in a conference room. I cannot recall the last time I wanted to do either of those things. The need for external-display-while-portable is extremely rare for me.

So I went back to Framework and ordered a third USB-C expansion card and a second USB-A expansion card. I figured I would either run 3 USB-C and 1 USB-A, or 2 USB-C and 2 USB-A. Having both options seemed worthwhile. (None of the other [expansion card options](https://frame.work/marketplace/expansion-cards) have appealed to me yet.)

Last week I needed to decrypt a file while away from my desk. I plugged my YubiKey into the USB-A expansion card<sup class="footnote-ref" id="fnref:yubi-c"><a rel="footnote" href="#fn:yubi-c" title="see footnote">1</a></sup>, and it didn't read. I tried plugging in a different USB-A device, and it also did not read. I ejected the USB-A expansion card, slotted it back in, and then it worked. The expansion card did not look or feel loose before I ejected it, so I don't know what the problem was. Initially this was troubling, as during my pre-purchase research I did come across (seemingly rare) reports of expansion cards completely dying shortly after purchase. I was relieved to find that this was an easy fix and nothing was broken.

This was my first time ever ejecting one of the expansion cards, and my first time installing one since I removed the laptop from the box and assembled it. I wasn't sure if mucking with the slots would require a reboot, but I watched `dmesg` as I did it and slotting the expansion card back in read just like plugging in any plug-and-play USB device.

For now I have decided to replace the HDMI card with USB-A. I will run with two USB-A and two USB-C. I am not a USB-C absolutist and still have plenty of USB-A devices in my life that work perfectly fine and do not need to be replaced. Two ports each ought to useful, and it gives me a backup of both in case one expansion card does die at some point.

<div id="footnotes">
    <h2>Notes</h2>
    <ol>
        <li id="fn:yubi-c"><a rev="footnote" href="#fnref:yubi-c" class="footnote-return" title="return to article">&crarr;</a> When I <a href="/2024/06/yubikey-replacement/">replaced my YubiKey</a> last year I did evaluate if it would be more appropriate to move to a USB-C model. I decided against it.</li>
    </ol>
</div>
