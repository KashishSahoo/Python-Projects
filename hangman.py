import random
import hangman_stages
import word_file

chosen_word=random.choice(word_file.words)
print("Welcome To Hangman Game:'Here Computer Will Choose A Random Word '")
print("And You Have To Guess It And You Have Only 6 Lives.")
print("\n")
#print(chosen_word)
display=[]
lives=6

for i in range(len(chosen_word)):
    display+='_'
print(display)
game_over=False

while not game_over:
    guessed_letter=input("Guess A Letter=").lower()

    for position in range(len(chosen_word)):
        letter=chosen_word[position]

        if letter==guessed_letter:
            display[position]=guessed_letter
    print(display)

    if guessed_letter not in chosen_word:
        lives-=1

        if lives==0:
            game_over=True
            print("You Loose!!")
    if '_' not in display:
        game_over=True
        print("You Win!!")
    print(hangman_stages.stages[lives])