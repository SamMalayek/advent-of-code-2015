parsed = open("input.txt",'r').read().rstrip()
parens = {
	'(': 1,
	')': -1,
}

resp = 0

for i, c in enumerate(parsed):
	resp += parens[c]
	if resp < 0:
		print(i+ 1)
		break
