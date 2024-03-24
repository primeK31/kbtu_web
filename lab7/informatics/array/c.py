n = int(input())
t = input()
k = 0

l = list(map(int, t.split()))

for i in range(len(l)):
    if l[i] > 0:
        k += 1

print(k)
