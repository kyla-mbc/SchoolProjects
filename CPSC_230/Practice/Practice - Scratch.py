# # # wage = 60 
# # # hours = 40
# # # weeks = 52 
# # # salary = wage*hours*weeks 

# # # print ("Your salary is", salary)

# # #float example 

# # # float ('42')
# # # print (float)


# # # #same row texts 
# # # # print ('Halt!' ,end='')
# # # # print ("No Access!")

# # # x= True 
# # # print (type(x))

# # # import antigravity 



# # # answer = 8
# # # userAnswer = 0

# # # if userAnswer == 8:
# # #     print ("That is the correct answer!")
# # # while userAnswer !=8:
# # #     print ("Guess again!")
# # #     userAnswer += 1
# # #     print ("Adding 1. X is now:", userAnswer)

# # # petDog = {"Breed":"Pitbull", "Age": 4, "Name":"Brie"}
# # # if len(petDog["Name"])==(petDog["Age"]) :
# # #     print ("Cool, what a coincidence!")
# # # else:
# # #     print ("That's a cute name!")

# # # pet01 = ["Yellow Lab", 4, "M"]
# # # pet02 = ["German Shepard" , 2, "F"]
# # # pet03 = ["Corgi", 5, "M"]

# # # print ("Hello! The dog's breed is" + (pet03[0]) + "and their age is" + str(pet03[1]))

# # # myDog_list = ["Rex", 4, ["Corgi", "Lab", "Pitbull"]]
# # # print(myDog_list[0] + " is " + str(myDog_list[1]))

# # # dogAge = 3
# # # dogYears = dogAge * 3
# # # print (dogYears)

# # # age = int(input("What is your age?"))
# # # print(age)

# # # number = 5 <= 2
# # # print (type(number))

# # # my_str = "ABCDEFG"
# # # # x = 10
# # # # print(my_str + str(x))
# # # # my_str = list(my_str)
# # # print(my_str[:])

# # # species = "clownfish"
# # # print ("o" not in species)

# # # pw_not_found = True
# # # pw = input("Please set a new password:")

# # # while pw_not_found: 
# # #     if pw != "ThisIsMyOldPassword123" and len(pw) > 10:
# # #         pw_not_found = False
# # #     else:
# # #         print ("That is a bad password.")
# # #         pw = input("Please set a new password:")
        
# # # Total = 0
# # # x = 1 

# # # while x <= 5: 
# # #     Total += x
# # #     x += 1

# # # print (Total)

# # curr_power = 2
# # user_char = 'y'

# # while user_char == 'y':
# #     print (curr_power)
# #     curr_power = curr_power * 2
# #     user_char = input ()

# # print ('Done')

# def get_minutes_as_hours(orig_minutes):
#     hours = orig_minutes/60.0
#     return hours

# orig_minutes = float(input())
# print(get_minutes_as_hours(orig_minutes))

# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)s

# my_string = "Hello, World!"
# result = my_string[::-2]
# print(result)

# x = 10  # Global variable

# def my_function():
#     y = 20  # Local variable
#     print(x)  # Accessing the global variable 'x'
#     print(y)  # Accessing the local variable 'y'

# my_function()
# print(x)  # Accessing the global variable 'x' again
# # print(y)  # This would result in a NameError because 'y' is not accessible outside the function

# def myFun(*hello):
#     for arg in hello:
#         print(arg)

# myFun('Hello', 'Welcome', 'to', 'Python')
# print(" ")

#def functions 

# def word_lengths(word_list):
#     for each_word in word_list:
#         word = [len(each_word)]
#     return word

# lengths = word_lengths(word_list)
# print(lengths)

# def length_list(word_list):
#     for i in word_list:
        

# def list_lengths(word_list):
#     largest_list = [len(i) for i in word_list]
#     return list_lengths

# lenghts = list_lengths(word_list)
# print(lenghts)

# def length_of_largest_list(list_of_lists):
#     max_length = 0
#     for i in list_of_lists:
#         current_length = len(i)
#         if current_length > max_length:
#             max_length = current_length
#     return max_length

# # Example usage:
# lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9], [10, 11, 12]]
# largest_length = length_of_largest_list(lists)
# print("Length of the largest list:", largest_length)

# for i in range (10):
#     for j in range(3):
#         print (f'{i}.{j}')

# new_list =["python", "development"]
# new_list.append("in progress")
# print (new_list)

# def is_vowel(char):
#     vowels = ["a", "e", "i", "o", '"u']
#     if char.lower() in vowels: 
#         return True
#     else: 
#         return False

# print (is_vowel("E"))


# def vowel_count(string):
#     num_vowels = 0
#     vowels = ["a", "e", "i", "o", '"u']
#     for char in string:
#         if char.lower() in vowels:
#             num_vowels = num_vowels + 1
#     return num_vowels 

# print (vowel_count("I love Python"))

# def every_other(string):
#     return string[0:len(string):2]
# print (every_other("python"))

# def reverse(string):
#     return string[::-1]

# print (reverse("Chapman"))

# def calc_sum(x,y):
#     sum = (float(x + y))
#     return sum

# def calc_avg (x,y):
#     avg = calc_sum (x,y) / 2
#     return avg

# print (calc_avg(2,3))

# email_input = input ("Email: ")

# def verify_email(email):
#     if "@" in email and "." in email:
#         return True
#     else: 
#         return False

# while verify_email(email_input) == False: 
#     print ("Wrong: ")
#     email_input = input ("Email: ")
# print ("correct")

# tuple2 = (1,2,3)
# print (tuple2[2])

# nested_list = [[1,2,3] [3,2,1]]

# for element in nested_list:
#     element [0] = 10
# print (nested_list)

# def update_database(database)

# nums = [1,2,3,4]
# word = "Shark"


# for i in nums:
#     print(word[i])
#     if i%2 == 0:
#         print(i, "is even!")
#     print("on to the next!")

# prices = {'apples': 1.99, 'oranges': 1.49, 'kiwi': 0.79}
# prices['oranges'] = 1.29
# print (prices)


# def add_student(l, studentName):
#     l.append(studentName)

# students = ["Frasier", "Niles", "Daphne"]

# add_student(students, "Roz")
# print(students)

# my_dict = {'Ahmad': 1, 'Jane': 42}
# print(my_dict.get('Jane', 'N/A'))
# print (my_dict.get('Chad', 'N/A'))

# fish = ["parrot", 'happy', 'fart', 'else', 'if']
# print (fish[::-2])

# def myFun(*hello):
#     for arg in hello:
#         print(arg)

# myFun('Hello', 'Welcome', 'to', 'Python')
# print(" ")

# import time
# def count(start,end):
#     for x in range (start,end+1):
#         print (x)
#         time.sleep(1)
#     print ("DONE!")

# count (0,10)

# monsters = {'Gorgon', 'Medusa'}
# trolls = {'William', 'Bert', 'Tom'}
# horde = {'Gorgon', 'Bert', 'Tom'}

# print (monsters.difference(trolls))

# Python3 program to
# demonstrate instantiating
# a class
# class Dog:

# 	# A simple class
# 	# attribute
# 	attr1 = "mammal"
# 	attr2 = "dog"

# 	# A sample method
# 	def fun(self):
# 		print("I'm a", self.attr1)
# 		print("I'm a", self.attr2)


# # Driver code
# # Object instantiation
# Rodger = Dog()a

# # Accessing class attributes
# # and method through objects
# print(Rodger.attr1)
# Rodger.fun()


class Person(): 
        age = 21 
        weight = 100
        height = 125
        first = "Kyla"
        last = "Bond"
        catch = "Hello"
        
user = Person()
print (user.catch)


class Person():
    def __init__ (self, age, weight, height, first, last, catch):
        self.age = age
        self.weight = weight 
        self.height = height 
        self.first = first
        self.last = last 
        self.catch = catch
        
user = Person(21, 100, 125, "Kyla", "Bond", "Hello")
print (user.first)
                
			