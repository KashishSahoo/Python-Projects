foods=[]
prices=[]
total=0

print("****SHOPPING CART****")
print("Enter'q' To Quit")

while True:
    print()
    food=input("Enter A Food To Buy=")

    if food.lower()=='q':
        break
    else:
        price=int(input(f"Enter The Price Of {food}=Rs"))
        print()
        foods.append(food)
        prices.append(price)
print()
print("---YOUR CART---")

for food in foods:
    print(food, end=" ")
for price in prices:
    total+=price
    
print()
print(f"Your Total Is: Rs {total}.")
