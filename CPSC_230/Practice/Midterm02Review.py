#String Operation
string = "1" + "1"
print (string)

#String Comparison
print ("hello" == "Hello")
print ("Hello" == "Hello")

#String Methods 
text = "Hello, World!"
uppercase = text.upper()
lowercase = text.lower()
print(uppercase)  # Output: "HELLO, WORLD!"
print(lowercase)  # Output: "hello, world!"

text = "Python is easy to learn"
new_text = text.replace("easy", "powerful")
print(new_text)  # Output: "Python is powerful to learn"


text = "Python is easy to learn"
new_text = text.replace("easy", "powerful")
print(new_text)  # Output: "Python is powerful to learn"

sentence = "Python is great"
words = sentence.split()
print(words)  # Output: ['Python', 'is', 'great']


text = "Python is awesome"
sliced = text[7:10]
print(sliced)  # Output: "is "

#Boolean Methods 
text = "Python"
is_alpha = text.isalpha()
print(is_alpha)  # Output: True

text = "12345"
is_digit = text.isdigit()
print(is_digit)  # Output: True

text = "UPPERCASE"
is_upper = text.isupper()
print(is_upper)  # Output: True

text = "lowercase"
is_lower = text.islower()
print(is_lower)  # Output: True


#List Operations
my_list = [1,2,3,4,5]
my_list = (my_list*2)
print (my_list)

#List_Comparison
# Sample lists
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]

# Check if two lists are equal
if list1 == list2:
    print("The lists are equal.")
else:
    print("The lists are not equal.")

# Check if two lists are identical (same object in memory)
if list1 is list2:
    print("The lists are identical (same object).")
else:
    print("The lists are not identical (different objects).")

#List Methods 
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)  # Output: [1, 2, 3, 4, 5, 6]

my_list = [1, 2, 3]
my_list.insert(1, 4)  # Insert 4 at index 1
print(my_list)  # Output: [1, 4, 2, 3]

my_list = [1, 2, 3, 4, 3]
my_list.remove(3)  # Removes the first occurrence of 3
print(my_list)  # Output: [1, 2, 4, 3]

my_list = [1, 2, 3, 4, 5]
removed_element = my_list.pop(2)  # Remove and return element at index 2
print(removed_element)  # Output: 3
print(my_list)  # Output: [1, 2, 4, 5]

my_list = [4, 2, 1, 3, 5]
my_list.sort()
print(my_list)  # Output: [1, 2, 3, 4, 5]


#List Functions
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
length = len(my_list)
print("Length of the list:", length)  # Output: 11

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
minimum = min(numbers)
maximum = max(numbers)
print("Minimum value:", minimum)  # Output: 1
print("Maximum value:", maximum)  # Output: 9

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
total = sum(numbers)
print("Sum of elements:", total)  # Output: 44

my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_list = sorted(my_list)
print("Original list:", my_list)
print("Sorted list:", sorted_list)
# Output: Original list: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# Output: Sorted list: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]




