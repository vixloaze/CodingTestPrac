def solution(a,b,c):
    for i in range(c):
        a = (a%b)*10
        answer = a // b  
    return answer

a,b,c = map(int, input().split())

print(solution(a,b,c))