puzzleInput = int(open("input.txt",'r').read().rstrip())


def main():
	def findGifts(n): # finds factors and multiplies by gifts
		resp = 0
		for i in range(n//2, 0, -1):
			if n % i == 0:
				if 50 * i >= n:
					resp += i*11
				else:
					break
		resp += n*11
		return resp

	i = 750000  # deductive reasoning (overall very naive solution)
	resp = 0
	while resp < puzzleInput:
		resp = findGifts(i)
		i += 1
		if i % 10000 == 0:
			print(i)
			print(resp)

	print("DONE:")
	print(i-1)
	print(resp)
	
main()
