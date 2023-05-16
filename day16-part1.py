import re
from collections import defaultdict
parsed = open("input.txt",'r').read().splitlines()

mfcsamResults = {
	'children': 3,
	'cats': 7,
	'samoyeds': 2,
	'pomeranians': 3,
	'akitas': 0,
	'vizslas': 0,
	'goldfish': 5,
	'trees': 3,
	'cars': 2,
	'perfumes': 1,
}

def main():
	sueDict = defaultdict(dict)
	for l in parsed:
		cur = re.split(': |, | ', l)
		sueDict[cur[1]][cur[2]] = int(cur[3])
		sueDict[cur[1]][cur[4]] = int(cur[5])
		sueDict[cur[1]][cur[6]] = int(cur[7])

	for sueNum, sueItems in sueDict.items():
		for item, quant in sueItems.items():
			if mfcsamResults[item] != quant:
				break
		else:
			print(sueNum)
			break

main()
