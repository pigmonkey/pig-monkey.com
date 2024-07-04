Title: Working with ACSM Files on Linux
Date: 2024-07-03
Tags: books, toolchain, linux

I acquire books from various [OverDrive](https://www.overdrive.com/) instances. OverDrive provides an [ACSM](https://en.wikipedia.org/wiki/Adobe_Content_Server) file, which is not a book, but instead an XML ticket meant to be exchanged for the actual book file -- similar to requesting a book in meatspace by turning in a catalog card to a librarian. [Adobe Digital Editions](https://www.adobe.com/solutions/ebook/digital-editions.html) is used to perform this exchange. As one would expect from Adobe, this software does not support Linux.

Back in 2013 I setup a Windows 7 virtual machine with Adobe Digital Editions v2.0.1.78765, which I used exclusively for turning ACSM files into EPUB files. A few months ago I was finally able to retire that VM thanks to the discovery of [libgourou](https://forge.soutade.fr/soutade/libgourou/), which is both a library and a suite of utilities that can be used to work with ACSM files.

To use, I first register an anonymous account with Adobe.

    $ adept_activate -a

Next I export the private key that the files will be encrypted to.

    $ acsmdownloader --export-private-key

This key can then be imported into the [DeDRM_tools](https://github.com/noDRM/DeDRM_tools) plugin of [Calibre](https://calibre-ebook.com/).

Whenever I receive an ACSM file, I can just pass it to the `acsmdownloader` utility from libgourou.

    $ acsmdownloader -f foobar.acsm

This spits out the EPUB, which may be imported into [my standard Calibre library](/2018/11/ebooks/).
