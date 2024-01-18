#우선순위큐를 활용한 문제
#강의 시작시간으로 배열을 정렬 하고 힙에는 강의끝나는 시간을 추가한다
#배열을 순회하며 힙에 있는 강의 중 가장 일찍 끝나는 강의(최소힙)가 현재 순회중인
#강의시작 시간보다 늦게 끝나면 힙에 순회중인 강의 추가, else: 최소힙을 pop 한다.
import heapq

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key = lambda x:x[1]) # 시작 시간으로 오름차순 정렬

min_heap = []
count = 0

#다른 수업 시간과 겹치지 않으면 이전 수업 pop
for i in arr:
    while min_heap and min_heap[0]<=i[1]: #가장 일찍 끝나는 수업보다 늦게 시작하면(겹치지 않으면)
        heapq.heappop(min_heap) #heap에서 가장 작은 원소 내보냄
    heapq.heappush(min_heap, i[2]) #i 수업의 끝나는 시간 힙에 추가
    count = max(count, len(min_heap))

print(count)

