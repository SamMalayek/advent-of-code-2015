def getPrevRowCol(curRow, curCol):
	prevRow = curRow + 1
	prevCol = curCol - 1
	if prevCol < 0:
		prevRow = 0
		prevCol = curRow - 1
	return prevRow, prevCol

def getNextRowCol(curRow, curCol):
	nextRow = curRow - 1
	nextCol = curCol + 1
	if nextRow < 0:
		nextRow = curCol + 1
		nextCol = 0
	return nextRow, nextCol


def main():
	grid = [[0]*6050 for _ in range(6050)]

	curRow = 2
	curCol = 0

	grid[0][0] = 20151125
	grid[1][0] = 31916031
	grid[0][1] = 18749137

	while curRow < 6050 and curCol < 6050:
		prevRow, prevCol = getPrevRowCol(curRow, curCol)
		prev = grid[prevRow][prevCol]
		cur = prev * 252533 % 33554393
		grid[curRow][curCol] = cur
		if curRow == 3009 and curCol == 3018:
			print(f'ANSWER: {cur}')
			quit()
		curRow, curCol = getNextRowCol(curRow, curCol)


	print(grid[3009][3018])


main()
