import sys
from collections import deque

input = sys.stdin.readline

com = int(input())
n = int(input())
graph = [[] for _ in range(com+1)]

visited = [False] * (com+1)

for i in range(n):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) # 양방향 고려

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True # 현재 노드 방문 처리 
    cnt = 0
    while queue:
        v = queue.popleft() # 큐에서 하나 원소 출력
        for i in graph[v]: # 해당 원소와 연결된 아직 방문하지 않은 원소를 큐에 삽입
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                cnt +=1
    return cnt

print(bfs(graph,1,visited))               