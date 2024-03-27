#! /bin/bash

car =('bmw' 'toyota' 'honda')
echo "${car[@]}"	# prints all the array
echo "${!car[@]}"	# prints all the indexes of the array

unset car[1]	# removes toyota from the array so that echo "${!car[@]}" returns 0 2 instead 0 1 2
# return/replase this value:
car[2]='mercedes'







