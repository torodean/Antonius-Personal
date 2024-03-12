#!/bin/bash

# Iterate through each directory in the current location
for dir in */; do
    # Check if it's a directory
    if [ -d "$dir" ]; then
        # Enter the directory
        cd "$dir" || continue
        
        # Check if it's a Git repository
        if [ -d ".git" ]; then
            echo "...Updating repository for $dir"
            # Update the repository
            git pull
            git status
            echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        else
            echo "Skipping $dir - Not a Git repository"
        fi

        # Go back to the original directory
        cd - >/dev/null || exit
    fi
done
