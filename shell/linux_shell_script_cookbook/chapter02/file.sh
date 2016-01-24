#!/bin/bash

# compare two files
#comm a.txt b.txt -1 -2
# diff a.txt b.txt
# create immutable file 
#chattr +i file.sh

#sudo chattr -i file.sh

# pushd popd dirs

grep "main" . -r --include *.{java,class}
grep "main" . -r --exclude "README"
cut -f 2,3 file.py
