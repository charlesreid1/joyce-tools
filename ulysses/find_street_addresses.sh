#!/bin/bash

PREFIX="${HOME}/codes/corpus-joyce-ulysses-tei"

rm -f possible_addresses
    
for FILENAME in `/bin/ls -1 ${PREFIX}/u*.xml`; do

    echo "\n--------------${FILENAME}-------------\n" >> possible_addresses

    cat ${FILENAME} | \
        \
        sed 's/<lb n="......"\/>//g' | \
        sed 's/<said who=".\{1,\}">//g' | \
        sed 's/<sp who=".\{1,\}">//g' | \
        \
        /usr/bin/grep -iv "episode" | \
        \
        /usr/bin/grep -i "[0-9]\{1,3\}\|street" \
        >> possible_addresses

    echo "\n" >> possible_addresses

done 

NUM="`wc -l possible_addresses | awk {'print $1'}`"

echo "Found ${NUM} possible addresses."
echo "To review the list of possible addresses, run:"
echo ""
echo "cat ./possible_addresses"
