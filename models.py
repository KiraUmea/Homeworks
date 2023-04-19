import random
from exceptions import enemy_down
from exceptions import game_over
import settings

chars = ["1", "2", "3"]


class Enemy:
	level: int
	health: int = 50
	health_unit = 10
	enemy_attack: str
	enemy_defence: str

	def __init__(self, level):
		self.level = 1

	def decrease_health(self, health):
		health -= 10
		if health < 10:
			raise enemy_down

	@staticmethod
	def select_attack():
		enemy_attack = random.choice(chars)
		return enemy_attack

	@staticmethod
	def select_defence():
		enemy_defence = random.choice(chars)
		return enemy_defence


enemy = Enemy


class Player:
	name: str
	health: int = 50
	score: int = 0
	score_unit = 10
	user_attack: str
	user_defence: str

	def __init__(self, name):
		self.name: str

	@staticmethod
	def select_attack():
		user_attack = input("Please choose your character. Type 1 for knight, 2 for thief, 3 for wizard.")
		return user_attack

	@staticmethod
	def select_defence(self, user_defence):
		user_defence: str = input("Please choose your character. Type 1 for knight, 2 for thief, 3 for wizard.")
		return user_defence

	def attack(self, score, score_unit, enemy: Enemy, select_attack):
		pl_attack = player.select_attack()
		en_var = enemy.select_defence()

		if (pl_attack == "1" and en_var == "2") or (pl_attack == "2" and en_var == "3") or \
			(pl_attack == "3" and en_var == "1"):
			enemy.decrease_health()
			score += score_unit
			print("YOUR ATTACK IS SUCCESSFUL!")
		elif (pl_attack == "1" and en_var == "3") or (pl_attack == "2" and en_var == "1") or \
			(pl_attack == "3" and en_var == "2"):
			print("YOUR ATTACK IS FAILED!")
		else:
			print("IT’S A DRAW!")

	def defence(self, health, health_unit, enemy: Enemy, select_defence):
		pl_def = player.select_defence()
		en_var = enemy.select_attack()

		if (pl_def == "1" and en_var == "2") or (pl_def == "2" and en_var == "3") or \
			(pl_def == "3" and en_var == "1"):
			print("YOU DEFENDED YOURSELF!")
		elif (pl_def == "1" and en_var == "3") or (pl_def == "2" and en_var == "1") or \
			(pl_def == "3" and en_var == "2"):
			health -= health.unit
			print("YOU WAS ATTACKED! YOUR HEALTH DETERIORATED")
		else:
			print("IT’S A DRAW!")


player = Player

