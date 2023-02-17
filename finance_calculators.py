import math

def investment_calculator():
    '''
    One of the calculator functions called from the menu. Asks the user for
    information about the investment and parametres and returns the total
    value of the investment.
    '''
    while True:
        try:
            print('How much money are you depositing?')
            deposit = float(input('>>> '))
            print('What is the interest rate (%)?')
            interest_rate = float(input('>>> '))
            print('How many years will you invest your money?')
            years = int(input('>>> '))
        except ValueError:
            print('\t\tError!\nMake sure you are entering only numbers!\n')
        else:
            break
    print('''Calculate compount or simple interest:
            1 - Compound
            2 - Simple
            0 - Cancel''')
    while True:
        compound_simple_choice = input('>>> ').strip()
        if compound_simple_choice == '1':
            total_amount = deposit * math.pow((1+ (interest_rate/100)), years)
            print('Total interest, assuming compound interest:')
            print(round(total_amount, 2))
            break
        if compound_simple_choice == '2':
            total_amount = deposit * (1 + (interest_rate/100) * years)
            print('Total interest, assuming simple interest:')
            print(round(total_amount, 2))
            break
        if compound_simple_choice == '0':
            print('Returning to menu...')
            break
        else:
            print('Invalid choice. Please try again')

def bond_calculator():
    '''
    One of the calculator functions. Prompts the user for details about the
    bond, and then returns the monthly fee
    '''
    while True:
        try:
            print('What is the current value of the property?')
            property_value = int(input('>> '))
            print('What is the interest rate (%)?')
            month_interest= float(input('>> '))/12
            print('How many months will you have the bond?')
            months = int(input('>> '))
        except ValueError:
            print('\t\tError!\nMake sure you are entering only numbers!\n')
        else:
            break
    monthly_fee = ((month_interest/100) * property_value) / (1 - (1 + (month_interest/100)) ** (-months))
    monthly_fee = round(monthly_fee, 2)
    print(f'Your fees will be {monthly_fee} a month')


# Main menu - functions are called from here
print('''Calculate investment or bond:
            1 - Investment: the amount of interest you'll earn on an investment
            2 - Bond: the amount you'll have to pay on a home loan
            0 - Exit''')

while True:
    user_choice = input('>>> ').strip()
    if user_choice == ('1'):
        investment_calculator()
    if user_choice == ('2'):
        bond_calculator()
    if user_choice == ('0'):
        print('Goodbye')
        exit()
    else:
        print('Invalid choice - Please try again')
