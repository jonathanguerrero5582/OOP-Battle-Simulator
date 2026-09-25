import random
from enemy import Enemy

class Boss(Enemy):

    def __init__(self, name):
        super().__init__(name, health = 200, attackPower = 25)

    def attack(self):
        attackStyle = random.randit(1,3)
        if attackStyle == 1:
            print("FIREBALL")
            return 5 * random.randit(1,3)
        elif attackStyle == 2:
            print("Swing Sword")
            return self.attack_power
        else:
            print("STOMP")
            return 2 * random.randit(2,6)

    def take_damage(self, damage):
        damage = damage * .75
        super().take_damage(damage)