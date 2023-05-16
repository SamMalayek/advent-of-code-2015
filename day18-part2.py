parsed = open("input.txt",'r').read().splitlines()

lines = [list(l) for l in parsed]

numRows = len(lines)
numCols = len(lines[0])

def handleLight(row, col, curLines):
	isOn = curLines[row][col] == '#'
	numOn = 0
	if row > 0 and curLines[row-1][col] == '#': # top
		numOn += 1
	if row > 0 and col < numCols - 1 and curLines[row-1][col+1] == '#': # top-right
		numOn += 1
	if col < numCols - 1 and curLines[row][col+1] == '#': # right
		numOn += 1
	if row < numRows - 1 and col < numCols - 1 and curLines[row+1][col+1] == '#': # bot-right
		numOn += 1
	if row < numRows - 1 and curLines[row+1][col] == '#': # bot
		numOn += 1
	if row < numRows - 1 and col > 0 and curLines[row+1][col-1] == '#': # bot-left
		numOn += 1
	if col > 0 and curLines[row][col-1] == '#': # left
		numOn += 1
	if row > 0 and col > 0 and curLines[row-1][col-1] == '#': # top-left
		numOn += 1

	if isOn and numOn not in {2,3}:
		return '.'
	elif isOn and numOn in {2,3}:
		return '#'
	elif not isOn and numOn == 3:
		return '#'
	else:
		return '.'

def goLights(curLines):
	newLines = [l[:] for l in curLines]
	for row in range(len(curLines)):
		for col in range(len(curLines[0])):
			cur = handleLight(row, col, curLines)
			newLines[row][col] = cur
	newLines[0][0] = '#'
	newLines[0][numCols-1] = '#'
	newLines[numRows-1][0] = '#'
	newLines[numRows-1][numCols-1] = '#'
	return newLines

def main():
	iterations = 100

	lines[0][0] = '#'
	lines[0][numCols-1] = '#'
	lines[numRows-1][0] = '#'
	lines[numRows-1][numCols-1] = '#'

	cur = lines
	while iterations > 0:
		cur = goLights(cur)
		iterations -= 1

	numOn = 0
	for l in cur:
		for i in l:
			if i == '#':
				numOn += 1
	print(numOn)

main()
