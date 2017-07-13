#!/usr/bin/env python
#coding:utf-8

L=['Michael', 'Sarah', 'Tracy']

r=[]
n=3

for i in range(n):
    r.append(L[i])

print r

print L[0:3]

print L[-1:]
print L[-2:-1]
print L[-2:]

L=range(100)
print L
print L[-10:]

T=(0,1,2,3,4,5)
print T[-3:]

print 'ABCDEFG'[:3]
