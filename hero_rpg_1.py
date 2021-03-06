# RPG Game 1
#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power
    def alive(self):
        if self.health > 0:
            return True

class Hero(Character):
    def __init__(self, health, power):    
        super().__init__(health, power)
        
    def attack(hero, goblin):
        # Hero attacks goblin
        goblin.health -= hero.power
        print("You do {} damage to the goblin.".format(hero.power))
        if goblin.health <= 0:
            print("The goblin is dead.")
    
    def print_status(hero):
        print("You have {} health and {} power.".format(hero.health, hero.power))

class Goblin(Character):
    def __init__(self, health, power):    
        super().__init__(health, power)
        
    def attack(goblin, hero):
        # Goblin attacks hero
        hero.health -= goblin.power
        print("The goblin does {} damage to you.".format(goblin.power))
        if hero.health <= 0:
            print("You are dead.")
    
    def print_status(goblin):
        print("The goblin has {} health and {} power.".format(goblin.health, goblin.power))
       
def main():
    # hero_health = 10
    # hero_power = 5
    # goblin_health = 6
    # goblin_power = 2

    hero = Hero(10, 5)
    goblin = Goblin(6, 2)

    while goblin.alive() and hero.alive():
        # print("You have {} health and {} power.".format(hero.health, hero.power))
        # print("The goblin has {} health and {} power.".format(goblin.health, goblin.power))
        hero.print_status()
        goblin.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin.health > 0:
            # Goblin attacks hero
            goblin.attack(hero)

main()