#!/bin/python

def fact(f):
	if f == 0:
		return 1;
	return f * fact(f-1)

print fact(12)
