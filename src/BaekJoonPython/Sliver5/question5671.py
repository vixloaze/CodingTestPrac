import sys

while True:
    try:
        N, M = map(int, sys.stdin.readline().split())
        cnt = 0
        for i in range(N, M+1):
            num = str(i)
            numList = list(num)
            # set으로 만드는 순간 중복이 제거 되어서 만들어 집니다.
            numSet = set(num)
            if len(numList) == len(numSet): cnt+=1
        print(cnt)
    except:
        break
    