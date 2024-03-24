def make_bricks(small, big, goal):
    big_bricks_needed = goal // 5
    if big_bricks_needed >= big:
        goal -= big * 5
    else:
        goal -= big_bricks_needed * 5
    return goal <= small
