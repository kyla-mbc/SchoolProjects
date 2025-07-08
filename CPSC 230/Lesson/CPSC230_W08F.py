'''Positional Arguments'''
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

## Correct function use depends on the order
## of the arguments/paramaters in the call
nameAge("Jordan", 27)
nameAge(27, "Jordan")

'''Keyword Arguments'''
'''Named Arguments'''
def student(firstname, lastname):
    print(firstname, lastname)

## Correction function use does NOT depent on order
student(firstname='Cassandra', lastname='Donatelli') #names are declared in variables. 
student(lastname='Donatelli', firstname='Cassandra')

'''Default Arguments'''
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)

myFun(125)

'''Arbutrary Keyword Arguments'''
### *args and *kwargs

### Use *args for variable number of arguments
def myFun(*hello):
    for arg in hello:
        print(arg)

myFun('Hello', 'Welcome', 'to', 'Python')
print(" ")

### use *kwargs for variable number of KEYWORD arguments
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
 
# myFun(first='Fish', mid='are', last='Friends')
# print(" ")


'''Docstrings'''
y = "Friends" # This is a global variable

def nameAge(name, age):
    '''Prints out name and age of a user'''
    print("Hi, I am", name)
    print("My age is ", age)
    x = "Fish" # This is a local variable


# print(nameAge.__doc__)
# nameAge('Kyla', 18)

'''None'''
## "None" prints out when you forget to return a variable
print(nameAge("Jude", 100))