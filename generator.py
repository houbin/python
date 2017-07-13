#!/usr/bin/env python
#coding=utf-8

g=(x*x for x in range(10))
for n in g:
    print n

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        b = a + b
        a = b
        n = n + 1

def fib_yield(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        b = a + b
        a = b
        n = n + 1

print "start print fib"
fib(9)
print "end print fib"
print

print
print "start print fib yield"
for n in fib_yield(9):
    print n
print "end print fib yield"
print



