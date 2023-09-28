import sys

n = int(sys.stdin.readline().strip())

numlist = [int(sys.stdin.readline().strip()) for _ in range(n)]
numlist = sorted(numlist)
temp = []

for i in range(0,n):
    cnt = 0
    for j in range(numlist[i], numlist[i]+5):
        if j not in numlist:
            cnt += 1
    temp.append(cnt)

print(min(temp))