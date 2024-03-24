def last2(str):
  if len(str) < 2:
    return 0
  s = str[len(str)-2:]
  c = 0
  for i in range(len(str)-2):
    b = str[i:i+2]
    if b == s:
      c += 1

  return c
