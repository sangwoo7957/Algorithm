n, m = map(int, input().split())
queue = []
arr = [list(input()) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
queue = [[0, 0]]
arr[0][0] = 1
while queue:
    a, b = queue[0][0], queue[0][1]
    queue.pop(0)
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < n and 0 <= y < m and arr[x][y] == "1":
            arr[x][y] = arr[a][b] + 1
            queue.append([x, y])

print(arr[-1][-1])