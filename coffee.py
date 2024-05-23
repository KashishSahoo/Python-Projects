menu={
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24
        },
        "cost":150
    },

        "espresso":{
           "ingredients":{
            "water":50,
            "coffee":18
        },
        "cost":100
    },

        "cappuccino":{
           "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24
        },
        "cost":200
    }
}

profit=0
resources={
    "water":1000,
    "milk":500,
    "coffee":300
}

def check(order_ingrediants):
    for item in order_ingrediants:#water  #milk  #coffee
        if order_ingrediants[item]>resources[item]:
            print(f"Sorry There Is Not Enough {item}")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    total=0
    c_five=int(input("Enter Rs5 Coins="))
    c_ten=int(input("Enter Rs10 Coins="))
    c_twenty=int(input("Enter Rs20 Coins="))
    total=c_five*5+c_ten*10+c_twenty*20
    return total


def is_pay_success(m_receive,coffee_cost):
    if m_receive>=coffee_cost:
        global profit
        profit+=coffee_cost
        change=m_receive-coffee_cost
        print(f"Here Is Your Rs{change} In Change.")
        return True
    else:
        print("Sorry That's Not Enough Money.Money Refunded..")
        return False


def make_coffee(coffee_name,coffee_ingredients):
    for item in coffee_ingredients:
        resources[item]-=coffee_ingredients[item]
    print(f"Here Is Your {coffee_name}..Enjoy It...!!!")



is_on=True
while is_on:
    choice=input("What Would You Like To Have?(Latte/Espresso/Cappuccino)=")
    
    if choice=="off":
        is_on=False

    elif choice=="report":
        print(f"Water= {resources['water']} ml")
        print(f"Milk= {resources['milk']} ml")
        print(f"Coffee= {resources['coffee']} g")
        print(f"Money= Rs {profit}")
    
    else:
        coffee_type=menu[choice]
        print(coffee_type)

        if check(coffee_type["ingredients"]):
            pay=process_coins()
            if is_pay_success(pay,coffee_type['cost']):
                make_coffee(choice,coffee_type['ingredients'])