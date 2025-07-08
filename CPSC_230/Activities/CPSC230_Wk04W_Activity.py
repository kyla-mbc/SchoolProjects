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

answer = 8
userAnswer = int(input("Guess a number between 1-10?"))

if userAnswer == 8:
    print ("That is the correct answer!")
while userAnswer != answer:
    userAnswer = int(input("Guess a number between 1-10?"))

print ("Congratulations! You guessed my number!")


'''
2.  Modify your code above to keep track of how many guesses it takes the 
    user to get teh correct answer. Be sure to display their guess count
    when they finally get it right!
'''


answer = 8
userAnswer = int(input("Guess a number between 1-10?"))
numGuess = 1

if userAnswer == 8:
    print ("That is the correct answer!")
while userAnswer != answer:
    userAnswer = int(input("Guess a number between 1-10?"))
    numGuess += 1

print ("Congratulations! You guessed my number! It took", str(numGuess), "tries" )


'''
3.  Modify your code again so that you can play the game yourself! This 
    will require you to use the randint() function in the random module:
    https://docs.python.org/3/library/random.html#module-random
'''
import random 

answer = random.randint(1,10)
userAnswer = int(input("Guess a number between 1-10?"))
numGuess = 1

if userAnswer == answer:
    print ("That is the correct answer!")
while userAnswer != answer:
    userAnswer = int(input("Guess a number between 1-10?"))
    numGuess += 1

print ("Congratulations! You guessed my number! It took", str(numGuess), "tries" )

'''
4.  Modify your code one last time. This time, use and/or statements to
    limit the number of guesses the user has to 5. If the user does not
    guess correctly after 5, tell them "Sorry, better luck next time!" 
    If the user does guess correctly, tell them "Nice work! You guessed
    the rignt number in X tries!" (where X is the number of guesses)
'''
import random 

answer = random.randint(1,10)
userAnswer = int(input("Guess a number between 1-10?"))
guess_limit = 5
numGuess = 1

if userAnswer == answer:
    print ("That is the correct answer!")
while userAnswer != answer and numGuess < guess_limit:
    userAnswer = int(input("Guess a number between 1-10?"))
    numGuess += 1

if numGuess > guess_limit:
    print ("Sorry, better luck nect time!")
else:
    print("Congratulations! You guessed my number! It took", str(numGuess), "tries" )
