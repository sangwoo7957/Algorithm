def solution():
    distances = [[inf for _ in range(v+1)] for _ in range(v+1)]
    for _ in range(e):
        a, b, c = map(int, input().split())
        distances[a][b] = min(c, distances[a][b])

    for k in range(1, v+1):
        for i in range(1, v+1):
            for j in range(1, v+1):
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
    return distances

v, e = map(int, input().split())
inf = 100000000
arr = solution()
answer = inf
for i in range(1, v+1):
    answer = min(answer, arr[i][i])
if answer == inf:
    print(-1)
else:
    print(answer)