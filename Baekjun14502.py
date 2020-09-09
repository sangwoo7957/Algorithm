n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
virus = []
num_virus = 9999
safe = -3

def dfs(x, y):
    res = 1
    visited[x][y] = True
    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):  # 위, 아래, 좌, 우
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:  # 맵의 경계보다 커진다면
            continue  # 넘어간다.
        if not (visited[nx][ny] or board[nx][ny]):  # 방문하지 않았거나, 빈칸이 아니라면
            res += dfs(nx, ny)
    return res

def solve(start, wall):
    global n, m, num_virus, visited
    if wall == 3: # 벽이 3개라면
        count = 0
        visited = [[False]*m for _ in range(n)]
        for x, y in virus:
            count += dfs(x, y)
        num_virus = min(num_virus, count)
        return
    for i in range(start, n*m): # 2차원 배열에서 x, y의 조합을 뽑습니다.
        x = i // m
        y = int(i % m)
        if board[x][y] == 0: # 빈칸(0) 이라면
            board[x][y] = 1 # 벽(1)을 세운다
            solve(i+1, wall+1)
            board[x][y] = 0 # 위에서 세운 벽을 다시 빈칸(0)으로 만든다. (초기화)

for i in range(n):
    for j in range(m):
        if board[i][j] != 1:
            safe += 1
        if board[i][j] == 2:
            virus.append((i, j))

solve(0, 0)
print(safe - num_virus)