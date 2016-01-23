#!/bin/bash

gedit &
PID=`pgrep gedit`
cat /proc/$PID/environ | tr '\0' '\n'
kill -9 $PID

VAR=LEEEEEEE
# used by other shells opened from this indirectly or directly.
export VAR

echo -e '\e[31;45m'
# length of string
echo ${#VAR}

# /bin/bash
echo $SHELL
#env.sh
echo $0

if [ $UID -ne 0 ];then
    echo current user is root.
else
    echo current user is not root.
fi
