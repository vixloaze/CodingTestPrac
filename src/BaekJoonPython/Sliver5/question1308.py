from datetime import *

today = list(map(int,input().split()))
d_day = list(map(int,input().split()))

if(today[0] + 1000 < d_day[0]):
    print('gg')
elif(today[0] + 1000 == d_day[0] and (today[1], today[2]) <= (d_day[1],d_day[2])):
    print('gg')
else:
    today = date(*today)
    d_day = date(*d_day)
# toordinal() : 역산 그레고리력 서수를 돌려줍니다. 1년 1월 1일의 서수는 1입니다
    print("D-"+str(d_day.toordinal()- today.toordinal()))