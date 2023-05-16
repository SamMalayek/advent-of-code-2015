parsed = open("input.txt",'r').read().splitlines()

travelDur = 2503

class Reindeer:
	def __init__(self, raw_line):
		cur = raw_line.split(' ')
		self.name = cur[0]
		self.speed = int(cur[3])
		self.flyDuration = int(cur[6])
		self.restDuration = int(cur[-2])

	def getFlyDistance(self, dur):
		dist = 0
		while dur > 0:
			dur -= self.flyDuration
			if dur > 0:
				dist += self.speed * self.flyDuration
			dur -= self.restDuration
		return dist

def main():
	reindeers = {}
	travelTime = {}
	for l in parsed:
		cur = Reindeer(l)
		reindeers[cur.name] = cur
		travelTime[cur.name] = cur.getFlyDistance(travelDur)

	print(sorted(travelTime.values())[-1])

main()
