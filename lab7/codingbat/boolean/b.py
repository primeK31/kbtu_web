def caught_speeding(speed, is_birthday):
  s1 = 60
  s2 = 61
  s3 = 80
  if is_birthday:
    s1 += 5
    s2 += 5
    s3 += 5
  if speed <= s1:
    return 0
  elif speed >= s2 and speed <= s3:
    return 1
  else:
    return 2
