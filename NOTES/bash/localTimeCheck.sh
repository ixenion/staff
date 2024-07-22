#!/bin/bash
val1=$(date +%s)
sleep 1
val2=$(date +%s)
#difference=$(echo $(date +%s) "-" $(date +%s) | bc)
difference=$(echo $val2 "-" $val1 | bc)
echo $difference
