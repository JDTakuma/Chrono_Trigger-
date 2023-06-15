import random

class Character: # Create the class "character"(Father) 
    def __init__(self, name, strength, weaknees, heal_items):
#Characteristics for any character 
        self.name = name
        self.strength = strength
        self.weaknees = weaknees
        self.heal_items = [40,40] #Only two healing items per character
        self.life = 150 #maximum life

 #operation of the attack
    def attack(self, enemy): 
        damage = random.randint(5, 20)
        #Implementation of weakness and strength
        if enemy.weakness == self.strength: 
            damage *= 2 # Only if the strength is the same that weakness
            print("¡Effective attack!") # Indicates that the attack was effective
        enemy.life -= damage 
        print(f"{self.name} attacks {enemy.name} does {damage} points of damage.") #Result

    def defend(self): #Funtion of defense 
        defense = random.randint(10, 20) #Its more like a healing system 
        self.life += defense 
        if self.life > 150: 
            self.life = 150 # The restored life cannot be greater than the maximum life of the character
        print(f"{self.name} has defended himself and healed {defense} points of life.")

    def use_healing_item(self):
        if self.healing_items:
            healing = self.healing_items.pop(0) #Removes the element that is in the position
            if self.health > 150:
                self.health = 150 # The restored life cannot be greater than the maximum life of the character
            print(f"{self.name} #has used a healing item and has healed  {healing} points of life.")
        else:
            print("No healing objets left.")
#Characters
class Chrono(Character): #Is the character we are going to use 
    def __init__(self): #Funtion 
        super().__init__("Chrono", "Warrior", "Wizard")# Name, strength and weakness 

class Marle(Character):# She is the CPU
    def __init__(self):
        super().__init__("Marle", "Wizard", "Warrior") # Name, strength and weakness