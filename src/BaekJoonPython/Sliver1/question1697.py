import sys
from collections import deque

input = sys.stdin.readline

def bfs(x):
    queue = deque()
    queue.append(x)
    while queue:
        x = queue.popleft()
        if x == K:
            return visited[x]
        for i in (x-1, x+1, 2*x):
            if 0 <= i < MAX and not visited[i]:
                visited[i] = visited[x] + 1
                queue.append(i)
    

MAX = 100001
N, K= map(int, input().split())
visited = [0] * MAX 
print(bfs(N))