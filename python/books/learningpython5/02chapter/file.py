#!/usr/bin/env python
# coding=utf-8

fl = open('file.py','r')
print fl.read()
fl.close()


for line in open('file.py','r'):
    print line

