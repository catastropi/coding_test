a, b, c, d, e, f = map(int, input().split())

x, y = -999, -999

while True:
  if y*(b*d - a*e) == c*d - f*a:
    break
  else:
    y += 1

while True:
  if a == 0:
    if x == (f - e*y) / d:
      break
    else:
      x += 1
  else:  
    if x == (c - b*y) / a:
      break
    else:
      x += 1

print(x, y)