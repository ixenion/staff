#! /bin/bash


# if execute this command twise, error 
mkdir directory
# to avoid that:
mkdir -p directory


# check if the dir exists:
echo "Enter dir to check"
read direct
if [ -d "$direct" ]
then
	echo "exists"
else
	echo "not exists"


# crate a file
echo "Enter fileName to create"
read filename
touch $dilename


# check if the file exists:
echo "Enter file to check"
read filename
if [[ -f "$filename" ]]
then
	echo "exists"
else
	echo "not exists"



# read file line by line
echo "Enter file to read"
read filename
if [[ -f "$filename" ]]
then
	while IFS= read -r line
	do
		echo "$line"
	done < $filename
else
	echo "not exists"

# remove the file
echo "Enter file to remove"
read filename
if [[ -f "$filename" ]]
then
	rm $filename
else
	echo "not exists"



