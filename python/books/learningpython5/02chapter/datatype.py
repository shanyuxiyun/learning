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
