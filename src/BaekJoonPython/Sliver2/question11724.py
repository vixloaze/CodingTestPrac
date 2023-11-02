import sys
from collections import deque

input = sys.stdin.readline

N, M= map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

cnt = 0 
visited = [False] * (N+1)

for i in range(1, N+1):
    if not visited[i]:
        bfs(graph, i ,visited)
        cnt +=1

print(cnt)

