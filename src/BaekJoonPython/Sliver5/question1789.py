num = int(input())

sum=0
result=0

for i in range(1,num+1):
    sum += i
    result += 1
    if sum > num:
        result -= 1
        break

print(result)