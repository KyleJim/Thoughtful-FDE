def sort(width, height, length, mass):
  volumn = width * height * length
  isBulky = volumn >= 1000000 or max(width, height, leng) >= 150
  isHeavy = mass >= 20

  if isBulky and isHeavy:
    return "REJECTED"
  elif isBulky or isHeavy:
    return "SPECIAL"
  else:
    return "STANDARD"
