import random
g=["rock","paper","sccissor"]
comp_score=0
user_score=0
draw=0
for i in range(5):
    user = int(input("Enter Your Choice= 0 for Rock,1 for Paper,2 for Scissors="))
    comp = random.randint(0, 2)
    if user >= 3 or user < 0:
        print("Invalid Choice!!!")
        print("Start Again!!!")
        break
    else:
        print("User Choose=", g[user])
        print("Computer Choose=", g[comp])
    if (comp == user):
        print("Draw!!!")
        print("\n")
        draw+=1
    elif (comp == 0 and user == 2):
        print("You Loose!!!")
        print("\n")
        comp_score += 1
    elif (comp == 2 and user == 0):
        print("You Win!!!!!")
        print("\n")
        user_score += 1
    elif (comp > user):
        print("You Loose!!!")
        print("\n")
        comp_score += 1
    elif (user > comp):
        print("You Win!!!!")
        print("\n")
        user_score += 1


print(("****RESULTS*****"))
print("Your Score=",user_score)
print("Computer Score=",comp_score)
print("Draws=",draw)
if(user_score>comp_score):
    print("You Wins")
else:
    print("You Loose")