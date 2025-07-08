fish1 = input('Please input a species of fish: ') #asks the user for input and stores it in variable. 
fish2 = input('Give me another type of fish: ') #asks the user for input and stores it in variable. 
fish3 = input ('One more fish type: ') #asks the user for input and stores it in variable. 

fishSet = {fish1 , fish2, fish3} #stores all the inputted fish types into a set. 

if len(fishSet) == 1: #if length of the created set is 1, we know all inputs were the same species of fish.
    print('Fish') #print "fish" to represent one fish species.  
else:
    print('Fishes') #print "fishes" to represent multilple fish species. 

