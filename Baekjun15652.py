n, m = map(int, input().split())
num_list = [i+1 for i in range(n)]
check_list = [False] * n
arr = []

def solution(cnt, idx):
    if (cnt == m):
        print(*arr)
        return

    for i in range(idx, n):
        arr.append(i+1)
        solution(cnt+1, i)
        arr.pop()

solution(0, 0)