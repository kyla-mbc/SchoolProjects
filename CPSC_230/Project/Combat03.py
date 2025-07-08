import random
from prettytable import PrettyTable

#Transcript File 
def transcript_file(file, message):
    with open(file, "a") as file:
        file.write(message + "\n")

#PC Health stats
#The function gets and prints out starting stats for the user which incldes the opponent's player type, opponent's health, and player's health.
def playerstats():
    print(f"\tOpponent's Player Type: {NPCstats.player_type}")
    print(f"\tOpponent's Starting Health: {NPCstats.health}")
    if playerInput.lower() == "warlock":
        print(f"\tYour Starting Health: {PCstats.health}")
    elif playerInput.lower() == "ranger":
        print(f"\tYour Starting Health: {PCstats.health}")
    elif playerInput.lower() == "wizard":
        print(f"\tYour Starting Health: {PCstats.health}")
    elif playerInput.lower() == "barbarian":
        print(f"\tYour Starting Health: {PCstats.health}")
    elif playerInput.lower() == "cleric":
        print(f"\tYour Starting Health: {PCstats.health}")
    print(f"\tGood Luck! You're going to need it.")

#Dice Rolling Function
# Dice rolling will take into account how many sides are on a dice and chooses a random number from the amount of sides on the dice when this function is called.
def dice_roller(attack_sides):
    if attack_sides < 2:
        raise ValueError("Number of sides must be at least 2")
    return random.randint(1, attack_sides)

#Damage Function
#Damage function is used to take into consideration the number the dice rolls when calculating the amount of damage done to an opponent. 
def attack_damage(attacker):
    global PCtypes
    global NPCtypes
    while True:
        attack_dice = attacker["Attack Dice"]
        dice_damage = dice_roller(attack_dice)
        damage = dice_damage + attacker["Attack"]
        if attacker in NPCtypes.values():
            if dice_damage == attacker["Attack Dice"]:
                print("\t MAXIMUM POSSIBLE DAMAGE DONE TO PLAYER")
            elif dice_damage == 1:
                print("\t LOWEST POSSIBLE DAMAGE DONE TO PLAYER")
        if attacker in PCtypes.values():
            if dice_damage == attacker["Attack Dice"]:
                print("\t MAXIMUM POSSIBLE DAMAGE DONE TO NPC")
            elif dice_damage == 1:
                print("\t LOWEST POSSIBLE DAMAGE DONE TO NPC")
        return damage

#Dodge Dice Function
#Dodge Dice function to roll the amount of sides on the dodge dice of a character. 
def dodge_dice(dodge_dice_sides):
    if dodge_dice_sides < 2:
        raise ValueError("Dodge Dice must have at least 2 sides")
    dodge_value = random.randint(1, dodge_dice_sides)
    return dodge_value

#End Game Function
def end_game_message(PCstats, NPCstats, userName, NPC):
    if PCstats.health == 0 and NPCstats.health == 0:
        return "The match ended in a draw."
    elif PCstats.health == 0:
        return f"Oh no {userName.capitalize()}! You were defeated by the {NPC}."
    elif NPCstats.health == 0:
        return f"Congratulations {userName.capitalize()}, You have defeated the {NPC}!"
    

#Character and Damage Class
class Character:
    def __init__(self, player_type, health, attack_modifier, attack_dice, dodge_dice):
        self.player_type = player_type
        self.health = health
        self.attack_modifier = attack_modifier
        self.attack_dice = attack_dice
        self.dodge_dice = dodge_dice

    def calculate_damage(self, attacker, defender):
        attack_modifier = attacker.attack_modifier
        attack_dice = attacker.attack_dice
        dodge_dice = defender.dodge_dice
        base_damage = attack_modifier + self.roll_dice(attack_dice)
        dodge = self.roll_dice(dodge_dice)
        damage_dealt = max(0, base_damage - dodge)
        return damage_dealt
    
    def roll_dice(self, sides):
        if sides < 2:
            raise ValueError("Number of sides must be at least 2")
        return random.randint(1, sides)

#Creating Player Types
PCtypes = {
    "PC01": Character("Warlock", 90, 20, 10, 20),
    "PC02": Character("Ranger", 70, 20, 10, 10),
    "PC03": Character("Wizard", 80, 28, 15, 25),
    "PC04": Character("Barbarian", 100, 25, 20, 10),
    "PC05": Character("Cleric", 80, 25, 15, 20)
}

#Creating NPC Types
NPCtypes = {
    "NPC1": Character("Sorcerer", 100, 20, 10, 20),
    "NPC2": Character("Paladin", 80, 25, 5, 25),
    "NPC3": Character("Rogue", 60, 15, 5, 15)
}

#Displaying Player Types in table 
PCtable = PrettyTable(["Player Type", "Health", "Attack", "Attack Dice", "Dodge Dice"])
for pc, PCdata in PCtypes.items():
    PCtable.add_row([PCdata.player_type, PCdata.health, PCdata.attack_modifier, PCdata.attack_dice, PCdata.dodge_dice])

#Displaying NPC Types in table
NPCtable = PrettyTable(["Player Type", "Health", "Attack", "Attack Dice", "Dodge Dice"])
for npc, NPCdata in NPCtypes.items():
    NPCtable.add_row([NPCdata.player_type, NPCdata.health, NPCdata.attack_modifier, NPCdata.attack_dice, NPCdata.dodge_dice])

#Greeting the user
transcript_file_path = input("What would you like to name your transcript? \nPlease add '.txt' at the end of your file name: ")
userName = input("Welcome to the Combat Game! What is your name: ")
print(f"Welcome {userName.capitalize()}! First, you will need to choose your Player Type!\nHere are your choices and some information about them:")
print(PCtable)

# Choosing Player Type
while True:
    playerInput = input("Choose the Player Type you would like to use: ").capitalize()
    if playerInput.lower() in [data.player_type.lower() for data in PCtypes.values()]:
        PCstats = next(pc for pc in PCtypes.values() if pc.player_type.lower() == playerInput.lower())
        PLAYER = PCstats.player_type
        break
    else:
        print("Invalid input. Please choose a valid Player Type.")

print(f"Great! Your player is {PLAYER.capitalize()}. Now you must choose your opponent.")
print(NPCtable)

#Choosing Opponent 
while True:
    NPCplayer = input("You can choose your opponent or input 'random' and we can choose your opponent for you.\nWho would you like to go against: ")
    NPC = NPCplayer
    if NPCplayer.lower() == "random":
        NPCplayer = random.choice(list(NPCtypes.keys()))
        NPCstats = NPCtypes[NPCplayer]
        NPC = NPCstats.player_type
        playerstats()
        break
    elif NPCplayer.lower() in [data.player_type.lower() for data in NPCtypes.values()]:
        NPCstats = next(npc for npc in NPCtypes.values() if npc.player_type.lower() == NPCplayer.lower())
        NPC = NPCstats.player_type
        playerstats()
        break
    else:
        print("Invalid input. Please choose a valid opponent.")


# Playing the Game 
with open(transcript_file_path, "a") as transcript:  # Use with so that the open file automatically closes. 
    transcript.write(f"\nPlayer: {PLAYER}({userName.capitalize()}) vs {NPC.capitalize()}\n\n")

    round = 1
    while PCstats.health > 0 and NPCstats.health > 0:
        option = input("Attack or Dodge: ")

        # Define the damage variables outside the conditions
        player_damage = 0
        NPC_damage = 0

        if option.lower() == "attack":
            npc_choice = random.choice(["Attack", "Dodge"])
            print(f"\t Round {round}:")
            print("\t You chose to attack.")
            if npc_choice == "Attack":
                print(f"\t The {NPC} attacked you!")
                player_damage = PCstats.calculate_damage(PCstats, NPCstats)
                NPC_damage = NPCstats.calculate_damage(NPCstats, PCstats)
                PCstats.health -= NPC_damage
                NPCstats.health -= player_damage
                if PCstats.health <= 0:
                    PCstats.health = 0
                if NPCstats.health <= 0:
                    NPCstats.health = 0
                print(f"\t You did a damage of {player_damage}.")
                print(f"\t The {NPC} caused a damage of {NPC_damage}, watch out next time.")
            else:
                print(f"\t The {NPC} dodged!")
                dodge = dodge_dice(NPCstats.dodge_dice)
                player_damage = PCstats.calculate_damage(PCstats, NPCstats) - dodge
                if player_damage < dodge:
                    player_damage = 0
                NPCstats.health -= player_damage
                print(f"\t You did a damage of {player_damage}. Great job!")
                print("\t You dealt with 0 damage.")
                if PCstats.health <= 0:
                    PCstats.health = 0
                if NPCstats.health <= 0:
                    NPCstats.health = 0
            print(f"\t Your health is {PCstats.health} and your opponent's health is {NPCstats.health}.")
        elif option.lower() == "dodge":
            npc_choice = random.choice(["Attack", "Dodge"])
            print(f"\t Round {round}:")
            print("\t You chose to dodge.")
            if npc_choice == "Attack":
                print(f"\t The {NPC} attacked you!")
                dodge = dodge_dice(PCstats.dodge_dice)
                NPC_damage = NPCstats.calculate_damage(NPCstats, PCstats) - dodge
                if NPC_damage < dodge:
                    NPC_damage = 0
                PCstats.health -= NPC_damage
                print(f"\t The {NPC} did {NPC_damage} damage to you.")
                print(f"\t The {NPC} dealt no damage.")
                if PCstats.health <= 0:
                    PCstats.health = 0
                if NPCstats.health <= 0:
                    NPCstats.health = 0
            else:
                print(f"\t The {NPC} dodged! They dealt 0 damage.")
                print("\t You dealt 0 damage.")
            print(f"\t Your health is {PCstats.health} and your opponent's health is {NPCstats.health}.")
        else:
            continue

        # Writing round information to the transcript file
        transcript.write(f"\nRound {round}:\n")
        transcript.write(f"\t{PLAYER} chose: {option.capitalize()}\n")
        transcript.write(f"\t{NPC} chose: {npc_choice.capitalize()}\n")
        transcript.write(f"\t{PLAYER}'s damage done: {player_damage}\n")
        transcript.write(f"\t{NPC}'s damage done: {NPC_damage}\n")
        transcript.write(f"\t{PLAYER}'s health: {PCstats.health}, {NPC}'s health: {NPCstats.health}\n")
        round += 1

# Check if the game is over before writing the end game message
        if PCstats.health <= 0 or NPCstats.health <= 0:
            transcript.write(f"\n{(end_game_message(PCstats, NPCstats, userName, NPC))}")

# Ending the Game
print(end_game_message(PCstats, NPCstats, userName, NPC))
art = """
            ,
           .:/
.      ,,///;,   ,;/
  .   o:::::::;;///
     >::::::::;;\\\\\\
       ''\\\\\\\'" ';\\
          ';\ 
"""
print(art)

#Printing the Transcript
while True:
    transcriptchoice = input(f"\nWould you like to view the full transcript of the game?\nPlease input 'Y' or 'N': ")
    if transcriptchoice.lower() == 'y':
        print (f"Here is your transcript titled {transcript_file_path}")
        print("\n=== Transcript ===")
        with open(transcript_file_path, "r") as transcript_file:
            print(transcript_file.read())
        break
    elif transcriptchoice.lower() == 'n':
        print ("Thank you for playing the game!")
        print (f"If you want to see your transcript, its name is {transcript_file_path}")
        break
    else:
        continue
