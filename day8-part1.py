parsed = open("input.txt",'r').read().splitlines()
resp = sum([len(l) - len(eval(l)) for l in parsed])

print(resp)
