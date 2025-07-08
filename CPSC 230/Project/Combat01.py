PC01 = {"Player Type":"Warlock", "Health": 90, "Attack":20, "Dodge":40} #compose dictionaries for types of Characters that will be present in the game.
PC02 = {"Player Type":"Ranger", "Health": 70, "Attack":30, "Dodge":60}
npc_difficulties = {
    "Easy": {"Player Type": "Monk", "Health": 80, "Attack": 8, "Dodge": 30}, #Three difficulties for the NPC for users to choose from. 
    "Medium": {"Player Type": "Monk", "Health": 100, "Attack": 10, "Dodge": 50},
    "Hard": {"Player Type": "Monk", "Health": 120, "Attack": 12, "Dodge": 70}
}
print("Welcome to the combat game!") #Introduction of game.
print("First, you will need to choose your character.") #Asks user which character they would like to play by providing options and prints stats of each character.
print("Your choices are:" ) 
print(f"1) {PC01['Player Type']} with an attack of {PC01['Attack']}, dodge of {PC01['Dodge']}, and health of {PC01['Health']}")
print(f"2) {PC02['Player Type']} with an attack of {PC02['Attack']}, dodge of {PC02['Dodge']}, and health of {PC02['Health']}")

while True: #while loop for user to choose through different intensities of the game after they have chosen their character. 
    playerInput = input("Choose your character! Warlock or Ranger: ")
    if playerInput.lower() == "warlock": #does not let the input be case sensitive, so user could input either 'warlock' or 'Warlock' and they would both be valid. 
        PLAYER = PC01 #assign variable "PLAYER" if user chooses Warlock.
        print(f"Hello {playerInput.capitalize()}! Choose your difficulty:") #make input upper first letter
        print("1) Easy")
        print("2) Medium")
        print("3) Challenging")
        while True:
            difficulty_choice = input("Select the difficulty (1/2/3): ") #asks user to choose difficulty. 
            if difficulty_choice in ["1", "2", "3"]:
                chosen_difficulty = list(npc_difficulties.keys())[int(difficulty_choice) - 1]
                NPC = npc_difficulties[chosen_difficulty]
                print(f"You will be going against {NPC['Player Type']} with an attack of {NPC['Attack']}, dodge of {NPC['Dodge']}, and health of {NPC['Health']}. Good luck, you're going to need it. As a reminder, your starting health is {PLAYER['Health']}.")
                break
            else:
                print('Please Pick a Difficulty.') #if user does not choose either options: 1, 2, or 3, they will be prompted to choose a difficulty setting. 
        break
    elif playerInput.lower() == "ranger": #does not let the input be case sensitive, so user could input either 'ranger' or 'Ranger' and they would both be valid. 
        PLAYER = PC01 #assign variable "PLAYER" if user chooses Warlock.
        PLAYER = PC02 #assign variable "PLAYER" if user chooses Ranger. 
        print(f"Hello {playerInput.capitalize()}! Choose your difficulty:") #code is rewritten again this time applying to Ranger as their player instead of Warlock
        print("1) Easy")
        print("2) Medium")
        print("3) Hard")
        while True:
            difficulty_choice = input("Select the difficulty (1/2/3): ")
            if difficulty_choice in ["1", "2", "3"]:
                chosen_difficulty = list(npc_difficulties.keys())[int(difficulty_choice) - 1]
                NPC = npc_difficulties[chosen_difficulty]
                print(f"You will be going against {NPC['Player Type']} with an attack of {NPC['Attack']}, dodge of {NPC['Dodge']}, and health of {NPC['Health']}. Good luck, you're going to need it. As a reminder, your starting health is {PLAYER['Health']}.")
                break
            else:
                print('Please Pick a Difficulty.')
        break
    
import random

while PLAYER['Health'] > 0 and NPC['Health'] > 0: #code will run as long as both the NPC and Player still have remaining health. 
    option = input("Attack or Dodge: ") #asks the user to choose if they would like to Attack or Dodge their opponent. This loop repeats as long as the health of both characters are above 0. 
    if difficulty_choice == "1": #lets the NPC choose only between "Attack" and "Dodge" so it is a 50/50 chance. 
        npc_choice = random.choice(["Attack", "Dodge"])
    elif difficulty_choice == "2": #as difficulty increases, there is a higher chance of the NPC choosing to attack the user. 
        npc_choice = random.choice(["Attack", "Dodge", "Attack"])
    elif difficulty_choice == "3": #as difficulty increases, there is a higher chance of the NPC choosing to attack the user. 
        npc_choice = random.choice(["Attack", "Dodge", "Attack", "Attack"])
    
    if option.lower() == "attack": #if user chooses to attack, the following code will run.
        print("\t You chose to attack.")
        if npc_choice == "Attack": #if the NPC chooses to attack as well, the code below will run and print results. 
            print("\t The Monk attacked you!")
            PLAYER['Health'] -= NPC['Attack'] #if both characters attack, the player's health will decrease by the attack of the NPC.
            NPC['Health'] -= PLAYER['Attack'] #if both characters attack, the NPC's health will decrease by the attack of the Player.
            print(f"\t You did a damage of {PLAYER['Attack']}.") #prints out how much damage was done to the NPC. 
            print(f"\t The Monk caused a damage of {NPC['Attack']}, watch out next time.") #Prints out how much damage was done to the user's character. 
        else:
            print("\t The Monk dodged!") #if the NPC chooses to dodge, while the user attacks, the code below will run. 
            damage = int(NPC['Dodge']/100 * PLAYER['Attack']) #The damage done will be calculated by a dodge modifier. 
            NPC['Health'] -= damage #The health of the NPC would still be affected if they dodged, but it would not be the user's full amount of Attack, it would only be a percentage of it. 
            print(f"\t You did a damage of {damage}. Great job!") #prints how much damage the user did to the health of the NPC. 
            print("\t You dealt with 0 damage.") #prints that user did not receive any damage to their health since they attacked and the NPC dodged. 
        print(f"\t Your health is {PLAYER['Health']} and your opponent's health is {NPC['Health']}.")
    elif option.lower() == "dodge":
        print("\t You chose to dodge.") #if the user chooses to dodge, the code below will run.
        if npc_choice == "Attack": #if the NPC chooses to dodge, the below code will run and print results. 
            print("\t The Monk attacked you!") 
            damage = int(PLAYER['Dodge']/100 * NPC['Attack']) #The damage done will be calculated by a dodge modifier. 
            PLAYER['Health'] -= damage #The health of the Player would still be affected if they dodged, but it would not be the NPC's full amount of Attack, it would only be a percentage of it. 
            print(f"\t The Monk did {damage} damage to you.") #prints how much damage the NPC did. 
            print("\t The Monk dealt no damage.") #prints how much damage the NPC dealt. 
        else: #if both characters dodged, the code below will run.
            print("\t The Monk dodged! They dealt 0 damage.") 
            print("\t You dealt 0 damage.")  
        print(f"\t Your health is {PLAYER['Health']} and your opponent's health is {NPC['Health']}.")   
    
if PLAYER['Health'] <= 0: #if player's health goes to or below 0, the code will print that they were defeated by the Monk.
    print("You were defeated by the Monk!")
elif PLAYER['Health'] <= 0 and NPC['Health'] <= 0: #If both the player and the NPC's health go to 0 or below on the same round, the code will print that the game ended in a draw. 
    print("This duel has ended in a draw.")
else:
    print("You have defeated the Monk!") #The game will print the player defeated the monk if both options above are not true. 
