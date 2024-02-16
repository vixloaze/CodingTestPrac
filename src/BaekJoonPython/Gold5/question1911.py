import sys
input = sys.stdin.readline

n, l = map(int, input().split())

puddles = [(list(map(int,input().split()))) for _ in range(n)]

puddles.sort(key=lambda x : x[0])
result = 0
boundary = puddles[0][0]

for start, end in puddles:
    if start > boundary:
        boundary = start
    diff = end-boundary
    if diff % l == 0:
        count=diff//l
        boundary = end
    else:
        count = diff//l + 1
        boundary = end + (l - diff%l) # l - diff%l 은 초과분 (예시 널빤지 크기 3인데 5인 면적을 덮었을 경우 2개를 쓰고 1이 남음)
    result += count

print(result)