def missing_char(str, n):
  s = ""
  for i in range(len(str)):
    if i != n:
      s += str[i]
  
  return s

s = input()
n = int(input())

print(missing_char(s, n))
