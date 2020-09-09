n = int(input())
num = 0

while n > 0:
    num += 1
    num_str = str(num)
    if "666" in num_str:
        n -= 1
print(num)