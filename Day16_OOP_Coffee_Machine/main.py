from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeMaker = CoffeeMaker()
menu = Menu()
moneyMachine = MoneyMachine()

shutDown = False
while not shutDown:
    choice = input(f"What would you like? {menu.get_items()}: ")
    if choice == "report":
        coffeeMaker.report()
        moneyMachine.report()
    elif choice == "off":
        shutDown = True
    else:
        drink = menu.find_drink(choice)
        if coffeeMaker.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost):
            coffeeMaker.make_coffee(drink)
