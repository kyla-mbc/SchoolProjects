'''Indexing Collections'''
myStr = "Hello Buddy"
print(myStr[0])

myDog_dict = {"Name": "Rex", "Age" : 4, "Breed" : ["Corgi", "Lab", "Pitbull"]}
# print(myDog_dict["Name"], " is ", myDog_dict["Age"])

# myDog_list = ["Rex", 4, ["Corgi", "Lab", "Pitbull"]]
# print(myDog_list[0] + " is " + str(myDog_list[1]))

'''NOTE: Sets are unorded and are therefore not indexable'''
dataScientist = {'Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'}
dataEngineer = {'Python', 'Java', 'Scala', 'Git', 'SQL', 'Hadoop'}

# print(dataScientist)
# print(dataEngineer)

### Using sets to remove duplicates
myList = [1,2,3,4,2,1,4,4]
myNewList = list(set(myList))

# print(myList)
# print(myNewList)

'''Reminder: Operators'''

'''Logical Operators'''
# print(1 == 1)

# print(1 == 6)

# print(9 != (6/2))
# print(3 > 3)

'''int Operators'''
# print(1 + 3)
#
# print(2 * 8)

# print(10/3)
# print(10//3)

# print(100//6)
# print(100%6)

# print(10%2)

# print(2**3)

'''floats and ints'''
# print(1.0 + 2)
# print(10/3)

'''Reminder: precedence'''

# print(2 + 3 * 5 ** 2)
# print(2 + (3 * (5 ** 2)))

# print(1 + 2 + 4 * 6 + 7**2)

# print(1 + 2 + (4 * 6) + (7**2))

# print(6//2 * 4**2 + 1)

'''Reminder: shortcuts'''
# userNumber = int(input("What is your total $"))

# if userNumber >= 10:
#     userNumber -= 5
#     print("Wow, you spent $10 or more and earned 5 points!")
#     print("Your new total is $", userNumber)
# else:
#     print("Thank you, have a great day!")

# a = 1
# print(a)
# a = a + 1
# print(a)

# a = 1
# # print(a)
# a += 1
# print(a)

# a = 1
# print(a)
# a += a
# print(a)
# a += a
# # a = a + a
# print(a)
