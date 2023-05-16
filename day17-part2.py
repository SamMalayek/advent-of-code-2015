parsed = list(map(int, open("input.txt",'r').read().splitlines()))

allContainers = [(parsed[i], i) for i in range(len(parsed))]


def main():
	memo = {}
	solutions = set() # set of sorted container tuples
	minSize = 999999999
	def dfs(litersRemaining, containersUsed, containers):
		nonlocal minSize
		if litersRemaining < 0:
			return
		containersUsedTuple = tuple(sorted(containersUsed))
		if containersUsedTuple in memo:
			return

		if litersRemaining == 0:
			minSize = min(minSize, len(containersUsedTuple))
			solutions.add(containersUsedTuple)

		for i in range(len(containers)):

			cur, curI = containers.pop(i)
			dfs(litersRemaining - cur, containersUsed + [(cur, curI)], containers)
			containers.insert(i, (cur, curI))

		memo[containersUsedTuple] = True # don't need to store value since we're using closure

	dfs(150, [], allContainers)

	resp = 0

	for solution in solutions:
		if len(solution) == minSize:
			resp += 1

	print(resp)

main()






























