#!/bin/bash

cd "$(dirname "$0")"

git push github

pipenv run pelican content -s publishconf.py

rsync -av --delete output/ silicon:/var/www/pig-monkey.com/public/

cd "$OLDPWD"
