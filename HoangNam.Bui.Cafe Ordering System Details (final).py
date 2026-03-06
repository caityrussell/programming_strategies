"""
Cafe Ordering System
Programming Strategies Assignment
Hoang Nam Bui
"""

COFFEE_NAME = "Coffee"
COFFEE_PRICE = 3.00
TEA_NAME = "Tea"
TEA_PRICE = 2.50
HOT_CHOCOLATE_NAME = "Hot Chocolate"
HOT_CHOCOLATE_PRICE = 3.75

SUGAR_NAME = "Sugar"
SUGAR_PRICE = 0.10
CREAM_NAME = "Cream"
CREAM_PRICE = 0.50
SYRUP_NAME = "Syrup"
SYRUP_PRICE = 0.75

DISCOUNT_THRESHOLD = 5.00
DISCOUNT_RATE = 0.10
TAX_RATE = 0.05

EXIT_EXTRAS = 0
BEVERAGE_MIN = 1
BEVERAGE_MAX = 3
EXTRA_MIN = 0
EXTRA_MAX = 3


beverages = [
    (COFFEE_NAME, COFFEE_PRICE),
    (TEA_NAME, TEA_PRICE),
    (HOT_CHOCOLATE_NAME, HOT_CHOCOLATE_PRICE)
]

extras = [
    (SUGAR_NAME, SUGAR_PRICE),
    (CREAM_NAME, CREAM_PRICE),
    (SYRUP_NAME, SYRUP_PRICE)
]




print("=" * 40)
print("        WELCOME TO Python CAFE         ")
print("=" * 40)
print()

# Initialize running totals
order_count = 0
running_subtotal = 0.0
running_tax = 0.0
running_grand_total = 0.0

more_orders = 'y'
order_number = 1


while more_orders == 'y' or more_orders == 'Y':
    print(f"Order #{order_number} --------")
    print()

    print("=" * 40)
    print("        Beverage Menu:")
    print("=" * 40)
    print(f"1. {beverages[0][0]:15} ${beverages[0][1]:.2f}")
    print(f"2. {beverages[1][0]:15} ${beverages[1][1]:.2f}")
    print(f"3. {beverages[2][0]:15} ${beverages[2][1]:.2f}")
    print("=" * 40)

    #Beverage selection with validation
    beverage_choice = int(input("Your selection (1-3): "))
    while beverage_choice < BEVERAGE_MIN or beverage_choice > BEVERAGE_MAX:
        print("Please enter a number between 1 and 3.")
        beverage_choice = int(input("Your selection (1-3): "))

    # Get beverage details
    selected_beverage = beverages[beverage_choice - 1]
    beverage_name = selected_beverage[0]
    beverage_price = selected_beverage[1]
    print(f"You chose {beverage_name}.")
    print()

    # Extras selection
    selected_extras = []      # list of indices of chosen extras
    extras_subtotal = 0.0
    extra_choice = -1

    while extra_choice != EXIT_EXTRAS:
        print("=" * 40)
        print("              Add Extras")
        print("=" * 40)
        for i in range(len(extras)):
            extra_name = extras[i][0]
            extra_price = extras[i][1]
            checkmark = " ✓" if i in selected_extras else ""
            print(f"{i+1}. {extra_name:10} ${extra_price:.2f}{checkmark}")
        print(f"{EXIT_EXTRAS}. Finish order")
        print("=" * 40)

        extra_choice = int(input("Select extra (0-3): "))
        while extra_choice < EXTRA_MIN or extra_choice > EXTRA_MAX:
            print("Please enter a number between 0 and 3.")
            extra_choice = int(input("Select extra (0-3): "))

        if extra_choice == EXIT_EXTRAS:
            break

        extra_index = extra_choice - 1

        if extra_index in selected_extras:
            extra_name = extras[extra_index][0]
            print(f"{extra_name} is already added.")
        else:
            selected_extras.append(extra_index)
            extra_name = extras[extra_index][0]
            extra_price = extras[extra_index][1]
            extras_subtotal += extra_price
            print(f"{extra_name} added (+${extra_price:.2f}).")
        print()

    # Calculate order totals 
    subtotal = beverage_price + extras_subtotal
    discount = 0.0
    if subtotal > DISCOUNT_THRESHOLD:
        discount = subtotal * DISCOUNT_RATE
    after_discount = subtotal - discount
    order_tax = after_discount * TAX_RATE
    order_total = after_discount + order_tax

    # Display order summary
    print("=" * 40)
    print("           ORDER SUMMARY")
    print("=" * 40)
    print(f"Beverage: {beverage_name:20} ${beverage_price:.2f}")
    if selected_extras:
        print("Extras:")
        for idx in selected_extras:
            extra_name = extras[idx][0]
            extra_price = extras[idx][1]
            print(f"  • {extra_name:22} ${extra_price:.2f}")
    print(f"{'Subtotal:':30} ${subtotal:.2f}")
    if discount > 0:
        print(f"{'Discount (10%)':30} -${discount:.2f}")
        print(f"{'After discount:':30} ${after_discount:.2f}")
    print("=" * 40)

    # Update running totals 
    order_count += 1
    running_subtotal += after_discount
    running_tax += order_tax
    running_grand_total += order_total

    #Ask for another order 
    print()
    more_orders = input("Would you like to order another drink? (Y/N): ")
    if more_orders == "":
        more_orders = 'N'
    order_number += 1
    print()

# Final receipt
print("=" * 40)
print("           RECEIPT SUMMARY")
print("=" * 40)
print()
print(f"{'Number of Drinks:':25} {order_count}")
print(f"{'Subtotal:':25} ${running_subtotal:.2f}")
print(f"{'Tax (5%):':25} ${running_tax:.2f}")
print(f"{'Grand Total:':25} ${running_grand_total:.2f}")
print("=" * 40)
print()
print("Thank you for visiting Python Cafe!")
print("We hope to see you again soon!")