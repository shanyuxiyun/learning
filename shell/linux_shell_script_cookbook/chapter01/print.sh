#!/bin/bash

echo "Hello ! World"
echo -e "Lee\tDong"
echo "Lee\tDong"

range='0 1 2 3 4 5 6 7'
for i in $range;do
    for j in $range;do
        echo -e "\e[3${i};4${j}m this is 3${i};4${j}m  \e[0m"
        echo -e "\e[4${j};3${i}m this is 4${j};3${i}m  \e[0m"
    done
    echo
done

printf "%s is %d years old.\n" "Li Dong" 21



