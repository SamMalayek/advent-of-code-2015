parsed = open("input.txt",'r').read().rstrip()

locs = set([(0,0)])

cur = [0,0] # x,y
cur2 = [0,0]

dirs = {
	'^': (0,1),
	'v': (0,-1),
	'<': (-1,0),
	'>': (1,0),
}

for i, c in enumerate(parsed):
	if i % 2 == 0:
		cur[0] += dirs[c][0]
		cur[1] += dirs[c][1]
		locs.add(tuple(cur))
	else:
		cur2[0] += dirs[c][0]
		cur2[1] += dirs[c][1]
		locs.add(tuple(cur2))

print(len(locs))
