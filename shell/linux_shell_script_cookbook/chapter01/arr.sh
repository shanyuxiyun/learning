#!/bin/bash

arr=(1 2 3 4)
for i in ${arr[*]};do
    echo $i
done

a[0]=1
a[1]=2
a[2]=3
for i in ${a[*]};do
    echo $i
done
echo "len of a is ${#a[*]}"

declare -A fruits
fruits=([apple]='101' [pear]='102')
echo ${fruits[*]}
echo ${!fruits[*]}
echo ${fruits[apple]}
