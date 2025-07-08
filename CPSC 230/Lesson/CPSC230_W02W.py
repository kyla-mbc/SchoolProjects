### numeric types
x = 1
y = 6.34
z = 1.0

print(type(x))
print(type(y))
print(type(z))

### booleans
x = True
print(type(x))
y = False
print(type(y))

z = 10
j = 15

whatIsThis = (z == j)
print(whatIsThis)

### string
s1 = 'Stickleback'
s2 = "Prickleback"
s3 = '''Dogfish'''
# print (s1[0])each letter has a number 

print(type(s1), type(s2), type(s3))

print(s1)
print(s2)
print(s3)

y = input("Give me a number : ")
print(type(y))

# y = int(input("Give me a number : ")) use "int" to turn into integer. 
# print(type(y))

### lists
my_list = [1,2,3,4,5]
print(my_list [3])

my_list2 = ["hello", 9, 1.2, [1,2,3,4,5]]
print (my_list2[0])


### dictionaries and sets
cat1 = {"species":"Cat", "name": "Calvin", "age": 4, "breed": "Tabby"}
print(type(cat1))
print (cat1["species"])


my_set = {1,2,3,4,5,5,5,5,5}
print(my_set) 
print(type(my_set))