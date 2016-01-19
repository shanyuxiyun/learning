#!/usr/bin/env python
# coding=utf-8

'''
usage :
python buildins.py > builtins.guide
'''

flag = '#######*****_*****#######'
cmds = dir(__builtins__)
for idx,cmd in enumerate(cmds):
    print '%s%d%s' % (flag,idx,flag)
    print help (cmd)
