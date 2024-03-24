def power(a, b): # lol
    if b == 0:
        return 1
    c = power(a, b // 2)
    if b % 2 == 0:
        return c * c
    else:
        return a * c * c

    
t = input()
l = list(map(float, t.split()))
a = l[0]
b = l[1]
b = int(b)

print(power(a, b))
