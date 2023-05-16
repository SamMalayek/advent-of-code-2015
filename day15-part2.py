import re
import math
parsed = open("input.txt",'r').read().splitlines()


def main():
	ingredientVals = []

	# Schema: ['Butterscotch:', 'capacity', '-1', 'durability', '-2', 'flavor', '6', 'texture', '3', 'calories', '8']

	for l in parsed:
		cur = re.split(", | ", l)
		ingredientVals.append([int(cur[2]), int(cur[4]), int(cur[6]), int(cur[8]), int(cur[10])])

	resp = 0
	memo = {}
	def dfs(*args):
		nonlocal resp
		argsHashable = tuple(args)
		if argsHashable in memo:
			return

		ingredientProperties = [0] * 5
		for i, ingredients in enumerate(ingredientVals):
			for j, ingredient in enumerate(ingredients):
				ingredientProperties[j] += ingredient * args[i]

		for i in range(len(ingredientProperties)):
			if ingredientProperties[i] < 0:
				ingredientProperties[i] = 0

		cur = math.prod(ingredientProperties[:-1])

		if ingredientProperties[-1] == 500:
			resp = max(resp, cur)
		memo[argsHashable] = True

		if args[0] > 0:
			dfs(args[0] - 1, args[1] + 1, args[2], args[3])
			dfs(args[0] - 1, args[1], args[2] + 1, args[3])
			dfs(args[0] - 1, args[1], args[2], args[3] + 1)

	dfs(100, 0, 0, 0)

	print(resp)

main()
