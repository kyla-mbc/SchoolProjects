# Class Activities

'''
0. Call Stacks
Look through these functions and try to guess what will print out
when a() is called on line 26
'''

def a():
    fish = "Ribbon Eel"
    print("my favorite fish is a " + fish)
    b()
    print("my favorite fish is a " + fish)

def b():
    fish = "Electric Eel"
    print("my favorite fish is a " + fish)
    c()
    print("my favorite fish is a " + fish)

def c():
    fish = "Garden Eel"
    print("my favorite fish is a " + fish)

# what will print out?
a() 


'''
1.  Write a function, tens(), that takes in an integer and returns True if 
    the integer is divisible by 10, and False if it is not.
'''
number = int(input ("Give me an integer: "))
def tens(number):
    if number % 10 == 0:
        return True
    else:
        return False 
    
print(tens(number))

'''
2.  Let's re-visit our art-piece dictionary problem.
    
    Create a list of 5 dictionaries containing the title, artist, and cost 
    of 5 different paintings in a museum (or any 5 dictionaries containing
    the same 3 keys to define an object).

    Write a function that 
        - takes a dictionary as an input and tells the user the title, 
          artist, and cost in sentence form.
        - returns the cost of the painting as a float

    Write a for-loop to go through your list of dictionarues, adding up
    the cost of each painting along the way. Tell the user the total 
    value of all the paintings in your museum 
'''

painting1 = {"title":"Starry Night", "arist":"Van Gogh", "cost": "priceless" }
painting2 = {"title":"Hip Hop Dancing", "arist":"Bob Smith", "cost": "1 Million Dollars"}
painting3 = {"title":"Mona Lisa", "arist":"Da Vinci", "cost": "860 million dollars"}

def painting(title, artist, cost):
    print ("The painting" , title , "was created by" , artist, "and the cost for it is" , cost)
    
    


'''
3.  Distance Formula
    Write a functions that calculates the distance between two points
    https://en.wikipedia.org/wiki/Distance (just 2D distance is fine)
        - The function should take 2 lists as inputs
            - pt1 = [x1, y1]
            - pt2 = [x2, y2]
        - The function should return the distance
        - Remember that a distance cannot be a negative number
        - BONUS 01: Write your script so that the user can enter the 
          X and Y coordinates of their two points
        - BONUS 02: Write your function so it only returns 3 
          significant digits
'''
## The answer with these coordinates will be 13.928
pt1 = [5, 2]
pt2 = [10, 15]



'''
4.  BONUS CHALLENGE: Global Distance
    Write a functions that calculates the distance between two points on earth
    https://www.igismap.com/haversine-formula-calculate-geographic-distance-earth/
    You will yse the Haversine formula (link above)
        - The function should take 2 lists as inputs (you can get lattitude and
          longetude using google maps)
            - pt1 = [lattitude1, longetude1]
            - pt2 = [lattitude2, longetude2]
        - The function should return the distance in kilometers
        - Don't be afraid to dig around on Google!
'''


