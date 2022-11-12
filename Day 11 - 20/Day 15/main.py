# Coffee Machine Project
import data


def print_report(resources):
    print(
        f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}")


def check_resources(ingredients, resources):
    if ingredients['water'] > resources['water']:
        return 'water'
    elif ingredients['milk'] > resources['milk']:
        return 'milk'
    elif ingredients['coffee'] > resources['coffee']:
        return 'coffee'
    else:
        return True


def calculate_money(quarters, dimes, nickels, pennies):
    sum = quarters*0.25 + dimes*0.10 + nickels*0.05 + pennies*0.01
    return sum


resources, MENU = data.resources, data.MENU

ON = True
while ON:
    choice = input("What would you like?(espresso/latte/cappuccino): ").lower()

    if choice == "off":
        ON = False

    elif choice == "report":
        print_report(resources)

    elif choice in ["espresso", "latte", "cappuccino"]:
        ingredients = MENU[choice]['ingredients']
        eligible = check_resources(ingredients, resources)
        if eligible != True:
            print(f'Sorry there is not enough {eligible}')
            continue
        else:
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))

            total = calculate_money(quarters, dimes, nickels, pennies)
            cost = MENU[choice]['cost']
            if total < cost:
                print("Sorry that's not enough money. Money refunded.")
                continue
            else:
                if total > cost:
                    print(f"Here is ${total - cost} in change.")
                print(f"Here is your {choice}☕. Enjoy!")

            resources['water'] -= ingredients['water']
            resources['milk'] -= ingredients['milk']
            resources['coffee'] -= ingredients['coffee']
            resources['money'] += cost
