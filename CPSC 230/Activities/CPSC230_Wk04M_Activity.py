'''
1.  Use this space to test out your answers for the quiz. Use 
    comments to make notes about how you answered the question 
    and/or what concepts you would like to focus on in preparation 
    for the midterm.
'''

# Question 1
num01 = 1+1
print(type(num01))

num02 = 10/5
print(type(num02))

num03 = 10//5
print(type(num03))

num04 = 1 * 2.0
print (type(num04))

num05 = 10%8
print (type(num05))

#Question 2
userAnswer = int(input ("How Many Classes are you taking?"))

if userAnswer > 0 and userAnswer <= 3:
    print("That sounds pretty manageable.")
elif userAnswer == 4:
    print("Cool, me too!")
elif userAnswer >= 5:
    print ("Wow, you must be busy!")

#Question 03
bestGame = {"title":"Monopoly" , "main_character":"steamboat" , "platform":"mobile phone"}

if len(bestGame["title"]) >= 10:
    print ("Wow, that's a long name!")
else:
    print ("Cool, sounds fun!")


''' 
2.  Emojis. Use pip install to install the emojis library.
        To install: pip install emojis

    Use it to print a short story in the terminal where every
    noun is replaced by an emoji.
        https://www.webfx.com/tools/emoji-cheat-sheet/

    If you are having issues with pip, you may need to reinstall
    follow instructions here: https://realpython.com/what-is-pip/
'''

# import emojis
# emojified = emojis.encode("There is a :snake: in my boot !")
# print(emojified)


'''
3.  Find, install, and use one other library of your choosing.
    You can just google "interesting libraries in python"

    NOTE: It is normal to have issues installing libraries. Python
    is open-source, so sometimes working with less commonly used 
    libraries is a pain. It's not you! Google is your friend here. 
'''