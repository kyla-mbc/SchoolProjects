'''Basic Functions'''
def printFish(species):
    print("Wow", species, "is really cool!")

# printFish("Clown Fish")

'''Namespaces'''
# x = 5

# def addOne(n):
#     x = n + 1
#     print("X is", x)
#     return(x)

# x = addOne(x)
# print(x)

## add a return


'''Multiple Inputs and Returning Items'''
# def helloWorld(name, userNumber):
#     mathStuff = userNumber*5
#     print("Hello", name)
#     print("Your number x 5 is" + str(mathStuff))
#     return name

# myName = helloWorld("Cassandra", 5)
# print("The user's name is", myName)


'''Functions to simplify code (with modules)'''
# def rootSquare(n):
#     import math
#     square = n**2
#     root = math.sqrt(n)
#     return[square, root]

# tenSquare = rootSquare(10)
# print(tenSquare)

# for i in range(1,10):
#     print(square(i))


'''split (reminder)'''
# fullName = input("What is your first and last name? ")
# print(fullName)
# names = fullName.split()
# print(names)
# print(names[1], ",", names[0])

'''Name Printer'''
# def namePrinter(name):
#     names = name.split()
#     print(names[1] + ", " + names[0])

# namePrinter(fullName)

# namePrinter("Cassandra Donatelli")


'''Default Arguments'''

# def aquariumTasks(task = "Feed Fish"):
#     print("Today your task is to " + task + ". Thank You!")

# aquariumTasks()

# aquariumTasks()
# aquariumTasks("Change Water")
# aquariumTasks(task = "Check pH") # <- Named argument

'''Named Arguments 01'''
def boxVolume(length, width, height, units):
    volume = length*width*height
    print("The volume of your box is", volume, units)
    return(volume)

###NOTE: add default arguments

# boxVolume(1,2,3,"cubic inches")

# boxVolume(height = 10, length = 5, units = "cubic meters", width = 3)
# boxVolume(1,2,3)
# boxVolume(length = 1, width = 2, height = 3)
# boxVolume(10,60,100)




'''Function Practice - Opponent Action'''

# def opponentAction(number):
#     if number == 1:
#         return("Normal Attack")
#     elif number == 2:
#         return("Special Attack")
#     elif number == 3:
#         return("Dodge")
#     elif number == 4:
#         return("Heal")
#     else:
#         return("Move")

# import random
# randNum = random.randint(1,5)   
# action = opponentAction(randNum)
# print("Your opponent chose", action)


'''Function Practice - Health Math'''

# NPC = dict(Health = 100, Dodge = 0.5, Attack = 10)
# PC = dict(Health = 100, Dodge = 0.75, Attack = 15)

# def healthMath(NPCHealth, NPCAction, NPCDodge, PCAction, PCAttack):
#     if NPCAction == "Attack":
#         if PCAction == "Attack":
#             NPCHealth = NPCHealth-PCAttack
#     elif NPCAction == "Dodge":
#         if PCAction == "Attack":
#             NPCHealth = NPCHealth-(PCAttack*NPCDodge)
#     else:
#         print("Error, invalid inputs")
    
#     return(NPCHealth)

# print(healthMath(NPC["Health"], "Attack", NPC["Dodge"], "Attack", PC["Attack"]))
# print(healthMath(NPC["Health"], "Dodge", NPC["Dodge"], "Attack", PC["Attack"]))
# print(healthMath(NPC["Health"], "Attack", NPC["Dodge"], "Dodge", PC["Attack"]))
# print(healthMath(NPC["Health"], "Dodge", NPC["Dodge"], "Dodge", PC["Attack"]))