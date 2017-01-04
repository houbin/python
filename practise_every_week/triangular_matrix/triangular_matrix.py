#!/usr/bin/env python
# coding:utf-8

import sys

input=raw_input().split()

S=int(input[0]) # start number
T=int(input[1]) # max number
N=int(input[2]) # metrix size

print "start: debug info"
print "S:", S
print "T:", T
print "N:", N
print "end: debug info"
print
print

y=1
while y <= N:
	max_print = N - y + 1
	print_count=0
	x = 1
	while x <= N:
		if print_count >= max_print:
			break
		print_count += 1

		if print_count != 1:
			sys.stdout.write(' ')

		v = (((x - 1) * (2*N - x + 2) / 2) + y + S - 1) % T
		if v == 0:
			v = T
		sys.stdout.write(str(v))
		
		x += 1
	
	sys.stdout.write('\n')
	y += 1
