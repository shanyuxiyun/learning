#!/usr/bin/env python
# coding=utf-8

'''
usage :
python buildins.py > results
'''
cmds = dir(__builtins__)
for idx,cmd in enumerate(cmds):
    print '%s%d%s' % (8*'*',idx,8*'*')
    print help (cmd)
