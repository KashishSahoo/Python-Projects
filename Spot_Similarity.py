import string
import random
symbols=[]
symbols=list(string.ascii_letters)
card1=[0]*5
card2=[0]*5
pos1=random.randint(0,4)
pos2=random.randint(0,4)
#pos1 and pos2 are same symbols in card1 and card2
same_symbol=random.choice(symbols)
symbols.remove(same_symbol)
if(pos1==pos2):
    card1[pos1]=same_symbol
    card2[pos1]=same_symbol
else:
    card1[pos1]=same_symbol
    card2[pos2]=same_symbol

    card1[pos2]=random.choice(symbols)
    symbols.remove(card1[pos2])
    card2[pos1]=random.choice(symbols)
    symbols.remove(card2[pos1])
i=0
while(i<5):
    if(i!=pos1 and i!=pos2):
        a1=random.choice(symbols)
        symbols.remove(a1)

        a2=random.choice(symbols)
        symbols.remove(a2)

        card1[i]=a1
        card2[i]=a2
    i=i+1
print(card1)
print(card2)

ch=input("Spot The Similar Symbol=")

if(ch==same_symbol):
    print("Correct Answer")
else:
    print("Better Luck Next Time")

