parsed = open("input.txt",'r').read().splitlines()

resp = 0

for s in parsed:
	for i in range(len(s)):
		if s[i:i+2] in s[i+2:]:
			break
	else:
		continue

	for i in range(len(s)):
		if i + 2 < len(s) and s[i] == s[i+2]:
			break
	else:
		continue

	resp += 1

print(resp)
