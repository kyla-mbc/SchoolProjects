'''WHILE LOOP REVIEW'''
####################################################
## NOTE:  This was covered before the midterm     ##
####################################################
'''sentinel loop'''

'''Example 01'''
# pw_not_found = True     ## sentinel value

# pw = input("Please set a new password: ")

# while pw_not_found:
#     if pw != "OldPassword123" and len(pw) > 8:
#         pw_not_found = False
#     else:
#         print("That's a bad pw.")
#         pw = input("Please set a new password: ")
# print("Password Set!")

'''Break'''
s = 'Fish are friends, not food.'
i = 0
  
# while True:
#     # break the loop as soon it sees a space (" ")
#     if s[i] == ' ':
#         break
#     print(s[i])
#     i += 1
# print("Done!", i)

'''Continue'''
# number = int(input("Give me a number:"))
# while number > 0:
#     number -= 1
#     if number % 2 == 0:
#         continue
#     print ("This number is even.")

'''STRINGS'''

'''string creation'''

s1 = 'Hello'
s2 = "Hello"
s3 = '''Hello'''

# print(s1, s2, s3)

'''whitespace'''

# newLines = "Hey \nHi \nHello \n ..."
# print(newLines)

# tabs = "Big\tStretch"
# print(tabs)

'''strings as collections'''

my_string = "Fish are friends, not food!"

# print(my_string)
# print(my_string[0:4])
# print(my_string[10])

'''slicing'''
# print(my_string[0:5])

print(my_string[12:])

# print(my_string[::2])

# newString = my_string[0:4]
# print(newString)

# print(my_string[::-2])

'''operations'''
### add ###
# print(1 + 1)

# print('1' + '1')

# ## multiply ###

# print(1 * 10)

# print('1' * 10)


'''in'''
species = "clownfish"
# print("fsh" in species)

name = "Cassandra"

# print('a' in name)
# print("j" in name)
# print('c' in name)

# print("Cass" not in name)

'''immutability'''
myString = "Best Fishes!"
# print(myString)

myBrokenString = "Test Fishes!"

# myBrokenString[0] = "B"
# print(myBrokenString)

########################################################################
## NOTE:  Everything above this line was covered before the midterm   ##
##                                                                    ##
##        Everything after this is new                                ##
########################################################################

'''comparison'''
# print("hello" == "hello")
# print("help" == "hello")

# print("applet" > "apple")

# print("Mac" > "Mary")

# print("apple" < "burrito")

# print("a" > "A")

'''methods'''
greeting = "Hello"
# print(greeting.upper())

### upper and lower ###
# user_input = input("Please type a phrase: ")

# print(user_input)
# print(user_input.upper())
# print(user_input.lower())

### isdigit ###

# user_input_number = int(input("Please enter a number 0-100: "))

### instead try.... ###
# user_input_number = input("Please enter a number 0-100: ")

# while not user_input_number.isdigit():
#     print("that is not a number, silly!")
#     user_input_number = input("Please enter a number 0-100: ")

# user_input_number = int(user_input_number)

### shout ###
### isupper ###
# shout = input("Please shout something: ")

# if not shout.isupper():
#     print("I SAID SHOUT!")

### replace ###

pythonQuote = '''
Mob: “She's a witch!”
Bedevere: “What makes you think she is a witch?”
Peasant: “She turned me into a newt.”
Bedevere: “A newt?”
Peasant: “Well I got better.”
'''
# print(pythonQuote)
newCritter = pythonQuote.lower().replace("newt", "fish").replace("witch", "ichthyologist")
# print(newCritter)

### startswith ###
# name = input("Please enter 'My name is' and then your name in French: ")

# if name.lower().startswith("je m'appelle"):
#     print("GREAT!")

## strip ###
# id_num = input("please enter your chapman id number: ")

# id_num = id_num.strip()
# print(id_num)

### .split() ###
sentence = "The quick brown fox jumps over the lazy dog"
# print(sentence.split())

my_variable_name = "This variable name is so long"
print(my_variable_name.split(" "))

### checking for substrings ###
# myList = ["This is a string", "This is also a string", "This string is longer than the others"]

# for i in myList:
#     if "also" in i:
#         print("Cool!")
#     else:
#         print(i)

var =  "fish2005"
print (var.isalpha())