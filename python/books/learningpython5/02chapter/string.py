#!/usr/bin/env python
# coding=utf-8

import math
import random

print random.random()
print random.choice([1,2,3,4])
print math.pi

s = '123456'

assert len(s) == 6
assert s[0] == '1'
assert s[5] == '6'
assert s[-1] == '6'
assert s[-6] == '1'

assert s[0:3] == '123'

assert s.find('23') == 1
assert s.replace('1','0') == '023456'
assert s.split('4')[1] == '56'
assert s.isdigit()



l = list(s)
assert ''.join(l) == s

b = bytearray(b'123456')
b.extend('7')
assert b.decode() == '1234567'

s = '*'
assert s*3 == '***'


s = 'Lee,Dongw'
print s.upper()
print s.rstrip()
print s.split(',')

print '{0} is {1}'.format('lee',10)
print '{} is {}'.format('Lee',11)

import re
m = re.match('Hello (.*)','Hello World')
print m.group(1)
