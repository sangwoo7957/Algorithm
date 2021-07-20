n = int(input())
v = int(input())

def dfs(start):
    check[start] = 1
    for i in range(1, n+1):
        if check[i] == 0 and arr[start][i] == 1:
            dfs(i)

arr = [[0] * (n+1) for _ in range(n+1)]
check = [0] * (n+1)
answer = -1
for _ in range(v):
    s, e = map(int, input().split())
    arr[s][e] = arr[e][s] = 1

dfs(1)
for i in range(1, n+1):
    if check[i] == 1:
        answer += 1
print(answer)