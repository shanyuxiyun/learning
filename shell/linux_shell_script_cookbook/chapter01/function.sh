#!/bin/bash
 foo(){
if [ $# -eq 2 ];then
    echo $2 $1
else 
    echo $@ # list
    echo $* # single entry
fi
}

#export -f foo

foo A
foo A B
foo A B C 
foo 
