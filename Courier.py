# Compulsory Task

# Declaring all the if variables equal to 0
modePrice = 0
insurePrice = 0
giftPrice = 0
priorityPrice = 0

price = input ("What is the price of the product you wish to courier?\nR") # Allowing for the user to input the price of the product to declare the price variable.
price = float(price) # Changing the price entered to a float.

distance = input ("Please enter the total distance of the delivery in km (Only enter the number)?\n") # Allowing the user to input the distance they want the product delivered over to declare the distance variable.
distance = float(distance) # Changing the distance to a float.

# Declaring a variable named mode to determine whether the user would like the product to be delivered via air or freight.
mode = input ("Would you like an air delivery (Yes or No)?\n")
mode = mode.lower()

# if, else statement based on the user's input for the mode variable to determine which price to use in the final calculation.
if mode == "yes":
    modePrice = float(0.36)
else:
    modePrice = float(0.25)
    
# Declaring a variable named insure to determine whether the user would like the product to have full insurance or standard insurance.
insure = input ("Would you like full insurance (Yes or No)?\n")
insure = insure.lower()

# if, else statement based on the user's input for the insure variable to determine which price to use in the final calculation.
if insure == "yes":
    insurePrice = float(50)
else:
    insurePrice = float(25)
    
# Declaring a variable named gift to determine whether the user would like the product to be a gift or not.
gift = input ("Is this a gift (Yes or No)?\n")
gift = gift.lower()

# if, else statement based on the user's input for the gift variable to determine which price to use in the final calculation.
if gift == "yes":
    giftPrice = float(15)
else:
    giftPrice = float(0)
    
# Declaring a variable named priority to determine whether the delivery is high priority or not
priority = input ("Is this a high priority delivery (Yes or No)?\n")
priority = priority.lower()

# if, else statement based on the user's input for the priority variable to determine which price to use in the final calculation
if priority == "yes":
    priorityPrice = float(100)
else:
    priorityPrice = float(20)

totalCost = price + (distance*modePrice) + insurePrice + giftPrice + priorityPrice # Calculation to determine the full price of delivering the item based on the price variables.
print ("R" + str(totalCost))



