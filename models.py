import random

import settings
from exceptions import EnemyDown
from exceptions import GameOver

chars = ["1", "2", "3"]
enemy_down1 = EnemyDown


class Enemy:

    def __init__(self, level: int = settings.INITIAL_ENEMY_LEVEL):
        self.level = level
        self.health = level

    def decrease_health(self):
        self.health -= 1  # self.health = self.health - 1
        if self.health < 1:
            raise EnemyDown

    @staticmethod
    def select_attack():
        return random.choice(settings.VALID_CHOICES)

    @staticmethod
    def select_defence():
        return random.choice(settings.VALID_CHOICES)


class Player:
    name: str
    health: int = 50
    health_unit = 10
    score: int = 0
    score_unit = 10
    user_attack: str
    user_defence: str
    enemy = Enemy
    enemy_down = EnemyDown
    game_over = GameOver

    def __init__(self, name):
        self.name = name
        self.health = settings.INITIAL_PLAYER_HEALTH
        self.score = 0

    def decrease_health(self):
        self.health -= 1  # self.health = self.health - 1
        if self.health < 1:
            raise GameOver

    @staticmethod
    def select_attack():
        choice: int = 0
        msg = f"Make your choice from {settings.VALID_CHOICES}: "
        while choice not in settings.VALID_CHOICES:
            try:
                choice = int(input(msg))
            except ValueError:
                pass

        return choice

    @staticmethod
    def select_defence():
        choice: int = 0
        msg = f"Make your choice from {settings.VALID_CHOICES}: "
        while choice not in settings.VALID_CHOICES:
            try:
                choice = int(input(msg))
            except ValueError:
                pass

        return choice

    @staticmethod
    def fight(attack: int, defence: int) -> int:
        if attack == defence:
            return settings.DRAW

        successful_attacks = (
            (settings.WIZARD, settings.KNIGHT),
            (settings.KNIGHT, settings.THIEF),
            (settings.THIEF, settings.WIZARD),
        )
        if (attack, defence) in successful_attacks:
            return settings.SUCCESS

        return settings.FAILURE

    def attack(self, enemy: Enemy) -> None:
        attack = player.select_attack()
        defence = enemy.select_defence()
        fight_result = self.fight(attack, defence)

        if fight_result == settings.SUCCESS:
            print("YOUR ATTACK IS SUCCESSFUL!")
            enemy.decrease_health()
            self.score += settings.SCORE_SUCCESS_ATTACK
        elif fight_result == settings.FAILURE:
            print("YOUR ATTACK IS FAILED!")
        else:
            print("IT’S A DRAW!")

    def defence(self, enemy: Enemy) -> None:
        attack = enemy.select_attack()
        defence = self.select_defence()
        fight_result = self.fight(attack, defence)

        if fight_result == settings.SUCCESS:
            print("YOU DEFENDED YOURSELF!")
        elif fight_result == settings.FAILURE:
            print("YOU WAS ATTACKED! YOUR HEALTH DETERIORATED")
            self.decrease_health()
        else:
            print("IT’S A DRAW!")
