#!/bin/bash
a="Hello"
b="Hello"
[[ $a == $b ]] && echo Equal

echo "a's length is ${#a}"
echo "a's length is "`expr length $a`

echo `expr substr "this is a string" 6 2`
echo `expr index "this is a string" "is"`
echo `expr match "this is a string" "[a-z]*is[a-z]*"`

var="this is me"
var_arr=($var) # to array
echo ${var[0]}
echo ${var_arr[0]}
echo ${var_arr[*]}
echo ${var_arr[@]}
echo ${#var_arr[@]}

echo ${var:5} == "is me"
echo ${var:5:2} == "is"
echo ${var:(-2)} == "me"

echo ${var/me/you} == "this is you"
echo ${var//is/IS} == "thIS IS you"
echo ${var/%is*/IS} == "thIS"
echo ${var/#*is/IS} == "IS me"

echo ${var/ /_ }  == "this_ is me" #insert

echo ${var//is/} == "th  me" #delete

echo ${var#*is} == " is me" # delete from begin of the string
echo ${var##*is} == "me"

echo ${var%is*} == 'this' # delete from end of the string
echo ${var%%is*} == 'th'
