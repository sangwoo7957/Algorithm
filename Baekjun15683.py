cctv_allcase = []

up, right, down, left = 0, 1, 2, 3
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

def watch(x, y, dir):
    return_set = set()
    for d in dir:
        new_x = x
        new_y = y
        while True:
            new_x = new_x + dx[d]
            new_y = new_y + dy[d]
            if not (0 <= new_x < n and 0 <= new_y < m):
                break
            if arr[new_x][new_y] == 6:
                break
            if arr[new_x][new_y] == 0:
                return_set.add((new_x, new_y))
    return return_set

def dfs(n, union_set):
    global max_v
    if n == len(cctv_allcase):
        if max_v < len(union_set):
            max_v = len(union_set)
        return
    for i in cctv_allcase[n]:
        dfs(n + 1, union_set | i)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

empty = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            empty = empty + 1
        elif arr[i][j] == 1:
            cctv_allcase.append([watch(i, j, [up]), watch(i, j, [right]), watch(i, j, [down]), watch(i, j, [left])])
        elif arr[i][j] == 2:
            cctv_allcase.append([watch(i, j, [up, down]), watch(i, j, [right, left])])
        elif arr[i][j] == 3:
            cctv_allcase.append([watch(i, j, [up, right]), watch(i, j, [right, down]), watch(i, j, [down, left]),
                                 watch(i, j, [left, up])])
        elif arr[i][j] == 4:
            cctv_allcase.append(
                [watch(i, j, [up, right, down]), watch(i, j, [right, down, left]), watch(i, j, [down, left, up]),
                 watch(i, j, [left, up, right])])
        elif arr[i][j] == 5:
            cctv_allcase.append([watch(i, j, [up, right, down, left])])

max_v = 0
dfs(0, set())

print(empty - max_v)