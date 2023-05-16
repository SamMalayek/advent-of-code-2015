file_input = open("input.txt",'r').read().splitlines()
parsed = [list(map(int, l.split('x'))) for l in file_input]

resp = 0

for l, w, h in parsed:
	sides = sorted([l, w, h])
	resp += sides[0]*2 + sides[1]*2 + (l*w*h)

print(resp)
