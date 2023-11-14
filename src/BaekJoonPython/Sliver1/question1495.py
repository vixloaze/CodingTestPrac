import sys
input = sys.stdin.readline

N, S, M= map(int, input().split())
volunm = list(map(int,input().split()))

dp = [[0]* (M+1) for _ in range(N+1)]

dp[0][S] = 1

for i in range(1, N+1):
    for j in range(M+1):
        if dp[i-1][j] != 0:
            if 0 <= j+volunm[i-1] <= M:
                dp[i][j+volunm[i-1]] = 1
            if 0 <= j-volunm[i-1] <= M:
                dp[i][j-volunm[i-1]] = 1

ans = -1
# 볼륨의 최대값을 출력하기 위해 내림차순으로 반복문 실행
for i in range(M, -1, -1):
    if dp[N][i]==1: # 최대값 발견하면 중단
        ans = i
        break

print(ans)