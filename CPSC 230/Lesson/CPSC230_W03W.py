
'''Basic if-statement'''
thisNumber = 10

if thisNumber == 13: #use a colon to end your boolean statement. 
    print("That's my lucky number")
    print ("hi")
    newNumber = thisNumber*100 
#the above code will only run if thisNumber is 13, if not, none of the indented statements will run. 

print("Nice work!")

'''if-statements with user input'''
userGuess = int(input("Pick a number between 1-7 "))
if userGuess == 7:
    print("You got it!")
else:
    print ("Not Quite")

print("Thanks for Playing!")

'''else'''
weather = input("What is the weather? ")

if weather == "sunny":
    print("What a Sunny Day!")
else:
    print("It could be nicer.")


'''elif'''
# x = int(input("How many fish do you have? "))

# if x == 4:
#     print("Wow, me too!")
# elif x == 10:
#     print("Wow, cool!")
# elif x == 20:
#     print("That's so many!")

# print("Have a nice day!")


# userNumber = int(input("Enter a number: "))

# if userNumber%2 == 1:
#     print("Your number is odd")
# elif userNumber%2 == 0:
#     print("Your number is even")

# print("You're Welcome!")

'''and/or'''
thisNumber = 13
# if thisNumber < 15 and thisNumber < 12:
#     print("true")

# if thisNumber < 15 or thisNumber < 12:
#     print("true")

# weather = input("What is the weather? ")

# if weather == "sunny" or weather == "Sunny" or weather == "sonny":
#     print("What a Sunny Day!")
# else:
#     print("It could be nicer.")

# '''if statement shortcut'''
# weather = "sunny"

# if weather == "sunny":
#     print("What a nice Day!")
# else:
#     print("It could be nicer.")

# print("What a nice day!") if weather == "sunny" else print("It could be nicer")