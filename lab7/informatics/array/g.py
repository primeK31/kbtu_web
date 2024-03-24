n = int(input())
t = input()

l = list(map(int, t.split()))

for i in range(n // 2):
    l[i], l[n - i - 1] = l[n - i - 1], l[i]

for i in l:
    print(i)
