import heapq, sys
input = sys.stdin.readline

INF = int(1e9)

n,m = map(int, input().split())

graph = [[] for i in range(n+1)]

for _ in range(m):
    a,b,c = map(int , input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1, v2 = map(int,input().split())

def dijkstra(start):
    distance = [INF] * (n+1)
    q= []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

# 출발점이 각각 1, v1, v2일 때의 최단 거리 배열
ori_distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

# 1-> v1 -> v2 -> n 인 최소 경로
v1_path = ori_distance[v1] + v1_distance[v2] + v2_distance[n]
# 1-> v2 -> v1 -> n 인 최소 경로
v2_path = ori_distance[v2] + v2_distance[v1] + v1_distance[n]

result = min(v1_path, v2_path )
print(result if result < INF else -1)