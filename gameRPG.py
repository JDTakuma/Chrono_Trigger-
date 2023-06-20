import random

class Character: # Create the class "character"(Father) 
    def __init__(self, name, strength, weaknees, heal_items):#Characteristics for any character 

        self.name = name #name character
        self.strength = strength 
        self.weaknees = weaknees
        self.use_healing_items = [40, 40] #Only two healing items per character
        self.health = 150 #maximum health

 #operation of the attack
    def attack(self, enemy): 
        damage = random.randint(5, 20) #Implementation of weakness and strength
        if enemy.weaknees == self.strength: 
            damage *= 2 # Only if the strength is the same that weakness
            print("¡Effective attack!") # Indicates that the attack was effective
        self.health -= damage 
        print(f"{self.name} attacks {enemy.name} does {damage} points of damage.") #Result

    def defend(self): #Funtion of defense 
        defense = random.randint(10, 20) #Its more like a healing system 
        player2.health += defense 
        if player2.health > 150: 
            player2.health = 150 # The restored life cannot be greater than the maximum life of the character
        print(f"{player1.name} has defended himself and healed {defense} points of life.")

    def use_healing_item(self):
        if player2.use_healing_items:
            healing = player2.use_healing_items.pop(0) #Removes the element that is in the position
            player2.health += healing
            if player2.health > 150:
                player2.health = 150 # The restored life cannot be greater than the maximum life of the character
            print(f"{player1.name} has used a healing item and has healed  {healing} points of life.")
        else:
            print("No healing objets left.") #They don´t have more healing objects
#Characters
class Chrono(Character): #Is the character we are going to use 
    def __init__(self): #Function to call the father class and all its properties 
        super().__init__("Chrono", "Warrior", "Wizard", [40,40])# Name, strength and weakness 

class Marle(Character):# She is the CPU
    def __init__(self): #Function to call the father class and all its properties
        super().__init__("Marle", "Wizard", "Warrior", [40,40]) # Name, strength and weakness
   
    def battle(self):
        while player1.health > 0 and player2.health > 0: #The condition for continuing to play the game (or finish the game)
       #Basic menu      
            print("------")
            print(f"{player1.name} (health: {player2.health}) (class: {player1.weaknees})")
            print(f"{player2.name} (health: {player1.health}) (class: {player2.weaknees})")
            print("------")
            print("1. Attack") #Action options 
            print("2. Defend")
            print("3. Use a healing item") 
            choice = input("Choose a action: ") #Decide on one of the three actions 
#Actions to choose in the basic menu 
            if choice == "1":
                player1.attack(player2) #Objetive to attack
            elif choice == "2":
                player1.defend() #Recover points of life 
            elif choice == "3":
                player1.use_healing_item() #use one object  
            else:
                print("Invalid option. Try again.") # Miss input        
        
            if player2.health <= 0:
                print(f"{player2.name} wins the combat .")
                break

#the current status of the characters is shown
            print("------")
            print(f"{player1.name} (health: {player2.health})") #Current health
            print(f"{player2.name} (health: {player1.health})") #Current health
            print("------")
            print(f"{player2.name} is attacking...") 
            player2.attack(player1) #Objetive

            if player1.health <= 0: #Condition to win 
                print(f"{player1.name} wins the combat.")
                break 
    
    #Start the game
player1 = Chrono()
player2 = Marle()
player2.battle()
