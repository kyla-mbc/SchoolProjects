'''CPSC230 - Week 03 Monday'''

''' Basic Indexing '''
# myStr = "Hello"
# print(myStr[0])

myDog_dict = {"Name": "Rex", "Age" : 4}
# print(myDog_dict["Name"] + " is " + str(myDog_dict["Age"]))

print("My dog's name is " + myDog_dict["Name"] + " and they are " + str(myDog_dict["Age"]) + " years old")

myDog_list = ["Rex", 4]
print(myDog_list[0] + " is " + str(myDog_list[1]))

''' Logical Operators '''
# print(1 == 1)

# print(1 == 6)

# print(9 != (6/2))
# print(3 > 3)

''' Int Operators '''
# print(1 + 3)
# print(2 * 8)
# print(10/3)
# print(10//3)
# print(100//6)
# print(100%6)
# print(10%2)
# print(2**3)

''' Floats and Ints '''
# print(1.0 + 2)
# print(10/3)

''' Presidence - Order of Operations '''

#print(2 + 3 * 5 ** 2)
# print(2 + (3 * (5 ** 2)))

# print(1 + 2 + 4 * 6 + 7**2)

# print(1 + 2 + (4 * 6) + (7**2))

# print(6//2 * 4**2 + 1)

''' Shortcuts '''
a = 1
print(a)
a = a + 1 #a +=1 is an alternative way to write this 
print(a)


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