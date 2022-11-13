#Financial calculator project

import math #Import the required modules

#Prints the required lines:
print("\nChoose either 'investment' or 'bond' from the menu below to proceed:\n")
print("investment \t - \t to calculate the amount of interest you'll earn on your investment")
print("bond \t\t - \t to calculate the amount you'll have to pay on a home loan\n")

user_choice = input(">>\t").lower().strip() #User choice is assigned to a variable. .lower() and .strip() so it is not case sensitive
valid_choice = False #Setting up a flag for the while loop

while not valid_choice:
    if user_choice == "investment" or user_choice == "bond": #Checks the user has entered a valid choice, if so, changes the flag to true and continues
        valid_choice = True
    else:
        print("\t\tError!\n") #if neither bond nor investment is entered, the else statement triggers and the user has an opportunity to try again (indefinitely)
        print("Please enter 'investment' or bond'")
        user_choice = input(">>\t").lower().strip()

# if investment is entered, this block of code runs:
if user_choice == "investment":
    # if the user adds types letters, attempts to cast it as a float or int will cause a crash, to prevent this I used a while loop and a try-except
    valid_numbers = False # sets this to false so the while loop runs at least once
    while not valid_numbers:
        try: #errors will occur in this section. A try block will catch these errors
            print("How much money are you depositing?:")
            deposit = float(input(">>\t"))
            print("What is the interest rate (%)?:")
            interest_rate = float(input(">>\t"))
            print("How many years will you invest your money?: ")
            years = int(input(">>\t"))
        except: #If an error occurs, the following will print, and the loop will start again (flag is still false)
            print("\t\tError!\nMake sure you are entering only numbers!\n")
        else:
            valid_numbers = True #No errors detected, so flag is changed to true and we leave the while loop
    
    print("Calculate 'simple' or 'compound' interest:")
    interest_type = input(">>\t").lower().strip() #Looks for simple or compound. Same logic as user choice at the start.

    #This part works in the same way as the user_choice at the start
    valid_interest_type = False
    while not valid_interest_type:
        if interest_type == "simple" or interest_type == "compound":
            valid_interest_type = True
        else:
            print("\t\tError!\n")
            print("Please enter 'simple' or 'compound'")
            interest_type = input(">>\t").lower().strip()

    #checks what option was chosen and calculates the interest rate from the formulae given
    if interest_type == "simple":
        total_amount = deposit * (1 + (interest_rate/100) * years)
    else: #Because of the while loop, if it is not simple it must be compound
        total_amount = deposit * math.pow((1+ (interest_rate/100)), years)
    total_amount = round(total_amount,2) #rounds the answer to 2 decimal places here to simplify the above lines   
    print(f"\nThe total amount after interest will be {total_amount}, assuming {interest_type} interest\n") #Finally prints out the result

#This block of code runs when user chooses 'bond'. The while loop means only investment or bond can be selected so this must be bond
else:
    valid_numbers = False #Same logic as before. While and try-except to catch errors from wrong data being entered.
    while not valid_numbers:
        try:
            print("What is the current value of the property?: ")
            property_value = int(input(">>\t"))
            print("What is the interest rate (%)?:")
            month_interest_rate = float(input(">>\t"))/12 #get the monthly interest by diving by 12 here
            print("How many months will you have the bond?: ")
            months = int(input(">>\t"))
        except:
            print("\t\tError!\nMake sure you are entering only numbers!\n")
        else:
            valid_numbers = True
    #calculate the monthly payments as given in the task:
    monthly_fee = ((month_interest_rate/100) * property_value) / (1 - (1 + (month_interest_rate/100)) ** (-months))
    monthly_fee = round(monthly_fee, 2) #Rounds two decimal places here so the above line is simpler
    print(f"Your fees will be {monthly_fee} a month") #Finally prints the monthly fee