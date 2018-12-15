Title: Reading Books
Date: 2018-12-15
Tags: books

While I do not subscribe to [Umberto Eco's idea of the antilibrary](https://www.brainpickings.org/2015/03/24/umberto-eco-antilibrary/) -- having too great a collection of unread books is a mental weight that I find uncomfortable -- I do have a constant collection of books that I have acquired but have yet to consume.

As [previously](/2018/11/ebooks/) [mentioned](/2018/11/vanity-covers/), I manage my e-book library with [Calibre](https://calibre-ebook.com/). Calibre allows the user to create [custom metadata properties](http://blog.calibre-ebook.com/2011/11/calibre-custom-columns.html), which I've taken advantage of to add a simple boolean property called `read`. This allows me to track which books I have read, filter the library for those books that are unread, and easily queue up the next thing whenever I finish reading a book. It also allows me to know that my Calibre library averages around 20% unread.

I enjoy seeing lists of books that other people have read or are reading. In case anyone else feels that way, I've [published a list of read books from my Calibre library](/books/). Generating this list is fairly simple.

First I ask Calibre to dump a CSV of my library, including the fields that are most useful, and filtering only for those books that I have marked as read.

    $ calibredb catalog content/media/library/books.csv --fields=id,author_sort,title,isbn,identifiers,series,series_index,uuid --search="#read:yes"

The first character in this file is some sort of Unicode weirdness. I make sure this character and anything like it is stripped from the header row with sed.

    $ LANG=C sed -i '1 s/[\d128-\d255]//g' content/media/library/books.csv

I want to display this list in a web page using [DataTables](https://datatables.net/), allowing users to perform simple sorting and searching. DataTables can read from a JSON source, so the easiest solution was to use [csvkit](https://csvkit.readthedocs.io/) to convert the output.

    $ ~/.virtualenvs/csvkit/bin/csvjson -i 4 content/media/library/books.csv > content/media/library/books.json

The resulting output is [processed by DataTables](https://datatables.net/examples/ajax/custom_data_flat.html) for [display](/books/).
