from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    cnt = 0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >=n or ny >= m:
                continue
            if graph[nx][ny] != "X" and not visited[nx][ny]:
                queue.append((nx,ny))
                visited[nx][ny] = True
                if graph[nx][ny] == "P":
                    cnt += 1
    return print(cnt if cnt > 0 else 'TT')

n, m = map(int, input().split())

graph = list(input() for _ in range(n))
visited = [[False]*m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            bfs(i,j)



