#!/usr/bin/env python
# coding:utf-8

print 'hello, world'
print 'hello, world','jump over','the layz dog'
print '100 + 200 = ', 100+200

name = raw_input("please enter your name: ")
print name

# print absolute value of an integer;
a = -100
if a >= 0:
    print a
else:
    print -a

print "I\'am \"OK\""

print "I\'am learning\nPython"

print "\\\n\\"

print "\\\t\\"
print r"\\\t\\"

# print multiple lines
print '''line1
line2
line3
'''

print r'''line1
line2
line3
'''

# print bool
print True
print False

print "(3 > 2) is", 3>2
print "(2 > 3) is", 2>3

# and
print "True and True is", True and True
print "False and False is", False and False
print "True and False is", True and False

# or
print "True or True is", True or True
print "False or False is", False or False
print "True or False is", True or False

# not
print "not True is", not True
print "not False is", not False

# bool judgement
age = 10
if age >= 18:
    print "adult"
#	print "just a test"
elif age >= 12:
    print "younger"
else:
    print "child"

# assignment
a = 123
print a
a = "abc"
print a

a = 123
b = a
a = "xyz"
print b

# 
PI = 3.1415926

print "10.0 / 3 is", 10.0/3
print "10 / 3 is", 10/3
print "10 % 3 is", 10%3

# diff type
print "\n====== this is different type ====="
type_int = 123
type_string = "houbin"
type_int = type_string
print type_int
print type_string

# print unicode
print "\n====== this is unicode ======="
print u"中文"
print u"\u4e2d"

