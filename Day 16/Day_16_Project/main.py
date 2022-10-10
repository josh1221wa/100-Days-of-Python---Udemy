from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
cash_register = MoneyMachine()

ON = True
while ON:
    choice = input(f"What would you like?({menu.get_items()}): ").lower()

    if choice == "off":
        ON = False

    elif choice == "report":
        coffeemaker.report()
        cash_register.report()

    else:
        drink = menu.find_drink(choice)
        if drink == None:
            print("Drink not available.")
            continue
        if coffeemaker.is_resource_sufficient(drink) == False:
            continue
        if cash_register.make_payment(drink.cost) == False:
            continue
        coffeemaker.make_coffee(drink)