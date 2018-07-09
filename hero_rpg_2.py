# Hero RPG Game: Part 2
import random

class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power
    def alive(self):
        if self.health > 0 or self.name == 'Zombie':
            return True
        
class Medic(Character):
    def __init__(self, health, power):
        super().__init__(health, power)
        self.name = 'Medic'
        self.bounty = 3
    def attack(medic, hero):
        if hero.armor == 2:
            medic.power -= 1
        # Before attacking, medic has 20% prob of recuperating 2 health points
        p = random.randint(1, 6)
        if p == 1: # 20% prob that random number will be 1
            self.health += 2
            print('The Medic gained 2 HP.')
        # medic attacks hero
        hero.health -= medic.power
        print("The Medic does {} damage to you.".format(medic.power))
        if hero.health <= 0:
            print("You are dead.")
    
    def print_status(medic):
        print("The medic has {} health and {} power.".format(medic.health, medic.power))

class Shadow(Character):
    def __init__(self, health, power):
        super().__init__(health, power)
        self.name = 'Shadow'
        self.bounty = 6
    def attack(shadow, hero):
        if hero.armor == 2:
            shadow.power -= 1
        # Shadow attacks hero
        hero.health -= shadow.power
        print("The Shadow does {} damage to you.".format(shadow.power))
        if hero.health <= 0:
            print("You are dead.")
    
    def print_status(shadow):
        print("The Shadow has {} health and {} power.".format(shadow.health, shadow.power))

class Zombie(Character):
    def __init__(self, health, power):    
        super().__init__(health, power)
        self.name = 'Zombie'
        # self.bounty = 2
    def attack(zombie, hero):
        if hero.armor == 2:
            zombie.power -= 1
        # Zombie attacks hero
        hero.health -= zombie.power
        print("The zombie does {} damage to you.".format(zombie.power))
        if hero.health <= 0:
            print("You are dead.")
    
    def print_status(zombie):
        print("The zombie has {} health and {} power.".format(zombie.health, zombie.power))

class Tank(Character): # Tank has large amount of health but small amount of power
    def __init__(self, health, power):    
        super().__init__(health, power)
        self.name = 'Tank'
        self.bounty = 7
    def attack(tank, hero):
        if hero.armor == 2:
            tank.power -= 1
        # Tank attacks hero
        hero.health -= tank.power
        print("The Tank does {} damage to you.".format(tank.power))
        if hero.health <= 0:
            print("You are dead.")
    
    def print_status(tank):
        print("The Tank has {} health and {} power.".format(tank.health, tank.power))

class Tryndamere(Character): # Once tryndamere reaches 0 health point, he will become invisible for a round until his second wind wears off
    def __init__(self, health, power):
        super().__init__(health, power)
        self.name = 'Tryndamere'
        self.bounty = 7
    def attack(tryndamere, hero):
        if hero.armor == 2:
            tryndamere.power -= 1
        # Tryndamere attacks hero
        hero.health -= tryndamere.power
        print("The Tryndamere does {} damage to you.".format(Tryndamere.power))
        if hero.health <= 0:
            print("You are dead.")
    
    def print_status(tryndamere):
        print("The Tryndamere has {} health and {} power.".format(tryndamere.health, tryndamere.power))
class Hero(Character):
    def __init__(self, health, power):    
        super().__init__(health, power)
        self.name = 'Hero'
        self.coins = 0
        self.armor = 0
        self.evade = 0
    def attack(hero, enemy):
        if enemy.name == 'Goblin':
            # Hero attacks goblin
            p = random.randint(1, 6) # Double damage is random numbers match, 20% prob
            if p == 1: # 20% prob that random number will be 1
                goblin.health -= hero.power * 2
                print("You do {} damage to the goblin.".format(hero.power * 2))
            else:
                goblin.health -= hero.power
                print("You do {} damage to the goblin.".format(hero.power))
            if goblin.health <= 0:
                print("The goblin is dead.")
                print("You've collected the Goblin's bounty of {} coins.".format(enemy.bounty))
                hero.coins += enemy.bounty
        elif enemy.name == 'Medic':
            # Hero attacks medic
            p = random.randint(1, 6) # Double damage is random numbers match, 20% prob
            if p == 1: # 20% prob that random number will be 1
                medic.health -= hero.power * 2
                print("You do {} damage to the medic.".format(hero.power * 2))
            else:
                medic.health -= hero.power
                print("You do {} damage to the medic.".format(hero.power))
            if medic.health <= 0:
                print("The medic is dead.")
                print("You've collected the Medic's bounty of {} coins.".format(enemy.bounty))
                hero.coins += enemy.bounty
        elif enemy.name == 'Shadow':
            no_dodge = random.randint(1, 11)
            if no_dodge == 1:
                # Hero attacks shadow
                p = random.randint(1, 6) # Double damage is random numbers match, 20% prob
                if p == 1: # 20% prob that random number will be 1
                    shadow.health -= hero.power * 2
                    print("You do {} damage to the shadow.".format(hero.power * 2))
                else:
                    shadow.health -= hero.power
                    print("You do {} damage to the shadow.".format(hero.power))
                if shadow.health <= 0:
                    print("The Shadow is dead.")
                    print("You've collected the Shadow's bounty of {} coins.".format(enemy.bounty))
                    hero.coins += enemy.bounty
            else:
                print('You missed the Shadow.')
        elif enemy.name == 'Zombie':
            # Hero attacks Zombie
            p = random.randint(1, 6) # Double damage is random numbers match, 20% prob
            if p == 1: # 20% prob that random number will be 1
                zombie.health -= hero.power * 2
                print("You do {} damage to the Zombie.".format(hero.power * 2))
            else:
                zombie.health -= hero.power
                print("You do {} damage to the zombie.".format(hero.power))
            if zombie.health <= 0:
                print("The zombie is already dead. You cannot kill it.")
        elif enemy.name == 'Tank':
            # Hero attacks Tank
            p = random.randint(1, 6) # Double damage is random numbers match, 20% prob
            if p == 1: # 20% prob that random number will be 1
                tank.health -= hero.power * 2
                print("You do {} damage to the Tank.".format(hero.power * 2))
            else:
                tank.health -= hero.power
                print("You do {} damage to the Tank.".format(hero.power))
            if tank.health <= 0:
                print("The Tank is dead.")
                print("You've collected the Tank's bounty of {} coins.".format(enemy.bounty))
                hero.coins += enemy.bounty
        elif enemy.name == 'Tryndamere':
            second_wind = 1
            # Hero attacks Tryndamere
            p = random.randint(1, 6) # Double damage is random numbers match, 20% prob
            if p == 1: # 20% prob that random number will be 1
                tryndamere.health -= hero.power * 2
                print("You do {} damage to the tryndamere.".format(hero.power * 2))
            else:
                tryndamere.health -= hero.power
                print("You do {} damage to the tryndamere.".format(hero.power))
            if tryndamere.health <= 0 and second_wind == 0:
                print("The tryndamere is dead.")
                print("You've collected the Tryndamere's bounty of {} coins.".format(enemy.bounty))
                hero.coins += enemy.bounty
            else:
                second_wind -= 1
                enemy.health += 2
                print('Tryndamere has a second wind.')

    def print_status(hero):
        print("You have {} health and {} power.".format(hero.health, hero.power))

class Goblin(Character):
    def __init__(self, health, power):    
        super().__init__(health, power)
        self.name = 'Goblin'
        self.bounty = 5
    def attack(goblin, hero):
        # Goblin attacks hero
        if hero.armor == 2: # Reduce character power if hero has armor
            goblin.power -= 1
        hero.health -= goblin.power
        print("The goblin does {} damage to you.".format(goblin.power))
        if hero.health <= 0:
            print("You are dead.")
    
    def print_status(goblin):
        print("The goblin has {} health and {} power.".format(goblin.health, goblin.power))


class SuperTonic:
    cost = 5
    name = 'SuperTonic'
    def apply(self):
        self.health = 10
        print('{}\'s health is now {}'.format(self.name, self.health))
class Armor:
    cost = 2
    name = 'Armor'
    def apply(self):
        self.armor += 2
        print('Hero armor is now {}'.format(self.armor))
class Evade:
    cost = 6
    name = 'Evade'
    def apply(self):
        self.evade += 2
        print('Hero evade is now {}'.format(self.evade))

class Store:
    items = [SuperTonic(), Armor(), Evade()]
    def shop(self, hero):
        print('Hero has {} coins.'.format(hero.coins))
        for i in range(0, len(Store.items)):
            item = Store.items[i]
            print("{}. {}: {}".format(i+1, item.name, item.cost))
        print('10. Exit Shop')

        option = int(input("Enter Option: "))

        if option == 10:
            pass
        else:
            hero.buy(Store.items[option - 1])



hero = Hero(10, 5)
goblin = Goblin(6, 2)
medic = Medic(10, 2)
shadow = Shadow(1, 2)
zombie = Zombie(10, 1)
tank = Tank(20, 2)
tryndamere = Tryndamere(5, 5)  

def main(hero, enemy):
    # hero_health = 10
    # hero_power = 5
    # goblin_health = 6
    # goblin_power = 2

    while enemy.alive() and hero.alive():
        # print("You have {} health and {} power.".format(hero.health, hero.power))
        # print("The goblin has {} health and {} power.".format(goblin.health, goblin.power))
        hero.print_status()
        enemy.print_status()
        print()
        print("What do you want to do?")
        print("1. fight {}".format(enemy.name))
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks enemy
            hero.attack(enemy)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if enemy.health > 0:
            # enemy attacks hero
            enemy.attack(hero)

main(hero, goblin)

# testing commit after rename