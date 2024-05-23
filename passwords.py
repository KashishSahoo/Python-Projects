import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','$','%','&','(',')','*','+','-','/']
print("Welcome To Password Generator")
n_letters=int(input("How Many Letters You Want In Your Password="))
n_symbols=int(input("How Many Symbols You Want In Your Password="))
n_numbers=int(input("How Many numbers You Want In Your Password="))
password=[]
for i in range(1,n_letters+1):
    char=random.choice(letters)
    password+=char
for i in range(1,n_symbols+1):
    char=random.choice(symbols)
    password+=char
for i in range(1,n_numbers+1):
    char=random.choice(numbers)
    password+=char

random.shuffle(password)
p=""
for i in password:
    p+=i
print(p)
