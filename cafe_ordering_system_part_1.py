'''
program name: cafe_ordering_system_part1
author: Caitlyn Russell
date: February 23, 2026
'''

#set constants
COFFEE_PRICE = 3.00
TEA_PRICE = 2.50
HOTCHOC_PRICE = 3.75

SUGAR_PRICE = .10
CREAM_PRICE = .50
SYRUP_PRICE = 0.75

DISCOUNT_THRESHOLD = 5.00
DISCOUNT_RATE = 0.10
TAX_RATE = 0.05

#create dictionaries 
BEVERAGES = {'Coffee': COFFEE_PRICE, 'Tea': TEA_PRICE, 'Hot Chocolate': HOTCHOC_PRICE}
EXTRAS = {'Sugar': SUGAR_PRICE, 'Cream': CREAM_PRICE, "Syrup": SYRUP_PRICE}
extras_choice_dict = {}

#display banner
print("="*40)
print(f'{"WELCOME TO Python CAFE" :^40}')
print("="*40)

#set drink number, subtotal and order counter
total_drinks = 0
final_subtotal = 0
order_number = 1 
order_again = 'y'

#start main order loop
while order_again == 'y':

    #display order number
    print(f'\nOrder #{order_number}')
    print(f"{'-'*8}\n")
    order_number += 1

    #display menu with prices 
    print(f'{"="*40}')
    print(f'{"Beverage Menu:":>22}')
    print(f'{"="*40}')
    num = 1
    for item in BEVERAGES:
        bev_price = BEVERAGES[item]
        print(f"{num}. {item:<15} ${bev_price:.2f}")
        num = num + 1
    print("="*40)

    #ask for user's beverage choice
    beverage_choice = input('Your Selection (1-3): ')

    #validate input
    while beverage_choice not in ("1", "2", "3"):
        print('Please select a number between 1 and 3')
        beverage_choice = input('Your Selection (1-3): ')

    #store beverage choice and price in variable
    if beverage_choice == '1':
        beverage_name = 'Coffee'
        beverage_price = COFFEE_PRICE
        

    elif beverage_choice == '2':
        beverage_name = 'Tea'
        beverage_price = TEA_PRICE
        

    elif beverage_choice == '3':
        beverage_name = 'Hot Chocolate'
        beverage_price = HOTCHOC_PRICE
        
    print(f"You chose {beverage_name}")

    #set extras counters
    sugar_added = False
    cream_added = False
    syrup_added = False 

    extras_choice = ""
    extras_total = 0

    while extras_choice != "0":
    
        #extras selection menu
        print("="*40)
        print(f'{"Add Extras":^40}')
        print("="*40)

        num = 1
        for item in EXTRAS:
            if item == "Sugar" and sugar_added:
                check = " ✓"
            elif item == "Cream" and cream_added:
                check = " ✓"
            elif item == "Syrup" and syrup_added:
                check = " ✓"
            else:
                check = ""

            print(f"{num}. {item:<10} ${EXTRAS[item]:.2f}{check}")
            num += 1

        print('0. Finish Order')
        print(f'{"="*40}') 

        #user selects their extra choice
        extras_choice = input('Select extra (0-3): ')
    
        #validate extra choice input 
        while extras_choice not in ("0", "1","2", "3"):    
            print('Please enter a number between 0 and 3.')
            extras_choice = input('Select extra (0-3): ')

        
        #process extras
        if extras_choice == '1':
            if sugar_added:
                print("Sugar is already added.")
            else:
                sugar_added = True
                extras_name = 'Sugar'
                extras_price = SUGAR_PRICE
                extras_choice_dict['Sugar'] = SUGAR_PRICE
                print('Sugar added (+$0.10)')

        elif extras_choice == '2':
            if cream_added:
                print("Cream is already added.")
            else:
                cream_added = True
                extras_name = 'Cream'
                extras_price = CREAM_PRICE
                extras_choice_dict['Cream'] = CREAM_PRICE
                print('Cream added (+$0.50)')

        elif extras_choice == '3':
            if syrup_added:
                print("Syrup is already added.")
            else:
                syrup_added = True
                extras_name = 'Syrup'
                extras_price = SYRUP_PRICE
                extras_choice_dict['Syrup'] = SYRUP_PRICE
                print('Syrup added (+$0.75)')


    #display order summary
    print(f'\n{"="*40}')
    print(f'{"ORDER SUMMARY:":^40}')
    print(f'{"="*40}')
    print(f"Beverage: {beverage_name:<12}${beverage_price:>.2f}")
    print(f"Extras")
    for item in extras_choice_dict:
        price = extras_choice_dict[item]
        print(f" {'•':<2}{item:<18} ${price:>.2f}")

    order_again = input('Would you like to order another drink? (Y/N): ').lower()

#order summary calculations
subtotal = beverage_price + extras_total

if subtotal > DISCOUNT_THRESHOLD:
    discount_amount = subtotal * DISCOUNT_RATE
else:
    discount_amount = 0 

after_discount = subtotal - discount_amount 




