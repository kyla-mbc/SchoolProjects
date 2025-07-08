'''FOR LOOP REVIEW'''

# numbers = [1,2,3,4,5,6]
# for i in numbers[::-1]:
#     print(i)
#     print("Hello your number is :" + str(i))


'''range()'''

# for i in range(1,7):
#     print("Easier with range: " , str(i))

'''Example: Evens'''

# for i in range(0,10):
#     if i%2 == 0:
#         print("EVEN")
#     else:
#         print("ODD")


'''STRINGS REVIEW 
    ... plus error handling'''

'''comparison'''
# print("hello" == "hello")
# print("hello" == "Hello")

'''methods'''
# userString = input("Enter a string")
# newString = userString.lower()

# print(newString)


### upper and lower ###
userInput = input("Please say 'Hello': ")

# print(userInput)
# print(userInput.upper())
# print(userInput.lower())

# if userInput == "hello" or userInput == "Hello":
#     print("Well hello to you too!")
# else:
#     print("... rude")

# newInput = userInput.lower()
# print (newInput)

# if newInput == "hello":
#     print("Well hello to you too!")
# else:
#     print("... rude")

### isdigit ###

userNum = int(input("Please enter a number 0-100: "))

### instead try.... ###
# userNum = input("Please enter an integer 0-100: ")

# while not userNum.isdigit():
#     print("that is not an integer, silly!")
#     userNum = input("Please enter a number 0-100: ")

# print(int(userNum) * 100)

### strip ###
# userNum = userNum.strip()

# while userNum.isdigit() == False or int(userNum) > 100:
#     print("that is not an integer from 0-100")
#     userNum = input("Please enter a number 0-100: ")

# print(int(userNum) * 100)