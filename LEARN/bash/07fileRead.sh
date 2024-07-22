#! /bin/bash

# read file using stdin

while read line
do
	echo "$line"
done < "${1:-/dev/stdin}"

# usage
# ./07... untitled\ document
#untitled\ document is "untitled document" - file name

