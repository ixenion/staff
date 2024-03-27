#! /bin/bash
# send output from one script to another

MESSAGE="hello"
export MESSAGE
./09pipes2.sh

# prints "msg from 1 is: hello"

