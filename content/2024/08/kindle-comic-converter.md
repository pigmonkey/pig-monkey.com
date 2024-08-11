Title: In Which Graphic Novels Are Optimized for Portability
Date: 2024-08-10
Tags: books, toolchain

[Kindle Comic Converter](https://github.com/ciromattia/kcc) is a program that optimizes comic book files for e-readers. I have not read many graphic novels in the past, but I think that is likely to change now that I have found a good workflow for consuming them digitally. The portability of my [Kobo Libra 2](https://us.kobobooks.com/products/kobo-libra-2) makes it more convenient than [reading on my laptop](/2019/01/portrait-rotate/). Its 7" screen is large enough for me to enjoy comics when properly formatted, unlike the 6" screen of my old Kindle Paperwhite. (8" would probably be the best screen size for this type of content, but I am not sure that I would be pleased with the decrease in the packability of the device.)

I am using the command line version of KCC (surprising no one), typically as such:

    $ kcc-c2e --profile KoL --upscale --cropping 2 --splitter 2 input-file.cbr

* `--profile KoL` specifies that the target device is my Kobo Libra 2. The program will optimize the output file for the resolution and color profile of this device.
* `--upscale` instructs the program to [enhance](https://knowyourmeme.com/memes/zoom-and-enhance) images smaller than the device's resolution.
* `--cropping 2` will attempt to crop out margins and page numbers.
* `--splitter 2` instructs the program to duplicate double page spreads. The spread will first be displayed as a single rotated page (so that I can see the whole image at once, as the illustrator intended), and then split into two pages (so that I can see details and read text without zooming). This sometimes makes poor decisions on filler pages -- pages of credits, praise blurbs, etc -- but it seems to always do the right thing when you're in the pages of the comic itself.

I import the original source file into [my Calibre library](/2018/11/ebooks/), and then add the KCC-generated EPUB as an additional file to the same book record. When loading the book onto my reader, I explicitly tell Calibre to send the EPUB. I do not allow Calibre to do any further conversion to this file.

The resulting files do not look great when viewed on my computer. The lack of margins from the `--cropping 2` flag is annoying, and the images look [dark and jagged](https://github.com/ciromattia/kcc/wiki/FAQ#images-inside-file-created-by-kcc-dont-look-very-well-on-my-pc-did-i-do-something-wrong). But on the E Ink screen they look great.

I used this process to read Craig Thompson's [Blankets](https://en.wikipedia.org/wiki/Blankets_(comics)), which I [learned](https://en.wikipedia.org/wiki/Streisand_effect) about thanks to [Utah's attempt to ban it](https://www.sltrib.com/news/education/2024/08/02/utah-book-ban-list-these-titles/). This book was fantastic. For maximum teenage angst, I recommend reading it while listening to The Cure. (I don't even especially like The Cure, but when I finished Blankets I was struck with the strange desire to spend the next day repeatedly listening to [the](https://en.wikipedia.org/wiki/Kiss_Me,_Kiss_Me,_Kiss_Me) [few](https://en.wikipedia.org/wiki/Disintegration_(The_Cure_album)) [albums](https://en.wikipedia.org/wiki/Wish_(The_Cure_album)) of The Cure that I do own -- so I did.) The minimalist, black-and-white art style of Blankets lends itself perfectly to a grayscale E Ink screen. I was impressed at how much emotion he can communicate with so few lines.

<a href="https://www.flickr.com/photos/pigmonkey/53914380312/in/dateposted/" title="Blankets by Craig Thompson"><img src="https://live.staticflickr.com/65535/53914380312_f19d4b4b04_c.jpg" width="800" height="600" alt="Blankets by Craig Thompson"/></a>

I have recently begun to read [Monstress](https://en.wikipedia.org/wiki/Monstress_(comics)) by Marjorie Liu and Sana Takeda. This one is weird. (Utahns are going to lose their shit when they learn about it.) Unlike Blankets, Monstress is drawn with lush, full-color artwork. It also has a lot more text, whereas Blankets was much more about emotion than exposition. I read the first issue on the Libra 2, and then borrowed the dead-tree version from the library and reread it to compare. I think it still looks great on the grayscale E Ink screen -- it gives the impression of being extremely detailed graphite pencil work -- but the color does add a little something extra (gore, mostly). The text is legible without zooming, but on the small side. I am jumping back and forth between reading further issues on the Libra 2 and on color paper. The portability of the Libra 2 counts for a lot -- I carry it with me every day -- but I think Monstress is probably better consumed on paper -- or digitally on a larger color screen.

<a href="https://www.flickr.com/photos/pigmonkey/53915266761/in/dateposted/" title="Monstress by Marjorie Liu &amp; Sana Takeda"><img src="https://live.staticflickr.com/65535/53915266761_391800ec2b_c.jpg" width="800" height="600" alt="Monstress by Marjorie Liu &amp; Sana Takeda"/></a>
