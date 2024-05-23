import random
import datetime

birth_day=[]
birth=[]
bday=[]
years=[]

ul=[]
dl=[]
f={}
i=0
while(i<50):
    year=random.randint(1895,2017)
    if(year%4==0 and year%100!=0 or year%400==0):
        leap=1
    else:
        leap=0
    month=random.randint(1,12)

    if (month==2 and leap==1):
        day=random.randint(1,29)
    elif(month==2 and leap==0):
        day=random.randint(1,28)
    elif(month==7 or month==8):
        day=random.randint(1,31)
    elif(month%2!=0 and month<7):
        day=random.randint(1,31)
    elif(month%2==0 and month>7 and month<12):
        day=random.randint(1,31)
    else:
        day=random.randint(1,30)

    dd=datetime.date(year,month,day)
    y=dd.strftime("%Y")
    years.append(y)

    # dd_mm=datetime.date(year,month)
    day_of_year=dd.timetuple().tm_yday
    i=i+1
    birth_day.append(dd)

    # birth.append(dd_mm)
    bday.append(day_of_year)
birth.sort()
i=0
while(i<50):
    # print(birth_day[i])
    # print(birth[i])
    # print(bday[i])
    print(years[i])
    i=i+1
for i in years:
    if i not in ul:
        ul.append(i)
    elif i not in dl:
        dl.append(i)
print(dl)
print()

for item in years:
    if item in f:
        f[item]+=1
    else:
        f[item]=1

for key,value in f.items():
    if value>1:
        print(f"{key}:{value}")


