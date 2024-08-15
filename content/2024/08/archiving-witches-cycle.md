Title: Archiving The Witches Cycle
Date: 2024-08-14
Tags: books, shell

I [recently](/2024/07/link-log-20240729/) learned about The Witches Cycle, a French manga by Tony Concrete, thanks to [a post by the author on /r/xbiking](https://old.reddit.com/r/xbiking/comments/1e6b56d/a_xbikecore_character_design_for_my_manga/). It has similar vibes to [Kiki's Delivery Service](https://en.wikipedia.org/wiki/Kiki's_Delivery_Service) -- one of my favorite Studio Ghibli films -- with the addition of sweet bikes. I'm not completely hooked on the story yet, but the art is great.

Thus far the English translations have only been [published on The Radavist](https://theradavist.com/tag/manga/). Their Javascript gallery viewer leaves something to be desired in this application. If the English translations are ever published as a book, I'll buy it. In the meantime, the manga is easy to liberate.

A quick inspection of The Radavist's pages for [chapter 1](https://theradavist.com/bikepacking-manga-the-witches-cycle/), [chapter 2](https://theradavist.com/witches-cycle-chapter-two/), [chapter 3](https://theradavist.com/witches-cycle-bikepacking-manga-chapter-3/), and [chapter 4](https://theradavist.com/the-witches-cycle-chapter-4/) shows that the chapters consist of sequentially numbered JPGs (though they are not consistent in their naming scheme, for shame). I'm a big fan of [downloading JPGs](https://www.web3isgoinggreat.com/).

    $ mkdir witches-chapter-0{1..4}
    $ wget https://media.theradavist.com/uploads/2023/11/Witches-Cycle-{1..76}.jpg --directory-prefix witches-chapter-01/
    $ wget https://media.theradavist.com/uploads/2024/02/2024_Witches_Cycle_Chapter_2-{1..30}.jpg --directory-prefix witches-chapter-02/
    $ wget https://media.theradavist.com/uploads/2024/03/2024_Witches_Cycle_Chp3-{1..38}.jpg --directory-prefix witches-chapter-03/
    $ wget https://media.theradavist.com/uploads/2024/06/chap4{05..49}.jpg --directory-prefix witches-chapter-04/

The [previously mentioned Kindle Comic Converter](/2024/08/kindle-comic-converter/) is happy to operate on a directory of images.

    $ for i in {01..04}; do kcc-c2e --profile KoL --upscale --cropping 2 --splitter 2 --author "Tony Concrete" --title "The Witches Cycle, Chapter $i" witches-chapter-$i/; done

This results in 3 well-formatted EPUB files I can archive in my Calibre library and read on my e-reader.
