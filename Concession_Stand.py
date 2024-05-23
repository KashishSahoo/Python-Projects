menu={"chips":30,
      "popcorn":40,
      "soda":50,
      "pastry":35,
      "pizza":90,
      "fries":60,
      "ice cream":40,
      "puff":20,
      "chocalate":45,
      "nachos":30}
cart=[]
total=0

print("---------MENU---------")
for key,value in menu.items():
    print(f"{key:10}: Rs {value}")
print("---------------------")

print("Enter 'q' To Quit...")
while(True):
    food=input("Select An Item=").lower()
    if food=="q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("------YOUR ORDER------")
for food in cart:
    total+=menu.get(food)
    print(food,end=",")
print()
print(f"Total Is = Rs {total}")