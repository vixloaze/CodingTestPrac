import sys

input = sys.stdin.readline

n = int(input())

dp = [[0]* 10 for _ in range(n)]

dp[0][0] = 0
for i in range(1,10):
    dp[0][i] = 1

for i in range(1,n):
    for j in range(10):
        # 끝 자리 수 0일 경우 전 길이 수의 끝 자리 수(0) +1에 해당하는 값 저장
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        # 끝 자리 수 1 ~ 8일 경우 전 길이 수에서 끝자리수 -1, +1에 해당하는 값을 더하기
        elif 0 < j < 9:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
        # 끝 자리 수 9일 경우 전 길이 수의 끝 자리 수(9) -1에 해당하는 값 저장
        else:
            dp[i][j] = dp[i-1][j-1]

sum = 0

for i in range(10):
    sum += dp[n-1][i]
print(sum % 1000000000)