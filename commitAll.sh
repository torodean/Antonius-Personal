#!/bin/sh

echo "...Loading."
echo "...Please make sure you are connected to the Internet."
echo "...If this script isn't working, make sure EOL Conversion is set to Unix."
echo "..."

# Ensure the git is up to date.
git pull || { echo "git pull failed"; exit 1; }
echo "..."
git status
echo "..."
git add -A
echo "..."
git status
echo "..."
commit_message=""

# See if the -m option was specified.
while getopts ":m:" opt; do
  case ${opt} in
    m ) commit_message="$OPTARG";;
    \? ) echo "Invalid option: -$OPTARG" 1>&2; exit 1;;
    : ) echo "Option -$OPTARG requires an argument." 1>&2; exit 1;;
  esac
done


# Call the appropriate git commit command.
if [ -z "$commit_message" ]; then
  shift $((OPTIND - 1))
  if [ -n "$1" ]; then
    git commit -m "$1"
  else
    git commit -m "Updating Repo (unspecified commit message)."
  fi
else
  git commit -m "$commit_message"
fi


echo "..."
git status
echo "..."
git push
echo "..."
echo "...Finished."
