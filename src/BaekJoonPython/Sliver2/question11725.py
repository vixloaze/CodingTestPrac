import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
parents = [0 for _ in range(N+1)]

for _ in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True # 현재 노드 방문 처리 
    while queue:
        v = queue.popleft() # 큐에서 하나 원소 출력
        for i in graph[v]: # 해당 원소와 연결된 아직 방문하지 않은 원소를 큐에 삽입
            if not visited[i]:
                parents[i] = v
                queue.append(i)
                visited[i] = True

bfs(graph, 1, visited)

for i in range(2, N+1):
    print(parents[i])