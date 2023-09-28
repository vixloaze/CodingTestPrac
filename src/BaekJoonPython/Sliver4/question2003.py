import sys

n, m = map(int, sys.stdin.readline().split())
numlist = list(map(int,sys.stdin.readline().split()))

count = 0
interval_sum = 0
end = 0

for start in range(n):
    while interval_sum < m and end < n:
        interval_sum += numlist[end] 
        end += 1
    if interval_sum == m:
        count += 1
    interval_sum -= numlist[start]

print(count)