def game(num1,num2,bit1,bit2):
    p1=int(num1[bit1])%3
    p2=int(num2[bit2])%3
    pp1=0
    pp2=0
    if(player1[p1]==player2[p2]):
        print(f"Player 1:{player1[p1]} And Player 2:{player2[p2]}")
        print("Draw")
    elif(player1[p1]=="Rock" and player2[p2]=="Scissor"):
        print(f"Player 1:{player1[p1]} And Player 2:{player2[p2]}")
        pp1+=1
        print("Player One Wins ")
    elif(player1[p1]=="Rock" and player2[p2]=="Paper"):
        print(f"Player 1:{player1[p1]} And Player 2:{player2[p2]}")
        pp2+=1
        print("Player Two Wins ")
    elif(player1[p1]=="Paper" and player2[p2]=="Scissor"):
        print(f"Player 1:{player1[p1]} And Player 2:{player2[p2]}")
        pp2+=1
        print("Player Two Wins ")
    elif(player1[p1]=="Paper" and player2[p2]=="Rock"):
        print(f"Player 1:{player1[p1]} And Player 2:{player2[p2]}")
        pp1+=1
        print("Player One Wins ")
    elif(player1[p1]=="Scissor" and player2[p2]=="Rock"):
        print(f"Player 1:{player1[p1]} And Player 2:{player2[p2]}")
        pp2+=1
        print("Player Two Wins ")
    elif(player1[p1]=="Scissor" and player2[p2]=="Paper"):
        print(f"Player 1:{player1[p1]} And Player 2:{player2[p2]}")
        pp1+=1
        print("Player One Wins ")

player1={0:'Rock',1:'Paper',2:'Scissor'}
player2={0:'Paper',1:'Rock',2:'Scissor'}

while(1):
    n1=input("Player 1:Enter Your Choice=")
    n2=input("Player 2:Enter Your Choice=")
    print()

    bit1=int(input("Player 1:Enter The Secret Bit Position="))
    bit2=int(input("Player 2:Enter The Secret Bit Position="))
    print()

    game(n1,n2,bit1,bit2)

    print()
    print(f"SCORES:Player1={pp1} And Player2={pp2}")
    ch=input("Do You Want To Continue?y/n=")

    if(ch=='n'):
        break