#! /bin/bash
# compare 2 strings (equal or less or more of each other), concatunate

echo "enter 1st string"
read st1

echo "enter 2nd string"
read st2

# check content equality
if [ "$st1" == "$st2" ]
then
	echo "Both strings match"
else
	echo "strings don't match"
fi


# check length equality
if [ "$st1" \< "$st2" ]
then
	echo "st1 < st2"
elif [ "$st1" \> "$st2" ]
	echo "st1 > st2"
else
	echo "equal"
fi


# concatination
c=$st1$st2
echo $c


# make all lower case
echo ${st1^}
echo ${st2^^}
# capitalize particular letter
echo ${st1^g}

