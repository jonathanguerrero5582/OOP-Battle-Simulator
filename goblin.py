import random
from enemy import Enemy

class Goblin(Enemy):
    """A completed character class students can examine as an OOP example."""

    def __init__(self, name, health = 100, attackPower = 15):
        super().__init__(name, 100)
        self.attack_power = 15
        self.gold = 0

    def stealGold(self, hero):
        "Returns a random amount of damage."
        self.gold += hero.gold
        hero.gold = 0
        print("Gold Stolen")