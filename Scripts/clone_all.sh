#!/bin/bash

# Define an array of GitHub repositories to clone
repositories=(
    "torodean/Antonius-Handbook"
    "torodean/Antonius-Handbook-II"
    "torodean/Antonius-Compendium"
    "torodean/Antonius-Adventure"
    "torodean/DnD"
    "torodean/Antonius-DnD"
    "torodean/Antonius-Personal"
    "torodean/Antonius-MIA"
    "torodean/Antonius-Websites"
    "torodean/Antonius-Templates"
    "torodean/Antonius-GINA"
    "torodean/Antonius-Cookbook"
    "torodean/Antonius-Survival"
    "torodean/Antonius-Workouts"
    "torodean/Antonius-Notes"
    "torodean/The-Potato-Pages"
    "torodean/torodean.github.io"
    "torodean/Antonius-InventoryManagement"
    "torodean/Antonius-GameTemplate"
    "GitWebsiteTutorial/GitWebsiteTutorial.github.io"
    "MMORPDND/MMORPDND.github.io"
)

# Loop through each repository and clone it
for repo in "${repositories[@]}"; do
    echo "Cloning repository: $repo"
    git clone "git@github.com:$repo.git"
    echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
done
