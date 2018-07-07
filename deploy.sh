#!/bin/bash

cd "$(dirname "$0")"

git push origin

git push github

pipenv run pelican content -s publishconf.py

rsync -av output/ pigmonkey@pig-monkey.com:~/pig-monkey.com/

cd "$OLDPWD"
