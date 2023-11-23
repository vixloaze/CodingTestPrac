import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline

def dfs(x,y):
    
    dx = [1,-1,0,0,1,1,-1,-1]
    dy = [0,0,1,-1,1,-1,1,-1]
    
    global checked
    
    visited[x][y] = True
    
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
    
        if -1< nx <N and -1 < ny <M :
            if graph[x][y] <  graph[nx][ny]:
                checked = False
            if not visited[nx][ny] and graph[nx][ny] == graph[x][y]:
                dfs(nx,ny)
                
N, M= map(int, input().split())

graph = []
visited = [[False] *M for _ in range(N)]

for i in range(N):
    graph.append(list(map(int, input().split())))

result = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] != 0 and not visited[i][j]:
            checked = True
            dfs(i,j)
            
            if checked:
                result +=1
            
print(result)
            