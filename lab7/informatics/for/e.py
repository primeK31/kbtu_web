import math

x = int(input())
k = 0
a = 0

while x > 0:
    k += x % 10
    x = math.floor(x / 10)

print(k)
