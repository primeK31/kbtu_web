a = int(input())
k = 0
c = 1

while a > 0:
    k += (a % 10) * c
    c *= 2
    a //= 10

print(k)
