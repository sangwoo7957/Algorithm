import sys

N = int(sys.stdin.readline())
W = []
INF = sys.maxsize
for _ in range(N):
    W.append(list(map(int, sys.stdin.readline().split())))
DP = [[None] * (1 << N) for _ in range(N)]


def find_path(last, visited):
    if visited == (1 << N) - 1:
        return W[last][0] or INF

    if DP[last][visited] is not None:
        return DP[last][visited]  # 있는값 반환

    tmp = INF
    for city in range(N):
        if visited & (1 << city) == 0 and W[last][city] != 0:
            tmp = min(tmp, find_path(city, visited | (1 << city)) + W[last][city])
    DP[last][visited] = tmp
    return tmp


print(find_path(0, 1 << 0))
