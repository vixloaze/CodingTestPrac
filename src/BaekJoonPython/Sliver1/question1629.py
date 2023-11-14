import sys

input = sys.stdin.readline

A,B,C= map(int, input().split())

## 나머지 분배 법칙 (AxB)%C = (A%C)x(B%C)%C
def power(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a%C ## 나머지 분배 법칙 
    
    x = power(a, n//2)
    
    if n % 2 == 0:
        return (x * x) % C
    else:
        return (x  * x * a) % C

print(power(A,B))

