import sys
from collections import deque

wheels = []
rotates = []

def turnLeft(i, dir):
    if i < 0:
        return

    if wheels[i][2] != wheels[i + 1][6]:
        turnLeft(i - 1, -dir)
        wheels[i].rotate(dir)

def turnRight(i, dir):
    if i > 3:
        return

    if wheels[i][6] != wheels[i - 1][2]:
        turnRight(i + 1, -dir)
        wheels[i].rotate(dir)

def solution():
    for rotate in rotates:
        [idx, direction] = rotate

        turnLeft(idx - 1, -direction)
        turnRight(idx + 1, -direction)

        wheels[idx].rotate(direction)

for _ in range(4):
    wheels.append(deque(list(sys.stdin.readline())[:8]))

k = int(sys.stdin.readline())
for i in range(k):
    v1, v2 = map(int, sys.stdin.readline().split())
    rotates.append([v1 - 1, v2])

solution()
answer = 0
for i, wheel in enumerate(wheels):
    answer += int(wheel[0]) * (1 << i)
print(answer)
print(answer)