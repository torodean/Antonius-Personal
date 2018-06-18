#!/bin/sh
echo "...Loading."
echo "...Created by Antonius Torode."
echo "...Please make sure you are connected to the Internet."
echo "...Please enter a URL."
read URLLINK
echo "...Creating project ${URLLINK}."

wget -r --no-parent ${URLLINK}