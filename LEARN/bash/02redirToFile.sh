#! /bin/bash

#echo "hello bash script" > temp02.txt

# user input
#cat > temp.txt

# append. not replace
cat >> temp.txt

# multiple line comment
: '
fsdfsdfsdfsdfsff
sdfsdfsdfsfsfdf
sdfsdfsdfsdfsdf'

cat << variable
some text
and another text
variable
# returns (prints to the terminal) all between 2 "variable" delimeters


