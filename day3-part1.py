parsed = open("input.txt",'r').read().rstrip()

locs = set([(0,0)])

cur = [0,0] # x,y

dirs = {
	'^': (0,1),
	'v': (0,-1),
	'<': (-1,0),
	'>': (1,0),
}

for c in parsed:
	cur[0] += dirs[c][0]
	cur[1] += dirs[c][1]
	locs.add(tuple(cur))

print(len(locs))
