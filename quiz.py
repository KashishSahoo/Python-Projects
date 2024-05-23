questions=("How many elements are there in periodic table?:",
           "Which animal lays the largest egg?:",
           "Most abundant gas in earth atmosphere?:",
           "How many bones are there in human body?:",
           "Hottest Planent In solar system?:")

options=(("A.116 ","B.117 ","C.118 ","D.119 "),
         ("A.Whale. ","B.Crocodile","C.Elephant ","D.Ostritch "),
         ("A.Nitrogen ","B.Oxygen ","C.Carbon Dioxide ","D.Hydrogen "),
         ("A.206 ","B.207 ","C.208 ","D.209 "),
         ("A.Mercury ","B.Venus","C.Earth ","D.Mars "))

answers=("C","D","A","A","B")
guesses=[]
score=0
question_num=0

for question in questions:
    print("---------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess=input("Enter (A,B,C,D):").upper()
    guesses.append(guess)
    if guess==answers[question_num]:
        score+=1
        print("Correct")
    else:
        print("Incorrect")
        print(f"{answers[question_num]} is correct answer")
    question_num+=1


print("----------------")
print("****RESULTS****")
print("answers:",end="")
for answer in answers:
    print(answer,end=" ")
print()

print("Guesses:",end="")
for guess in guesses:
    print(guess,end=" ")
print()

print(f"Your Score={score} out of {len(questions)}")
s=int(score/len(questions)*100)
print(f"Total Percentage={s}%")