Title: Beginning Framework
Date: 2025-01-18
Tags: hardware

Near the end of 2024 I decided it was time to replace the Thinkpad X270. I still think the [X2{6,7}0 is Peak Laptop](/2021/01/peak-laptop/). Unfortunately, as software gets worse, I need more CPU.

Everything on the market seemed inferior in one way or another to the X270. I considered:

* [Thinkpad X1 Carbon Gen 9](https://en.wikipedia.org/wiki/ThinkPad_X1_series#X1_Carbon_Gen_9) (used)
* [Thinkpad X1 Carbon Gen 12](https://en.wikipedia.org/wiki/ThinkPad_X1_series#X1_Carbon_Gen_12) (used)
* [Star Labs StarBook](https://us.starlabs.systems/pages/starbook) (new)
* [Framework 13](https://frame.work/products/laptop-diy-13-gen-amd) (new)

After about two months of shopping around -- including buying and returning an X1C Gen 12 from eBay -- I settled on the Framework 13. Specifically, the DIY model with AMD Ryzen 5 7640U CPU, 2.8K matte display, and 61Wh battery. (I purchased the [SSD](https://www.bhphotovideo.com/c/product/1791000-REG/crucial_ct2000t500ssd8_2tb_t500_pcie_4_0.html) and [RAM](https://www.bhphotovideo.com/c/product/1735729-REG/crucial_crucial_ram_32gb_kit.html) separately.)

I have notes.

The keyboard is not as good as that on the X270 (which is not as good as that on older Thinkpads). But it seems to be on par with other modern laptop keyboards that I've seen. There is room for improvement, but it is acceptable. I've seen (and felt) much worse.

The hinges are not as good as on a Thinkpad. They feel nice when you move the lid -- the feel is about the same as the hinges on my X270 -- and they do hold the lid in position. But when typing with gusto, the lid shakes a bit. I did not notice this until I tested out the webcam. The movement of the lid is noticeable in the image. I practically never use a cam -- if asked about this when on a call, I reply that I exist in a black hole devoid of light, warmth, love, etc -- so this is acceptable to me.

The speakers are incredibly bad. Traditionally, Thinkpads had the worst speakers of any laptop, but Framework has lowered the bar here. I tried messing with [EasyEffects](https://wiki.archlinux.org/title/PipeWire#EasyEffects) and various scavenged presets. I suppose this made the speakers sound slightly less bad. But they're still really bad. Fortunately, this is firmly in the category of things I do not care about. I tickle my eardrums [with headphones when at a desk](/2024/01/desktop-audio/) and [with earbuds when mobile](/2024/01/mobile-audio/). About the only time I use the speakers on my laptop is for things like [a countdown timer with a bell](/2019/07/termdown/), for which shitty speakers are just as adequate as nice speakers.

I've not had the Framework 13 for long enough to comment on battery life. Less-than-stellar battery life was one of the main critiques I heard before purchasing the machine (though often it is not clear what specific machine generation and configuration the critic has). Framework [explicitly says not to use TLP](https://knowledgebase.frame.work/en_us/optimizing-ubuntu-battery-life-Sye_48Lg3), which is unfortunate for me. I first installed TLP shortly after its initial release in 2010 and haven't thought about it much since. I am trying to grok this brave new world of [TuneD](https://github.com/redhat-performance/tuned) and [power-profiles-daemon](https://gitlab.freedesktop.org/upower/power-profiles-daemon) and [subpar battery control](https://wiki.archlinux.org/title/Framework_Laptop_13#Battery_control). We'll see how that goes.

The design aesthetic of the Framework 13 feels very mediocre. I find the aluminum slab design language pioneered by Apple and now emulated by everyone else to be inferior to the Thinkpad aesthetic. I would rather Framework copy [Sapper](https://en.wikipedia.org/wiki/Richard_Sapper) than [Ive](https://en.wikipedia.org/wiki/Jony_Ive). But this is purely a personal aesthetic judgment that does not translate into functionality. I have no complaints about the actual build quality of the machine (yet). Eventually I may [stickerbomb](https://xn--gckvb8fzb.com/stickerbombed-star-labs-starbook-mk-vi/) the chassis to make myself feel better about it. I'd be embarrassed if someone saw it and mistakenly thought I was an Apple customer.

I point out what I dislike because that is easier than enumerating what I like. Everything else about the laptop is pretty nice. I am pleased with the purchase overall. The 3:2 aspect ratio of the Framework 13 screen is especially great -- at least for how I use a computer (which can mostly be summed up as "[reading and manipulating text](https://en.wikipedia.org/wiki/Unix_philosophy)").

The promise of the Framework is in its modularity and repairability, which hopefully means that any shortcomings can be corrected over time. One of the small things that decided my purchase was seeing that [Framework actually builds replacement screws into the machine](https://old.reddit.com/r/framework/comments/1hnsmo7/replacement_screws_thats_neat_d/). In my head the Thinkpad X260 and X270 are basically the same machine, and I used that same machine for nine years. My hope is that the Framework 13 can at least match that, and be as boring as possible during that time.
