'''sentinel loop'''

'''Example 01'''
# pw_not_found = True     ## sentinel value

# pw = input("Please set a new password: ")

# while pw_not_found:
#     if pw != "OldPassword123" and len(pw) > 10:
#         pw_not_found = False
#     else:
#         print("That's a bad pw.")
#         pw = input("Please set a new password: ")

'''Example 02'''
# sum = 0
# data = int(input("How long was your commute today? (enter 0 to end) "))    ## sentinel value
# while data != 0:
#     sum = sum + data
#     data = int(input("How long was your commute today? (enter 0 to end) "))
# print("You drove for:",sum,"minutes this week")


'''Example 03'''
# endString = "DONE"    ## sentinel value
# faves = []
# prompt = "What is one of your favorite things? Enter '" + endString + "' to stop: "
# newFave = input(prompt)
 
# while newFave != endString:
#     faves.append(newFave)   ## note the "append" function. We will learn about this next week.
#     newFave = input(prompt)

# print("These are a few of your favorite things: ", faves)

# '''Break'''
  
# s = 'Fish are friends, not food.'
# i = 0
  
# while True:
#     # break the loop as soon it sees a space (" ")
#     if s[i] == ' ':
#         break
#     print(s[i])
#     i += 1
# print("Out of while loop", i)

'''Continue'''

# numbers = 5                  
# while numbers > 0:              
#    numbers -= 1
#    if numbers%2 == 1:
#       continue
#    print('This number is even :', numbers)
# print("Good bye!")