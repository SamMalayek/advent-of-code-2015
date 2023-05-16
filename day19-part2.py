import sys
from collections import defaultdict
raw = open("input.txt",'r').read().splitlines()
linesSplit = [list(l.split(' => ')) for l in raw]

lines = []

for l in linesSplit:
	lines.append((l[1], l[0]))

lines.sort(key=lambda x: -len(x[0])) # biggest replacements first

def main():
	startMolecule = sys.argv[1]
	numTokens = len([a for a in startMolecule if a.isupper()])
	numRn = len([a for a, b in zip(startMolecule, startMolecule[1:]) if a+b == 'Rn'])
	numAr = len([b for a, b in zip(startMolecule, startMolecule[1:]) if a+b == 'Ar'])
	numY = len([b for b in startMolecule if b == 'Y'])
	print(f'num tokens: {numTokens}')
	print(f'num Rn: {numRn}')
	print(f'num Ar: {numAr}')
	print(f'num Y: {numY}')
	print(numTokens - numAr - numRn - 2*numY - 1)

main()
