#!/usr/bin/python

f = open("input.txt")
f = f.read()
f = f.split("\n")
inp = []
for l in f:
	l = l.split("\t")
	if l != ['']:
		inp.append(l)

def Closer(G, start):
	path = [start]
	cost = 0
	k = start
	for i in range(len(G)):
		row = k
		k = G[k].index(min(G[k]))
		if k == start and i < len(G) - 1:
			k = G[row].index(min(G[row][0:k] + G[row][k+1:]))
		path.append(k)
		cost += G[path[-2]][path[-1]]
		for j in range(len(G)):
			G[j][k] = float("inf")
	return cost

for i in range(len(inp)):
	for j in range(len(inp[i])):
		inp[i][j] = int(inp[i][j])

print Closer(inp, 0);


