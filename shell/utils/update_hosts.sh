#!/bin/bash

PWD=008\r
CURRENT=`pwd`
cd ~/bin

wget -O hosts https://raw.githubusercontent.com/racaljk/hosts/master/hosts

if [ ! -f ~/bin/hosts ];then
    echo download hosts fail and exit now.
    exit 1
fi

[ -f /etc/hosts ] && echo $PWD | sudo -S mv /etc/hosts /etc/hosts.bak 
[ $? -eq 0 ] && echo $PWD | sudo -S mv ~/bin/hosts /etc/hosts

if [ $? -eq 0 ];then
    echo update hosts successfully.
else 
    echo update hosts fail.
fi

cd $CURRENT
