import random
from prettytable import PrettyTable

# Transcript File
def transcript_file(file, message):
    with open(file, "a") as file:
        file.write(message + "\n")

# Customization Options
customization_options = ["Increase Health", "Increase Attack", "Increase Dodge"]

# Customize Character Function  
def customize_character(character, is_player=True):
    if is_player: 
        print("\tChoose a customization option:")
 
    if not is_player:
        print(f"\t{character.player_type} is customizing...")

    while True:
        if is_player:
            choice = input("\tEnter the number corresponding to your choice: ")
        else:
            # NPC chooses randomly
            choice = str(random.randint(1, len(customization_options)))

        if choice.isdigit() and 1 <= int(choice) <= len(customization_options):
            selected_option = customization_options[int(choice) - 1]
            if selected_option == "Increase Health":
                if is_player:
                    character.health += 10
                    print(f"\tYou chose to increase your health. Your health is now {character.health}.")
                else:
                    character.health += 10
            elif selected_option == "Increase Attack":
                if is_player:
                    character.attack_modifier += 5
                    print(f"\tYou chose to increase your attack. Your attack modifier is now {character.attack_modifier}.")
                else:
                    character.attack_modifier += 5
            elif selected_option == "Increase Dodge":
                if is_player:
                    character.dodge_dice += 5
                    print(f"\tYou chose to increase your dodge. Your dodge dice is now {character.dodge_dice}.")
                else:
                    character.dodge_dice += 5
            break
        else:
            print("Invalid choice. Please enter a valid number.")

# Player stats
def playerstats():
    print(f"\tOpponent's Player Type: {NPCstats.player_type}")
    print(f"\tOpponent's Starting Health: {NPCstats.health}")
    if playerInput.lower() in ["warlock", "ranger", "wizard", "barbarian", "cleric"]:
        print(f"\tYour Starting Health: {PCstats.health}")
    print(f"\tGood Luck! You're going to need it.")

# Dice Rolling Function
def dice_roller(attack_sides):
    if attack_sides < 2:
        raise ValueError("Number of sides must be at least 2")
    return random.randint(1, attack_sides)

# Dodge Dice Function
def dodge_dice(dodge_dice_sides):
    if dodge_dice_sides < 2:
        raise ValueError("Dodge Dice must have at least 2 sides")
    dodge_value = random.randint(1, dodge_dice_sides)
    return dodge_value

# End Game Function
def end_game_message(PCstats, NPCstats, userName, NPC):
    if PCstats.health == 0 and NPCstats.health == 0:
        return "The match ended in a draw."
    elif PCstats.health == 0:
        return f"Oh no {userName.capitalize()}! You were defeated by the {NPC}."
    elif NPCstats.health == 0:
        return f"Congratulations {userName.capitalize()}, You have defeated the {NPC}!"

# Character and Damage Class
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

# Creating Player Types
PCtypes = {
    "PC01": Character("Warlock", 90, 20, 10, 20),
    "PC02": Character("Ranger", 70, 20, 10, 10),
    "PC03": Character("Wizard", 80, 28, 15, 25),
    "PC04": Character("Barbarian", 100, 25, 20, 10),
    "PC05": Character("Cleric", 80, 25, 15, 20)
}

# Creating NPC Types
NPCtypes = {
    "NPC1": Character("Sorcerer", 100, 20, 10, 20),
    "NPC2": Character("Paladin", 80, 25, 5, 25),
    "NPC3": Character("Rogue", 60, 15, 5, 15)
}

# Displaying Player Types in table 
PCtable = PrettyTable(["Player Type", "Health", "Attack", "Attack Dice", "Dodge Dice"])
for pc, PCdata in PCtypes.items():
    PCtable.add_row([PCdata.player_type, PCdata.health, PCdata.attack_modifier, PCdata.attack_dice, PCdata.dodge_dice])

# Displaying NPC Types in table
NPCtable = PrettyTable(["Player Type", "Health", "Attack", "Attack Dice", "Dodge Dice"])
for npc, NPCdata in NPCtypes.items():
    NPCtable.add_row([NPCdata.player_type, NPCdata.health, NPCdata.attack_modifier, NPCdata.attack_dice, NPCdata.dodge_dice])

# Greeting the user
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

# Choosing Opponent 
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
with open(transcript_file_path, "a") as transcript:  
    transcript.write(f"\nPlayer: {PLAYER}({userName.capitalize()}) vs {NPCstats.player_type}\n\n")

    round = 1

    while PCstats.health > 0 and NPCstats.health > 0:
        option = input("Attack, Dodge, or Customize: ")

        # Define the damage variables outside the conditions
        player_damage = 0
        NPC_damage = 0
        npc_choice = ""  # Initialize npc_choice outside the while loop

        if option.lower() not in ["attack", "dodge", "customize"]:
            continue
        else:
            print(f"\tRound {round}:")

        if option.lower() == "attack":
            npc_choice = random.choice(["Attack", "Dodge"])
            print("\tYou chose to attack.")
            if npc_choice == "Attack":
                print(f"\tThe {NPCstats.player_type} attacked you!")
                player_damage = PCstats.calculate_damage(PCstats, NPCstats)
                NPC_damage = NPCstats.calculate_damage(NPCstats, PCstats)
                PCstats.health -= NPC_damage
                NPCstats.health -= player_damage
                if PCstats.health <= 0:
                    PCstats.health = 0
                if NPCstats.health <= 0:
                    NPCstats.health = 0
                print(f"\tYou did a damage of {player_damage}.")
                print(f"\tThe {NPCstats.player_type} caused a damage of {NPC_damage}, watch out next time.")
            else:
                print(f"\tThe {NPCstats.player_type} dodged!")
                dodge = dodge_dice(NPCstats.dodge_dice)
                player_damage = PCstats.calculate_damage(PCstats, NPCstats) - dodge
                if player_damage < dodge:
                    player_damage = 0
                NPCstats.health -= player_damage
                print(f"\tYou did a damage of {player_damage}. Great job!")
                print("\tYou dealt with 0 damage.")
                if PCstats.health <= 0:
                    PCstats.health = 0
                if NPCstats.health <= 0:
                    NPCstats.health = 0
            print(f"\tYour health is {PCstats.health} and your opponent's health is {NPCstats.health}.")
        elif option.lower() == "dodge":
            npc_choice = random.choice(["Attack", "Dodge"])
            print("\tYou chose to dodge.")
            if npc_choice == "Attack":
                print(f"\tThe {NPCstats.player_type} attacked you!")
                dodge = dodge_dice(PCstats.dodge_dice)
                NPC_damage = NPCstats.calculate_damage(NPCstats, PCstats) - dodge
                if NPC_damage < dodge:
                    NPC_damage = 0
                PCstats.health -= NPC_damage
                print(f"\tThe {NPCstats.player_type} did {NPC_damage} damage to you.")
                print(f"\tThe {NPCstats.player_type} dealt no damage.")
                if PCstats.health <= 0:
                    PCstats.health = 0
                if NPCstats.health <= 0:
                    NPCstats.health = 0
            else:
                print(f"\tThe {NPCstats.player_type} dodged! They dealt 0 damage.")
                print("\tYou dealt 0 damage.")
            print(f"\tYour health is {PCstats.health} and your opponent's health is {NPCstats.health}.")
        elif option.lower() == "customize":
            print("\tYou chose to customize.")
            # User customizes
            customize_character(PCstats)

            # NPC chooses randomly between attack, dodge, and customize
            npc_choice_customize = random.choice(["Attack", "Dodge", "Customize"])
            print(f"\tThe {NPCstats.player_type} chose to {npc_choice_customize.lower()}.")

            if npc_choice_customize == "Customize":
                customize_character(NPCstats, is_player=False)

            print(f"\tYour health is {PCstats.health} and your opponent's health is {NPCstats.health}.")


        # Writing round information to the transcript file
        transcript.write(f"\nRound {round}:\n")
        transcript.write(f"\t{PLAYER} chose: {option.capitalize()}\n")
        transcript.write(f"\t{NPCstats.player_type} chose: {npc_choice_customize.capitalize()}\n")
        transcript.write(f"\t{PLAYER}'s damage done: {player_damage}\n")
        transcript.write(f"\t{NPCstats.player_type}'s damage done: {NPC_damage}\n")
        transcript.write(f"\t{PLAYER}'s health: {PCstats.health}, {NPCstats.player_type}'s health: {NPCstats.health}\n")
        round += 1

        # Check if the game is over before writing the end game message
        if PCstats.health <= 0 or NPCstats.health <= 0:
            transcript.write(f"\n{(end_game_message(PCstats, NPCstats, userName, NPCstats.player_type))}")

# Ending the Game
print(end_game_message(PCstats, NPCstats, userName, NPCstats.player_type))

# Printing the Transcript
while True:
    transcriptchoice = input(f"\nWould you like to view the full transcript of the game?\nPlease input 'Y' or 'N': ")
    if transcriptchoice.lower() == 'y':
        print("\n=== Transcript ===")
        with open(transcript_file_path, "r") as transcript_file:
            print(transcript_file.read())
        break
    elif transcriptchoice.lower() == 'n':
        print("Thank you for playing the game!")
        break
    else:
        continue
