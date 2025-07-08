#Quiz04
#Name: Kyla Monique Cabrera
#Table Members: Lance 
import math

class Shapes():
    def __init__ (shape, sides, length):
        shape.sides = sides
        shape.length = length

    def what_shape(shape):
        if shape.sides == 3:
            return  "Triangle"
        elif shape.sides == 4:
            return "Square"
        elif shape.sides == 6:
            return "Hexagon"
        
    def calculating_area(shape):
        if shape.sides == 3:
            return (shape.length ** 2 * 3 ** 0.5) / 4 #Triangle Area
        elif shape.sides == 4:
            return shape.length ** 2 #Square Area
        elif shape.sides == 6: 
            return 3 * (3 ** 0.5) * (shape.length ** 2) / 2 #Hexagon Area 
        else: 
            return "Area not available"
    
    def calculating_perimeter(shape):
        if shape.sides == 3:
            return shape.length * 3
        elif shape.sides == 4:
            return shape.length * 4
        elif shape.length == 6: 
            return shape.length * 6
        else: 
            return "Perimeter not available"

#Demonstration 
triangle = Shapes(3,6)
square = Shapes (4,4)
hexagon = Shapes(6,6)

print (f"The shape is: {triangle.what_shape()}")
print (f"The area is: {triangle.calculating_area()}")
print (f"The perimeter is: {triangle.calculating_perimeter()}\n")

print (f"The shape is: {square.what_shape()}")
print (f"The area is: {square.calculating_area()}")
print (f"The perimeter is: {square.calculating_perimeter()}\n")

print (f"The shape is: {hexagon.what_shape()}")
print (f"The area is: {hexagon.calculating_area()}")
print (f"The perimeter is: {hexagon.calculating_perimeter()}")
