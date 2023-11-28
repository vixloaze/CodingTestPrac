from collections import deque

M, N= map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = deque()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i,j))

def bfs():
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if -1< nx <N and -1< ny <M:
                if graph[nx][ny] == -1:
                    continue
                if graph[nx][ny] == 0:
                    queue.append([nx,ny])
                    graph[nx][ny] = graph[x][y] + 1

bfs()
ans =0
for line in graph:
    for tomato in line:
        if tomato == 0:
            print(-1)
            exit()
    ans = max (ans, max(line))

print(ans -1)