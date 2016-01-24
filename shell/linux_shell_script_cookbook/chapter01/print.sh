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

# more info visit http://www.tldp.org/LDP/abs/html/colorizing.html
# The simplest, and perhaps most useful ANSI escape sequence is bold text, \033[1m ... \033[0m. The \033 represents an escape, the "[1" turns on the bold attribute, while the "[0" switches it off. The "m" terminates each term of the escape sequence. "]]"]]

# black='\E[30;47m'
#red='\E[31;47m'
#green='\E[32;47m'
#yellow='\E[33;47m'
#blue='\E[34;47m'
#magenta='\E[35;47m'
#cyan='\E[36;47m'
#white='\E[37;47m'
echo -e '\E[37;44m'"\e[1mContact List\e[0m"
for i in 0 1 2 3 4 5;do
    echo -e "\e[${i}mChoose one of [${i}m the following persons:\e[0m"
done

