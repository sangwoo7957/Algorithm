n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

def solution():
    answer = 0
    for i in range(n):
        if a[i] > 0:
            a[i] -= b
            answer += 1
        if a[i] > 0:
            answer += a[i] // c
            if a[i] % c != 0:
                answer += 1

    return answer

print(solution())
