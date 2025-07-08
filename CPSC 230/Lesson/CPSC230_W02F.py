### Constructors
five = 5
print (type(five))
five = str(five)
print(five)
print(type(five))

six = 6.0
print(type(six))
six = float(six)
print(type(six))

my_str = "ABCDEFG"
x = 10
print(my_str + str(x))
my_str = list(my_str)
print(my_str)
print(type(my_str))

addNumbers = 1 + 1
print(addNumbers)

addStrings = "1" + "1"
print(addStrings)

var1 = "1"
var2 = "2"

var3 = int(var1)+int(var2)
print(var3)

### Working with User Input
y = input("Give me a number : ")
print (int(y)+10)
newNumber = int(y)+10

print("Your result is" + str(newNumber))
int("10")

# convert to numeric types to perform operations on user input
y2 = int(y)**2

# Print statements want to add things of the same type
print("Your number squared is " + str(y2))


### Using imported libraries
import math

testNumber = 49
print(testNumber)

num_sqrt = math.sqrt(testNumber)
print(num_sqrt)
