import json
d = json.loads(open("input.txt",'r').read())

def main():
	resp = 0

	def dfs(node):
		nonlocal resp
		if type(node) == dict:
			for k, v in node.items():
				dfs(k)
				dfs(v)
		if type(node) == list:
			for e in node:
				dfs(e)
		if type(node) == int:
			resp += node

	dfs(d)

	print(resp)

main()
