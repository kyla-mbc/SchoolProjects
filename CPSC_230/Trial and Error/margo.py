import math
import random

def DiceRoll(x):
    sides = x
    global roll
    roll = random.randrange(1, 1 + sides)
    return roll

def Line(i):
    line = ('-' * i)
    return line

def Intro():
    global transcript_filename
    global Name
    print('Welcome to the Game')
    transcript_filename = input("Enter the filename for the transcript: ")
    open(f'{transcript_filename}.txt', "a")
    Name= input('What is your name? ')
    print('A difficult battle is in your future,', Name) 

def TableNPC():
    NPCType = {1: ['Easy', 'Sorcerer', 80, 20, 10, 7],
         2: ['Medium','Wizard', 105, 30, 30, 12],
         3: ['Hard','Ranger', 115, 40, 40, 15],
         }
    print("{:<11} {:<11} {:<11} {:<11} {:<11} {:<11}".format('Difficulty','Type','Health', 'Dodge', 'Attack', 'Min Attack'))
    for key, value in NPCType.items():
        difficulty, option, health, dodge, attack, minattack = value
        print("{:<11} {:<11} {:<11} {:<11} {:<11} {:<11}".format(difficulty,option, health, dodge, attack, minattack))

class NPC:
    def __init__(self,NPCType, Health, AttackModifier, AttackDice, DodgeDice):
        self.NPCType = NPCType
        self.NPCHealth = Health
        self.NPCAttackModifier = AttackModifier
        self.NPCAttackDice = AttackDice
        self.NPCDodgeDice = DodgeDice

    def NPCStat(self):
        print(f'You are attacking a {self.NPCType} that has {self.NPCHealth} heath, {self.NPCDodgeDice} dodge, and {self.NPCAttackDice} attack with a minimun attack of {self.NPCAttackModifier }.')
         
    def NPCDamageMod(self, player_type):
        global NDamage
        DiceRoll(self.NPCAttackDice)
        NDamage = self.NPCAttackModifier + roll
        print(f'The {self.NPCType} rolled a {roll}, hitting the you for a total of {NDamage}')
        if roll == self.NPCAttackDice:
            print(f'They rolled a critical hit! They deal maximum damage!\n')
        if roll == 1:
            print(f'They rolled a critical failure, dealing the minimum damage\n')
        with open(f'{transcript_filename}.txt', "a") as transcript:
            transcript.write(f'The {self.NPCType} rolled a {roll}, hitting the you for a total of {NDamage}\n')
        return NDamage

    def NPCDodgeMod(self, player_type):
        global NDodge
        DiceRoll(self.NPCDodgeDice)
        NDodge = roll
        print(f'The {self.NPCType} rolled a {roll}, dodging {roll} damage from the {player_type}')
        if roll == self.NPCDodgeDice:
            print(f'They rolled a critical dodge! They dodge maximum!\n')
        if roll == 1:
            print(f'They rolled the lowest dodge, they are in trouble\n')
        with open(f'{transcript_filename}.txt', "a") as transcript:
            transcript.write(f'The {self.NPCType} rolled a {roll}, dodging {roll} damage from the {player_type}\n')
        return NDodge

NPC1 = NPC('Sorcerer',80, 7, 20,10)
NPC2 = NPC('Wizard',105, 12, 30,30)
NPC3 = NPC('Ranger',115, 15, 40,40)

def NPCPick(User):
    global Bot 
    BotChoice = input('\nWould you like to choose your opponent? (Yes/No)\nOtherwise, it will be random ').lower()
    BotUndecided = True 
    Bot = None 
    

    while BotUndecided:
        if BotChoice == 'yes' or BotChoice == 'y':
            BotClass = input('Would you like to play an easy, medium, or hard NPC? ').lower()
            if BotClass == 'easy':
                Bot = NPC1
                BotUndecided = False 
            elif BotClass == 'medium':
                Bot = NPC2
                BotUndecided = False
            elif BotClass == 'hard':
                Bot = NPC3
                BotUndecided = False
            else:
                BotClass = input('Error. Would you like to play an easy, medium, or hard NPC?' ).lower()
        elif BotChoice == 'no' or BotChoice =='n':
            BotClass = random.randint(1, 3)
            if BotClass == 1:
                Bot = NPC1
                BotUndecided = False 
            elif BotClass == 2:
                Bot = NPC2
                BotUndecided = False
            elif BotClass == 3:
                Bot = NPC3
                BotUndecided = False   
        else:
            BotChoice = input('Would you like to choose your opponent? (Yes/No)' ).lower()

    if Bot is not None:
        print(Line(10))
        Bot.NPCStat()
        print(Line(10))
    else:
        print("Invalid choice.")
        BotChoice = input('Would you like to choose your opponent? (Yes/No)' ).lower()

    return Bot 

def TablePlayer():
    #PLAYER TABLE STATs
    TypeClass = {1: ['Cleric', 95, 35, 30, 8,],
            2: ['Sorcerer',90, 20, 25, 10],
            3: ['Barbarian',90, 15, 25, 13],
            4: ['Warlock',110, 30, 20, 7],
            5: ['Monk',105, 20, 15, 5]
            }
    print("{:<11} {:<11} {:<11} {:<11} {:<11}".format('Type','Health', 'Dodge', 'Attack', 'Min Attack'))
    for key, value in TypeClass.items():
        option, health, dodge, attack, minattack = value
        print("{:<11} {:<11} {:<11} {:<11} {:<11}".format(option, health, dodge, attack, minattack))

class Character:
    def __init__(self,PlayerType, Health, AttackModifier, AttackDice, DodgeDice):
        self.PlayerType = PlayerType
        self.Health = Health
        self.AttackModifier = AttackModifier
        self.AttackDice = AttackDice
        self.DodgeDice = DodgeDice

    def PlayerStat(self):
        print(f'You are a {self.PlayerType} that has {self.Health} heath, {self.DodgeDice} dodge, and {self.AttackDice} attack with a minimun attack of {self.AttackModifier }.')

    def PlayerDamageMod(self, npc_type):
        global UDamage
        roll = DiceRoll(self.AttackDice) 
        UDamage = self.AttackModifier + roll
        print(f'You rolled a {roll}, hitting the {npc_type} for a total of {UDamage}')
        if roll == self.AttackDice:
            print(f'You rolled a critical damage! Yippee')
            with open(f'{transcript_filename}.txt', "a") as transcript:
                transcript.write(f'You rolled a critical damage! Yippee\n')
        if roll == 1:
            print(f'You rolled the lowest damage, ooppsie')
            with open(f'{transcript_filename}.txt', "a") as transcript:
                transcript.write(f'You rolled the lowest damage, ooppsie\n')
        with open(f'{transcript_filename}.txt', "a") as transcript:
            transcript.write(f'You rolled a {roll}, hitting the {npc_type} for a total of {UDamage}\n')
        return UDamage  

    def PlayerDodgeMod(self, npc_type):
        global Userdodge_amount
        roll = DiceRoll(self.DodgeDice)  
        Userdodge_amount = roll
        print(f'You rolled a {roll}, dodging {roll} damage from the {npc_type}')
        if roll == self.DodgeDice:
            print(f'You rolled a critical dodge!')
            with open(f'{transcript_filename}.txt', "a") as transcript:
                transcript.write(f'You rolled a critical dodge!\n')
        if roll == 1:
            print(f'You rolled the lowest dodge, you are in trouble')
            with open(f'{transcript_filename}.txt', "a") as transcript:
                transcript.write('You rolled the lowest dodge, you are in trouble\n')
        with open(f'{transcript_filename}.txt', "a") as transcript:
            transcript.write(f'You rolled a {roll}, dodging {roll} damage from the {npc_type}\n')
        return Userdodge_amount

P1 = Character('Cleric',95, 8, 35,30)
P2 = Character('Sorcerer',90,10,20,25)
P3 = Character('Barbarian',90,13,25,15)
P4 = Character('Warlock',110,7,30,20)
P5 = Character('Monk',105,5,20,15)

def UserPick():
    UserClass = input('\nWhat class do you want to be, Cleric, Sorcerer, Barbarian, Warlock, or Monk? ').lower()
    ClassUndecided = True 
    global User
    while ClassUndecided:
        if UserClass == 'cleric':
            User = P1
            ClassUndecided = False 
        elif UserClass == 'sorcerer':
            User = P2
            ClassUndecided = False
        elif UserClass == 'barbarian':
            User = P3
            ClassUndecided = False
        elif UserClass == 'warlock':
            User = P4
            ClassUndecided = False
        elif UserClass == 'monk':
            User = P5
            ClassUndecided = False
        else:
            UserClass = input('Not a Class. What class do you want to be, Cleric, Sorcerer, Barbarian, Warlock, or Monk? ').lower()

    print(Line(10))
    User.PlayerStat()
    print(Line(10))
    return User

def end_game(User, Bot):
    if User.Health <= 0:
        print("So unslay! You've been slain!")
        with open(f'{transcript_filename}.txt', "a") as transcript:
                transcript.write("So unslay! You've been slain!")
    elif Bot.NPCHealth <= 0:
        print("So slay! You are the slayer!")
        with open(f'{transcript_filename}.txt', "a") as transcript:
                transcript.write("So slay! You are the slayer!")
    elif Bot.NPCHealth <= 0 or User.Health <= 0:
        print("both died")
        with open(f'{transcript_filename}.txt', "a") as transcript:
                transcript.write("both died")

def Turn(User, Bot):
    while User.Health > 0 and Bot.NPCHealth > 0:
        global BotChoice
        global Choice
        global damage_to_bot
        global damage_to_user
        global Userdodge_amount
        global NPCdodge_amount
        UserChoice = True
        damage_to_user = 0  # Initialize damage_to_user here
        damage_to_bot = 0 
        
        while UserChoice:
            Choice = input('Will you attack or dodge? ').lower()
            BotChoice = random.randrange(1, 3)

            if Choice == 'attack':
                if BotChoice == 1:
                    damage_to_user = Bot.NPCDamageMod(User.PlayerType)
                    damage_to_bot = User.PlayerDamageMod(Bot.NPCType)
                    User.Health -= damage_to_user
                    Bot.NPCHealth -= damage_to_bot
                else:
                    print(f'The {Bot.NPCType} dodged!')
                    damage_to_bot = User.PlayerDamageMod(Bot.NPCType)
                    NPCdodge_amount = Bot.NPCDodgeMod(Bot.NPCType)
                    if damage_to_bot > NPCdodge_amount:
                        damage_to_bot -= NPCdodge_amount
                        Bot.NPCHealth -= damage_to_bot
                UserChoice = False
            elif Choice == 'dodge':
                if BotChoice == 1:
                    damage_to_user = Bot.NPCDamageMod(User.PlayerType)
                    NPCdodge_amount = User.PlayerDodgeMod(User.PlayerType)
                    #User.PlayerDodgeMod()
                    if damage_to_user > Userdodge_amount:
                        damage_to_user -= Userdodge_amount
                        User.Health -= damage_to_user
                elif BotChoice == 2:
                    print(f'The {Bot.NPCType} dodged!')
                    print(f'You dealt 0 damage')
                UserChoice = False
            else:
                print(f'Invalid Input. {Choice}.')
        
        if Bot.NPCHealth > 0 and User.Health > 0:
            print(f'Your health: {User.Health}, {Bot.NPCType} health: {Bot.NPCHealth}')
            print(Line(10))
            with open(f'{transcript_filename}.txt', "a") as transcript:
                transcript.write(f'Your health: {User.Health}, {Bot.NPCType} health: {Bot.NPCHealth}\n')
                transcript.write(f'{Line(10)}\n')
        if Bot.NPCHealth >= 0 or User.Health >= 0:
            end_game(User, Bot)

def Gameplay():
    Intro()
    print(Line(10))
    TablePlayer()
    User = UserPick() 
    TableNPC()
    Bot = NPCPick(User)
    Turn(User, Bot)  

Gameplay()
open(f'{transcript_filename}.txt', "r")



# import random

# transcript_filename = "your_transcript_filename"  # Replace with the desired transcript filename

# def DiceRoll(sides):
#     return random.randint(1, sides)

# class Combatant:
#     def __init__(self, char_type, health, attack_modifier, attack_dice, dodge_dice):
#         self.char_type = char_type
#         self.health = health
#         self.attack_modifier = attack_modifier
#         self.attack_dice = attack_dice
#         self.dodge_dice = dodge_dice

#     def stat_display(self, opponent_type):
#         print(f'You are a {self.char_type} that has {self.health} health, {self.dodge_dice} dodge, and {self.attack_dice} attack with a minimum attack of {self.attack_modifier}.')
#         print(f'You are attacking a {opponent_type} that has {self.health} health, {self.dodge_dice} dodge, and {self.attack_dice} attack with a minimum attack of {self.attack_modifier}.')

#     def damage_mod(self, opponent_type):
#         roll = DiceRoll(self.attack_dice)
#         damage = self.attack_modifier + roll
#         print(f'You rolled a {roll}, hitting the {opponent_type} for a total of {damage}')
#         if roll == self.attack_dice:
#             print(f'You rolled a critical damage! Yippee')
#             with open(f'{transcript_filename}.txt', "a") as transcript:
#                 transcript.write(f'You rolled a critical damage! Yippee\n')
#         if roll == 1:
#             print(f'You rolled the lowest damage, oopsie')
#             with open(f'{transcript_filename}.txt', "a") as transcript:
#                 transcript.write(f'You rolled the lowest damage, oopsie\n')
#         with open(f'{transcript_filename}.txt', "a") as transcript:
#             transcript.write(f'You rolled a {roll}, hitting the {opponent_type} for a total of {damage}\n')
#         return damage

#     def dodge_mod(self, opponent_type):
#         roll = DiceRoll(self.dodge_dice)
#         dodge_amount = roll
#         print(f'You rolled a {roll}, dodging {roll} damage from the {opponent_type}')
#         if roll == self.dodge_dice:
#             print(f'You rolled a critical dodge!')
#             with open(f'{transcript_filename}.txt', "a") as transcript:
#                 transcript.write(f'You rolled a critical dodge!\n')
#         if roll == 1:
#             print(f'You rolled the lowest dodge, you are in trouble')
#             with open(f'{transcript_filename}.txt', "a") as transcript:
#                 transcript.write('You rolled the lowest dodge, you are in trouble\n')
#         with open(f'{transcript_filename}.txt', "a") as transcript:
#             transcript.write(f'You rolled a {roll}, dodging {roll} damage from the {opponent_type}\n')
#         return dodge_amount

# # Example instances
# NPC1 = Combatant('Sorcerer', 80, 7, 20, 10)
# NPC2 = Combatant('Wizard', 105, 12, 30, 30)
# NPC3 = Combatant('Ranger', 115, 15, 40, 40)

# P1 = Combatant('Cleric', 95, 8, 35, 30)
# P2 = Combatant('Sorcerer', 90, 10, 20, 25)
# P3 = Combatant('Barbarian', 90, 13, 25, 15)
# P4 = Combatant('Warlock', 110, 7, 30, 20)
# P5 = Combatant('Monk', 105, 5, 20, 15)

# # Displaying stats
# P1.stat_display(NPC1.char_type)
# NPC1.stat_display(P1.char_type)
