#!/usr/bin/env python
# coding=utf-8

import sys

print sys.platform
print 2 ** 100
str = 'Love'
print str * 10

strarr=dir(__builtins__)
for attr in strarr :
    if  attr.find('__') == -1 and attr.islower(): 
        print attr 
