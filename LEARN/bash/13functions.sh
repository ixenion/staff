#! /bin/bash

function funcname()
{
	echo "this is brand new function"
}

# calling
funcname


# function with args
function funcname2()
{
	echo $1 $2 $3
}

# calling
funcname2 this is hi


# vars inside the function
function funcname3()
{
	var1="I'm working"
	echo "$var1"
}
var1="I'm rest"
echo $var1	# return "rest"
funcname3
echo $var1	# return "working"





