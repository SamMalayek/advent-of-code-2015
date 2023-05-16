from collections import defaultdict
from itertools import permutations
import json
parsed = open("input.txt",'r').read().splitlines()


def main():
	parsedInput = []
	neighborVals = defaultdict(dict)  # participant -> left/right -> value
	for constraint in parsed:
		cur = constraint.split(' ')
		participant = cur[0]
		neighbor = cur[10][:-1]
		gainLose = cur[2]
		happiness = int(cur[3])

		parsedInput.append([participant, gainLose, happiness, neighbor])

		neighborVals[participant][neighbor] = happiness if gainLose == 'gain' else -happiness

	maxHappiness = 0
	participantsPermutations = list(permutations(neighborVals.keys(), 8))

	for s1, s2, s3, s4, s5, s6, s7, s8 in participantsPermutations:
		curHappiness = 0
		curHappiness += neighborVals[s1][s2]
		curHappiness += neighborVals[s1][s8]
		curHappiness += neighborVals[s2][s1]
		curHappiness += neighborVals[s2][s3]
		curHappiness += neighborVals[s3][s2]
		curHappiness += neighborVals[s3][s4]
		curHappiness += neighborVals[s4][s3]
		curHappiness += neighborVals[s4][s5]

		curHappiness += neighborVals[s5][s4]
		curHappiness += neighborVals[s5][s6]
		curHappiness += neighborVals[s6][s5]
		curHappiness += neighborVals[s6][s7]
		curHappiness += neighborVals[s7][s6]
		curHappiness += neighborVals[s7][s8]
		curHappiness += neighborVals[s8][s7]
		curHappiness += neighborVals[s8][s1]
		maxHappiness = max(maxHappiness, curHappiness)

	print(maxHappiness)

main()
