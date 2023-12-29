import heapq, sys
input = sys.stdin.readline

n = int(input())

# 강의 시작 시간 기준 정렬
lecture = sorted([list(map(int,input().split())) for _ in range(n)])
room = []

heapq.heappush(room, lecture[0][1]) # 첫 강의 끝나는 시간

for i in range(1, n):
    if lecture[i][0] < room[0]: # 강의의 시작 시간이 첫 강의 끝나는 시간보다 짧으면
        heapq.heappush(room,lecture[i][1]) #새로운 강의실에
    else:
        heapq.heappop(room) # 기존 강의 빼내고
        heapq.heappush(room, lecture[i][1]) # 새로운 강의 삽입

print(len(room))