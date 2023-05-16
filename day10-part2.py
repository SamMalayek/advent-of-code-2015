from itertools import groupby
myInput = open("input.txt",'r').read().rstrip()

def main():
	def genNext(numsStr):
		grouped = [''.join(group) for _, group in groupby(numsStr)]
		resp = ''

		for subGroup in grouped:
			resp += str(len(subGroup))
			resp += subGroup[0]

		return resp

	cur = myInput
	for _ in range(50):
		nextNum = genNext(cur)
		cur = nextNum
	print(len(cur))

main()
