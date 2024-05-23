import random
EASY_ATTEMPTS=5
HARD_ATTEMPTS=3

def set_diff(level):
    if level=='easy':
        return EASY_ATTEMPTS
    elif level=='hard':
        return HARD_ATTEMPTS
    else:
        return
    

def check_answer(g_no,answer,attempts):
    if g_no<answer:
        print("Your guess is too low")
        return attempts-1
    elif g_no>answer:
        print("Your guess is too high")
        return attempts-1
    else:
        print(f"Your Guess is right ... The Answer Was {answer}")


def game():
    
    print("Think A Number Between 1 To 50")
    answer=random.randint(1,50)
    print(answer)

    print("Choose The Difficulty")
    level=input("Type 'easy' or 'hard'=").lower()

    attempts=set_diff(level)
    if attempts!=EASY_ATTEMPTS and attempts!=HARD_ATTEMPTS:
        print("WRONG DIFFUCULTY CHOOSEN")
        return

    g_no=0

    while(g_no!=answer):
        print(f"You have {attempts} remaining to guess the number.")
        g_no=int(input("Guess A Number="))
        attempts=check_answer(g_no,answer,attempts)

        if attempts==0:
            print("You Are Out Of Guesses...")
            print("You Loose")
            print(f"The Actual Answer Is {answer}")
            return
        
        elif g_no!=answer:
           print("Guess Again")

game()