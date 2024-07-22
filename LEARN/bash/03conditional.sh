#! /bin/bash

count=10
if [ $count -eq 10 ]
then
	echo "True"
else
	echo "False"
fi

# eq - equal	ne - not equal	  -gt - greater than

# also it's possible to use regular < > by
if (( $count > 9 ))
	echo "1"
elif (( $count <= 9 ))
	echo "2"
fi


# and operator
age=10
if [ "$age" -gt 18 ] && [ "$age" -lt 40 ]	# 18 < x < 40
then
	echo "correct"
else
	echo "incorrect"
if

# these also works
if [[ "$age" -gt 18 && "$age" -lt 40 ]] then
if [ "$age" -gt 18 -a "$age" -lt 40 ]
if [ "$age" -gt 18 -o "$age" -lt 40 ]		# -o means or
if [[ "$age" -gt 18 || "$age" -lt 40 ]] then	# also or


# case. multiple if state
# see 04


