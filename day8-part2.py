parsed = open("input.txt",'r').read().splitlines()
table = str.maketrans({'"': r'\"', '\\': r'\\'})
resp = sum([len(l.translate(table)) + 2 - len(l) for l in parsed])
# Could just count the number of " and \ since those are what we double up
print(resp)
