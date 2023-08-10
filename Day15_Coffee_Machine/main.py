from menu import MENU, resources
from functionalities import enoughResources, totalAmt, brew, report


def coffeeMachine():
    shutDown = False
    while not shutDown:
        choice = input("What would you like? (Espresso: $1.5/Latte: $2.5/Cappuccino: $3.0): ").lower()
        if choice == "espresso" or choice == "cappuccino" or choice == "latte":
            if enoughResources(resources, MENU[choice]):
                amtPaid = round(totalAmt(int(input("How many quarters?: ")), int(input("How many dimes?: ")),
                                         int(input("How many nickels?: ")), int(input("How many pennies?: "))), 2)
                change = round(amtPaid - MENU[choice]["cost"], 2)
                if change < 0:
                    print(f"Sorry, ${amtPaid} is not enough money. Money refunded.")
                else:
                    brew(resources, MENU[choice])
                    print(f"Here is ${change} in change.")
                    print(f"Here is your {choice}. Enjoy!")
        elif choice == "report":
            report(resources)
        elif choice == "off":
            shutDown = True


coffeeMachine()
