#!/bin/sh
echo "...Loading."
echo "...Created by Antonius Torode."
echo "...Please make sure you are connected to the Internet."
echo "...Please enter script and customize for use."

MAX=5
for (( VAL=1; VAL <=$MAX; ++VAL ))
do
URLLINK="https://wow.zamimg.com/images/wow/maps/enus/zoom/4273-$VAL.jpg"
echo "...Gathering map from ${URLLINK}."
wget -r --no-parent ${URLLINK}
done