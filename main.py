#!/usr/bin/python

# we have a car and few cities. 
# we need to move the car in all of the cities only once
# and return back to the main city

f = open("input.txt")
f = f.read()
f = f.split("\n")

inp = []
for line in f:
	if line == '':
		continue
	inp.append(line.split("\t"))

def permutations(l):
	if len(l) <= 1:
		return [l]
	
	r = []
	for i in range(len(l)):
		s = l[:i] + l[i+1:]
		p = permutations(s)
		for x in p:
			r.append(l[i:i+1]+x)
	return r

def brute(Graph):
	perms = permutations(range(len(Graph)))
	weights = []
	for perm in perms:
		perm.append(perm[0])
		weight = 0
		for i in range(1, len(perm)):
			weight += Graph[perm[i-1]][perm[i]]

		weights.append(weight)
	
	minI = weights.index(min(weights))
	#print perms[minI] #the way
	print min(weights)

for i in range(len(inp)):
	for j in range(len(inp)):
		inp[i][j] = int(inp[i][j])

brute(inp)
