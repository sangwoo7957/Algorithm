import sys
import heapq

INF = sys.maxsize

def Dijkstra(start):
    q = []
    heapq.heappush(q, [0, start])
    result = [INF for _ in range(V + 1)]
    result[start] = 0
    while q:
        dis, s = heapq.heappop(q)
        if dis > result[s]:
            continue
        for d, x in G[s]:
            d += dis
            if d < result[x]:
                result[x] = d
                heapq.heappush(q, [d, x])
    return result

V, E = map(int, sys.stdin.readline().split())

G = [[] for _ in range(V + 1)]
for _ in range(E):
    start, end, distance = map(int, sys.stdin.readline().split())
    G[start].append([distance, end])
    G[end].append([distance, start])

D1, D2 = map(int, sys.stdin.readline().split())

dis1 = Dijkstra(1)
dis2 = Dijkstra(D1)
result1 = dis1[D1] + dis2[D2] + Dijkstra(D2)[V]
result2 = dis1[D2] + dis2[D2] + dis2[V]

if result2 >= INF and result1 >= INF:
    print(-1)
else:
    print(min(result1, result2))