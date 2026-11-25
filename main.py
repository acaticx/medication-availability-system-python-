
print(" ")
print(" ")
print("Welcome to the Medication Availability System!")

inventory = {
    "metformin": 50,
    "amoxicillin": 30,
    "lisinopril": 75,
    "sertraline": 25
}

def new_order():
## self note: pass is like a placeholder for code that will be added later. It allows the function to be defined without any implementation yet.
    new_order = bool()
    new_order = True

    while new_order == True: 

    
        print(" ")
        print("===================================================")
        print(" ")
        print(" ")
        print("Medication Inventory")
        print("----------------------------")
        print(" ")
        for medication, quantity in inventory.items():
            print(f"- {medication.title()}")

        print(" ")
        print("---------------------------")
        print(" ")
        print("Please enter medication name to check availability:")
        medication_name = input("->  ").lower()
        print(" ")
        if medication_name in inventory:
            print(f"{medication_name.title()} currently has {inventory[medication_name]} units in stock.")

            quantity_invalid = bool()
            quantity_invalid = True
            while quantity_invalid:
         
                print("--------------------------- ")
                print(" ")
                print("How many units are needed for pickup?")
                try:
                    requested_quantity = int(input("-> "))
                    quantity_invalid = False
                    if requested_quantity <= 0:
                        print(" ")
                        print("-------------------------- ")
                        print(" ")
                        print("Invalid input. Please enter a valid quantity.")
                        quantity_invalid = True
                except ValueError:
                    print(" ")
                    print("-------------------------- ")
                    print(" ")
                    print("Invalid input. Please enter a valid quantity.")
                    quantity_invalid = True


            if requested_quantity <= inventory[medication_name]:
                print(" ")
                print("-------------------------- ")   
                print(f"{requested_quantity} units of {medication_name.title()} are available for pickup.")

                print(" ")
                invalid_confirmation = bool()
                invalid_confirmation = True
                while invalid_confirmation:
                    print("-------------------------- ")
                    print("Would you like to proceed with this order? (yes/no)" )
                    confirmation = input("->  " ).lower()
                    if confirmation == "yes" or confirmation == "y":
                        inventory[medication_name] -= requested_quantity
                        print(" ")
                        print("-------------------------- ")
                        print(f"Order confirmed. Inventory updated. {inventory[medication_name]} units of {medication_name.title()} remaining.")
                        print(" ")
                       
                        invalid_confirmation = False
                        new_order = False
                    elif confirmation == "no" or confirmation == "n":
                        print(" ")
                        print("-------------------------- ")
                        print(" ")
                        print("Order Cancelled. No changes made to inventory.")
            
                        invalid_confirmation = False
                        new_order = False
                    else:
                        print(" ")
                        print("-------------------------- ")
                        print(" ")
                        print("Invalid input. Please enter 'yes' or 'no'.")
                        invalid_confirmation = True
            else:
                print(" ")
                print("-------------------------- ")
                print(" ")
                print("Insufficient stock available for pickup.")
                break

        else:
             print(" ")
             print("-------------------------- ")
             print(" ")
             print("Medication not found. Please try again.")
             break

new_order()


## first order ^^

## place new order feature vvv
## main function will ask to keep shopping, while yes
def keepShopping():
    shopping_active = bool()
    shopping_active = True
    
    while shopping_active:
        print(" ")
        print("-------------------------- ")
        print("Would you like to place another order? (yes/no)")
        Q_keepShopping = input("->  ").lower()

        if Q_keepShopping == "yes" or Q_keepShopping == "y":
            new_order()
        elif Q_keepShopping == "no" or Q_keepShopping == "n":
            shopping_active = False
        else: 
            print(" ")
            print("-------------------------- ")
            print('Invalid input. Please enter "yes" or "no":')
            print(" ")

        
## vv tells python to run defined functiion
keepShopping()

print(" ")
print("-------------------------- ")
print(" ")
print("Thank you for using the Medication Availability System. Goodbye!")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print("______________________________________")