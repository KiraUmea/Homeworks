class EnemyDown(Exception):
    def down(self):
        print(f"Enemy is down")

class GameOver(Exception):
    def fail(self):
        print(f"Game over")
