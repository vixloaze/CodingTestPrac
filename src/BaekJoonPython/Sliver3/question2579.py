import sys

n = int(sys.stdin.readline().strip())
stair = [int(sys.stdin.readline().strip()) for _ in range(n)]

dp = [0] * (n)
if len(stair) <= 2:
    print(sum(stair))
else:
    dp[0] = stair[0]
    dp[1] = stair[0]+stair[1]

    for i in range(2, n):
        dp[i] = max(dp[i-3]+stair[i-1]+stair[i] , dp[i-2]+stair[i])
    
    print(dp[-1]) # 최대값이 dp에 계속 저장되는 형식이라서 맨 마지막 것 출력하면 됨