n = int(input())
c = 1
is_ans = False

while c <= n:
    if c == n:
        print('YES')
        is_ans = True
    c *= 2

if is_ans != True:
    print('NO')
