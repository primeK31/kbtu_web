n = int(input())
t = input()
k = 0
is_ans = False

l = list(map(int, t.split()))

for i in range(len(l) - 1):
    if (l[i + 1] > 0) == (l[i] > 0):
        print('YES')
        is_ans = True
        break

if is_ans == False:
    print('NO')
