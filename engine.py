from models import Player
from models import Enemy
from exceptions import EnemyDown
from exceptions import GameOver


player1 = Player
enemy1 = Enemy


def get_player_name():
	name = input('Type your name')
	return name


def play():
	try:
		player1.select_attack()
		enemy1.select_defence()
		player1.attack()
		player1.select_defence()
		enemy1.select_attack()
		player1.defence()
	except EnemyDown:
		print("YOU WON! ENEMY IS DOWN")
	except GameOver:
		print("GAME OVER, YOU ARE DEAD")


