'''Homework 02 TotalPrice.py'''
# tax_rate = 0.0725  #declare variable "tax_rate" with the given tax rate of California. 
# item_price = float(input("Item Price: $")) #declare variable "item_price" to ask the user for the price of an item and store that price. 
# subtotal = item_price * tax_rate #declare varibale "subtotal" to multiply "item_price" and "tax_rate"
# Total = subtotal + item_price #declare vaiable "total" to add "subtotal" and "item_price"
# print ("Total Price: $" , Total) #print the output of the total price 

# This works too !!!
# item_price = int(input("Item Price:"))
# item_and_tax = (item_price) * (0.0725) 
# total_price = item_and_tax + item_price
# print ("Total Price:" , total_price)

'''Homework 03 TotalPrice.py'''
tax_rate = 0.0725
sub_total = 0 
Total = 0 

while True: 
    item_price = input("Item Price: $") #asks user for the price of an item.
    if item_price.isdigit() == False: #ensures that the input is a digit.
        print ("Invalid Sale Price, Please Enter a Valid Number") #if input is not a digit, the code will not accept it and ask the user to try again. 
        continue #continues the code without running the above code again. 
    else:
        item_price = float(item_price) #if the input is a digit, it will be converted into a float. 
    if item_price < 0: #item prices cannot be a negative number. 
        print ("Invalid Sale Price, Please Enter a Valid Number") #the user will be prompted to  input a valid price. 
    else:
        sub_total = item_price * tax_rate #regular calculations will be administed if input it a valid price value.
        Total = sub_total + item_price #formula of total. 
        print ("Total Price: $" , Total) #print the output of the total price.
        break #breaks the while loop, it will not run again once satisfied. 
