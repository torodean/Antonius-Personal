#!/bin/sh
echo "...Loading."
echo "...Created by Antonius Torode."
echo "...Please make sure you are connected to the Internet."
echo "...If this script isn't working, make sure EOL Conversion is set to Unix"

git status
git add -A
git commit -m "$1"
git push
