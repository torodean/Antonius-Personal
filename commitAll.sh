#!/bin/sh
echo "...Loading."
echo "...Created by Antonius Torode."
echo "...Please make sure you are connected to the Internet."
echo "...If this script isn't working, make sure EOL Conversion is set to Unix."
echo "..."
git pull
echo "..."
git status
echo "..."
git add -A
echo "..."
git status
echo "..."
commit_message=""
while getopts ":m:" opt; do
  case ${opt} in
    m ) commit_message="$OPTARG";;
    \? ) echo "Invalid option: -$OPTARG" 1>&2; exit 1;;
    : ) echo "Option -$OPTARG requires an argument." 1>&2; exit 1;;
  esac
done
if [ -z "$commit_message" ]
then
  git commit -m "$1"
else
  git commit -m "$commit_message"
fi
echo "..."
git status
echo "..."
git push
echo "..."
echo "...Finished."
