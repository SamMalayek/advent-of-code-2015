from hashlib import md5
parsed = open("input.txt",'r').read().rstrip()

i = 0

while True:
	curStr = parsed + str(i)
	cur = md5(curStr.encode('utf-8')).hexdigest()
	if cur[:6] == '000000':
		print(i)
		break
	i += 1
