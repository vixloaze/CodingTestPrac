import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

visited = [False] * (N+1)
visited2 = [False] * (N+1)

for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) # 양방향 고려

# 단, 방문할 수 있는 정점이 여러 개인 경우에는 
# 정점 번호가 작은 것을 먼저 방문해야 하기 때문에 오름차순 정렬한다
for i in graph:
    i.sort() 
    

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i , visited)
    
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True # 현재 노드 방문 처리 
    while queue:
        v = queue.popleft() # 큐에서 하나 원소 출력
        print(v, end=' ')
        for i in graph[v]: # 해당 원소와 연결된 아직 방문하지 않은 원소를 큐에 삽입
            if not visited[i]:
                queue.append(i)
                visited[i] = True

dfs(graph, V, visited)
print()
bfs(graph, V, visited2)