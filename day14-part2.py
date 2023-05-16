parsed = open("input.txt",'r').read().splitlines()

class Reindeer:
	def __init__(self, raw_line):
		cur = raw_line.split(' ')
		self.name = cur[0]
		self.speed = int(cur[3])
		self.flyDuration = int(cur[6])
		self.curFlyDuration = int(self.flyDuration)
		self.restDuration = int(cur[-2])
		self.curRestDuration = int(self.restDuration)
		self.curState = 'FLY' # or 'REST'
		self.distTraveled = 0
		self.curPoints = 0

	def getFlyDistance(self, dur):
		if self.curState == 'FLY':
			self.distTraveled += dur * self.speed
			self.curFlyDuration -= dur
			if self.curFlyDuration == 0:
				self.curState = 'REST'
				self.curFlyDuration = int(self.flyDuration)
		else:
			self.curRestDuration -= dur
			if self.curRestDuration == 0:
				self.curState = 'FLY'
				self.curRestDuration = int(self.restDuration)

		return self.distTraveled


def main():
	travelDur = 2503
	reindeers = {}
	travelTime = {}
	for l in parsed:
		cur = Reindeer(l)
		reindeers[cur.name] = cur

	while travelDur > 0:
		curDistances = []
		for reindeer in reindeers.values():
			curDistances.append((reindeer.getFlyDistance(1), reindeer.name))

		curDistances.sort()

		winning = curDistances[-1][1]
		reindeers[winning].curPoints += 1
		travelDur -= 1

	print(sorted(reindeers.values(), key=lambda reindeer: reindeer.curPoints)[-1].curPoints)

main()
