t = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    queue = [[i, j]]
    while queue:
        a, b = queue[0][0], queue[0][1]
        queue.pop(0)
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < n and 0 <= y < m and arr[x][y] == 1:
                arr[x][y] = 0
                queue.append([x, y])

for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    cnt = 0
    for i in range(k):
        a, b = map(int, input().split())
        arr[b][a] = 1

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)