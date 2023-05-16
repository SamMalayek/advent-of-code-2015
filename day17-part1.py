parsed = list(map(int, open("input.txt",'r').read().splitlines()))

allContainers = [(parsed[i], i) for i in range(len(parsed))]


def main():
	memo = {}
	solutions = set() # set of sorted container tuples
	def dfs(litersRemaining, containersUsed, containers):
		if litersRemaining < 0:
			return
		containersUsedTuple = tuple(sorted(containersUsed))
		if containersUsedTuple in memo:
			return

		if litersRemaining == 0:
			solutions.add(containersUsedTuple)

		for i in range(len(containers)):
			cur, curI = containers.pop(i)
			dfs(litersRemaining - cur, containersUsed + [(cur, curI)], containers)
			containers.insert(i, (cur, curI))

		memo[containersUsedTuple] = True # don't need to store value since we're using closure

	dfs(150, [], allContainers)
	print(len(solutions))

main()
