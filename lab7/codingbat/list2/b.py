def sum13(nums):
    k = 0
    i = 0
    while i < len(nums):
        if nums[i] == 13:
            i += 2
        else:
            k += nums[i]
            i += 1
    return k

