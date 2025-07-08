# Class Activities
# We will use these same activities for Wednesday and Friday
# There will only be one Discussion post in canvas (due friday)
# so no need to post your code today.

'''
1.  Use a for loop to loop through the list of strings below, and print 
    out their names in Last, First Middle format (e.g. Doe, Jane Anne).

    HINT: Remember the split and join methods we looked at on Monday
'''
names = ["Jane Anne Doe", "John Jacob Smith", "Betty Gloria White"]

for name in names: 
  parts = name.split()
  print  (f"{parts[2]}, {parts[0]} {parts[1]}")


'''
2.  Use the lists of our three user's favorite items below. 
      - use sort() and logical operators to figure out if u1 and u2 like 
        the same items. print the result with a nicely phrased message 
        for both a True and False condition
      - all 3 users have talked and decided that they like pie better 
        than ice cream or cake. replace these items in their list using 
        a for loop, pop(), and append()
        NOTE: we learned that, by default, pop() removes the last element 
              from a collection. But you can also specify an index.
        NOTE: all the desserts are at index-2 (ie user1[2])

'''

u1 = ["hiking", "dinosaurs", "ice cream", "board games"]
u2 = ["dinosaurs", "hiking", "ice cream", "board games"]
u3 = ["hiking", "dinosaurs", "cake", "video games"]

if u1.sort() == u2.sort():
    print("What a coincidence! You guys like the same items!")
else:
    print("It seems like youu guys aren't that similar.")

u1 = ["hiking", "dinosaurs", "ice cream", "board games"]
u2 = ["dinosaurs", "hiking", "ice cream", "board games"]
u3 = ["hiking", "dinosaurs", "cake", "video games"]

for i in [u1, u2, u3]:
    i.pop(-2)  
    i.append("pie")  
print (u1)
print (u2)
print (u3)


### Adventurer Backpack ###

'''
3.  Lets keep with the d&d theme and write a function that allows our
    adventurer to add items to their backpack.
      - Make an list called backpack and fill it with items (strings)
      - Create a variagble "maxItems" to store the maximum number of 
        items that fit in a backpack (say 10 items)
      - Create a function, storage_check() that takes in two paramaters
        the backpack list, and a new item as a string. 
        
        The function should 
          1) check whether the backpack is full. 
          2) If it is full , print out the items in the backpack and ask 
             user to choose item to remove. 
          3) Once they choose a valid item (check if they did using in), 
             remove it (using remove()).
          4) Insert the new item in its place (using append())
'''
backpack = ["sword", "shield", "potion", "torch", "map"]
maxItems = 10

def storage_check(backpack, new_item):
    if len(backpack) >= maxItems:
        print("Your backpack is full. You need to remove an item to make space.")
        print("Items in your backpack:", backpack)
        item_to_remove = input("Enter the item you want to remove: ")

        if item_to_remove in backpack:
            backpack.remove(item_to_remove)  
            backpack.append(new_item)        
            print(f"{new_item} has been added to your backpack.")
        else:
            print("Invalid item. Choose an item from your backpack.")
    else:
        backpack.append(new_item)
        print(f"{new_item} has been added to your backpack.")

new_item = input("What would you like to add to your bag?")
storage_check(backpack, new_item)
print("Updated Backpack:", backpack)


'''
4.  Using the code from #1, let's have our adventurer find an apple, 
    decide whether to pick it up, and then eat it.
        - Print out a message telling the adventurer they found an apple.
        - Ask the user to input a "yes" or "no" about whether or not to 
          pick up the apple.
        - If they say yes, use the storage_check function to help them 
          add the apple to their inventory. If they say no, then print 
          out "moving on".
'''
apple_message = "You've found an apple on the ground. It looks delicious."
print (apple_message)

while True: 
  userInput = input ("Would you like to pick up the apple?")
  if userInput == ("yes"):
      if len(backpack) >= maxItems:
        print("Your backpack is full. You need to remove an item to make space.")
        print("Items in your backpack:", backpack)
        item_to_remove = input("Enter the item you want to remove: ")

        if item_to_remove in backpack:
            backpack.remove(item_to_remove)  
            backpack.append(new_item)        
            print(f"{new_item} has been added to your backpack.")
        else:
            print("Invalid item. Choose an item from your backpack.")
      else:
        backpack.append("apple")
        print(f"apple has been added to your backpack.")
        print("Updated Backpack:", backpack)
      break
  else:
    print ("Moving on")
    break

      
'''
5.  Write a function, cursed_backpack() which takes in the backpack list and
    performs a curse on it! The curse takes a random item in the backpack,
    and scambles it so that it's an anagram of the item name. Return the 
    new cursed backpack list. NOTE: use my prompts (and your mini-activity
    code) from last class as a starting point.
'''
import random

def scramble_word(word):
    letters = list(word)
    random.shuffle(letters)
    return ''.join(letters)


def cursed_backpack(backpack):
    cursed_backpack = backpack.copy()

    if len(backpack) > 0:
        item_to_curse = random.choice(backpack)
        cursed_item = scramble_word(item_to_curse)
        cursed_backpack[cursed_backpack.index(item_to_curse)] = cursed_item
        return cursed_backpack
    else:
        return backpack  # Return the original backpack if it's empty

original_backpack = ["sword", "shield", "potion", "torch", "map"]
cursed = cursed_backpack(original_backpack)
print("Original Backpack:", original_backpack)
print("Cursed Backpack:", cursed)

  
###   Bonus Challenge   ###
### Bridge Crosser Game ###

'''
6.  Imagine a game where you are 100m above the ground on a platform. There are two columns
    of 10 glass panes in front of you, 10 on the right and 10 on the left. At each of the 
    10 rows, one glass pane is solid and the other will break the moment you step on it, 
    sending you plummeting to the floor below. :(
      
    direction --> --> --> --> --> --> -->
        start                              safety!
      (user) [l][l][l][l][l][l][l][l][l][l]
             [r][r][r][r][r][r][r][r][r][r]

    Finish the function bridge_crosser() (below) which does not take in any arguments. 
    The code below generates a random list of 0's and 1's, representing whether the solid
    glass pane is on the right (1) or the left (0), and stores it in the list bridge.
    Ask the user to indicate whether they want to go right ('r') or left ('l'), and at 
    each step, tell them whether they fell (chose the weak pannel) or stayed up (chose the 
    solid panel).
    
    If they make it across the bridge, print a congratulatory message!
'''

import random

def bridge_crosser():

    # list of 0's and 1's, 1 means right side is solid,
    # 0 means left side is solid
    bridge = [random.randint(0,1) for i in range(0,10)]
    print(bridge)

    # your code here #


'''
7.  Modify your bridge_crosser() function (from the last classwork),
    so that it returns a list with two things:
        - the # of successful steps,
        - a list of the successful steps made
            (e.g. ["l", "r", "l", "l"]).

    So the output of the function could look something like this if the 
    player made 4 successful steps:
    >>>[4, ['l', 'r', 'r', 'r']]
'''
