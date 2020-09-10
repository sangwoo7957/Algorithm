from itertools import combinations

def solution():
    global answer

    for i in combinations(num_list, n // 2):
        start_member = list(i)
        link_member = list(set(num_list) - set(i))

        start_comb = list(combinations(start_member, 2))
        link_comb = list(combinations(link_member, 2))

        start_sum = 0
        for x, y in start_comb:
            start_sum += (arr[x][y] + arr[y][x])

        link_sum = 0
        for x, y in link_comb:
            link_sum += (arr[x][y] + arr[y][x])

        if (answer > abs(start_sum - link_sum)):
            answer = abs(start_sum - link_sum)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
num_list = [i for i in range(n)]
answer = float('inf')
solution()
print(answer)