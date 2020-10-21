n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
cnt = []

def bfs(i, j):
    queue = [[i, j]]
    arr[i][j] = 0
    count = 1
    while queue:
        a, b = queue[0][0], queue[0][1]
        queue.pop(0)
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < n and 0 <= y < n and arr[x][y] == 1:
                arr[x][y] = 0
                queue.append([x, y])
                count += 1
    cnt.append(count)

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            bfs(i, j)

cnt.sort()
print(len(cnt))
for i in cnt:
    print(i)