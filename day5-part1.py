parsed = open("input.txt",'r').read().splitlines()

resp = 0
vowels = {'a', 'e', 'i', 'o', 'u'}
badStrings = {'ab', 'cd', 'pq', 'xy'}
for s in parsed:
	for a, b in zip(s, s[1:]):
		if a == b:
			break
	else:
		continue

	found = False
	for i in range(len(s)-2):
		if s[i:i+2] in badStrings:
			found = True
	if found:
		continue

	numVowels = 0
	for c in s:
		if c in vowels:
			numVowels += 1

	if numVowels < 3:
		continue

	resp += 1

print(resp)
