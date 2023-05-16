import math
raw = open("input.txt",'r').read().splitlines()
lines = list(reversed([int(l) for l in raw]))


def main():
	minGroup1Len = 9999999
	minGroup1QE = 99999999999999999

	memo = {}

	group1Weight = sum(lines) // 3

	# should have used itertools.combinations
	def dfs(packagesRemaining, group1):
		nonlocal minGroup1Len
		nonlocal minGroup1QE
		key = tuple([tuple(sorted(group1))])
		if key in memo:
			return

		# limit search space:
		if sum(group1) > group1Weight:
			memo[key] = True
			return
		if len(group1) > minGroup1Len:
			memo[key] = True
			return

		if sum(group1) == group1Weight:
			curLen = len(group1)
			curQE = math.prod(group1)

			if curLen <= minGroup1Len:
				if curLen < minGroup1Len:
					minGroup1Len = curLen
					minGroup1QE = curQE
				else:
					minGroup1QE = min(curQE, minGroup1QE)

		if packagesRemaining:
			for i in range(len(packagesRemaining)):
				dfs(packagesRemaining[:i] + packagesRemaining[i+1:], group1 + [packagesRemaining[i]])

		memo[key] = True

	dfs(lines, [])
	print(f'ANSWER: {minGroup1QE}')

main()
