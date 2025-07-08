'''
1. Create a function, setMethods() that takes in two sets as arguments and 
prints out the union, difference, intersection, and symmetric difference 
between them. Try it out on the sets below.
'''

great_britain = {"Scotland", "England", "Wales"}
uk_of_gb_and_northern_ireland = {"Scotland", "England", "Wales", "Northern Ireland"}
ireland = {"Northern Ireland", "Republic of Ireland"}
british_isles = {"Scotland", "England", "Wales", "Northern Ireland",
  "Republic of Ireland", "Isle of Man"}

def setMethods(set1, set2):
    print ("Union:" , set1.union(set2))
    print ("Difference:" , set1.difference(set2))
    print ("Intersection:" , set1.intersection(set2))
    print ("Symmetric Difference" , set1.symmetric_difference(set2))

setMethods(great_britain,british_isles)


'''
2.  Write a function scrabblePoints() which takes in 1) a word and 2) the dictionary below
    and uses "in" to calculate how many points the word is worth. Return the points value 
    as an integer. Go around the table (without looking online) and try to see who can
    come up with the highest scoring word.
'''

scrabbleValues = {  'a':1 , 'b':3, 'c':3, 'd':2, 'e':1, 'f':4, 'g':2, 'h':4, 'i':1, 
                    'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 
                    's':1, 't':1, 'u':1, 'v':8, 'w':4, 'x':8, 'y':4, 'z':10         }

def scrabblePoints(word,points):
    total = 0
    for letter in word:
        total += points[letter]

    return total
print (scrabblePoints(input("Give me a word:"), scrabbleValues))


'''
3.  Using the dictionary below that represents the possible grade breakdown for 
    a course, write a function that takes in a student dictionary as a paramater
    and calculate the weighted final grade using the weighting below. Include error
    handling (using get) to account for missing values.

- assignments: 30%
- participation: 30%
- challenges: 5%
- exam1: 10%
- exam2: 10%
- finalexam: 15%

'''

studentA = {"assignments": 90, "participation": 85, "challenges": 99,
            "exam1": 87,       "exam2": 82,         "finalexam": 79}

studentB = {"assignments": 60, "participation": 85,
            "exam1": 75,       "exam2": 75,         "finalexam": 81}

studentC = {"assignments": 80, "participation": 50, "challenges": 100,
            "exam1": 70,       "exam2": 80,         "finalexam": 90}

def weighted(student):
    weights = {
        "assignments": 0.30,
        "participation": 0.30,
        "challenges": 0.05,
        "exam1": 0.10,
        "exam2": 0.10,
        "finalexam": 0.15
    }
    total_weighted_grade = 0.0
    for component, weight in weights.items():
        grade = student.get(component, 0)
        total_weighted_grade += grade * weight

    return total_weighted_grade
    
print (weighted(studentA))


''' 
4.  Write a function shopping_list_helper() that takes in recipes for the week
    as a list of lists (see below) as an argument. Using sets, print out a list 
    of unique ingredients the user needs to buy to make al 5 recipes.
'''

my_recipes = [  ["apples", "sugar", "cinnamon", "nutmeg", "cloves", "butter", "flour"],
                ["ground beef", "refried beans", "lettuce", "cheese", "tomato", "sour cream", "avocado"],
                ["lettuce", "croutons", "parmesean", "anchovies", "mayo", "mustard", "worcestershire", "lemon"],
                ["lemon", "sugar", "flour", "vanilla", "butter", "eggs"],
                ["eggs", "tomato", "bacon", "blue cheese", "lettuce", "cheese", "cucumber"]]


def shopping_list_helper(recipes):
    unique_ingredients = set()
    for recipe in recipes:
        unique_ingredients.update(recipe)
    return list(unique_ingredients)

unique_ingredients = shopping_list_helper(my_recipes)

print("Unique ingredients to buy for all recipes:")
for ingredient in unique_ingredients:
    print(ingredient)


'''
5.  Create a function, stencil_finder(), that takes in a message (a string) as an argument.
    The function is to help a graffiti artist know which stencils they have to bring with them
    to tag a message in their city. Since stencils for graffiti can be reused, they only need
    to know which to take, not how many. The functions should use string methods and sets to
    look through the message, figure out which letter stencils are needed, and return a list 
    of them for the artist.
'''
def stencil_finder(message):
    cleaned_message = ''.join(filter(str.isalpha, message)).lower()
    unique_letters = set(cleaned_message)
    stencils_needed = sorted(list(unique_letters))

    return stencils_needed

message = input ("Give me a message: ")
needed_stencils = stencil_finder(message)

print("Stencils needed for the message:")
for stencil in needed_stencils:
    print(stencil)

'''
6.  Write a function consider_food() that takes in two arguments: 1) food (a dictionary with
    the different allergen/ingredient booleans - see below), and 2) allergies (a list of 
    strings indicating which allergens/foods this person cannot consume - e.g. ["gluten", "dairy"])

    The function should check whether the food is something the person can eat. If it is
    return True, else return False.
'''

sandwhich = {"name": "sandwhich","gluten": True, "meat": True, "Soy": True, "AnimalProducts": True}
apple = {"name":"apple","gluten": False, "meat": False, "Soy": False, "AnimalProducts": False}
cheese = {"name":"cheese","gluten": False, "meat": False, "Soy": False, "AnimalProducts": True}
tofu = {"name":"tofu","gluten": False, "meat": False, "Soy": True, "AnimalProducts": False}

def consider_food(food, allergies):
    for allergen in allergies:
        if allergen in food and food[allergen]:
            return False  

    return True  

# Define a list of allergies
allergies = ["gluten", "dairy"]
# Check if the person can eat each food
foods = [sandwhich, apple, cheese, tofu]

for food in foods:
    can_eat = consider_food(food, allergies)
    if can_eat:
        print(f"You can eat {food['name']}.")
    else:
        print(f"You should avoid {food['name']}.")



