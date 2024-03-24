def array_front9(nums):
  ans = False
  for i in range(len(nums)):
    if i == 4:
      break
    if nums[i] == 9:
      ans = True
  return ans
