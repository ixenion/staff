#! /bin/bash

number=1
# while works with true statements
while [ $number -lt 10 ]
do
	echo "$number"
	number=$(( number+1 ))
done

# -le - less or equal to

# until works with false statements
until [ $number -ge 10 ]
do
	echo "$number"
	number=$(( number+1 ))
done				# prints 1,2...9



# for loop
for i in {0..5}
do
	echo $i
done				# prints 0 1 2 3 4 5

# change increment
for i in {0..5..2}
do
	echo $i
done				# prints 0 2 4

for (( i=0; i<5; i++ ))		# c style
do
done


for (( i=0; i,=10; i++))
do
	if [ $i -gt 5 ]
	then
		break
	fi
	echo $i
done				# breaks at 5, no more prints


# skip 3 and 7
for (( i=0; i<=10; i++))
do
	if [ $i -gt 3 ] || [ $i -eq 7 ]
	then
		continue
	fi
	echo $i
done				# prints 1 2 4 5 6 8 9 10


