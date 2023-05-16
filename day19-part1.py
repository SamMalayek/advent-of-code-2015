import sys
from collections import defaultdict
raw = open("input.txt",'r').read().splitlines()
lines = [list(l.split(' => ')) for l in raw]

linesD = defaultdict(list)

for l in lines:
	linesD[l[0]].append(l[1])

def main():
	startMolecule = sys.argv[1] # second part of puzzle input is provided here.
	seen = set([])
	for i in range(len(startMolecule)):
		if startMolecule[i] in linesD:
			for swap in linesD[startMolecule[i]]:
				new = startMolecule[:i] + swap + startMolecule[i+1:]
				seen.add(new)
				
		if i < len(startMolecule) - 1 and startMolecule[i:i+2] in linesD:
			old = startMolecule[i:i+2]
			for swap in linesD[old]:
				new = startMolecule[:i] + swap + startMolecule[i+2:]
				seen.add(new)

	print(len(seen))

main()
