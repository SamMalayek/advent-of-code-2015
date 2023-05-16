import re
raw = open("input.txt",'r').read().splitlines()
lines = [re.split(', | ', l) for l in raw]


def main():
	regs = {
		'a': 1,
		'b': 0,
	}
	cur = 0
	while cur < len(lines):
		l = lines[cur]
		instruction = l[0]
		if instruction == 'hlf':
			reg = l[1]
			regs[reg] = regs[reg] // 2
			cur += 1
		elif instruction == 'tpl':
			reg = l[1]
			regs[reg] = regs[reg] * 3
			cur += 1
		elif instruction == 'inc':
			reg = l[1]
			regs[reg] += 1
			cur += 1
		elif instruction == 'jmp':
			to = int(l[1])
			cur += to
		elif instruction == 'jie':
			reg = l[1]
			if regs[reg] % 2 == 0:
				to = int(l[2])
				cur += to
			else:
				cur += 1
		elif instruction == 'jio':
			reg = l[1]
			if regs[reg] == 1:
				to = int(l[2])
				cur += to
			else:
				cur += 1

	print(regs['b'])
	
main()
