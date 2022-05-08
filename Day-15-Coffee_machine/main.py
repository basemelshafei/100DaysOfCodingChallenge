MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
p = 0.01
d = 0.10
n = 0.05
q = 0.25
espresso = 1.5
latte = 2.5
cappuccino = 3.0
water = 300
milk = 200
coffee = 100



def amount_paid(pennies, dimes, nickles, quarters):
    amount = ((p * pennies) + (d * dimes) + (n * nickles) + (q * quarters))
    return amount

def sufficient_resources(water, milk, coffee):
    if order == "espresso":
        resources["water"] += -50
        resources["coffee"] += -18
        return resources
    elif order == "report":
        return resources
    elif order == "latte":
        resources["water"] += -200
        resources["milk"] += -150
        resources["coffee"] += -24
        return resources
    else:
        resources["water"] += -250
        resources["milk"] += -100
        resources["coffee"] += -24
        return resources



def ordering():
        resources = sufficient_resources(water, milk, coffee)
        if order == "report":
            print(resources)
            return
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        money = amount_paid(pennies, dimes, nickles, quarters)
        if order == "espresso":
            change = money - espresso
            if change > 0:
                print(f"Here is your change: {change}")
                print("Here is your espresso.")
                print(resources)
            else:
                print("Please insert more coins")
        elif order == "latte":
            change = money - latte
            if change > 0:
                print(f"Here is your change: {change}")
                print("Here is your latte.")
                print(resources)
            else:
                print("Please insert more coins")
        elif order == "cappuccino":
            change = money - cappuccino
            if change > 0:
                print(f"Here is your change: {change}")
                print("Here is your cappuccino.")
                print(resources)
            else:
                print("Please insert more coins.")



def check_resources (water,milk,coffee):
        water_espresso = 50
        coffee_espresso = 18
        water_latte = 200
        coffee_latte = 24
        milk_latte = 150
        water_cappuccino = 250
        coffee_cappuccino = 24
        milk_cappuccino = 100
        if order == "espresso":
            if resources["water"] > water_espresso and resources["coffee"] > coffee_espresso:
                return ordering()
            else:
                print("Machine needs refilling")
                return
        elif order == "latte":
            if resources["water"] > water_latte and resources["coffee"] > coffee_latte and resources["milk"] > milk_latte:
                return ordering()
            else:
                print("Machine needs refilling")
                return
        elif order == "cappuccino":
            if resources["water"] > water_cappuccino and resources["coffee"] > coffee_cappuccino and resources["milk"] > milk_cappuccino:
                return ordering()
            else:
                print("Machine needs refilling")
                return
        else:
            print(resources)
is_on = True

while is_on:
    order = input("what would you like ? (espresso/latte/cappuccino): ")
    check_resources(water, milk, coffee)
    if order == "off":
        is_on = False
















