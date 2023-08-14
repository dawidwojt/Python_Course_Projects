
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
should_make = True
def coffee_machine():
    global resources
    global MENU
    global should_make

    # TODO:1 print report of all resources
    print("HELLO what would you like to drink? ")
    print("   MENU:")
    print(f"   1. ESPRESSO:     $ {MENU['espresso']['cost']}")
    print(f"   2. LATTE:        $ {MENU['latte']['cost']}")
    print(f"   3. CAPPUCCINO:   $ {MENU['cappuccino']['cost']}")
    question = input("Choose the number:            ")
    bev = ""

    if question == "report":
        print(resources)
    elif question == "refil":
        resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        }
    elif question == "1":
        bev = "espresso"
    elif question == "2":
        bev = "latte"
    elif question == "3":
        bev = "cappuccino"
    if MENU[bev]['ingredients']['water'] < resources['water'] and MENU[bev]['ingredients']['milk'] < resources['milk'] and MENU[bev]['ingredients']['coffee'] < resources['coffee']:
        should_make = True
    else:
        should_make = False
    if should_make == True:
        #print(resources)
        print(f"YOUR TOTAL: $ {MENU[bev]['cost']} Please start inserting coins: ")
        total_inserted = 0
        pennies = int(input("   INSERT pennies $0.01:       "))
        total_inserted += pennies*0.01
        print(f" You inserted: $ {pennies*0.01}. You need to insert {MENU[bev]['cost']-total_inserted}")
        nickles = int(input("   INSERT nickles $0.05:       "))
        total_inserted += nickles*0.05
        print(f" You inserted: $ {total_inserted + nickles*0.05}. You need to insert {MENU[bev]['cost'] - total_inserted}")
        dimes = int(input("     INSERT dimes $0.10:     "))
        total_inserted += dimes*0.1
        print(f" You inserted: $ {total_inserted + nickles * 0.1}. You need to insert {MENU[bev]['cost'] - total_inserted}")
        quarters = int(input("  INSERT quarters $0.25:      "))
        total_inserted += quarters*0.25
        print(f"You inserted: ${total_inserted}.")
        if total_inserted > MENU[bev]['cost'] or total_inserted == MENU[bev]['cost']:
            print(f"THANK YOU. Please take your change.")
        elif total_inserted < MENU[bev]['cost']:
            print("You did not insert enough money. Please try again")
            return
        print("Please wait... Your coffee is is being prepared... ")
        resources['water'] -= MENU[bev]['ingredients']['water']
        resources['milk'] -= MENU[bev]['ingredients']['milk']
        resources['coffee'] -= MENU[bev]['ingredients']['coffee']
    elif should_make == False:
        print("I am sorry but we are out of our resources. Please try again later. GOODBYE.")
        return

coffee_machine()
another_coffee = input("Would you like another coffee? [y/n]:   ").lower()
if another_coffee == "y":
    should_continue = True
else:
    should_continue = False
while should_continue == True and should_make == True:
    coffee_machine()




