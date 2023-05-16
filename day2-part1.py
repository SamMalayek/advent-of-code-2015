file_input = open("input.txt",'r').read().splitlines()
parsed = [list(map(int, l.split('x'))) for l in file_input]

resp = 0

for l, w, h in parsed:
	smallestSide = min(l*w, w*h, h*l)
	resp += (2*l*w + 2*w*h + 2*h*l + smallestSide)

print(resp)
