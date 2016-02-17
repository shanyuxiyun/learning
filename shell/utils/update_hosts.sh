#!/bin/bash

PASSWD=008
CURRENT=`pwd`
cd ~/bin

wget -O hosts https://raw.githubusercontent.com/racaljk/hosts/master/hosts

if [ ! -f ~/bin/hosts ];then
    echo download hosts fail and exit now.
    exit 1
fi
[ -f /etc/hosts ] && echo "$PASSWD" | sudo -S mv /etc/hosts /etc/hosts.bak 
[ $? -eq 0 ] && echo "$PASSWD" | sudo -S mv ~/bin/hosts /etc/hosts

if [ $? -eq 0 ];then
    echo update hosts successfully.
else 
    echo update hosts fail.
fi

cd $CURRENT
