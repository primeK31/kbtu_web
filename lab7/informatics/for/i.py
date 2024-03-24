import math

def c(x):
    k = 0
    for i in range(1, int(x ** .5) + 1):
        if x % i == 0:
            if i == x // i:
                k += 1
            else:
                k += 2
    return k

x = int(input())
print(c(x))
