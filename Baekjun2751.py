num = [int(input()) for _ in range(int(input()))]

def heapify(v, idx, n):
    left = idx * 2
    right = idx * 2 +1
    parent = idx
    if(left <= n and v[parent] > v[left]):
        parent = left
    if(right <= n and v[parent] > v[right]):
        parent = right
    if parent != idx:
        v[idx], v[parent] = v[parent], v[idx]
        return heapify(v, parent, n)

def solution(num):
    n = len(num)
    v = [0] + num
    for i in range(n, 0, -1):
        heapify(v, i, n)
    for i in range(n, 0, -1):
        print(v[1])
        v[i], v[1] = v[1], v[i]
        heapify(v, 1, i-1)

solution(num)