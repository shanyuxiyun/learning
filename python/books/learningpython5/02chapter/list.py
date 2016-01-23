#!/usr/bin/env python
# coding=utf-8

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print m
m[0][0] = 111
print m

g = (sum(row) for row in m)
print g.next()
print g.next()
print g.next()

print list(map(sum,m))

print {sum(row) for row in m} #set
print {i:sum(m[i]) for i in range(3)} #dict

print [row[1] for row in m]
print list(range(-5, 10, 2))

print [[x**2, x**3] for x in range(10) if x % 2 == 0]
