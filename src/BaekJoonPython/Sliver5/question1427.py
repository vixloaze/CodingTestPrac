num = int(input())

answer = list(str(num))

for i in range(len(answer)):
    for j in range(len(answer)- i -1):
        if int(answer[j]) < int(answer[j+1]):
            answer[j], answer[j+1] = answer[j+1], answer[j]

str = ''.join(answer)
print(str)