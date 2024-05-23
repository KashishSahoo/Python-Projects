import hi
import os
import comp
import random

print(hi.logo1[0])
print(hi.logo2[0])

score=0


def display(acc):
    name=acc["name"]
    desc=acc["descryption"]
    con=acc["country"]
    return(f"{name},a {desc}, from {con}")



def check(guess,f_count1,f_count2):
    if f_count1<f_count2:
        if guess==1:
            return False
        else:
            return True
    else:
        if guess==1:
            return True
        else:
            return False
        
acc2=random.choice(comp.data)
continue_flag=True

while continue_flag:
    acc1=acc2
    acc2=random.choice(comp.data)

    while acc1==acc2:
        acc2=random.choice(comp.data)

    print(f"Compare 1: {display(acc1)}")
    print(hi.logo3[0])
    print(f"Compare 2: {display(acc2)}")

    guess=int(input("Who Has More Followers? Type 1 or 2: "))

    f_count1=acc1["follower_count"]
    f_count2=acc2["follower_count"]

    is_correct=check(guess,f_count1,f_count2)
    os.system('cls')
    print(hi.logo1[0])
    print(hi.logo2[0])

    if is_correct:
        score+=1
        print(f"You Are Right. Your Score Is : {score}")
    else:
        print(f"You Are Wrong. Your Final Score Is : {score}")
        continue_flag=False