import sys
from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def change(d):
    if d == 0:
        return 3
    elif d == 1:
        return 0
    elif d == 2:
        return 1
    elif d == 3:
        return 2

def back(d):
    if d == 0:
        return 2
    elif d == 1:
        return 3
    elif d == 2:
        return 0
    elif d == 3:
        return 1

def solution(row, col, d):
    cnt = 1
    arr[row][col] = 2
    q = deque([[row, col, d]])

    while q:
        row, col, d = q.popleft()
        temp_d = d

        for i in range(4):
            temp_d = change(temp_d)
            new_row, new_col = row + dy[temp_d], col + dx[temp_d]

            if 0 <= new_row < n and 0 <= new_col < m and arr[new_row][new_col] == 0:
                cnt += 1
                arr[new_row][new_col] = 2
                q.append([new_row, new_col, temp_d])
                break

            elif i == 3:
                new_row, new_col = row + dy[back(d)], col + dx[back(d)]
                q.append([new_row, new_col, d])

                if arr[new_row][new_col] == 1:
                    return cnt

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

print(solution(r, c, d))