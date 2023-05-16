import re
from collections import defaultdict
parsed = open("input.txt",'r').read().splitlines()

def main():
	dag = defaultdict(list)

	for connection in parsed:
		cur = re.split(' to | = ', connection)
		startCity, endCity, dist = cur
		dag[startCity].append((endCity, int(dist)))
		dag[endCity].append((startCity, int(dist)))

	resp = 0

	def dfs(city, seen, travelled):
		nonlocal resp
		wentDeeper = False
		for neighbor, dist in dag[city]:
			if neighbor in seen:
				continue
			seen.add(neighbor)
			dfs(neighbor, seen, travelled+dist)
			seen.remove(neighbor)
			wentDeeper = True
		if not wentDeeper:  # reached end
			resp = max(resp, travelled)

	for city in dag.keys():
		seen = set([city])
		curResp = dfs(city, seen, 0)

	print(resp)
main()


