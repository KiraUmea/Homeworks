from models import Player
from models import Enemy
from exceptions import EnemyDown
from exceptions import GameOver


def get_player_name():
	name = input('Type your name:\n')
	return name


def play():
	player = Player
	enemy = Enemy
	while True:
		try:
			player.attack(enemy)
			player.defence(enemy)
		except EnemyDown:
			...
			enemy = Enemy(enemy.level + 1)
		except GameOver:
			break


get_player_name()
play()
