#!/bin/bash

OLD_IFS=$IFS
users=`cat /etc/passwd`
#IFS=':'
for user in $users;do
    echo $user
done
