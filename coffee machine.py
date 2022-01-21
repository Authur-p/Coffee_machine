MENU = {
    'espresso': {
        'ingredient': {
            'water': 50,
            'coffee': 18,
        },
        'cost': 1.5,
    },
    'latte': {
        'ingredient': {
            'water': 200,
            'coffee': 24,
            'milk': 150
        },
        'cost': 2.5,
    },
    'cappuccino': {
        'ingredient': {
            'water': 250,
            'coffee': 24,
            'milk': 100
        },
        'cost': 3.0,
    },
}
profit = 0
resources = {
    'water': 301,
    'milk': 200,
    'coffee': 100
}


def is_resource_sufficient(order_ingredient):
    """checks if resources is sufficient"""
    for items in order_ingredient:
        if order_ingredient[items] >= resources[items]:
            print(f'sorry, not enough {items}')
            return False
    return True


def process_coins():
    """collects the coins and returns total"""
    print('insert coins')
    total = int(input('how many quarters?: ')) * 0.25
    total += int(input('how many dime?: ')) * 0.1
    total += int(input('how many nickels?: ')) * 0.05
    total += int(input('how many penny?: ')) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """checks if transaction is succesful"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f'here is your ${change} in change')
        global profit
        profit += drink_cost
        return True
    else:
        print('sorry, that is not enough money, money refunded')
        return False


def make_coffee(drink_name, order_ingredient):
    """deduct the required ingredient from the resources"""
    for items in order_ingredient:
        resources[items] -= order_ingredient[items]
    print(f'here is your {drink_name}, enjoy')


while True:
    your_order = input('what would you like? (espresso/latte/cappuccino): ')
    if your_order == 'off':
        break
    elif your_order == 'report':
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Money: ${profit}')
    else:
        drink = MENU[your_order]
        if is_resource_sufficient(drink['ingredient']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(your_order, drink['ingredient'])
