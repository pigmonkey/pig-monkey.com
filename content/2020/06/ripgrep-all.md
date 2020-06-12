Title: Searching Books
Date: 2020-06-11
Tags: toolchain, linux, shell

[ripgrep-all](https://github.com/phiresky/ripgrep-all/) is a small wrapper around [ripgrep](https://github.com/BurntSushi/ripgrep) that adds support for additional file formats.

I discovered it while looking for a program that would allow me to search [my e-book library](/2018/11/ebooks/) without needing to open individual books and search their contents via [Calibre](https://calibre-ebook.com/). ripgrep-all accomplishes this by using [Pandoc](https://pandoc.org/) to convert files to plain text and then running ripgrep on the output. One of the numerous formats supported by Pandoc is [EPUB](https://en.wikipedia.org/wiki/EPUB), which is the format I use to store books.

Running Pandoc on every book in my library to extract its text can take some time, but ripgrep-all caches the extracted text so that subsequent runs are similar in speed to simply searching plain text -- which is blazing fast thanks to ripgrep's speed. It takes around two seconds to search 1,706 books.

    $ time(rga -li 'pandemic' ~/library/books/ | wc -l)
    33

    real    0m1.225s
    user    0m2.458s
    sys     0m1.759s
