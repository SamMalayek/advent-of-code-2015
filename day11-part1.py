cur = list(open("input.txt",'r').read().rstrip())

ignoreLetters = {9, 12, 15}

# Requirements:
# - one increasing straight of at least 3 letters
# - may not contain ignoreLetters
# - at least 2x non-overlapping pairs

# abcdefgh -> abcdffaa

def isCurValid(cur):
	# - one increasing straight of at least 3 letters
	for i in range(len(cur)):
		if i < len(cur)-3 and cur[i] == cur[i+1]-1 == cur[i+2]-2:
			break
	else:
		return False

	# - may not contain ignoreLetters
	for d in cur:
		if d in ignoreLetters:
			return False

	numPairs = 0
	i = 0
	# - at least 2x non-overlapping pairs
	while i < len(cur):
		if i < len(cur)-1 and cur[i] == cur[i+1]:
			numPairs += 1
			i += 2
		else:
			i += 1

	return numPairs > 1


def increment(cur, i):
	cur[i] += 1

	if cur[i] > 26:
		cur[i] = 1
		i -= 1
		if i < 0:
			i = len(cur) - 1
		return increment(cur, i)

	else:
		return cur


for i in range(len(cur)):
	cur[i] = ord(cur[i]) - 96

isValid = False

while not isValid:
	i = len(cur) - 1

	cur = increment(cur, i)

	isValid = isCurValid(cur)

for i in range(len(cur)):
	cur[i] = chr(cur[i] + 96) 

print(''.join(cur))
