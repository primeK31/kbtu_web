def array123(nums):
  c = 1
  for i in nums:
    if i == c:
      c += 1
  
  return c == 4
