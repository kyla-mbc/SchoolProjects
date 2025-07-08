'''Homework 02 Celsius.py'''
# F = int(input("Temperature in F°:")) #declare variable "F" to store a temperature input from the user. 
# C = ((F - 32) * (5/9)) # declare variable "C" to convert fahreneheit to celsius using formula. 
# print ("Temperature in C°:" , C) #print the output

# #print ("Temperature in C°:" , f'{C:.0f}') 
# #print ("Temperatue in C°:" , int(C))
# #other alternatives for print to set as integer. 

'''Homework 03 Celsius.py'''
while True: 
  F = float(input("Temperature in F°:"))
  if (-128.6 <= F <= 134):
    C = ((F - 32) * (5/9)) 
    print ("Temperature in C°:" , C) 
    break
  else:
    print ("Please enter a valid temperature on earth")

