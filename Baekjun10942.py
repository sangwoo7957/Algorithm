import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
dp = [[0] * n for _ in range(n)]
for i in range(n):
    for start in range(n):
        end = start + i
        if end >= n:
            break
        if start == end:
            dp[start][end] = 1
            continue
        if start + 1 == end:
            if arr[start] == arr[end]:
                dp[start][end] = 1
                continue
        if arr[start] == arr[end] and dp[start+1][end-1]:
            dp[start][end] = 1

m = int(input())
for i in range(m):
    s, e = map(int, input().split())
    print(dp[s - 1][e - 1])