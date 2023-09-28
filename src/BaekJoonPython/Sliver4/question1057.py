import sys

people, n, m = map(int, sys.stdin.readline().split())
count = 0
while n!= m:
    n -= n // 2 
    m -= m // 2
    count +=1
print(count)