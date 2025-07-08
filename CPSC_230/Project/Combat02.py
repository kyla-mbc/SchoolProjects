import random
from prettytable import PrettyTable

#PC Health stats
#The function gets and prints out starting stats for the user which incldes the opponent's player type, opponent's health, and player's health.
def playerstats():
    print(f"\tOpponent's Player Type: {NPCstats['Player Type']}")
    print(f"\tOpponent's Starting Health: {NPCstats['Health']}")
    if playerInput.lower() == "warlock":
        print(f"\tYour Starting Health: {PCtypes['PC01']['Health']}")
    elif playerInput.lower() == "ranger":
        print (f"\tYour Starting Health: {PCtypes['PC02']['Health']}")
    elif playerInput.lower() == "wizard":
        print (f"\tYour Starting Health: {PCtypes['PC03']['Health']}")
    elif playerInput.lower() == "barbarian":
        print (f"\tYour Starting Health: {PCtypes['PC04']['Health']}")
    elif playerInput.lower() == "cleric":
        print (f"\tYour Starting Health: {PCtypes['PC05']['Health']}")

#Dice Rolling Function
# Dice rolling will take into account how many sides are on a dice and chooses a random number from the amount of sides on the dice when this function is called.
def dice_roller(attack_sides):
    if attack_sides < 2:
        raise ValueError("Number of sides must be at least 2")
    return random.randint(1, attack_sides)

#Damage Function
#Damage function is used to take into consideration the number the dice rolls when calculating the amount of damage done to an opponent. 
def attack_damage(attacker):
    while True:
        attack_dice = attacker["Attack Dice"] #takes the character's "Attack Dice" which is the amount of sides on their attack dice.
        damage = dice_roller(attack_dice)
        damage = damage + attacker["Attack"] #damage calculates how much is the total damage after adding the amount from the attack dice after being rolled.
        return damage

#Dodge Dice Function
#Dodge Dice function to roll the amount of sides on the dodge dice of a character. 
def dodge_dice(dodge_dice_sides):
    if dodge_dice_sides < 2:
        raise ValueError("Dodge Dice must have at least 2 sides") #use value error to check if the dice has more than 1 side.
    dodge_value = random.randint(1, dodge_dice_sides) #the dodge_dice function will choose any number from 1 to the amout of sides the dice has. 
    return dodge_value

#Creating Player Types
#below is the dictionary of dictionaries for the player types
PCtypes = {
    "PC01" : {"Player Type":"Warlock", "Health": 90, "Attack":20, "Attack Dice":10, "Dodge Dice":20},#compose dictionaries for types of Characters that will be present in the game.
    "PC02" : {"Player Type":"Ranger", "Health": 70, "Attack":20, "Attack Dice":10, "Dodge Dice":10},
    "PC03" : {"Player Type":"Wizard", "Health":80, "Attack":28, "Attack Dice":15, "Dodge Dice":25},
    "PC04" : {"Player Type":"Barbarian", "Health":100, "Attack":25, "Attack Dice":20, "Dodge Dice":10},
    "PC05" : {"Player Type":"Cleric", "Health":80, "Attack":25, "Attack Dice":15, "Dodge Dice":20}
}

#Creating NPC Types
#below is the dictionary of dictionaries for the NPC types. 
NPCtypes = {
    "NPC1" : {"Player Type":"Sorcerer", "Health":100, "Attack":20, "Attack Dice":10, "Dodge Dice":20},
    "NPC2" : {"Player Type":"Paladin", "Health":80, "Attack":25, "Attack Dice":5, "Dodge Dice":25},
    "NPC3" : {"Player Type":"Rogue", "Health":60, "Attack":15, "Attack Dice":5, "Dodge Dice":15}
}

#Displaying Player Types in table 
#for an easier view, I added the Player's dictionary into a table.
PCtable = PrettyTable(["Player Type", "Health", "Attack", "Attack Dice", "Dodge Dice"])
for pc, PCdata in PCtypes.items():
    PCtable.add_row([PCdata["Player Type"], PCdata["Health"], PCdata["Attack"], PCdata["Attack Dice"], PCdata["Dodge Dice"]])

#Displaying NPC Types in table
#add the NPC's dictionary into a table.
NPCtable = PrettyTable(["Player Type", "Health", "Attack", "Attack Dice", "Dodge Dice"])
for npc, NPCdata in NPCtypes.items():
    NPCtable.add_row([NPCdata["Player Type"], NPCdata["Health"], NPCdata["Attack"], NPCdata["Attack Dice"], NPCdata["Dodge Dice"]])

#Greeting the user
userName = input("Welcome to the Combat Game! What is your name: " ) #welcome the user into the game and ask for their name. Store the user's name into a variable.
print (f"Welcome {userName.capitalize()}! First, you will need to choose your Player Type!\nHere are your choices and some information about them:") #use the variable into a statement, and capitalize the user's name. 
print (PCtable) #print the table of player's the user can choose from.

#Choosing Player Type
while True: 
    playerInput = input("Choose the Player Type you would like to use: ").capitalize()
    if playerInput.lower() == "warlock": #use error handling to accept the name of the character, whether or not it is capitalized.
        PCstats = PCtypes["PC01"] #store the data of the player into a variable called PCstats if this is the chosen character by the user. 
        PLAYER = PCstats["Player Type"] #assign variable "PLAYER" to the name of the character. 
    elif playerInput.lower() == "ranger": #apply same concept as the first if statement in this loop 
        PCstats = PCtypes["PC02"]
        PLAYER = PCstats["Player Type"]
    elif playerInput.lower() == "wizard":
        PCstats = PCtypes["PC03"]
        PLAYER = PCstats["Player Type"]
    elif playerInput.lower() == "barbarian":
        PCstats = PCtypes["PC04"]
        PLAYER = PCstats["Player Type"]
    elif playerInput.lower() == "cleric":
        PCstats = PCtypes["PC05"]
        PLAYER = PCstats["Player Type"]
    if playerInput in [data["Player Type"] for data in PCtypes.values()]: #if the user chooses a character from the possible options of "Player Types", break the loop. If they entered an invalid input, prompt them for a valid character.
        break
print(f"Great! Your player is {PLAYER.capitalize()}. Now you must choose your opponent.")
print(NPCtable)


#Choosing Opponent 
while True: 
    NPCplayer = input(f"You can choose your opponent or input 'random' and we can choose your opponent for you.\nWho would you like to go against: ")
    NPC = NPCplayer #assign NPC to the character the user chooses.
    if NPCplayer.lower() == "random":
        NPCplayer = random.choice (list(NPCtypes.keys())) #if the user inputs random, the code will choose an opponent for them.
        NPCstats = NPCtypes[NPCplayer] #assign NPCstats to the stats that are correlated with the player type the user has chosen. 
        NPC = NPCstats["Player Type"] # assign variable NPC to the opponent's character name.
        playerstats()
        break
    elif NPCplayer.lower() == "sorcerer": #use same code as first if statement in this loop.
        NPCstats = NPCtypes["NPC1"]
        NPC = NPCstats["Player Type"]
        playerstats()
        break
    elif NPCplayer.lower() == "paladin":
        NPCstats = NPCtypes["NPC2"]
        NPC = NPCstats ["Player Type"]
        playerstats()
        break
    elif NPCplayer.lower() == "rogue":
        NPCstats = NPCtypes["NPC3"]
        NPC = NPCstats ["Player Type"]
        playerstats()
        break
print ("\tGood Luck, you're going to need it!")

# Playing the Game 
while PCstats['Health'] > 0 and NPCstats['Health'] > 0: #continue running the code until one of the character's health has reached 0.
    option = input("Attack or Dodge: ") #prompts the user to attack or dodge.
    if option.lower() == "attack": #if the user chooses to attack the following code will run.
        print("\t You chose to attack.") #print the action the user chose. 
        npc_choice = random.choice(["Attack", "Dodge"]) #the npc will randomly choose from attack or dodge. 
        if npc_choice == "Attack": # if both character's attack, the following code will run.
            print(f"\t The {NPC} attacked you!") #print the action the NPC randomly chose. 
            player_damage = attack_damage(PCstats) #call the attack_damage function to calculate damage done by the user. 
            NPC_damage = attack_damage(NPCstats) # call the attack_damage function to calculate damage done by the NPC.
            PCstats['Health'] -= NPC_damage #subtract the amount of damage done by the NPC from the current health of the user's character.
            NPCstats['Health'] -= player_damage #subtract the amount of damage done by the user from the current health of the NPC.
            print(f"\t You did a damage of {player_damage}.") # print the damage done by the user.
            print(f"\t The {NPC} caused a damage of {NPC_damage}, watch out next time.") #print the damage done by the NPC.
            if PCstats['Health'] <= 0: #these 4 lines of code ensure that the health of both charater's do not go below 0 and that the game will end when it reaches 0.
                PCstats['Health'] = 0
            elif NPCstats['Health'] <= 0:
                NPCstats['Health'] = 0
        else:
            print(f"\t The {NPC} dodged!") #print the action the NPC chose when user chooses to attack.
            dodge = dodge_dice(NPCstats['Dodge Dice'])
            player_damage = attack_damage(PCstats) - dodge #calculate player_damage by subtracting the dodge_dice function from the attack_damage function. 
            if player_damage < dodge: 
                player_damage = 0 #ensures the code damage does not go below 0.
            NPCstats['Health'] -= player_damage #subtract the calculated damage from the current health of the NPC.
            print(f"\t You did a damage of {player_damage}. Great job!") #print out how much damage the user did.
            print("\t You dealt with 0 damage.") #print out hose much damage the user took
            if PCstats['Health'] <= 0: #these 4 lines of code ensure that the health of both charater's do not go below 0 and that the game will end when it reaches 0.
                PCstats['Health'] = 0
            elif NPCstats['Health'] <= 0:
                NPCstats['Health'] = 0
        print(f"\t Your health is {PCstats['Health']} and your opponent's health is {NPCstats['Health']}.") #prints the current health of both characters.
    elif option.lower() == "dodge": #the following code will run if the user chooses to dodge.
        print("\t You chose to dodge.") #prints out the user's choice.
        npc_choice = random.choice(["Attack", "Dodge"]) #the npc will randomly choose if it wants to attack or dodge.
        if npc_choice == "Attack": #if the npc chooses to attack the following code will run.
            print(f"\t The {NPC} attacked you!")
            dodge = dodge_dice(PCstats['Dodge Dice'])
            NPC_damage = attack_damage(NPCstats) - dodge #the amount of damage the npc makes relies on the attack_damage function an the dodge_dice function.
            if NPC_damage < dodge: #ensures the code damage does not go below 0.
                NPC_damage = 0
            PCstats['Health'] -= NPC_damage #the health of the user decreases by the amount of damage the NPC does. 
            print(f"\t The {NPC} did {NPC_damage} damage to you.") #prints out the amount of damage the NPC made. 
            print(f"\t The {NPC} dealt no damage.") #prints that the NPC dealt no damage since they attacked and you dodged.
            if PCstats['Health'] <= 0: #these 4 lines of code ensure that the health of both charater's do not go below 0 and that the game will end when it reaches 0.
                PCstats['Health'] = 0
            elif NPCstats['Health'] <= 0:
                NPCstats['Health'] = 0
        else:
            print(f"\t The {NPC} dodged! They dealt 0 damage.") #if both players dodge, neither character's health changes.
            print("\t You dealt 0 damage.")
        print(f"\t Your health is {PCstats['Health']} and your opponent's health is {NPCstats['Health']}.") #prints the current health of both character's.

#Ending the Game 
#Pring Game Results, use username variable to print results. 
if PCstats['Health'] == 0:
    print(f"Oh no {userName.capitalize()}! You were defeated by the {NPC}.") 
elif NPCstats['Health'] == 0:
    print(f"Congratulations {userName.capitalize()}, You have defeated the {NPC}!") 