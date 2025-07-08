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
        self.cooldown_count = 0  # Start with cooldown_count at 0

    def calculate_damage(self, attacker, defender, is_special_attack=False):
        attack_modifier = attacker.attack_modifier
        attack_dice = attacker.attack_dice
        dodge_dice = defender.ac  # Replacing dodge_dice with ac for defender
        base_damage = attack_modifier + self.roll_dice(attack_dice)
        
        if is_special_attack:
            base_damage += attacker.special_attack

        dodge = self.roll_dice(dodge_dice)
        damage_dealt = max(0, base_damage - dodge)
        return damage_dealt

    def roll_dice(self, sides):
        if sides < 2:
            raise ValueError("Number of sides must be at least 2")
        return random.randint(1, sides)

    def use_special_attack(self):
        if self.cooldown_count == 0:
            return True
        else:
            print(f"\t {self.player_type} is on cooldown. Special Attack not available. Cooldown Count: {self.cooldown_count}")
            return False

    def perform_special_attack(self, defender):
        if self.use_special_attack():
            self.cooldown_count = self.cooldown  # Reset cooldown count
            special_damage = self.roll_dice(self.attack_dice) + self.special_attack
            defender.health -= special_damage
            print(f"\t {self.player_type} used Special Attack!")
            print(f"\t You dealt {special_damage} damage.")
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
    "PC01": Character("Warlock", 90, 10, 20, 20, 10, 3),
    "PC02": Character("Ranger", 70, 10, 20, 10, 10, 3),
    "PC03": Character("Wizard", 80, 15, 28, 25, 10, 3),
    "PC04": Character("Barbarian", 100, 20, 25, 10, 10, 3),
    "PC05": Character("Cleric", 80, 15, 25, 15, 10, 3)
}

NPCtypes = {
    "NPC1": Character("Sorcerer", 100, 15, 20, 20, 10, 3),
    "NPC2": Character("Paladin", 80, 10, 25, 25, 10, 3),
    "NPC3": Character("Rogue", 60, 20, 15, 15, 10, 3)
}

# Displaying Player Types in table
PCtable = PrettyTable(["Player Type", "Health", "Attack", "Attack Dice", "AC", "Special Attack", "Cooldown"])
for pc, PCdata in PCtypes.items():
    PCtable.add_row([PCdata.player_type, PCdata.health, PCdata.attack_modifier, PCdata.attack_dice, PCdata.ac,
                     PCdata.special_attack, PCdata.cooldown])

# Displaying NPC Types in table
NPCtable = PrettyTable(["Player Type", "Health", "Attack", "Attack Dice", "AC", "Special Attack", "Cooldown"])
for npc, NPCdata in NPCtypes.items():
    NPCtable.add_row([NPCdata.player_type, NPCdata.health, NPCdata.attack_modifier, NPCdata.attack_dice, NPCdata.ac,
                      NPCdata.special_attack, NPCdata.cooldown])

# Transcript File
transcript_file_path = input("What would you like to name your transcript?\nPlease add '.txt' at the end of your file name: ")
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

# Playing the Game
with open(transcript_file_path, "a") as transcript:
    transcript.write(f"\nPlayer: {PLAYER}({userName.capitalize()}) vs {NPC.capitalize()}\n\n")

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
                dodge = PCstats.roll_dice(PCstats.ac)
                if PCstats.calculate_damage(PCstats, NPCstats) > dodge:
                    player_damage = PCstats.calculate_damage(PCstats, NPCstats) - dodge
                    NPCstats.health -= player_damage
                    print(f"\t You did a damage of {player_damage}. Great job!")
                    print("\t You dealt with 0 damage.")
                    if PCstats.health <= 0:
                        PCstats.health = 0
                    if NPCstats.health <= 0:
                        NPCstats.health = 0
                else:
                    print("\t You dealt with 0 damage.")
                    print(f"\t The {NPC} dealt with 0 damage.")
                    
            print(f"\t Your health is {PCstats.health} and your opponent's health is {NPCstats.health}.")
            
        elif option.lower() == "special attack":
            npc_choice = random.choice(["Attack", "Dodge", "Special Attack"])
            print(f"\t Round {round_number}:")
            print("\t You chose to use Special Attack.")
            if PCstats.perform_special_attack(NPCstats):
                if npc_choice == "Attack":
                    print(f"\t The {NPC} attacked you!")
                    player_damage = PCstats.calculate_damage(PCstats, NPCstats) + PCstats.special_attack
                    NPC_damage = NPCstats.calculate_damage(NPCstats, PCstats)
                    PCstats.health -= NPC_damage
                    NPCstats.health -= player_damage
                    if PCstats.health <= 0:
                        PCstats.health = 0
                    if NPCstats.health <= 0:
                        NPCstats.health = 0
                    print(f"\t You did a damage of {player_damage}.")
                    print(f"\t The {NPC} caused a damage of {NPC_damage}, watch out next time.")
                elif npc_choice == "Special Attack":
                    npc_special_damage = NPCstats.roll_dice(NPCstats.attack_dice) + NPCstats.special_attack
                    PCstats.health -= npc_special_damage
                    print(f"\t The {NPC} also used Special Attack!")
                    print(f"\t You did a damage of {player_damage}. Great job!")
                    print(f"\t The {NPC} dealt a damage of {npc_special_damage}.")
                    if PCstats.health <= 0:
                        PCstats.health = 0
                    if NPCstats.health <= 0:
                        NPCstats.health = 0
                else:
                    print(f"\t The {NPC} dodged!")
                    dodge = PCstats.roll_dice(PCstats.ac)
                    if PCstats.calculate_damage(PCstats, NPCstats) > dodge:
                        player_damage = PCstats.calculate_damage(PCstats, NPCstats) - dodge + PCstats.special_attack
                        NPCstats.health -= player_damage
                        print(f"\t You did a damage of {player_damage}. Great job!")
                        print("\t You dealt with 0 damage.")
                        if PCstats.health <= 0:
                            PCstats.health = 0
                        if NPCstats.health <= 0:
                            NPCstats.health = 0
                    else:
                        print("\t You dealt with 0 damage.")
                        print(f"\t The {NPC} dealt with 0 damage.")
                    
                print(f"\t Your health is {PCstats.health} and your opponent's health is {NPCstats.health}.")
        elif option.lower() == "dodge":
            npc_choice = random.choice(["Attack", "Dodge", "Special Attack"])
            print(f"\t Round {round_number}:")
            print("\t You chose to dodge.")
            if npc_choice == "Attack":
                print(f"\t The {NPC} attacked you!")
                dodge = PCstats.roll_dice(PCstats.ac)
                if dodge < PCstats.calculate_damage(PCstats, NPCstats):
                    NPC_damage = PCstats.calculate_damage(NPCstats, PCstats) - dodge
                    PCstats.health -= NPC_damage
                    print(f"\t The {NPC} did {NPC_damage} damage to you.")
                    print(f"\t The {NPC} dealt no damage.")
                    if PCstats.health <= 0:
                        PCstats.health = 0
                    if NPCstats.health <= 0:
                        NPCstats.health = 0
                else:
                    print(f"\t The {NPC} missed! They dealt 0 damage.")
                    print("\t You dealt 0 damage.")
            elif npc_choice == "Special Attack":
                print(f"\t The {NPC} used Special Attack!")
                print(f"\t You dodged, avoiding any damage.")
            else:
                print(f"\t The {NPC} dodged! They dealt 0 damage.")
                print("\t You dealt 0 damage.")
                
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
    transcript_choice = input(f"\nWould you like to view the full transcript of the game?\nPlease input 'Y' or 'N': ")
    if transcript_choice.lower() == 'y':
        print("\n=== Transcript ===")
        with open(transcript_file_path, "r") as transcript_file:
            print(transcript_file.read())
        break
    elif transcript_choice.lower() == 'n':
        print("Thank you for playing the game!")
        break
    else:
        continue
