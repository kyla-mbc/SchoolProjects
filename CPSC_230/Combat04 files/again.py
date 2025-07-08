import random
from prettytable import PrettyTable

# Transcript File
def transcript_file(file, message):
    with open(file, "a") as file:
        file.write(message + "\n")

# Player Stats
class Character:
    def __init__(self, player_type, health, attack_modifier, attack_dice, ac, special_attack, cooldown):
        self.player_type = player_type
        self.health = health
        self.attack_modifier = attack_modifier
        self.attack_dice = attack_dice
        self.ac = ac
        self.special_attack = special_attack
        self.cooldown = cooldown
        self.cooldown_count = 0

    def calculate_damage(self, attacker, defender, is_special_attack=False, action=None):
        if action == "Dodge":
            opponent_roll = self.roll_dice(attacker.attack_dice)  # Generate opponent's roll
            player_roll = 0  # Player's roll is not applicable when dodging
            print(f"\t {defender.player_type} chose to dodge! Opponent rolled a {opponent_roll}.")
            return player_roll, opponent_roll

        attack_modifier = attacker.attack_modifier
        attack_dice = attacker.attack_dice
        armor_class = defender.ac
        base_damage = self.roll_dice(attack_dice)

        if attacker in PCtypes.values():
            print(f"\t You rolled a {base_damage}!")
        elif attacker in NPCtypes.values():
            print(f"\t The {attacker.player_type} rolled a {base_damage}!")

        if base_damage == attack_dice:
            print("\t MAXIMUM DAMAGE DONE")
        elif base_damage == 1:
            print("\t MINIMUM DAMAGE DONE")

        if is_special_attack and base_damage >= armor_class:
            # Add special attack damage only if the attack hits
            base_damage += attacker.special_attack

        elif base_damage >= armor_class:
            # Add attack modifier only if the attack hits and it's not a special attack
            base_damage += attack_modifier

        opponent_roll = 0  # Opponent's roll is not applicable when attacking
        return base_damage, opponent_roll



    def roll_dice(self, sides):
        if sides < 2:
            raise ValueError("Number of sides must be at least 2")
        roll = random.randint(1, sides)
        return roll
    # print (f"{self.player_type} rolled", roll)
        

    def use_special_attack(self):
        if self.cooldown_count == 0:
            return True
        else:
            print(f"\t {self.player_type} is on cooldown. Special Attack not available. Cooldown Count: {self.cooldown_count}")
            return False

    def perform_special_attack(self, defender):
        if self.use_special_attack():
            self.cooldown_count = self.cooldown  # Reset cooldown count
            print(f"\t {self.player_type} used Special Attack!")
            return True
        else:
            return False


def end_game_message(player, opponent, player_name, opponent_name):
    if player.health <= 0:
        return f"Game Over! {opponent_name.capitalize()} wins! Better luck next time, {player_name.capitalize()}!"
    elif opponent.health <= 0:
        return f"Congratulations, {player_name.capitalize()}! You defeated the {opponent_name.capitalize()}!"

# NPC and PC Types
PCtypes = {
    "PC01": Character("Warlock", 90, 10, 20, 15, 25, 3),
    "PC02": Character("Ranger", 70, 10, 20, 10, 25, 3),
    "PC03": Character("Wizard", 80, 15, 20, 10, 25, 3),
    "PC04": Character("Barbarian", 100, 21, 20, 25, 25, 3),
    "PC05": Character("Cleric", 80, 15, 20, 10, 25, 3)
}

NPCtypes = {
    "NPC1": Character("Sorcerer", 100, 15, 20, 10, 25, 3),
    "NPC2": Character("Paladin", 80, 10, 20, 15, 25, 3),
    "NPC3": Character("Rogue", 60, 20, 20, 20, 25, 3)
}

# Displaying Player Types in table
PCtable = PrettyTable(["Player Type", "Health", "Attack", "Attack Dice", "Armor Class", "Special Attack", "Cooldown"])
for pc, PCdata in PCtypes.items():
    PCtable.add_row([PCdata.player_type, PCdata.health, PCdata.attack_modifier, PCdata.attack_dice, PCdata.ac,
                     PCdata.special_attack, PCdata.cooldown])

# Displaying NPC Types in table
NPCtable = PrettyTable(["Player Type", "Health", "Attack", "Attack Dice", "Armor Class", "Special Attack", "Cooldown"])
for npc, NPCdata in NPCtypes.items():
    NPCtable.add_row([NPCdata.player_type, NPCdata.health, NPCdata.attack_modifier, NPCdata.attack_dice, NPCdata.ac,
                      NPCdata.special_attack, NPCdata.cooldown])

# Transcript File
while True:
    transcript_file_path = input("What would you like to name your transcript?\nPlease add '.txt' at the end of your file name: ")
    if transcript_file_path:
        break
    else:
        print("Invalid input. Please provide a valid transcript name. Try again.\n")

userName = input("Welcome to the Combat Game! What is your name: ")
print(f"Welcome {userName.capitalize()}! First, you will need to choose your Player Type!\n"
      f"Here are your choices and some information about them:")
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
    NPCplayer = input("You can choose your opponent or input 'random' and we can choose your opponent for you.\n"
                     "Who would you like to go against: ")
    NPC = NPCplayer
    if NPCplayer.lower() == "random":
        NPCplayer = random.choice(list(NPCtypes.keys()))
        NPCstats = NPCtypes[NPCplayer]
        NPC = NPCstats.player_type
        break
    elif NPCplayer.lower() in [data.player_type.lower() for data in NPCtypes.values()]:
        NPCstats = next(npc for npc in NPCtypes.values() if npc.player_type.lower() == NPCplayer.lower())
        NPC = NPCstats.player_type
        break
    else:
        print("Invalid input. Please choose a valid opponent.")

# Print opponent information
print(f"\n\tOpponent's Player Type: {NPCstats.player_type}")
print(f"\tOpponent's Starting Health: {NPCstats.health}")
print(f"\tYour Starting Health: {PCstats.health}")
print(f"\tGood Luck! You're going to need it.")

# Playing the Game
with open(transcript_file_path, "a") as transcript:
    transcript.write(f"\nPlayer: {PLAYER}({userName.capitalize()}) vs {NPC.capitalize()}\n")
    transcript.write(f"Opponent: {NPC.capitalize()}, Starting Health: {NPCstats.health}\n")
    transcript.write(f"Your Player Type: {PLAYER.capitalize()}, Starting Health: {PCstats.health}\n")
    transcript.write("Good Luck! You're going to need it.\n\n")

    round_number = 1
    while PCstats.health > 0 and NPCstats.health > 0:
        print(f"\nRound {round_number}: Choose your action:")
        option = input("Attack, Special Attack, or Dodge: ")

        # Define the damage variables outside the conditions
        player_damage = 0
        NPC_damage = 0

        if option.lower() == "attack":
            npc_choice = random.choice(["Attack", "Dodge", "Special Attack"])
            print(f"\t Round {round_number}:")
            print("\t You chose to attack.")
            if npc_choice == "Attack":
                print(f"\t The {NPC} attacked you!")
                player_damage, opponent_roll = PCstats.calculate_damage(PCstats, NPCstats, action=option)
                NPC_damage, player_roll = NPCstats.calculate_damage(NPCstats, PCstats)

                if player_damage < NPCstats.ac:
                    print("\t You missed!")
                elif player_damage >= NPCstats.ac:
                    NPCstats.health -= player_damage  
                    if PCstats.health <= 0:
                        PCstats.health = 0
                    if NPCstats.health <= 0:
                        NPCstats.health = 0
                    print(f"\t You did a damage of {player_damage}.")
                if NPC_damage < PCstats.ac:
                    print(f"\t The {NPC} missed!")
                elif NPC_damage >= PCstats.ac:
                    PCstats.health -= NPC_damage
                    if PCstats.health <= 0:
                        PCstats.health = 0
                    if NPCstats.health <= 0:
                        NPCstats.health = 0
                    print(f"\t The {NPC} caused a damage of {NPC_damage}, watch out next time.")
            elif npc_choice == "Dodge":
                print(f"\t The {NPC} dodged!")
                print(f"\t No damage was done to the {NPC}")
                if PCstats.health <= 0:
                    PCstats.health = 0
                if NPCstats.health <= 0:
                    NPCstats.health = 0
            else:
                print(f"\t The {NPC} used Special Attack!")
                player_damage, opponent_roll = PCstats.calculate_damage(PCstats, NPCstats, action=option)
                NPC_damage, player_roll = NPCstats.calculate_damage(NPCstats, PCstats, True)
                if player_damage < NPCstats.ac:
                    print("\t You missed!")
                elif player_damage >= NPCstats.ac:
                    NPCstats.health -= player_damage
                    if PCstats.health <= 0:
                        PCstats.health = 0
                    if NPCstats.health <= 0:
                        NPCstats.health = 0
                    print(f"\t You did a damage of {player_damage}.")
                if NPC_damage < PCstats.ac:
                    print(f"\t The {NPC} missed!")
                elif NPC_damage >= PCstats.ac:
                    PCstats.health -= NPC_damage
                    if PCstats.health <= 0:
                        PCstats.health = 0
                    if NPCstats.health <= 0:
                        NPCstats.health = 0
                    print(f"\t The {NPC} caused a damage of {NPC_damage}, watch out next time.")
            print(f"\t Your health is {PCstats.health} and your opponent's health is {NPCstats.health}.")
        elif option.lower() == "special attack":
            npc_choice = random.choice(["Attack", "Dodge", "Special Attack"])
            print(f"\t Round {round_number}: ")
            if PCstats.perform_special_attack(NPCstats):
                if npc_choice == "Attack":
                    print(f"\t The {NPC} attacked you!")
                    player_damage, opponent_roll = PCstats.calculate_damage(PCstats, NPCstats, True, action=option)
                    NPC_damage, player_roll = NPCstats.calculate_damage(NPCstats, PCstats)
                    if player_damage < NPCstats.ac:
                        print("\t You missed!")
                    elif player_damage >= NPCstats.ac:
                        NPCstats.health -= player_damage  
                        if PCstats.health <= 0:
                            PCstats.health = 0
                        if NPCstats.health <= 0:
                            NPCstats.health = 0
                        print(f"\t You did a damage of {player_damage}.")
                    if NPC_damage < PCstats.ac:
                        print(f"\t The {NPC} missed!")
                    elif NPC_damage >= PCstats.ac:
                        PCstats.health -= NPC_damage
                        if PCstats.health <= 0:
                            PCstats.health = 0
                        if NPCstats.health <= 0:
                            NPCstats.health = 0
                        print(f"\t The {NPC} caused a damage of {NPC_damage}, watch out next time.")
                elif npc_choice == "Special Attack":
                    if NPCstats.perform_special_attack(PCstats):
                        player_damage, opponent_roll = PCstats.calculate_damage(PCstats, NPCstats, True, action=option)
                        NPC_damage, player_roll = NPCstats.calculate_damage(NPCstats, PCstats, True)
                        if player_damage < NPCstats.ac:
                            print("\t You missed!")
                        elif player_damage >= NPCstats.ac:
                            NPCstats.health -= player_damage
                            if PCstats.health <= 0:
                                PCstats.health = 0
                            if NPCstats.health <= 0:
                                NPCstats.health = 0
                            print(f"\t You did a damage of {player_damage}.")
                        if NPC_damage < PCstats.ac:
                            print(f"\t The {NPC} missed!")
                        elif NPC_damage >= PCstats.ac:
                            PCstats.health -= NPC_damage
                            if PCstats.health <= 0:
                                PCstats.health = 0
                            if NPCstats.health <= 0:
                                NPCstats.health = 0
                            print(f"\t The {NPC} caused a damage of {NPC_damage}, watch out next time.")
                else:
                    print(f"\t The {NPC} dodged!")
                    print(f"\t No damage was done to the {NPC}")
                    if PCstats.health <= 0:
                        PCstats.health = 0
                    if NPCstats.health <= 0:
                        NPCstats.health = 0
                print(f"\t Your health is {PCstats.health} and your opponent's health is {NPCstats.health}.")
            else:
                print(f"\t Regular Attack Executed.")
                option = "Attack"
                if option.lower() == "attack":
                    npc_choice = random.choice(["Attack", "Dodge", "Special Attack"])
                    print("\t You chose to attack.")
                    if npc_choice == "Attack":
                        print(f"\t The {NPC} attacked you!")
                        player_damage, opponent_roll = PCstats.calculate_damage(PCstats, NPCstats, action=option)
                        NPC_damage, player_roll = NPCstats.calculate_damage(NPCstats, PCstats)
                        if player_damage < NPCstats.ac:
                            print("\t You missed!")
                        elif player_damage >= NPCstats.ac:
                            NPCstats.health -= player_damage  
                            if PCstats.health <= 0:
                                PCstats.health = 0
                            if NPCstats.health <= 0:
                                NPCstats.health = 0
                            print(f"\t You did a damage of {player_damage}.")
                        if NPC_damage < PCstats.ac:
                            print(f"\t The {NPC} missed!")
                        elif NPC_damage >= PCstats.ac:
                            PCstats.health -= NPC_damage
                            if PCstats.health <= 0:
                                PCstats.health = 0
                            if NPCstats.health <= 0:
                                NPCstats.health = 0
                            print(f"\t The {NPC} caused a damage of {NPC_damage}, watch out next time.")
                    elif npc_choice == "Dodge":
                        print(f"\t The {NPC} dodged!")
                        print(f"\t No damage was done to the {NPC}")
                        if PCstats.health <= 0:
                            PCstats.health = 0
                        if NPCstats.health <= 0:
                            NPCstats.health = 0
                    else:
                        print(f"\t The {NPC} used Special Attack!")
                        player_damage, opponent_roll = PCstats.calculate_damage(PCstats, NPCstats, action=option)
                        NPC_damage, player_roll = NPCstats.calculate_damage(NPCstats, PCstats)
                        if player_damage < NPCstats.ac:
                            print("\t You missed!")
                        elif player_damage >= NPCstats.ac:
                            NPCstats.health -= player_damage
                            if PCstats.health <= 0:
                                PCstats.health = 0
                            if NPCstats.health <= 0:
                                NPCstats.health = 0
                            print(f"\t You did a damage of {player_damage}.")
                        if NPC_damage < PCstats.ac:
                            print(f"\t The {NPC} missed!")
                        elif NPC_damage >= PCstats.ac:
                            PCstats.health -= NPC_damage
                            if PCstats.health <= 0:
                                PCstats.health = 0
                            if NPCstats.health <= 0:
                                NPCstats.health = 0
                            print(f"\t The {NPC} caused a damage of {NPC_damage}, watch out next time.")
                    print(f"\t Your health is {PCstats.health} and your opponent's health is {NPCstats.health}.")
        elif option.lower() == "dodge":
            npc_choice = random.choice(["Attack", "Dodge", "Special Attack"])
            print(f"\t Round {round_number}:")
            print("\t You chose to dodge.")
            if npc_choice == "Attack":
                print(f"\t The {NPC} attacked!")
                print(f"\t The {NPC} missed!")
                print(f"\t No damage was done to you.")
                if PCstats.health <= 0:
                    PCstats.health = 0
                if NPCstats.health <= 0:
                    NPCstats.health = 0
            elif npc_choice == "Special Attack":
                print(f"\t The {NPC} used special attack!")
                print(f"\t The {NPC} missed!")
                print(f"\t No damage was done to you..")
                if PCstats.health <= 0:
                    PCstats.health = 0
                if NPCstats.health <= 0:
                    NPCstats.health = 0
            else:
                print(f"\t Both you and the {NPC} dodged! No damage was done to either party.")   
            print(f"\t Your health is {PCstats.health} and your opponent's health is {NPCstats.health}.")
        else:
            print("Invalid option. Choose again.")
            continue

        # Writing round information to the transcript file
        transcript.write(f"\nRound {round_number}:\n")
        transcript.write(f"\t{PLAYER} chose: {option.capitalize()}\n")
        transcript.write(f"\t{NPC} chose: {npc_choice.capitalize()}\n")
        transcript.write(f"\t{PLAYER}'s damage done: {player_damage}\n")
        transcript.write(f"\t{NPC}'s damage done: {NPC_damage}\n")
        transcript.write(f"\t{PLAYER}'s health: {PCstats.health}, {NPC}'s health: {NPCstats.health}\n")
        round_number += 1

        # Update CooldownCount
        if option.lower() == "special attack" and PCstats.use_special_attack():
            PCstats.cooldown_count = PCstats.cooldown
        else:
            PCstats.cooldown_count = max(0, PCstats.cooldown_count - 1)

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

# Printing the Transcript
while True:
    transcriptchoice = input(f"\nWould you like to view the full transcript of the game?\nPlease input 'Y' or 'N': ")
    if transcriptchoice.lower() == 'y':
        print (f"\nHere is your transcript titled {transcript_file_path}")
        print("========== Transcript ==========")
        with open(transcript_file_path, "r") as transcript_file:
            print(transcript_file.read())
        break
    elif transcriptchoice.lower() == 'n':
        print ("Thank you for playing the game!")
        print (f"If you want to see your transcript, its name is {transcript_file_path}")
        break
    else:
        continue