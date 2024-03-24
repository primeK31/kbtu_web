def make_chocolate(small, big, goal):
    b = goal // 5
    if b > big:
        b= big
    c = goal - big_bars_needed * 5
    if c <= small:
        return c
    else:
        return -1
