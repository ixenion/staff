#!/bin/bash

servers="server1.... server2...."
seconds="3"  # value for servers to differ (in seconds)
for server in $servers
do
    difference=$(echo $(ssh -l root ${server} "( date +%s )") "-" $(date +%s) | bc)
    if [[ ${difference#-} -le ${seconds} ]] ; then
        echo $server - IN SYNC
    else
        echo $server - NOT IN SYNC 
    fi
done
