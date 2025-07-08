
'''
1.  Ask the user to guess how many pets you have. Print a statement 
    telling them how close they are. (i.e. "Your guess is 5 away from
    the correct answer"). No if-statements needed. Just a single print
    statement with the results of your calculation
'''
import math
Pets = 3
Guess = int(input("How many pets do I have?"))
Difference = math.fabs(Guess - Pets)
print ("Your guess is" , Difference , "away from the correct answer.")


'''
2.  Write some code that asks the user for 5 different numbers, and stores
    them in the variables x1, x2, x3, x4, and x5. Use a set to create a
    unique set of numbers entered (e.g. if they enter 5 twice, only count 
    it once.) Print out the set.
'''
x1 = int(input("Give me a number!"))
x2 = int(input("Give me a number!"))
x3 = int(input("Give me a number!"))
x4 = int(input("Give me a number!"))
x5 = int(input("Give me a number!"))

myList = [x1, x2, x3, x4, x5]
myNewList = list(set(myList))

print ("Set:" , myNewList)

'''
3.  Create three dictionaries storing the title, artist, and value of three 
    paintings in an art gallary of your choosing. Print out a string listing
    the title, artist, and value of your favorite of the paintings (use the 
    items in the dictionary not a new string) (no if-statement needed, just
    regular dictionary indexing)
'''
# ## There are two different ways to make a dictionary. Both are indexed in the same way ##
# ### 1) Curly Brackets
# myDog = {"Name": "Rex", "Age" : 4}
# print(myDog["Name"])

# ### 2)  dict() constructor
# myDog2 = dict(Name = "Rover", Age = 3)
# print(myDog2["Name"])

paint1 = dict(Title = "Starry Night", Artist = "Vincent van Gogh", Value = "Plenty Money")
print (paint1["Title"], "is a painting by", paint1 ["Artist"], "which cost is", paint1 ["Value"])

paint2 = dict (Title = "Mona Lisa", Artist = "Margo Burbank", Value = "Priceless")
print (paint2["Title"], "is a painting by", paint2 ["Artist"], "which cost is", paint2 ["Value"])

paint3 = dict(Tite = "self_portrait", Artist = "Lance Nguyen" , Value ="$50")
print (paint3["Title"], "is a painting by", paint3 ["Artist"], "which cost is", paint3 ["Value"])


'''
4.  Write some code that asks the user to name the first woman to win a
    Nobel prize (just last name is fine). Write an if-statement that 
    tells the user if they got the answer right. BONUS: Have your code
    tell them they got the right answer even if they forget to capitalize
    the name
'''



'''
5.  You are swimming in a pool and want to increase the length of the laps you
    are taking, so you start swimming diagonally from corner to corner. You know
    the length (35 ft) and width (20ft) of the pool, but not the length of the 
    diaganoal. Using the Pythagorean theoum (and the math module) write some code 
    that asks the user for the number of laps they took across the diagonal of
    the pool and display the total distance they swam.
'''

# your code here

'''
6.  BONUS: Using your operators (%,/,//,*), write some code to convert time in 
    minutes (e.g. 257) to hours and minutes (e.g. 4 hours and 17 minutes).
    Print out the numbers of hours/minutes in the form "X hours, Y minutes".
        Try it with multiple values:
            - 12,938 (answer: 215 hours, 38 minutes)
            - 55 (answer: 0 hours, 55 minutes)
            - 525,600 (answer: 8760 hours, 0 minutes )
            - 432 (answer: 7 hours, 12 minutes)
'''

# your code here


