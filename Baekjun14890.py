import sys
input = sys.stdin.readline

def check(path):
    current = path[0]
    visited = [False for _ in range(n)]

    for i, height in enumerate(path):
        if current == height:
            continue
        elif current + 1 == height:
            for j in range(i-1, i-1-l, -1):
                if j < 0 or current != path[j] or visited[j] == True:
                    return False
                visited[j] = True
            current = height
        elif current - 1 == height:
            for j in range(i, i+l):
                if j >= n or current - 1 != path[j] or visited[j] == True:
                    return False
                visited[j] = True
            current = height
        else:
            return False
    return True

def solution():
    answer = 0
    for i in range(n):
        if check(arr[i]):
            answer += 1

    for j in range(n):
        path = []
        for i in range(n):
            path.append(arr[i][j])

        if check(path):
            answer += 1

    print(answer)

n, l = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

solution()