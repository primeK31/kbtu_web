def front_back(str):
  if len(str) <= 1:
    return str
  s = ""
  s += str[len(str) - 1]
  for i in range(1, len(str) - 1):
    s += str[i]
  s += str[0]

  return s
