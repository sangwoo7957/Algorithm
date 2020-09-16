n, m = map(int, input().split())
num_list = [i+1 for i in range(n)]
check_list = [False] * n
arr = []

def solution(cnt):
    if (cnt == m):
        print(*arr)
        return

    for i in range(0, n):
        if (check_list[i]):
            continue

        check_list[i] = True
        arr.append(num_list[i])
        solution(cnt+1)
        arr.pop()
        for j in range(i+1, n):
            check_list[j] = False

solution(0)