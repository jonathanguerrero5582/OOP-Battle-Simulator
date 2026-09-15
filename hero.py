import random

class Hero:
    """The hero blueprint will be implemented later in the project."""

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 10

    def attack(self):
        return random.randint(1, self.attack_power)

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def is_alive(self):
        return self.health > 0

    def entrance(self):
        print("The hero is on his way")
        print("═════════════════════")