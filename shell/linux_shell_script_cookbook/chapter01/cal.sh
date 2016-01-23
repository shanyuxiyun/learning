#!/bin/bash

# let (()) []
# expr bc

a=3
b=5
let c=a+b
echo ${c}
let c++
echo ${c}


c=$[ a + b ]
c=$(( a + b ))
c=`expr $a + $b`
echo $c

echo "scale=7;3.14 * 2.79" | bc
