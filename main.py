from menu import MENU
resources = {
    "water": 300,
    "milk": 250,
    "coffee": 100,
}


# TODO : 4. Check resources sufficient?


def check_resources(user_order):
    """Checks if there are sufficient resources available to make the coffee, and returns true if the
    ingredients are sufficient"""
    for item in user_order:
        if user_order[item] >= resources[item]:
            print(f"There is no sufficient {item}")
            return False
        return True

# TODO : 5. Process Coins


def process_coins():
    """returns the total calculated from the coins inserted"""
    print("Please insert coins")
    quarters = int(input("quarters: "))
    dimes = int(input("dimes: "))
    nickles = int(input("nickles: "))
    pennies = int(input("pennies: "))
    money = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return money
# TODO : 6. Check transaction successful?


def is_transaction_successful(received_money, drink_cost):
    """returns true if the payment is accepted and false otherwise"""

    if received_money >= drink_cost:
        global profit
        change = round(received_money - drink_cost, 2)
        print(f"Here is your change {change}")
        profit += drink_cost
        return True

    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# TODO : 7. . Make Coffee.


def make_coffee(user_order, order_ingredients):
    """deduces the inserted coffee ingredient from the current resource"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is your coffee {user_order}☕")

# TODO : 2. Turn off the Coffee Machine by entering “off” to the prompt


profit = 0
is_on = True
while is_on:
    # TODO : 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino)
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == 'off':
        is_on = False

    # TODO : 3. print report

    elif order == 'report':
        for resource in resources:
            if resource == 'water':
                water = resources[resource]
            if resource == 'milk':
                milk = resources[resource]
            if resource == 'coffee':
                coffee = resources[resource]
        print(f"water: {water}ml\nmilk: {milk}ml\ncoffee: {coffee}g")
        print(f"Money: ${profit}")

    else:
        drink = MENU[order]
        if check_resources(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(order, drink['ingredients'])



