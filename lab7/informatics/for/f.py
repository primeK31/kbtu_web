import math

x = int(input())
k = 0
a = 0
c = 1
b = x
s = 0

while b > 0:
    s += 1
    b = math.floor(b / 10)

for i in range(s - 1):
    c *= 10

while x > 0:
    k += (x % 10) * c
    x = math.floor(x / 10)
    c = math.floor(c / 10)

print(k)
