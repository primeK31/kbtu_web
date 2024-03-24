n = int(input())
t = input()

l = list(map(int, t.split()))

for i in range(len(l)):
    if i % 2 == 0:
        print(l[i])
