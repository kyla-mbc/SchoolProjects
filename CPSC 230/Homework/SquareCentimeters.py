tank_volumeL = float(input("Tank Volume (L):")) #declare variable "tank_volumeL" to store an input from the user. 
reptile = input ("Which reptile would you like to adopt?") #declare varible "reptile" to ask user what reptile they would like to adopt and store the response. 
print ("Wow! I think a pet" , reptile , "is so cool") #print response statement

import math 
cubic = (tank_volumeL * 1000) #muliply tank volume inputted by 1000 to find cubic length. 
length = math.cbrt(cubic) #use formula to find the length of one side
footprint = (length**2) #square "length" to get bottom area of the cube. 
footprint = str(footprint) #add footprint to string

print ("Footprint of tank:" , footprint , "cm²")

# print("Square Centimeter of Tank:", tank_volumeSC)

'''
liters -> square centimeters 
'''