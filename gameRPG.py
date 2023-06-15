import random

class Character: # Create the class "character"(Father) 
    def __init__(self, name, strength, defense, healing_items):
#Characteristics for any character 
        self.name = name
        self.strength = strength
        self.defense = defense
        self.healing_items = healing_items
 
 def attack(self, target): #Define funtion of attack
        damage = self.strength - target.defense #How the "attack" works is defined 
        target.receive_damage(damage) #result of "strength minus defense"
