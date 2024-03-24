n = int(input())
t = input()
k = 0

l = list(map(int, t.split()))

for i in range(1, len(l) - 1):
    if l[i + 1] < l[i] and l[i - 1] < l[i]:
        k += 1

print(k)
