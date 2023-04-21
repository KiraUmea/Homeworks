import settings
from exceptions import EnemyDown
from exceptions import GameOver
from models import Enemy
from models import Player


def get_player_name():
    name = input('Type your name:\n')
    return name


def play():
    name = get_player_name()
    player = Player(name)
    enemy = Enemy()
    while True:
        try:
            player.attack(enemy)
            player.defence(enemy)
        except EnemyDown:
            print("Enemy down")
            player.score += settings.SCORE_ENEMY_DOWN
            enemy = Enemy(enemy.level + 1)
        except GameOver:
            print("Game over")
            break


if __name__ == "__main__":
    try:
        play()
    except KeyboardInterrupt:
        pass
