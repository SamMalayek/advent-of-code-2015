parsed = open("input.txt",'r').read().splitlines()

resp = [[0 for _ in range(1000)] for _ in range(1000)]

def turn(x1, y1, x2, y2, onOff):
	for x in range(x1, x2+1):
		for y in range(y1, y2+1):
			resp[x][y] = onOff

def toggle(x1, y1, x2, y2):

	for x in range(x1, x2+1):
		for y in range(y1, y2+1):
			if resp[x][y] == 1:
				resp[x][y] = 0
			else:
				resp[x][y] = 1

for cmdRaw in parsed:
	cmd = cmdRaw.replace(',', ' ').split(' ')
	
	if cmd[0] == 'toggle':
		x1 = int(cmd[1])
		y1 = int(cmd[2])
		x2 = int(cmd[4])
		y2 = int(cmd[5])
		toggle(x1, y1, x2, y2)
	elif cmd[0] == 'turn':
		if cmd[1] == 'on':
			x1 = int(cmd[2])
			y1 = int(cmd[3])
			x2 = int(cmd[5])
			y2 = int(cmd[6])
			turn(x1, y1, x2, y2, 1)
		else:
			x1 = int(cmd[2])
			y1 = int(cmd[3])
			x2 = int(cmd[5])
			y2 = int(cmd[6])
			turn(x1, y1, x2, y2, 0)

respCount = 0
for x in range(len(resp)):
	for y in range(len(resp[0])):
		if resp[x][y] == 1:
			respCount += 1

print(respCount)
