def reverse3(nums):
  l = list()
  for i in range(2, -1, -1):
    l.append(nums[i])
  for i in range(3, len(nums)):
    l.append(nums[i])
  return l
