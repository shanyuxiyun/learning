#!/usr/bin/env python
# coding=utf-8

d = {'name':'lee','age':33}
print d
d = dict(name='lee',age=33)
print d

d = zip(['name','age'],['lee',33])
print d
d = dict(d)
print d
