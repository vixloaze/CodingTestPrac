import sys

num = int(input())

cnt = 0

while True:
    if num % 5 == 0:
        cnt += num // 5
        break
    else:
        num -= 3
        cnt += 1
    
    if num <0:
        break

if num<0: print(-1)
else: print(cnt)