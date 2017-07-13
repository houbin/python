#!/usr/bin/env python
#coding=utf-8

from collections import Iterable
 
print 'print list: start'
l=[1, 2, 3, 4, 5, 6]

for i in l:
    print i
    
print 'print list: end'
print

print 'print dict: start'
d={'z':123, 'houbin':123, 'wangjing':456, 'yaya':789}
for i in d:
    print i
print 'print list: end'
print

print 'print dict k,v : start'
for k,v in d.iteritems():
    print k, v
print 'print dict k,v : end'

print 'check instance iterable start'
print isinstance('abc', Iterable)
print isinstance([1,2,3], Iterable)
print isinstance(123, Iterable)
print 'check instance iterable end'

