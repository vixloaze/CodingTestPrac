import sys
sys.setrecursionlimit(1000000)

input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
parents = [0 for _ in range(N+1)]

for _ in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, start, visited):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            parents[i] = start
            dfs(graph, i , visited)

dfs(graph, 1, visited)

for i in range(2, N+1):
    print(parents[i])