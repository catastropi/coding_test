u = int(input())

a, b, c = 1, 1, 0

while u > c:
  if c == 0:
    c += 1
  else:
    if (abs(a-b)+1) % 2 == 1:
      b += 1
      c += 1
      if c == u:
        break
      else:
        for n in range(abs(a-b)):
          a += 1
          b -= 1
          c += 1
          if c == u:
            break
    else:
      a += 1
      c += 1
      if c == u:
        break
      else:
        for n2 in range(abs(a-b)):
          a -= 1
          b += 1
          c += 1
          if c == u:
            break
    
print("{}/{}".format(a, b))