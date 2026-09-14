from goblin import Goblin
from hero import Hero

ARENA_NAME = "JB's Circle"


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

if __name__ == "__main__":
    hero = Hero("Key")
    print(f"{hero.name} enters the arena with {hero.health} health.")
    entrance()
    attack1 = goblin.attack()
    goblin.health - attack
    attack2 = goblin.attack()
    hero.health - attack
main()

