#!/bin/bash

# call by /etc/rc.local

MOUNT_DIR=/home/lee/disk
if [ -d $MOUNT_DIR ];then
    if [ "`ls -A $MOUNT_DIR`" == "" ];then
        echo "008" | sudo -S mount /dev/sda6 $MOUNT_DIR
    fi
fi
