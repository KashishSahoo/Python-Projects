import random

def choose():
    words=['rainbow','computer','science','programming','maths','player','condition',
           'reverse','water','board']
    pick=random.choice(words)
    return(pick)

def jumble(word):
    j="".join(random.sample(word,len(word)))
    return j

def thank(p1,p2,po1,po2):
    print(p1,"Your Score Is=",po1)
    print(p2,"Your Score Is=",po2)
    if(po1>po2):
        print(p1,"Won The Game!!!")
    elif(po1==po2):
        print("Draw Game!!!")
    else:
        print(p2,"Won The Game!!!")
    print("Thank You So Much For Playing!!!")
    print("Have A Nice Day!!!")

def play():
    p1=input("Player1,Please Enter Your Name= ")
    p2=input("Player2,Please Enter Your Name= ")
    po1=0
    po2=0
    turn=0
    while(1):
        #Computer's Task
        #Picked Word
        pw=choose()
        #Create The Question
        q=jumble(pw)
        print(q)
        #Player 1
        if(turn%2==0):
            print(p1,"Your Turn")
            ans=input("What's In Your Mind!!!!=")
            if (ans==pw):
                po1=po1+1
                print("Your Score Is=",po1)
            else:
                print("Better Luck Next Time!!")
                print("I Thought:",pw)
            
            c=int(input("Press 1 To Continue And 0 To Quit="))
            if(c==0):
                thank(p1,p2,po1,po2)
                break
        #Player 2
        else:
              
            print(p2,"Your Turn")
            ans=input("What's In Your Mind!!!!=")
            if(ans==pw):
                po2=po2+1
                print("Your Score Is=",po2)
            else:
                print("Better Luck Next Time!!!!")
                print("I Thought:",pw)
            c=int(input("Press 1 To Continue And 0 To Quit="))
            if(c==0):
                thank(p1,p2,po1,po2)
                break
        turn=turn+1
  
play()




