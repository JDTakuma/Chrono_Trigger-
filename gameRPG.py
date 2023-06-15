import random

class Character: # Create the class "character"(Father) 
    def __init__(self, name, strength, weaknees, healing_items):
#Characteristics for any character 
        self.name = name
        self.strength = strength
        self.weaknees = weaknees
        self.heal_items = [40,40] #Only two healing items per character
        self.life = 150
 
    def attack(self, enemy):
        damage = random.randint(5, 20)
        if enemy.weakness == self.strength:
            damage *= 2
            print("¡Effective attack!")
        enemy.health -= damage
        print(f"{self.name} attacks {enemy.name} does {damage} points of damage.")

