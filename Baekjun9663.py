import sys
n, answer = int(sys.stdin.readline()), 0
a, b, c = [False] * n, [False] * (2*n-1), [False] * (2*n-1)

def solution(cnt):
    global answer
    if cnt == n:
        answer += 1
        return

    for i in range(n):
        if (not a[i] and not b[cnt+i] and not c[cnt-i+n-1]):
            a[i] = b[cnt+i] = c[cnt-i+n-1] = True
            solution(cnt+1)
            a[i] = b[cnt+i] = c[cnt-i+n-1] = False

solution(0)
print(answer)