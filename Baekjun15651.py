n, m = map(int, input().split())
num_list = [i+1 for i in range(n)]
check_list = [False] * n
arr = []

def solution(cnt):
    if (cnt == m):
        print(*arr)
        return

    for i in range(n):
        check_list[i] = True
        arr.append(num_list[i])
        solution(cnt+1)
        arr.pop()
        check_list[i] = False

solution(0)