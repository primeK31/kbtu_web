def close_far(a, b, c):
    return (abs(a - b) <= 1 and not abs(a - c) <= 1 and not abs(b - c) <= 1) or (abs(a - c) <= 1 and not abs(a - b) <= 1 and not abs(b - c) <= 1)
