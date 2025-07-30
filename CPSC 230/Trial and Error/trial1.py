import random

class Character:
    def __init__(self, player_type, health, attack_modifier, attack_dice, dodge_dice):
        self.player_type = player_type
        self.health = health
        self.attack_modifier = attack_modifier
        self.attack_dice = attack_dice
        self.dodge_dice = dodge_dice

    def roll_dice(self, sides):
        if sides < 1:
            return 0
        return random.randint(1, sides)

    def calculate_damage(self, attacker, defender):
        attack_modifier = attacker.attack_modifier
        attack_dice = attacker.attack_dice
        dodge_dice = defender.dodge_dice
        base_damage = attack_modifier + self.roll_dice(attack_dice)
        dodge = self.roll_dice(dodge_dice)
        damage_dealt = max(0, base_damage - dodge)
        return damage_dealt

# Define character stats for different classes as instances of the Character class
character_stats = {
    "druid": Character("Druid", 60, 6, 10, 6),
    "barbarian": Character("Barbarian", 80, 8, 12, 3),
    "rogue": Character("Rogue", 60, 7, 8, 8),
    "sorcerer": Character("Sorcerer", 65, 6, 8, 5),
    "warlock": Character("Warlock", 50, 8, 9, 9),
    "ranger": Character("Ranger", 60, 4, 8, 4),
    "fighter": Character("Fighter", 85, 8, 10, 2),
    "monk": Character("Monk", 75, 7, 9, 6),
}

# Character customization options
customization_options = {
    "heal": {
        "name": "Heal",
        "description": "This will heal 15 of your health points.",
        "effect": "heal",
        "effect_value": 15
    },
    "strengthen_attack": {
        "name": "Strengthen Attack",
        "description": "You attack modifier will be increased by 5 the next turn.",
        "effect": "attack_boost",
        "effect_value": 5
    },
    "enhance_dodge": {
        "name": "Enhance Dodge",
        "description": "Your dodge dice will be increased by 3 the next turn.",
        "effect": "dodge_boost",
        "effect_value": 3
    }
}

# Ask the user for their name
name = input("Hello! What is your name? ")
print("Welcome to combat", name, "!")
print("It's great to have you here! Before you choose a class, please enter the desired name for the transcript of this game, and I would love to give you some information regarding the options after.")

# Ask the user for the file name
file_name = input("Enter the desired file name for the transcript (without extension): ")

# Open the file in write mode
transcript_file = open(f"{file_name}.txt", "w")

# Write a header to the transcript file
transcript_file.write(f"Transcript for {name}'s Combat Game\n\n")

# Display stats of the different characters and write to the transcript
for class_name, stats in character_stats.items():
    print(f"The {stats.player_type} class has the following stats:")
    print(f"Health: {stats.health}")
    print(f"AttackModifier: {stats.attack_modifier}")
    print(f"DodgeDice: {stats.dodge_dice}")
    transcript_file.write(f"\nThe {stats.player_type} class has the following stats:\n")
    transcript_file.write(f"Health: {stats.health}\n")
    transcript_file.write(f"AttackModifier: {stats.attack_modifier}\n")
    transcript_file.write(f"DodgeDice: {stats.dodge_dice}\n")

# Have the user choose a class with error handling
player_class = input("So which class would you like to choose?").lower()
while player_class not in character_stats:
    print("You chose an invalid class :( Please check your spelling!")
    player_class = input("So which class would you like to choose?").lower()

# Choose an opponent while excluding the player's class
randomchoice = input("Do you want to choose the class you fight?")
while randomchoice != "yes" and randomchoice != "no":
    print("You chose an invalid option :( Please choose either yes or no!")
    randomchoice = input("Do you want to choose your class?").lower()
options = [cls for cls in character_stats if cls != player_class]
if randomchoice == "no":
    NPC = random.choice(options)
elif randomchoice == "yes":
    print("Choose one of the following options:", options)
    NPC = input("Your choice: ").lower()

# Selecting difficulty
print("Your health is: ", character_stats[player_class].health)
print("Your opponent's health is: ", character_stats[NPC].health)
difficulty = input("Choose a difficulty: Easy, Medium, or Challenging!").lower()
if difficulty not in ["easy", "medium", "challenging"]:
    print("That's an invalid difficulty level! Please check your spelling and try again!")
    difficulty = input("Choose a difficulty: Easy, Medium, or Challenging!").lower()
else:
    player_health = character_stats[player_class].health
    if difficulty == "easy":
        opponent_health = character_stats[NPC].health
    elif difficulty == "medium":
        opponent_health = character_stats[NPC].health * 2
    elif difficulty == "challenging":
        opponent_health = character_stats[NPC].health * 3
print("Your starting health is:", player_health)
print("Your opponent's starting health is:", opponent_health)

# Game loop
round_number = 1
while player_health > 0 and opponent_health > 0:
    # Character customization option
    print(f"\nRound {round_number}: Choose an action (1, 2, or 3):")
    print("1. Attack")
    print("2. Dodge")
    print("3. Customize")

    player_action = input("Your choice: ").lower()
    while player_action not in ["1", "2", "3"]:
        print("You chose an invalid action :( Please enter 1, 2, or 3!")
        player_action = input("Your choice: ").lower()

    if player_action == "3":  # Customization
        print("Choose a customization option:")
        for option_key, option in customization_options.items():
            print(f"{option_key.capitalize()}: {option['description']}")

        customization_choice = input("Your choice: ").lower()
        while customization_choice not in customization_options:
            print("You chose an invalid customization option :( Please check your spelling!")
            customization_choice = input("Your choice: ").lower()

        # Randomly assign a customization option to the NPC
        npc_customization = random.choice(list(customization_options.keys()))
        print(f"You chose to customize your character with {customization_options[customization_choice]['name']}!")
        print(f"The opponent chose to customize with {customization_options[npc_customization]['name']}!")
        transcript_file.write(f"\n{player_class.capitalize()} chose to customize with {customization_options[customization_choice]['name']}!\n")
        transcript_file.write(f"{NPC.capitalize()} chose to customize with {customization_options[npc_customization]['name']}!\n")

        # Apply customization 
        player_effect = customization_options[customization_choice]['effect']
        player_effect_value = customization_options[customization_choice]['effect_value']
        opponent_effect = customization_options[npc_customization]['effect']
        opponent_effect_value = customization_options[npc_customization]['effect_value']

        if player_effect == "heal":
            player_health += min(player_effect_value, character_stats[player_class].health - player_health)
        elif player_effect == "attack_boost":
            character_stats[player_class].attack_modifier += player_effect_value
        elif player_effect == "dodge_boost":
            character_stats[player_class].dodge_dice += player_effect_value

        if opponent_effect == "heal":
            opponent_health += min(opponent_effect_value, character_stats[NPC].health - opponent_health)
        elif opponent_effect == "attack_boost":
            character_stats[NPC].attack_modifier += opponent_effect_value
        elif opponent_effect == "dodge_boost":
            character_stats[NPC].dodge_dice += opponent_effect_value

        print(f"{player_class.capitalize()}'s health is now: {player_health}")
        print(f"{NPC.capitalize()}'s health is now: {opponent_health}")

        # Write customization information to the transcript file
        transcript_file.write(f"{player_class.capitalize()}'s health is now: {player_health}\n")
        transcript_file.write(f"{NPC.capitalize()}'s health is now: {opponent_health}\n")
    else:
        # Player's turn
        if player_action == "1":  # Attack
            player_damage = character_stats[player_class].calculate_damage(character_stats[player_class], character_stats[NPC])
            opponent_health -= player_damage
            print(f"You chose to Attack!")
            print(f"You dealt {player_damage} damage to {NPC.capitalize()}!")
            print(f"{NPC.capitalize()}'s health is now: {max(0, opponent_health)}")

            # Write player's turn information to the transcript file
            transcript_file.write("\nPlayer's Turn:\n")
            transcript_file.write(f"Player Action: Attack\n")
            transcript_file.write(f"NPC: {NPC.capitalize()}\n")
            transcript_file.write(f"Damage Dealt: {player_damage}\n")
            transcript_file.write(f"{NPC.capitalize()}'s health is now: {max(0, opponent_health)}\n")
        elif player_action == "2":  # Dodge
            print(f"You chose to Dodge!")
            # Write player's turn information to the transcript file for dodge
            transcript_file.write("\nPlayer's Turn:\n")
            transcript_file.write(f"Player Action: Dodge\n")
            transcript_file.write(f"NPC: {NPC.capitalize()}\n")
            # Write additional information about dodge to the transcript file if needed

        # NPC's turn
        npc_action = random.choice(["attack", "dodge"])
        npc_damage = 0
        if npc_action == "attack":
            npc_damage = character_stats[NPC].calculate_damage(character_stats[NPC], character_stats[player_class])
            player_health -= npc_damage
            print(f"{NPC.capitalize()} chose to Attack!")
            print(f"{NPC.capitalize()} dealt {npc_damage} damage to you!")
            print(f"Your health is now: {max(0, player_health)}")
        elif npc_action == "dodge":
            print(f"{NPC.capitalize()} chose to Dodge!")

        # Write NPC's turn information to the transcript file
        transcript_file.write("\nNPC's Turn:\n")
        transcript_file.write(f"NPC Action: {npc_action.capitalize()}\n")
        transcript_file.write(f"Player: {player_class.capitalize()}\n")
        if npc_action == "attack":
            transcript_file.write(f"Damage Dealt: {npc_damage}\n")
            transcript_file.write(f"Your health is now: {max(0, player_health)}\n")
        elif npc_action == "dodge":
            # Write additional information about NPC's dodge to the transcript file if needed
            pass

    # Print the results of the game
    if player_health <= 0 or opponent_health <= 0:
        break

    # Increment the round number
    round_number += 1

# Print the final results of the game
if player_health > opponent_health:
    print("Amazing job! You won", name, "!")
    transcript_file.write(f"\nCongratulations! You won the game!\n")
elif player_health < opponent_health:
    print("So close! Better luck next time", name, ".")
    transcript_file.write(f"\nUnfortunately, you lost the game. Better luck next time, {name}.\n")

# Close the transcript file
transcript_file.close()
