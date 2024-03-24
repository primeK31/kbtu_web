import math

n = int(input())

for i in range(1, n + 1):
    if math.sqrt(i) == math.floor(math.sqrt(i)):
        print(i)

