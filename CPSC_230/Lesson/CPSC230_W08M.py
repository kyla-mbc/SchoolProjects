'''Basic Functions'''
# def printFish(species):
#     print("Wow", species, "is really cool!")

# printFish("Clown Fish")

'''Multiple Inputs and Returning Items'''
# def helloWorld(name, userNumber):
#     mathStuff = userNumber*5
#     print("Hello", name)
#     print("Your number x 5 is" + str(mathStuff))
#     return name

# myName = helloWorld("Cassandra", 5)
# print("The user's name is", myName)

# helloWorld("Monty", 10)
# helloWorld("Python", 55)
# helloWorld("Grail", 1)
# printFish("Garden Eel")
# printFish("White Shark")
# printFish("Gold Fish")

'''Variable Returns'''
# def greaterThan10(n):
#     if n > 10:
#         return(True)
#     else:
#         return(False)

# gt = greaterThan10(5)
# print(gt)

'''Functions to simplify code'''
def square(n):
    n = n*100
    n = n/42
    return(n*n)

# tenSquare = square(10)
# print(tenSquare)

# for i in range(1,10):
#     print(square(i))

# print(newNumber)
# print(newNumber+50)

'''split (reminder)'''
# fullName = input("What is your first and last name? ")
# print(fullName)
# names = fullName.split()
# print(names)
# print(names[1], ",", names[0])

'''more functions'''
# def namePrinter(name):
#     names = name.split()
#     print(names[1] + ", " + names[0])

# namePrinter(fullName)

# namePrinter("Cassandra Donatelli")


'''name spaces'''
x = 5

# def addOne(n):
#     x = n + 1
#     print("X is", x)

# addOne(x)
# print("X is", x)

# x = addOne(x)
# print(x)
# print("X is", x)
# addOne(x)
# print("X is", x)

'''add a return'''

x = 5

# def addOne(n):
#     x = n + 1
#     print("X is", x)
#     return(x)

# print("X is", x)
# addOne(x)
# print("X is", x)


'''
Make a function adventure_mess() that prints the stats of a character
'''

PC1 = dict(type = "Barbarian", health = 100, attack = 10, dodge = 0.9)
PC2 = dict(type = "Rogue", health = 60, attack = 20, dodge = 0.1)
PC3 = dict(type = "Wizard", health = 80, attack = 20, dodge = 0.8)

# print("Welcome to the combat game!")
# print("First, you will need to choose your character.")
# print("Your choices are 1) ", PC1["type"], "with an attack of ", PC1["attack"], " dodge of ", PC1["dodge"], "and health of ", PC1["health"])
# print("or 2) ", PC2["type"], "with an attack of ", PC2["attack"], " dodge of ", PC2["dodge"], "and health of ", PC2["health"])
# print("or 3) ", PC3["type"], "with an attack of ", PC3["attack"], " dodge of ", PC3["dodge"], "and health of ", PC3["health"])


def statsPrinter(statBlock, num):
     print(num,":", statBlock["type"], "with an attack of ", statBlock["attack"], " dodge of ", statBlock["dodge"], "and health of ", statBlock["health"])

players = [PC1, PC2, PC3]
print("Welcome to the combat game!")
print("First, you will need to choose your character.")
print("Your choices are ...")
for i in range(0, len(players)):
    statsPrinter(players[i], i+1)