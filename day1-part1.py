parsed = open("input.txt",'r').read().rstrip()
parens = {
	'(': 1,
	')': -1,
}

resp = 0

for c in parsed:
	resp += parens[c]
print(resp)
