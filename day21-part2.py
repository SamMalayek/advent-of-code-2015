class Character:
	def __init__(self, defense = 0, damage = 0):
		self.hitPoints = 100
		self.defense = defense
		self.damage = damage

	def takeHit(self, damage):
		curDamage = max(1, damage - self.defense)
		self.hitPoints -= curDamage


def fight(player, boss):
	while player.hitPoints > 0 and boss.hitPoints > 0:
		boss.takeHit(player.damage)
		if boss.hitPoints <= 0:
			return "PLAYER"
		player.takeHit(boss.damage)

	return "BOSS" # fairly certain this is the only logical possiblity


def main():
	weapons = [(8, 4), (10, 5), (25, 6), (40, 7), (74, 8)] # cost, damage
	armors = [(0, 0), (13, 1), (31, 2), (53, 3), (75, 4), (102, 5)] # cost, defense
	rings = [(0, 0, 0), (0, 0, 0), (25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)] # cost, damage, defense
	resp = 0
	for w, weapon in enumerate(weapons):
		for a, armor in enumerate(armors):
			for r1, ring1 in enumerate(rings):
				for r2, ring2 in enumerate(rings):
					if r1 == r2:
						continue
					totalCost = weapon[0] + armor[0] + ring1[0] + ring2[0]
					boss = Character(2, 8)
					totalDamage = weapon[1] + ring1[1] + ring2[1]
					totalDefense = armor[1] + ring1[2] + ring2[2]
					player = Character(totalDefense, totalDamage)
					result = fight(player, boss)
					if result == 'BOSS':
						resp = max(resp, totalCost)

	print(resp)
	
main()
