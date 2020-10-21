from collections import deque
import sys
input = sys.stdin.readline
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    while queue:
        a, b, c = queue.popleft()
        visit[c][a][b] = 1
        for i in range(6):
            x = a + dx[i]
            y = b + dy[i]
            z = c + dz[i]
            if 0 <= x < n and 0 <= y < m and 0 <= z < h and arr[z][x][y] == 0 and visit[z][x][y] == 0:
                queue.append([x, y, z])
                arr[z][x][y] = arr[c][a][b] + 1
                visit[z][x][y] = 1

m, n, h = map(int, input().split())
arr = [[] for _ in range(h)]
visit = [[[0 for i in range(m)] for i in range(n)] for i in range(h)]
queue = deque()
isTrue = False
st = False
for i in range(h):
    for j in range(n):
        arr[i].append(list(map(int, input().split())))

for z in range(h):
    for x in range(n):
        for y in range(m):
            if arr[z][x][y] == 1:
                queue.append([x, y, z])

bfs()
result = -2
for z in range(h):
    for x in range(n):
        for y in range(m):
            if arr[z][x][y] == 0:
                isTrue = True
            result = max(result, arr[z][x][y])

if isTrue == True:
    print(-1)
else:
    print(result -1)