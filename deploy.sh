#!/bin/bash

cd "$(dirname "$0")"

git push github

uv run pelican content -s publishconf.py

rsync -av --delete output/ havenaut.net:/var/www/pig-monkey.com/

cd "$OLDPWD"
