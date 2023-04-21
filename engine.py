from models import Player
from models import Enemy
from exceptions import EnemyDown
from exceptions import GameOver


def get_player_name():
	name = input('Type your name:\n')
	return name


def play():
	player1 = Player
	enemy1 = Enemy
	while True:
		try:
			player1.attack(enemy1)
			player1.defence(enemy1)
		except EnemyDown:
			...
			enemy1 = Enemy(enemy1.level + 1)
		except GameOver:
			break


get_player_name()
play()
