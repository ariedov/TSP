#!/usr/bin/python
from random import randint
from sys import argv

script, count = argv
count = int(count)

output = ""

for i in range(count):
	for j in range(count):
		if i == j:
			output += `10000`
		else:
			output += `randint(1, 50)`
		output += "\t"
	output = output[0:-1]
	output += "\n"

f = open("input.txt", 'w')
f.write(output)
