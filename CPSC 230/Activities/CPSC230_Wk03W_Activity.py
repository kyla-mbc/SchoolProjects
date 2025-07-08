'''
1.  Using modulo, check whether 1069 is odd or even. Try this on a few different
    numbers. Can you use this idea to write an if-statement that tells the user if 
    their number is odd or even?
'''


userNumber = int(input("Enter a number:"))
if userNumber%2 == 1:
    print ("Your number is an odd number.")
elif userNumber%2 == 0:
    print ("Your number is an even number.")

'''
2.  Ask the user for the radius of a circle. Use the full value of pi stored 
    in the math module to calculate the area and circumference of that circle 
    and display the results.
'''
print ("Enter a number:")
import math 
radius_circle = int(input())

area = (math.pi)*(radius_circle**2)
circumference = int(2)*(math.pi)*(radius_circle)


print ("Area:" , area)
print ("Circumference:" , circumference)


'''
3.  Write some code to tell the user whether or not to water their succulent. 
    You can prompt them with the question "Is the soil wet?". If they say "yes"
    print a statement telling them to leave it alone. If they say "no" print
    a statement telling them to water the plant
'''
answer = input ("Is the soil wet?")
if answer == "yes":
    print ("Do not water plant!!")
else:
    print ("Water your plants!")


'''
4.  You can use the len() function to check the length of a collection type
    (ie numbers of characters in a string, individual items in a set, etc.).
    Ask the user to input a word and store it in the variable my_word. Using 
    len() and an if statement, write some code that checks whether the length 
    of a word is greater than or equal to 10. If it is, print out: 
    "Wow, that is a long word!"
'''
# exampleWord = "test"
# print(len(exampleWord))

my_word = input ("Give me a word:")
print(len(my_word))

if (len(my_word)) >= 10:
    print ("Wow, that is a long word!")




