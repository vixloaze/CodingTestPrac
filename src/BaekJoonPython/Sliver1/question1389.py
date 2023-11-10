import sys
from collections import deque

def bfs(graph, start):
    num = [0] * (N+1)
    visited = [start]
    queue = deque()
    queue.append(start)
    
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if i not in visited:
                num[i] = num[v] +1
                visited.append(i)
                queue.append(i)
    return sum(num)

input = sys.stdin.readline

N, M= map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = []

for i in range(1, N+1):
    result.append(bfs(graph,i))

print(result.index(min(result))+1)