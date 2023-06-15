import random

class Character: # Create the class "character"(Father) 
    def __init__(self, name, strength, weaknees, heal_items):
#Characteristics for any character 
        self.name = name #name character
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
        if self.heal_items:
            healing = self.heal_items.pop(0) #Removes the element that is in the position
            if self.life > 150:
                self.life = 150 # The restored life cannot be greater than the maximum life of the character
            print(f"{self.name} #has used a healing item and has healed  {healing} points of life.")
        else:
            print("No healing objets left.") #They don´t have more healing objects
#Characters
class Chrono(Character): #Is the character we are going to use 
    def __init__(self): #Function to call the father class and all its properties 
        super().__init__("Chrono", "Warrior", "Wizard")# Name, strength and weakness 

class Marle(Character):# She is the CPU
    def __init__(self): #Function to call the father class and all its properties
        super().__init__("Marle", "Wizard", "Warrior") # Name, strength and weakness

def main():# All features in two final objects 
    player1 = Chrono()
    player2 = Marle()

     while player1.life > 0 and player2.life > 0: #The condition for continuing to play the game (or finish the game)
       #Basic menu
        print("------")
        print(f"{player1.name} (Life: {player1.heal})")
        print(f"{player2.name} (Life: {player2.heal})")
        print("------")
        print("1. Attack") #Action options 
        print("2. Defend")
        print("3. Use a healing item") 
        choice = input("Choose a action : ") #Decide on one of the three actions 
