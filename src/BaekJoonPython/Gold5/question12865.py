import sys

n, k = map(int, input().split())

lst = [[0,0]]

for _ in range(n):
    lst.append(list(map(int, input().split())))

dp = [ [0]* (k+1) for _ in range(n+1)]

#물건을 넣지 않았을 때 총 가치 0으로 설정
for i in range(k+1): 
    dp[0][i] = 0

for i in range(1, n+1):
    for j in range(1, k+1):
        weight = lst[i][0]
        value = lst[i][1]

        if weight > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - weight]+value)

print(dp[n][k])
