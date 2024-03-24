def min(a, b):
    if a > b:
        return b
    else:
        return a


t = input()
l = list(map(int, t.split()))
k = l[0]

for i in range(len(l)):
    k = min(k, l[i])

print(k)
