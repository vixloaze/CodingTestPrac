def solution (list):
    for i in range(len(list)):
        for j in range(len(list) - i - 1):
            if list[j][2] < list[j+1][2]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

cnt=0
num = int(input())
scorelist =[ list(map(int, input().split())) for _ in range(num)]

answer = solution(scorelist)

for i in range(2):
    print(answer[i][0], answer[i][1])

if answer[0][0] == answer[1][0]: cnt+=1

for i in range(2, num):
    if cnt == 0:
        print(answer[i][0], answer[i][1])
        break
    else:
        if answer[1][0] != answer[i][0]:
            print(answer[i][0], answer[i][1])
            break