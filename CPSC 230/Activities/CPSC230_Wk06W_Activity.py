# '''
# 1.  Write a while loop asking students to enter the names of the classes
#     they are taking this semester. They should be able to enter DONE when
#     they have no classes to list. Each time they enter a class, print out
#     "Wow, [Class Name], sounds fun!". If the class contains the word 
#     "computer" (like CPSC 230: Computer Science 1) use string methods to 
#     change the text to be entirely upper-case. (you can also modify to 
#     highlight your own favorite topic other than "computer")
# '''
# classname=input("Enter the name of your class, type 'DONE' when all classes listed:")

# while classname != "DONE":
#     if "computer" in classname:
#         print ("Wow," ,classname.upper(), "sounds fun!")
#         classname=input("Enter the name of your class, type 'DONE' when all classes listed:")
#     else: 
#         print ("Wow," , classname , "sounds fun!")
#         classname=input("Enter the name of your class, type 'DONE' when all classes listed:")
    
# '''
# 2.  Ask the user to enter a number greater than 100 [userNum]. Include
#     error handling in a while loop so that your script keeps asking 
#     until the user enters an integer (using .isdigit()).
    
#     Using another while loop and modulo, calculate the sum of all the 
#     even numbers between 1 and [userNum]. Print out the sum.
    
#     HINT: Look at the code you wrote using modulo (%) to determine if 
#         a number was odd or even. (and look at the example code from 
#         lecture today)
# '''

# while True:
#     userNum = input("Give me a number greater than 100:")
#     if userNum.isdigit() == False:
#         print ("That isn't a number silly goose.")
#     elif userNum.isdigit() == True:
#         break

# while userNum > 100: 
#     range = [1,userNum]
#     for userNum in range:
#         if userNum % 2 == 1:
#             userNum += userNum

result = 0
userNum = 100
for i in range(1, userNum + 1):
    if i % 2 == 0:
        result += i
print(result)

# while userNum.isdigit() == True: 
#     userNum = [1,userNum]
    




# # '''
# # 3.  Update this piece of code to meet the following paramaters: 
# #         - Ask the user to enter their own string
# #         - Use string methods to change the user's string so it only 
# #           contains lowercase letters and has no spaces at the start or end
# #         - Pick your own "favorite word" to highlight (mine is "Fish" in 
# #           the example below)
# # '''
# # # i = 0
# # # word = "gdgdhkkrfzdhxghcbnxfxg"
# # # while i < len(word):
# # #     print(word[i])
# # #     if word[i] == "f":
# # #         print("Fish starts with the letter F!")
# # #         break
# # #     else:
# # #         i += 1

# # i = 0 
# word = str(input("Give me a word:"))
# word = (word.lower())
# while i < len(word):
#     print(word[i])
#     if word[i] == "P":
#         print("Pizza starts with the letter P!")
#         break
#     else:
#         i += 1