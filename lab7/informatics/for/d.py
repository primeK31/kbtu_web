import math

x = int(input())
d = int(input())
k = 0
a = 0

while x > 0:
    a = x % 10
    if a == d:
        k += 1
    x = math.floor(x / 10)

print(k)
