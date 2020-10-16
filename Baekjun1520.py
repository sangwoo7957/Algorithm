m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
dp = [[-1] * n for _ in range(m)]

def solution(x, y):
    if x == 0 and y == 0:
        return 1
    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if arr[x][y] < arr[nx][ny]:
                    dp[x][y] += solution(nx, ny)
    return dp[x][y]

print(solution(m-1, n-1))