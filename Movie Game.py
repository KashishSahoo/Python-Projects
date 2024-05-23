import random
movie = ["black friday", "tare zamin par", "nayak", "cargo","chuha billi", "saand ki atma", "corona ki jawani", "shila ki sardi","annkho dekhi", "chudiya ki prem katha","masaan"]

def create_question(movie):
    n = len(movie)
    letter = list(movie)
    temp = []
    for i in range(n):
        if letter[i]==" ":
            temp.append(" ")
        else:
            temp.append("*")
    qn="".join(str(x) for x in temp)
    return qn
def is_present(letter,movie):
    c=movie.count(letter)
    if c ==0:
        return False
    else:
        return True
def unlock(qn,movie,letter):
    ref=list(movie)
    qn_list =list(qn)
    temp =[]
    n=len(movie)
    for i in range(n):
        if ref[i]==" " or ref[i]==letter:
            temp.append(ref[i])
        else:
            if qn_list[i]=="*":
                temp.append("*")
            else:
                temp.append(ref[i])
    qn_new="".join(str(x) for x in temp)
    return qn_new
def play():
    player1 = input("player1 please enter your name=")
    player2 = input("player2 please enter your name=")
    pp1 = 0
    pp2 = 0
    turn = 0
    willing = True
    while willing:
        if turn%2==0:
            print(f"Its {player1} trun")
            picked_movie = random.choice(movie)
            qn = create_question(picked_movie)
            print (qn)
            modified_qn = qn
            not_said = True
            while not_said:
                letter = input("your letter: ")
                if(is_present(letter,picked_movie)):
                    modified_qn=unlock(modified_qn,picked_movie,letter)
                    print(modified_qn)
                    d = int(input("press 1 for movie and 2 for another letter: "))
                    if d ==1:
                        ans = input("enter your answer=")
                        if ans == picked_movie:
                            pp1=pp1+1
                            print("correct")
                            not_said = False
                            print(player1,"your score", pp1)
                        else:
                            print("wrong answer try again")
                    #else:
                        #print (letter,"not found")
            c = int(input("press 1 to continue 0 to exit"))
            if c ==0:
                print(player1,"your score:", pp1)
                print(player2,"your score:", pp2)
                turn = turn+1
        
                
        else:
            print(f"Its {player2} trun")
            picked_movie = random.choice(movie)
            qn = create_question(picked_movie)
            print (qn)
            modified_qn = qn
            not_said = True
            while not_said:
                letter = input("your letter: ")
                if(is_present(letter,picked_movie)):
                    modified_qn=unlock(modified_qn,picked_movie,letter)
                    print(modified_qn)
                    d = int(input("press 1 for movie and 2 for another letter: "))
                    if d ==1:
                        ans = input("enter your answer=")
                        if ans == picked_movie:
                            pp2=pp2+1
                            print("correct")
                            not_said = False
                            print(player2,"your score", pp2)
                        else:
                            print("wrong answer try again")
                    else:
                        print (letter,"not found")
            c = int(input("press 1 to continue 0 to exit"))
            if c ==0:
                print(player1,"your score:", pp1)
                print(player2,"your score:", pp2)
                willing = False
        turn = turn+1
play()