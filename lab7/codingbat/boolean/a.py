def cigar_party(cigars, is_weekend):
  if cigars < 40:
    return False
  if (cigars >= 40 and cigars <= 60):
    return True
  else:
    return is_weekend
