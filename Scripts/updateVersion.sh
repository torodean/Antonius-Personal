#!/bin/bash

# This Script will update the version number in the a changelog, code, and a manual file (setup using the PEGA project). 
# In the changelog, it will create a new line for adding changes under the new version as well.

HEADER_FILE=../bin/main.hpp
MAN_FILE=../doc/TeX_files/settings.tex
CHANGELOG_FILE=../changelog.md

echo "
...Updating ${HEADER_FILE}"
ORIG_VERSION=`grep -r "^   const double VERSION" ${HEADER_FILE} | sed "s/[^0-9.]*//g"`
echo "...Old version number: ${ORIG_VERSION}"

sed -i -r 's/(.*)(\VERSION = 0.)([0-9]+)(.*)/echo "\1\2$((\3+1))\4"/ge' ${HEADER_FILE}

NEW_VERSION=`grep -r "^   const double VERSION" ${HEADER_FILE} | sed "s/[^0-9.]*//g"`
echo "...New version number: ${NEW_VERSION}"


echo "
...Updating settings.tex"
ORIG_VERSION=`grep -r "\VERSION}{" ${MAN_FILE} | sed "s/[^0-9.]*//g"`
echo "...Old version number: ${ORIG_VERSION}"

sed -i -r 's/(.*)(VERSION\}\{0.)([0-9]+)(.*)/echo "\\%TMPVAR%{\\\2$((\3+1))\4"/ge' ${MAN_FILE}
sed -i -r 's/%TMPVAR%/newcommand/g' ${MAN_FILE}

NEW_VERSION=`grep -r "\VERSION}{" ${MAN_FILE} | sed "s/[^0-9.]*//g"`
echo "...New version number: ${NEW_VERSION}"

echo "
...Updating changelog.md"

DATE=$(date +'%m/%d/%Y')
echo "...The date is: ${DATE}"

# This part still not working.
STRING="### ${DATE}: VERSION ${NEW_VERSION}"
echo "...Appending with: ${STRING}"

sed -i "/${ORIG_VERSION}/i ${STRING}" ${CHANGELOG_FILE}
sed -i "/${ORIG_VERSION}/i \   -" ${CHANGELOG_FILE}
sed -i "/${ORIG_VERSION}/i \ " ${CHANGELOG_FILE}
sed -i "/${ORIG_VERSION}/i -------------------------------------------------------------------------------------" ${CHANGELOG_FILE}
