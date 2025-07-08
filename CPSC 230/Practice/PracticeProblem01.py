# # CPSC230 - Practice Problems 01

# # Question 1
# num01 = 1+1
# print(type(num01))

# num02 = 10/5
# print(type(num02))

# num03 = 10//5
# print(type(num03))

# num04 = 1 * 2.0
# print (type(num04))

# num05 = 10%8
# print (type(num05))

# #Question 2
# userAnswer = int(input ("How Many Classes are you taking?"))

# if userAnswer > 0 and userAnswer <= 3:
#     print("That sounds pretty manageable.")
# elif userAnswer == 4:
#     print("Cool, me too!")
# elif userAnswer >= 5:
#     print ("Wow, you must be busy!")



# #Question 03
# bestGame = {"title":"Monopoly" , "main_character":"steamboat" , "platform":"mobile phone"}

# if len(bestGame["title"]) >= 10:
#     print ("Wow! That's a long name!")
# else: 
#     print ("Cool, sounds fun!")


# #Question 03
# # bestGame = {"title":"Monopoly" , "main_character":"steamboat" , "platform":"mobile phone"}

# # bestGame = str(input())

# # if len(bestGame("What is your favorite board game?")) >= 10:
# #     print ("Wow! That's a long name!")
# # else: 
# #     print ("Cool, sounds fun!")


# # names = {"boy":"manny" , "girl":"kyla"}
# # print (names["boy"])
# # print (type(names))                                                          

# # a = "crossword"
# # b = "wordsearch"

# # print (a[2])

'''
1.  Guessing Game. Remember when we asked the user to guess a number and used 
    booleans to tell them if they were correct (see Wk02F_Activity)? Let's 
    make our game more interactive! 

    - First, create a number that will be the answer (answer = 7)
    - Second, create a counter variable to represent userAnswer (userAnswer = 0)
    - Then, create a while loop that repeatedly asks the user to guess a
      number between 1-10. The loop should only stop when userAnswer == answer
    - Congratulate the user when the loop ends (ie when they guess correctly)
'''
import random
answer = 8
userAnswer = int(input("Give me a number:"))
guess_count = 0
guess_limit = 5

if userAnswer == answer:
    print ("That is the right answer!")
while userAnswer != answer and guess_count <= guess_limit:
   userAnswer = int(input("give me a number:"))
   guess_count += 1

if guess_count > guess_limit: 
    print ("Better luck nect time")
else:
    print ("Congratulations, you guessed my number in" , str(guess_count), "tries")