from goblin import Goblin
from hero import Hero
from boss import Boss

ARENA_NAME = "JB's Circle"

def battle(hero: Hero, enemy: Goblin, boss: Boss):
    while hero.is_alive() and enemy.is_alive():
        hero_damage = hero.attack()
        enemy.take_damage(hero_damage)
        if enemy.is_alive():
            enemy_damage = enemy.attack()
            hero.take_damage(enemy_damage)    

    if hero.is_alive():
        print(f"{hero.name} wins!")    
    else:
        print(f"{enemy.name} wins!")    

def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("JB is coming...")

    goblin = Goblin("JB")
    print(f"{goblin.name} enters the arena with {goblin.health} health.")

    goblin2 = Goblin("Scribble")
    print(f"{goblin2.name} enters the arena with {goblin2.health} health.")
    
    print("But no hero has answered the call... yet.")
    bob = Hero("bobbert")
    print(f"{goblin.name} enters the arena with {goblin.health} health.")

    boss = Boss("Rick")
    battle(bob, boss)

if __name__ == "__main__":
    main()

