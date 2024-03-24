def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False

a = int(input())
b = int(input())

print(sleep_in(a, b))
