import random

class Character:
    def __init__(self, PlayerType, Health, AttackModifier, AttackDice, AC, SpecialAttack, Cooldown):
        self.PlayerType = PlayerType
        self.Health = Health
        self.AttackModifier = AttackModifier
        self.AttackDice = AttackDice
        self.AC = AC
        self.SpecialAttack = SpecialAttack
        self.Cooldown = Cooldown
        self.CooldownCount = Cooldown

    @classmethod
    def calculate_attack_damage(cls, character):
        attack_roll = cls.roll_dice(character.AttackDice)
        return character.AttackModifier + attack_roll

    @staticmethod
    def roll_dice(sides):
        return random.randint(1, sides)

class_types = {
    "Rogue": Character("Rogue", 100, 10, 8, 14, 20, 3),
    "Barbarian": Character("Barbarian", 120, 12, 10, 18, 15, 4),
    "Wizard": Character("Wizard", 80, 8, 12, 12, 25, 5),
    "Druid": Character("Druid", 110, 9, 6, 15, 18, 3),
    "Paladin": Character("Paladin", 140, 14, 8, 16, 22, 4),
    "Goblin": Character("Goblin", 40, 4, 4, 10, 5, 2),
    "Ogre": Character("Ogre", 80, 8, 12, 14, 10, 3),
    "Dragon": Character("Dragon", 200, 20, 20, 25, 30, 5)
}

# Game start
print("Welcome to the game!")
player_name = input("Please enter your name: ")
print(f"Hello, {player_name}!")

# Choosing character type
while True:
    print("Choose your PlayerType:")
    for class_name in class_types:
        print(f"{class_name} - Health: {class_types[class_name].Health}, Attack: {class_types[class_name].AttackModifier}, AC: {class_types[class_name].AC}")
    
    choice = input("Enter the PlayerType you want to play as: ")
    if choice in class_types:
        player_character = class_types[choice]
        break
    else:
        print("Invalid choice. Please enter a valid PlayerType.")

# Choosing opponent type
opponent_choice = input("Do you want to choose your opponent yourself (type 'choose') or have one chosen at random (type 'random')? ").lower()
if opponent_choice == "choose":
    while True:
        print("Choose your opponent:")
        for class_name in class_types:
            if class_name not in ["Rogue", "Barbarian", "Wizard", "Druid", choice]:
                print(f"{class_name} - Health: {class_types[class_name].Health}, Attack: {class_types[class_name].AttackModifier}, AC: {class_types[class_name].AC}")
        
        opp_choice = input("Enter the PlayerType of your opponent: ")
        if opp_choice in class_types and opp_choice not in ["Rogue", "Barbarian", "Wizard", "Druid", choice]:
            opponent = class_types[opp_choice]
            break
        else:
            print("Invalid choice. Please enter a valid PlayerType that is not the same as yours.")
else:
    opponent = random.choice([class_types[class_name] for class_name in class_types if class_name not in ["Rogue", "Barbarian", "Wizard", "Druid", choice]])

print(f"Your opponent is a {opponent.PlayerType} with {opponent.Health} health.")
print(f"Starting health -> {player_character.PlayerType}: {player_character.Health}, {opponent.PlayerType}: {opponent.Health}")

round_count = 1
while True:
    print(f"Round {round_count}: Choose your action:")
    player_choice = input("Enter 'attack', 'special attack', or 'dodge': ").lower()

    if player_choice == 'special attack':
        if player_character.CooldownCount != 0:
            print("You can't use your special attack yet!")
            continue
        player_character.CooldownCount = player_character.Cooldown
    else:
        player_character.CooldownCount += 1  # Increment CooldownCount when special attack is not used

    npc_choice = random.choice(['attack', 'special attack', 'dodge'])

    if player_choice == 'attack':
        player_damage = Character.calculate_attack_damage(player_character)
        if npc_choice == 'dodge':
            print("NPC dodged your attack!")
            player_damage = 0
        else:
            if npc_choice == 'special attack':
                print("NPC used a special attack!")
            opponent_damage = Character.calculate_attack_damage(opponent)
            if player_damage == player_character.AttackModifier + player_character.AttackDice:
                print("Max damage!")
            elif player_damage == player_character.AttackModifier:
                print("Min damage!")
            opponent.Health = max(opponent.Health - player_damage, 0)
    elif player_choice == 'special attack':
        player_damage = player_character.SpecialAttack
        opponent.Health = max(opponent.Health - player_damage, 0)
        player_character.CooldownCount = 0
        print("You used a special attack!")
    else:
        print("You chose to dodge!")

    if npc_choice == 'attack':
        npc_damage = Character.calculate_attack_damage(opponent)
        if player_choice == 'dodge':
            print("You dodged the NPC's attack!")
            npc_damage = 0
        else:
            if player_choice == 'special attack':
                print("You used a special attack!")
            player_damage = Character.calculate_attack_damage(player_character)
            if npc_damage == opponent.AttackModifier + opponent.AttackDice:
                print("Max damage!")
            elif npc_damage == opponent.AttackModifier:
                print("Min damage!")
            player_character.Health = max(player_character.Health - npc_damage, 0)
    elif npc_choice == 'special attack':
        npc_damage = opponent.SpecialAttack
        player_character.Health = max(player_character.Health - npc_damage, 0)
        opponent.CooldownCount = 0
        print("NPC used a special attack!")
    else:
        print("NPC chose to dodge!")

    print(f"Player's Health: {player_character.Health}, NPC's Health: {opponent.Health}")
    round_count += 1

    if player_character.Health <= 0 or opponent.Health <= 0:
        break

if player_character.Health <= 0:
    print(f"{player_name}, you were defeated by the {opponent.PlayerType}!")
else:
    print(f"Congratulations, {player_name}! You have defeated the {opponent.PlayerType}!")

filename = f"{player_name}_transcript.txt"
with open(filename, 'w') as file:
    file.write(f"Transcript for {player_name} vs {opponent.PlayerType}:\n")
    file.write(f"Player's Health: {player_character.Health}, NPC's Health: {opponent.Health}\n")
    file.write(f"Total Rounds: {round_count}\n")

print(f"Your transcript was saved as: {filename}")