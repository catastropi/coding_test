i = int(input())

i2, i3 = 0, 0

while True:
  i2 += 1
  if str(i2).find('666') != -1:
    i3 += 1
    if i3 == i:
      break

print(i2)