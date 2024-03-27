#! /bin/bash

# $1 - first program argument
# $0 - script selfname

args=("$@")	# represents unlimited number of args

#echo ${args[0]} ${args[1]}

# to print all
echo $@

# check how many inputs
echo $#
