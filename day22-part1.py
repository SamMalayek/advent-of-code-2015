def main():
	# - Effect tuple -> (effectName, turnsRemaining, damage, armor, mana)

	spells = [
		('shield', 0, 7, 0, 6, 0, 113),
		('drain', 2, 0, 2, 0, 0, 73),
		('poison', 3, 0, 0, 6, 0, 173), # Poison damage begins after being cast (only multi-turn damage spell!)
		('recharge', 0, 0, 0, 5, 101, 229),
		('magicMissile', 4, 0, 0, 0, 0, 53), # spellName, damage, defense, heal, turns, manaGain, manaCost
	]

	memo = {}
	manaUsedMin = 9999999

	def dfs(bossHP, playerHP, playerMana, manaUsed, effects, spellsUsed, actions):
		nonlocal manaUsedMin
		effectsSerialized = ''
		for k, v in effects.items():
			effectsSerialized += k
			effectsSerialized += str(v)
		if (bossHP, playerHP, playerMana, manaUsed, effectsSerialized) in memo:
			return
		
		for i, (spellName, damage, defense, heal, turns, manaGain, manaCost) in enumerate(spells): 
			# check effects if active
			curBossHP, curPlayerHP, curPlayerMana, curManaUsed, curEffects = bossHP, playerHP, playerMana, manaUsed, effects
			curActions = actions[:]
			# Note: If we cast a spell that deals damage while there's already a damage-dealing effect 
			# active, then the effect deals damage first according to the example: adventofcode.com/2015/day/22

			# player turn:
			curActions.append('-- Player turn --') # TODO Next time: always follow the order in the example. Don't get fancy.
			curArmor = 0

			for (effectName, turnsRemainingEffect, damageEffect, defenseEffect, manaEffect) in curEffects.values():
				curArmor += defenseEffect
			curActions.append(f'- Player has {curPlayerHP} hit points, {curArmor} armor, {curPlayerMana} mana')
			curActions.append(f'- Boss has {curBossHP} hit points')

			# timer/effect stuff here at start of player's turn
			newEffects = {}
			curArmor = 0
			for (effectName, turnsRemainingEffect, damageEffect, defenseEffect, manaEffect) in curEffects.values():
				turnsRemainingEffect -= 1
				if damageEffect > 0:
					curBossHP -= damageEffect
					curActions.append(f'Poison deals {damageEffect} damage; its timer is now {turnsRemainingEffect}.')
				if defenseEffect > 0:
					curArmor += defenseEffect
					curActions.append(f"Shield's timer is now {turnsRemainingEffect}.")
				if manaEffect > 0:
					curPlayerMana += manaEffect
					curActions.append(f"Recharge provides {manaEffect} mana; its timer is now {turnsRemainingEffect}.")
				if turnsRemainingEffect > 0:
					newEffects[effectName] = (effectName, turnsRemainingEffect, damageEffect, defenseEffect, manaEffect)
				elif defenseEffect > 0:
					curArmor = 0

			if spellName == 'magicMissile':
				curBossHP -= damage
				curActions.append(f'Player casts {spellName}, dealing {damage} damage.')
			elif spellName == 'drain':
				curBossHP -= damage
				curPlayerHP += heal
				curActions.append(f'Player casts {spellName}, dealing {damage} damage, and healing {heal} hit points.')
			elif spellName == 'shield':
				curActions.append(f'Player casts {spellName}, increasing armor by {defense}.')
			elif spellName == 'poison':
				curActions.append(f'Player casts {spellName}.')
			elif spellName == 'recharge':
				curActions.append(f'Player casts {spellName}.')

			curManaUsed += manaCost
			curPlayerMana -= manaCost

			if curPlayerMana < 0:
				continue

			if curBossHP <= 0:
				curActions.append('This kills the boss, and the player wins.')
				if curManaUsed < manaUsedMin:
					print('\n==================================\n')
					print('\n'.join(curActions))
					print(f'Mana used: {curManaUsed}')
				manaUsedMin = min(manaUsedMin, curManaUsed)
				continue

			# Add new effect to dict
			if turns > 0:
				if spellName not in newEffects:
					newEffects[spellName] = (spellName, turns, damage, defense, manaGain)
				else:
					continue

			# boss turn
			curActions.append('-- Boss turn --')
			curActions.append(f'- Player has {curPlayerHP} hit points, {curArmor} armor, {curPlayerMana} mana')
			curActions.append(f'- Boss has {curBossHP} hit points')

			# timer/effect stuff here at start of boss's turn
			newEffects2 = {}
			curArmor = 0
			for (effectName, turnsRemainingEffect, damageEffect, defenseEffect, manaEffect) in newEffects.values():
				turnsRemainingEffect -= 1
				if damageEffect > 0:
					curBossHP -= damageEffect
					curActions.append(f'Poison deals {damageEffect} damage; its timer is now {turnsRemainingEffect}.')
				if defenseEffect > 0:
					curArmor += defenseEffect
					curActions.append(f"Shield's timer is now {turnsRemainingEffect}.")
				if manaEffect > 0:
					curPlayerMana += manaEffect
					curActions.append(f"Recharge provides {manaEffect} mana; its timer is now {turnsRemainingEffect}.")
				if turnsRemainingEffect > 0:
					newEffects2[effectName] = (effectName, turnsRemainingEffect, damageEffect, defenseEffect, manaEffect)
				elif defenseEffect > 0:
					curArmor = 0

			bossDmg = max(1, 9 - curArmor)
			curActions.append(f'Boss attacks for 9 - {curArmor} = {bossDmg}.')
			curPlayerHP -= bossDmg
			if curPlayerHP <= 0:
				curActions.append('This kills the player, and the boss wins.')
				continue

			# recurse dfs
			dfs(curBossHP, curPlayerHP, curPlayerMana, curManaUsed, newEffects2, spellsUsed + [spellName], curActions)


		memo[(bossHP, playerHP, playerMana, manaUsed, effectsSerialized)] = True


	dfs(58, 50, 500, 0, {}, [], [])

	print(f'ANSWER: {manaUsedMin}')

	
main()
