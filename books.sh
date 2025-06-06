#!/bin/bash

cd "$(dirname "$0")"

calibredb catalog content/media/library/books.csv --fields=id,author_sort,title,isbn,identifiers,series,series_index,uuid --search="#read:yes not tag:=news"

LANG=C sed -i '1 s/[\d128-\d255]//g' content/media/library/books.csv

csvjson -i 4 content/media/library/books.csv > content/media/library/books.json

cd "$OLDPWD"
